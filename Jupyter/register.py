# version 1.0 - updated 2024/5/8

if "ser" not in globals():
    ser = None
crc_calc = None

def serial_init(which=None):
    import serial
    
    global ser
    if isinstance(ser, serial.Serial):
        ser.close()
        
    if isinstance(which, int):
        which = f"COM{which}"
        
    if which is not None:
        ser = serial.Serial(which, baudrate=115200, timeout=1)
        
    else:
        port_found = False
        import serial.tools.list_ports
        for port, desc, hwid in serial.tools.list_ports.comports():
            if desc.startswith("STMicroelectronics"):
                ser = serial.Serial(port, baudrate=115200, timeout=1)
                port_found = True
                print(f"{port}: {desc} [{hwid}]")
                break
                
        if not port_found:
            for port, desc, hwid in serial.tools.list_ports.comports():
                print(f"{port}: {desc} [{hwid}]")
                which = input("Which COM?")
                if which == "0":
                    return
                which = f"COM{which}"
                ser = serial.Serial(which, baudrate=115200, timeout=1)
    
    global crc_calc
    from crc import Configuration, Calculator
    config = Configuration(
        width=16,
        polynomial=0x1021,
        init_value=0x0000,
        final_xor_value=0x0000,
        reverse_input=False,
        reverse_output=False,
    )
    crc_calc = Calculator(config)

serial_init()

def serial_transmit(bs):
    if isinstance(bs, str):
        bs = bs.encode()
    
    l = len(bs)
    data = [0x55, 0xA5, l % 256, l // 256]
    data += bs
    crc = crc_calc.checksum(bs)
    data += [crc % 256, crc // 256]
    
    ser.write(data)

def serial_receive(size):
    bs = ser.read(size+6)
    
    if len(bs) != size+6 \
        or bs[0] != 0x55 or bs[1] != 0xA5 \
        or bs[2]+bs[3]*256 != size:
            print("Format error")
            ser.read_all()
            return bytes()
    
    crc = bs[-2] + bs[-1] * 256
    bs = bs[4:-2]
    if crc_calc.checksum(bs) != crc:
        print("CRC error")
        return bytes()
    
    return bs

def mask_shl(value, mask):
    result = 0
    j = 0
    for i in range(32):
        if mask & (1 << i):
            if value & (1 << j):
                result |= 1 << i
            j += 1
    return result

def mask_shr(value, mask):
    result = 0
    j = 0
    for i in range(32):
        if mask & (1 << i):
            if value & (1 << i):
                result |= 1 << j
            j += 1
    return result

def mask_to_pos(mask):
    pos = []
    for i in range(32):
        if 1 << i & mask:
            pos.append(i)
    return pos

def bin_repr(v, n):
    return f"0b{v:0{n}b}"

def hex_repr(v, n=32):
    return f"0x{v:0{(n+3)//4}X}"

def from_bin(s):
    if isinstance(s, BitField):
        s = s.__repr__()
    if s.startswith("0b"):
        s = s[2:]
    return int(s, base=2)

def from_hex(s):
    if isinstance(s, RegisterBase):
        s = s.__repr__()
    if s.startswith("0x"):
        s = s[2:]
    return int(s, base=16)

# assume all registers are 32-bit - true for G4
MASK_32B = 2**32 - 1

def to_4bytes(word):
    bs = [0, 0, 0, 0]
    for i in range(4):
        bs[i] = word & 0xFF
        word >>= 8
    return bytes(bs)

def read_register(addr, mask=MASK_32B, direct=False):
    bs = "RDR:".encode()
    bs += to_4bytes(addr)
    serial_transmit(bs)
    
    bs = serial_receive(4)
    value = bs[0] | bs[1]<<8 | bs[2]<<16 | bs[3]<<24
    
    if not direct:
        value = mask_shr(value, mask)
        
    return value

# write with mask (change bits with mask 1 only)
def write_register(addr, value, mask=MASK_32B, direct=False):
    if not direct:
        value = mask_shl(value, mask)
    
    bs = "WRR:".encode()
    bs += to_4bytes(addr)
    bs += to_4bytes(value)
    bs += to_4bytes(mask)
    serial_transmit(bs)

class InstanceSetter:
    def __setattr__(self, attr, value):
        try:
            at = super().__getattribute__(attr)
            at.__set__(self, value)
        except AttributeError:
            super().__setattr__(attr, value)

class BitField:
    def __init__(self, register, mask):
        self.register = register
        self.mask = mask
        self.n = bin(mask).count("1")
    
    def __repr__(self):
        return bin_repr(self.read(), self.n)
    
    def __set__(self, instance, value):
        self.write(value)
        return value
    
    def read(self):
        result = self.register.read(mask=self.mask)
        return result
    
    def write(self, value):
        self.register.write(value, mask=self.mask)
    
import IPython.display as ipydisp

class RegisterBase(InstanceSetter):
        
    def __init__(self, address):
        self.address = address
    
    def structure(self, value=-1):
        if value < 0:
            bits = ["N/A"] * 32
        else:
            bits = bin_repr(value, 32)[2:]
        
        html = """\
<style type="text/css">
    table.register th {
        font-weight: normal;
        text-align: center !important;
        padding: 2px;
    }
    table.register td {
        text-align: center !important;
        border: 1px solid;
        word-wrap: break-word;
        padding: 2px;
    }
    .jp-RenderedHTMLCommon tbody tr:nth-child(even) {
        background: var(--jp-layout-color0);
    }
    .jp-RenderedHTMLCommon tbody tr:hover {
        background: rgba(0, 0, 0, 0);
    }
</style>
"""
        
        # 下面这段代码太抽象了，我写完就看不懂了，但是它确实可以打印出一个表格
        mask = [None] * 32
        mask2 = [None] * 32
        for name in dir(self):
            bf = getattr(self, name)
            if not isinstance(bf, BitField):
                continue
            pos = mask_to_pos(bf.mask)
            if all(m is None for m in [mask[p] for p in pos]):
                if bf.n == 1:
                    mask[pos[0]] = [name, -1]
                else:
                    for i, p in enumerate(pos):
                        mask[p] = [name, i]
            elif all(m is None for m in [mask2[p] for p in pos]):
                if bf.n == 1:
                    mask2[pos[0]] = [name, -1]
                else:
                    for i, p in enumerate(pos):
                        mask2[p] = [name, i]
            else:
                return info
        mask = list(reversed(mask))
        mask2 = list(reversed(mask2))
        
        html += """\
<table class="register" style="width:800px">
"""
        
        for base in [0, 16]:
            
            html += """\
    <tr>
"""
            
            for i in range(base, base+16):
                html += f"""\
        <th>{31-i}</th>
"""
            html += """\
    </tr>
"""
            
            for mm in [mask, mask2]:
                mm = mm[base:base+16]
                if not all(m is None for m in mm):
                    html += """\
    <tr>
"""
                    i = 0
                    while i < 16:
                        if mm[i] is None:
                            html += """\
        <td></td>
"""
                            i += 1
                        elif mm[i][1] == -1:
                            html += f"""\
        <td>{mm[i][0]}</td>
"""
                            i += 1
                        else:
                            j = i + 1
                            while j < 16 and mm[j] is not None and \
                                mm[j][0] == mm[j-1][0] and mm[j][1] == mm[j-1][1]-1:
                                j += 1
                            if j == i + 1:
                                html += f"""\
        <td>{mm[i][0]}[{mm[i][1]}]</td>
"""
                            else:
                                html += f"""\
        <td colspan="{j-i}">{mm[i][0]}[{mm[i][1]}:{mm[j-1][1]}]</td>
"""
                            i = j
                    html += """\
    </tr>
"""
            html += """\
    <tr>
"""
            for i in range(base, base+16):
                html += f"""\
        <td>{bits[i]}</td>
"""
        html += """\
    </tr>
"""
        
        ipydisp.display(ipydisp.HTML(html))
    
    def __repr__(self):
        value = self.read()
        info = f"DEC: {value}, HEX: {hex_repr(value)}"
        
        self.structure(value)
        
        return info
    
    def __set__(self, instance, value):
        self.write(value)
        return value
        
    def read(self, mask=MASK_32B, direct=False):
        result = read_register(self.address, mask)
        return result
    
    # warning: value is always right-aligned
    # e.g. to write high 4 bits to 0b0100, set value=0b0100 and mask=0xF0000000
    # set direct=True to bypass the shifting
    def write(self, value, mask=MASK_32B, direct=False):
        write_register(self.address, value, mask)
    
class PeripheralBase(InstanceSetter):
        
    def __init__(self, base):
        self.base = base

