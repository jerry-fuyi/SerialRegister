# version 1.0 - updated 2024/5/8

from register import BitField, RegisterBase, PeripheralBase

class ADC_ISR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.ADRDY = BitField(self, 0x00000001)
        self.EOSMP = BitField(self, 0x00000002)
        self.EOC = BitField(self, 0x00000004)
        self.EOS = BitField(self, 0x00000008)
        self.OVR = BitField(self, 0x00000010)
        self.JEOC = BitField(self, 0x00000020)
        self.JEOS = BitField(self, 0x00000040)
        self.AWD1 = BitField(self, 0x00000080)
        self.AWD2 = BitField(self, 0x00000100)
        self.AWD3 = BitField(self, 0x00000200)
        self.JQOVF = BitField(self, 0x00000400)

class ADC_IER(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.ADRDYIE = BitField(self, 0x00000001)
        self.EOSMPIE = BitField(self, 0x00000002)
        self.EOCIE = BitField(self, 0x00000004)
        self.EOSIE = BitField(self, 0x00000008)
        self.OVRIE = BitField(self, 0x00000010)
        self.JEOCIE = BitField(self, 0x00000020)
        self.JEOSIE = BitField(self, 0x00000040)
        self.AWD1IE = BitField(self, 0x00000080)
        self.AWD2IE = BitField(self, 0x00000100)
        self.AWD3IE = BitField(self, 0x00000200)
        self.JQOVFIE = BitField(self, 0x00000400)

class ADC_CR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.ADEN = BitField(self, 0x00000001)
        self.ADDIS = BitField(self, 0x00000002)
        self.ADSTART = BitField(self, 0x00000004)
        self.JADSTART = BitField(self, 0x00000008)
        self.ADSTP = BitField(self, 0x00000010)
        self.JADSTP = BitField(self, 0x00000020)
        self.ADVREGEN = BitField(self, 0x10000000)
        self.DEEPPWD = BitField(self, 0x20000000)
        self.ADCALDIF = BitField(self, 0x40000000)
        self.ADCAL = BitField(self, 0x80000000)

class ADC_CFGR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.DMAEN = BitField(self, 0x00000001)
        self.DMACFG = BitField(self, 0x00000002)
        self.RES = BitField(self, 0x00000018)
        self.EXTSEL = BitField(self, 0x000003E0)
        self.EXTEN = BitField(self, 0x00000C00)
        self.OVRMOD = BitField(self, 0x00001000)
        self.CONT = BitField(self, 0x00002000)
        self.AUTDLY = BitField(self, 0x00004000)
        self.ALIGN = BitField(self, 0x00008000)
        self.DISCEN = BitField(self, 0x00010000)
        self.DISCNUM = BitField(self, 0x000E0000)
        self.JDISCEN = BitField(self, 0x00100000)
        self.JQM = BitField(self, 0x00200000)
        self.AWD1SGL = BitField(self, 0x00400000)
        self.AWD1EN = BitField(self, 0x00800000)
        self.JAWD1EN = BitField(self, 0x01000000)
        self.JAUTO = BitField(self, 0x02000000)
        self.AWD1CH = BitField(self, 0x7C000000)
        self.JQDIS = BitField(self, 0x80000000)

class ADC_CFGR2(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.ROVSE = BitField(self, 0x00000001)
        self.JOVSE = BitField(self, 0x00000002)
        self.OVSR = BitField(self, 0x0000001C)
        self.OVSS = BitField(self, 0x000001E0)
        self.TROVS = BitField(self, 0x00000200)
        self.ROVSM = BitField(self, 0x00000400)
        self.GCOMP = BitField(self, 0x00010000)
        self.SWTRIG = BitField(self, 0x02000000)
        self.BULB = BitField(self, 0x04000000)
        self.SMPTRIG = BitField(self, 0x08000000)

class ADC_SMPR1(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.SMP0 = BitField(self, 0x00000007)
        self.SMP1 = BitField(self, 0x00000038)
        self.SMP2 = BitField(self, 0x000001C0)
        self.SMP3 = BitField(self, 0x00000E00)
        self.SMP4 = BitField(self, 0x00007000)
        self.SMP5 = BitField(self, 0x00038000)
        self.SMP6 = BitField(self, 0x001C0000)
        self.SMP7 = BitField(self, 0x00E00000)
        self.SMP8 = BitField(self, 0x07000000)
        self.SMP9 = BitField(self, 0x38000000)
        self.SMPPLUS = BitField(self, 0x80000000)

class ADC_SMPR2(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.SMP10 = BitField(self, 0x00000007)
        self.SMP11 = BitField(self, 0x00000038)
        self.SMP12 = BitField(self, 0x000001C0)
        self.SMP13 = BitField(self, 0x00000E00)
        self.SMP14 = BitField(self, 0x00007000)
        self.SMP15 = BitField(self, 0x00038000)
        self.SMP16 = BitField(self, 0x001C0000)
        self.SMP17 = BitField(self, 0x00E00000)
        self.SMP18 = BitField(self, 0x07000000)

class ADC_TR1(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.LT1 = BitField(self, 0x00000FFF)
        self.AWDFILT = BitField(self, 0x00007000)
        self.HT1 = BitField(self, 0x0FFF0000)

class ADC_TR2(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.LT2 = BitField(self, 0x000000FF)
        self.HT2 = BitField(self, 0x00FF0000)

class ADC_TR3(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.LT3 = BitField(self, 0x000000FF)
        self.HT3 = BitField(self, 0x00FF0000)

class ADC_SQR1(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.L = BitField(self, 0x0000000F)
        self.SQ1 = BitField(self, 0x000007C0)
        self.SQ2 = BitField(self, 0x0001F000)
        self.SQ3 = BitField(self, 0x007C0000)
        self.SQ4 = BitField(self, 0x1F000000)

class ADC_SQR2(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.SQ5 = BitField(self, 0x0000001F)
        self.SQ6 = BitField(self, 0x000007C0)
        self.SQ7 = BitField(self, 0x0001F000)
        self.SQ8 = BitField(self, 0x007C0000)
        self.SQ9 = BitField(self, 0x1F000000)

class ADC_SQR3(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.SQ10 = BitField(self, 0x0000001F)
        self.SQ11 = BitField(self, 0x000007C0)
        self.SQ12 = BitField(self, 0x0001F000)
        self.SQ13 = BitField(self, 0x007C0000)
        self.SQ14 = BitField(self, 0x1F000000)

class ADC_SQR4(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.SQ15 = BitField(self, 0x0000001F)
        self.SQ16 = BitField(self, 0x000007C0)

class ADC_DR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.RDATA = BitField(self, 0x0000FFFF)

class ADC_JSQR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.JL = BitField(self, 0x00000003)
        self.JEXTSEL = BitField(self, 0x0000007C)
        self.JEXTEN = BitField(self, 0x00000180)
        self.JSQ1 = BitField(self, 0x00003E00)
        self.JSQ2 = BitField(self, 0x000F8000)
        self.JSQ3 = BitField(self, 0x03E00000)
        self.JSQ4 = BitField(self, 0xF8000000)

class ADC_OFR1(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.OFFSET1 = BitField(self, 0x00000FFF)
        self.OFFSETPOS = BitField(self, 0x01000000)
        self.SATEN = BitField(self, 0x02000000)
        self.OFFSET1_CH = BitField(self, 0x7C000000)
        self.OFFSET1_EN = BitField(self, 0x80000000)

class ADC_OFR2(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.OFFSET2 = BitField(self, 0x00000FFF)
        self.OFFSETPOS = BitField(self, 0x01000000)
        self.SATEN = BitField(self, 0x02000000)
        self.OFFSET2_CH = BitField(self, 0x7C000000)
        self.OFFSET2_EN = BitField(self, 0x80000000)

class ADC_OFR3(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.OFFSET3 = BitField(self, 0x00000FFF)
        self.OFFSETPOS = BitField(self, 0x01000000)
        self.SATEN = BitField(self, 0x02000000)
        self.OFFSET3_CH = BitField(self, 0x7C000000)
        self.OFFSET3_EN = BitField(self, 0x80000000)

class ADC_OFR4(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.OFFSET4 = BitField(self, 0x00000FFF)
        self.OFFSETPOS = BitField(self, 0x01000000)
        self.SATEN = BitField(self, 0x02000000)
        self.OFFSET4_CH = BitField(self, 0x7C000000)
        self.OFFSET4_EN = BitField(self, 0x80000000)

class ADC_JDR1(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.JDATA = BitField(self, 0x0000FFFF)

class ADC_JDR2(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.JDATA = BitField(self, 0x0000FFFF)

class ADC_JDR3(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.JDATA = BitField(self, 0x0000FFFF)

class ADC_JDR4(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.JDATA = BitField(self, 0x0000FFFF)

class ADC_AWD2CR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.AWD2CH = BitField(self, 0x0007FFFF)

class ADC_AWD3CR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.AWD3CH = BitField(self, 0x0007FFFF)

class ADC_DIFSEL(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.DIFSEL = BitField(self, 0x0007FFFF)

class ADC_CALFACT(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.CALFACT_S = BitField(self, 0x0000007F)
        self.CALFACT_D = BitField(self, 0x007F0000)

class ADC_GCOMP(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.GCOMPCOEFF = BitField(self, 0x00003FFF)

class ADC_TypeDef(PeripheralBase):

    def __init__(self, base):
        super().__init__(base)
        self.ISR = ADC_ISR(base + 0x0)
        self.IER = ADC_IER(base + 0x4)
        self.CR = ADC_CR(base + 0x8)
        self.CFGR = ADC_CFGR(base + 0xC)
        self.CFGR2 = ADC_CFGR2(base + 0x10)
        self.SMPR1 = ADC_SMPR1(base + 0x14)
        self.SMPR2 = ADC_SMPR2(base + 0x18)
        self.TR1 = ADC_TR1(base + 0x20)
        self.TR2 = ADC_TR2(base + 0x24)
        self.TR3 = ADC_TR3(base + 0x28)
        self.SQR1 = ADC_SQR1(base + 0x30)
        self.SQR2 = ADC_SQR2(base + 0x34)
        self.SQR3 = ADC_SQR3(base + 0x38)
        self.SQR4 = ADC_SQR4(base + 0x3C)
        self.DR = ADC_DR(base + 0x40)
        self.JSQR = ADC_JSQR(base + 0x4C)
        self.OFR1 = ADC_OFR1(base + 0x60)
        self.OFR2 = ADC_OFR2(base + 0x64)
        self.OFR3 = ADC_OFR3(base + 0x68)
        self.OFR4 = ADC_OFR4(base + 0x6C)
        self.JDR1 = ADC_JDR1(base + 0x80)
        self.JDR2 = ADC_JDR2(base + 0x84)
        self.JDR3 = ADC_JDR3(base + 0x88)
        self.JDR4 = ADC_JDR4(base + 0x8C)
        self.AWD2CR = ADC_AWD2CR(base + 0xA0)
        self.AWD3CR = ADC_AWD3CR(base + 0xA4)
        self.DIFSEL = ADC_DIFSEL(base + 0xB0)
        self.CALFACT = ADC_CALFACT(base + 0xB4)
        self.GCOMP = ADC_GCOMP(base + 0xC0)

ADC1 = ADC_TypeDef(0x50000000)
ADC2 = ADC_TypeDef(0x50000100)
ADC3 = ADC_TypeDef(0x50000400)
ADC4 = ADC_TypeDef(0x50000500)
ADC5 = ADC_TypeDef(0x50000600)

class ADC_Common_CSR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.ADRDY_MST = BitField(self, 0x00000001)
        self.EOSMP_MST = BitField(self, 0x00000002)
        self.EOC_MST = BitField(self, 0x00000004)
        self.EOS_MST = BitField(self, 0x00000008)
        self.OVR_MST = BitField(self, 0x00000010)
        self.JEOC_MST = BitField(self, 0x00000020)
        self.JEOS_MST = BitField(self, 0x00000040)
        self.AWD1_MST = BitField(self, 0x00000080)
        self.AWD2_MST = BitField(self, 0x00000100)
        self.AWD3_MST = BitField(self, 0x00000200)
        self.JQOVF_MST = BitField(self, 0x00000400)
        self.ADRDY_SLV = BitField(self, 0x00010000)
        self.EOSMP_SLV = BitField(self, 0x00020000)
        self.EOC_SLV = BitField(self, 0x00040000)
        self.EOS_SLV = BitField(self, 0x00080000)
        self.OVR_SLV = BitField(self, 0x00100000)
        self.JEOC_SLV = BitField(self, 0x00200000)
        self.JEOS_SLV = BitField(self, 0x00400000)
        self.AWD1_SLV = BitField(self, 0x00800000)
        self.AWD2_SLV = BitField(self, 0x01000000)
        self.AWD3_SLV = BitField(self, 0x02000000)
        self.JQOVF_SLV = BitField(self, 0x04000000)

class ADC_Common_CCR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.DUAL = BitField(self, 0x0000001F)
        self.DELAY = BitField(self, 0x00000F00)
        self.DMACFG = BitField(self, 0x00002000)
        self.MDMA = BitField(self, 0x0000C000)
        self.CKMODE = BitField(self, 0x00030000)
        self.PRESC = BitField(self, 0x003C0000)
        self.VREFEN = BitField(self, 0x00400000)
        self.VSENSESEL = BitField(self, 0x00800000)
        self.VBATSEL = BitField(self, 0x01000000)

class ADC_Common_CDR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.RDATA_MST = BitField(self, 0x0000FFFF)
        self.RDATA_SLV = BitField(self, 0xFFFF0000)

class ADC_Common_TypeDef(PeripheralBase):

    def __init__(self, base):
        super().__init__(base)
        self.CSR = ADC_Common_CSR(base + 0x0)
        self.CCR = ADC_Common_CCR(base + 0x8)
        self.CDR = ADC_Common_CDR(base + 0xC)

ADC12_COMMON = ADC_Common_TypeDef(0x50000300)
ADC345_COMMON = ADC_Common_TypeDef(0x50000700)

class FDCAN_Global_CREL(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.DAY = BitField(self, 0x000000FF)
        self.MON = BitField(self, 0x0000FF00)
        self.YEAR = BitField(self, 0x000F0000)
        self.SUBSTEP = BitField(self, 0x00F00000)
        self.STEP = BitField(self, 0x0F000000)
        self.REL = BitField(self, 0xF0000000)

class FDCAN_Global_ENDN(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.ETV = BitField(self, 0xFFFFFFFF)

class FDCAN_Global_DBTP(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.DSJW = BitField(self, 0x0000000F)
        self.DTSEG2 = BitField(self, 0x000000F0)
        self.DTSEG1 = BitField(self, 0x00001F00)
        self.DBRP = BitField(self, 0x001F0000)
        self.TDC = BitField(self, 0x00800000)

class FDCAN_Global_TEST(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.LBCK = BitField(self, 0x00000010)
        self.TX = BitField(self, 0x00000060)
        self.RX = BitField(self, 0x00000080)

class FDCAN_Global_RWD(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.WDC = BitField(self, 0x000000FF)
        self.WDV = BitField(self, 0x0000FF00)

class FDCAN_Global_CCCR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.INIT = BitField(self, 0x00000001)
        self.CCE = BitField(self, 0x00000002)
        self.ASM = BitField(self, 0x00000004)
        self.CSA = BitField(self, 0x00000008)
        self.CSR = BitField(self, 0x00000010)
        self.MON = BitField(self, 0x00000020)
        self.DAR = BitField(self, 0x00000040)
        self.TEST = BitField(self, 0x00000080)
        self.FDOE = BitField(self, 0x00000100)
        self.BRSE = BitField(self, 0x00000200)
        self.PXHD = BitField(self, 0x00001000)
        self.EFBI = BitField(self, 0x00002000)
        self.TXP = BitField(self, 0x00004000)
        self.NISO = BitField(self, 0x00008000)

class FDCAN_Global_NBTP(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.NTSEG2 = BitField(self, 0x0000007F)
        self.NTSEG1 = BitField(self, 0x0000FF00)
        self.NBRP = BitField(self, 0x01FF0000)
        self.NSJW = BitField(self, 0xFE000000)

class FDCAN_Global_TSCC(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.TSS = BitField(self, 0x00000003)
        self.TCP = BitField(self, 0x000F0000)

class FDCAN_Global_TSCV(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.TSC = BitField(self, 0x0000FFFF)

class FDCAN_Global_TOCC(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.ETOC = BitField(self, 0x00000001)
        self.TOS = BitField(self, 0x00000006)
        self.TOP = BitField(self, 0xFFFF0000)

class FDCAN_Global_TOCV(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.TOC = BitField(self, 0x0000FFFF)

class FDCAN_Global_ECR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.TEC = BitField(self, 0x000000FF)
        self.REC = BitField(self, 0x00007F00)
        self.RP = BitField(self, 0x00008000)
        self.CEL = BitField(self, 0x00FF0000)

class FDCAN_Global_PSR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.LEC = BitField(self, 0x00000007)
        self.ACT = BitField(self, 0x00000018)
        self.EP = BitField(self, 0x00000020)
        self.EW = BitField(self, 0x00000040)
        self.BO = BitField(self, 0x00000080)
        self.DLEC = BitField(self, 0x00000700)
        self.RESI = BitField(self, 0x00000800)
        self.RBRS = BitField(self, 0x00001000)
        self.REDL = BitField(self, 0x00002000)
        self.PXE = BitField(self, 0x00004000)
        self.TDCV = BitField(self, 0x007F0000)

class FDCAN_Global_TDCR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.TDCF = BitField(self, 0x0000007F)
        self.TDCO = BitField(self, 0x00007F00)

class FDCAN_Global_IR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.RF0N = BitField(self, 0x00000001)
        self.RF0F = BitField(self, 0x00000002)
        self.RF0L = BitField(self, 0x00000004)
        self.RF1N = BitField(self, 0x00000008)
        self.RF1F = BitField(self, 0x00000010)
        self.RF1L = BitField(self, 0x00000020)
        self.HPM = BitField(self, 0x00000040)
        self.TC = BitField(self, 0x00000080)
        self.TCF = BitField(self, 0x00000100)
        self.TFE = BitField(self, 0x00000200)
        self.TEFN = BitField(self, 0x00000400)
        self.TEFF = BitField(self, 0x00000800)
        self.TEFL = BitField(self, 0x00001000)
        self.TSW = BitField(self, 0x00002000)
        self.MRAF = BitField(self, 0x00004000)
        self.TOO = BitField(self, 0x00008000)
        self.ELO = BitField(self, 0x00010000)
        self.EP = BitField(self, 0x00020000)
        self.EW = BitField(self, 0x00040000)
        self.BO = BitField(self, 0x00080000)
        self.WDI = BitField(self, 0x00100000)
        self.PEA = BitField(self, 0x00200000)
        self.PED = BitField(self, 0x00400000)
        self.ARA = BitField(self, 0x00800000)

class FDCAN_Global_IE(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.RF0NE = BitField(self, 0x00000001)
        self.RF0FE = BitField(self, 0x00000002)
        self.RF0LE = BitField(self, 0x00000004)
        self.RF1NE = BitField(self, 0x00000008)
        self.RF1FE = BitField(self, 0x00000010)
        self.RF1LE = BitField(self, 0x00000020)
        self.HPME = BitField(self, 0x00000040)
        self.TCE = BitField(self, 0x00000080)
        self.TCFE = BitField(self, 0x00000100)
        self.TFEE = BitField(self, 0x00000200)
        self.TEFNE = BitField(self, 0x00000400)
        self.TEFFE = BitField(self, 0x00000800)
        self.TEFLE = BitField(self, 0x00001000)
        self.TSWE = BitField(self, 0x00002000)
        self.MRAFE = BitField(self, 0x00004000)
        self.TOOE = BitField(self, 0x00008000)
        self.ELOE = BitField(self, 0x00010000)
        self.EPE = BitField(self, 0x00020000)
        self.EWE = BitField(self, 0x00040000)
        self.BOE = BitField(self, 0x00080000)
        self.WDIE = BitField(self, 0x00100000)
        self.PEAE = BitField(self, 0x00200000)
        self.PEDE = BitField(self, 0x00400000)
        self.ARAE = BitField(self, 0x00800000)

class FDCAN_Global_ILS(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.RXFIFO0 = BitField(self, 0x00000001)
        self.RXFIFO1 = BitField(self, 0x00000002)
        self.SMSG = BitField(self, 0x00000004)
        self.TFERR = BitField(self, 0x00000008)
        self.MISC = BitField(self, 0x00000010)
        self.BERR = BitField(self, 0x00000020)
        self.PERR = BitField(self, 0x00000040)

class FDCAN_Global_ILE(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.EINT0 = BitField(self, 0x00000001)
        self.EINT1 = BitField(self, 0x00000002)

class FDCAN_Global_RXGFC(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.RRFE = BitField(self, 0x00000001)
        self.RRFS = BitField(self, 0x00000002)
        self.ANFE = BitField(self, 0x0000000C)
        self.ANFS = BitField(self, 0x00000030)
        self.F1OM = BitField(self, 0x00000100)
        self.F0OM = BitField(self, 0x00000200)
        self.LSS = BitField(self, 0x001F0000)
        self.LSE = BitField(self, 0x0F000000)

class FDCAN_Global_XIDAM(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.EIDM = BitField(self, 0x1FFFFFFF)

class FDCAN_Global_HPMS(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.BIDX = BitField(self, 0x00000007)
        self.MSI = BitField(self, 0x000000C0)
        self.FIDX = BitField(self, 0x00001F00)
        self.FLST = BitField(self, 0x00008000)

class FDCAN_Global_RXF0S(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.F0FL = BitField(self, 0x0000000F)
        self.F0GI = BitField(self, 0x00000300)
        self.F0PI = BitField(self, 0x00030000)
        self.F0F = BitField(self, 0x01000000)
        self.RF0L = BitField(self, 0x02000000)

class FDCAN_Global_RXF0A(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.F0AI = BitField(self, 0x00000007)

class FDCAN_Global_RXF1S(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.F1FL = BitField(self, 0x0000000F)
        self.F1GI = BitField(self, 0x00000300)
        self.F1PI = BitField(self, 0x00030000)
        self.F1F = BitField(self, 0x01000000)
        self.RF1L = BitField(self, 0x02000000)

class FDCAN_Global_RXF1A(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.F1AI = BitField(self, 0x00000007)

class FDCAN_Global_TXBC(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.TFQM = BitField(self, 0x01000000)

class FDCAN_Global_TXFQS(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.TFFL = BitField(self, 0x00000007)
        self.TFGI = BitField(self, 0x00000300)
        self.TFQPI = BitField(self, 0x00030000)
        self.TFQF = BitField(self, 0x00200000)

class FDCAN_Global_TXBRP(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.TRP = BitField(self, 0x00000007)

class FDCAN_Global_TXBAR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.AR = BitField(self, 0x00000007)

class FDCAN_Global_TXBCR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.CR = BitField(self, 0x00000007)

class FDCAN_Global_TXBTO(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.TO = BitField(self, 0x00000007)

class FDCAN_Global_TXBCF(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.CF = BitField(self, 0x00000007)

class FDCAN_Global_TXBTIE(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.TIE = BitField(self, 0x00000007)

class FDCAN_Global_TXBCIE(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.CFIE = BitField(self, 0x00000007)

class FDCAN_Global_TXEFS(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.EFFL = BitField(self, 0x00000007)
        self.EFGI = BitField(self, 0x00000300)
        self.EFPI = BitField(self, 0x00030000)
        self.EFF = BitField(self, 0x01000000)
        self.TEFL = BitField(self, 0x02000000)

class FDCAN_Global_TXEFA(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.EFAI = BitField(self, 0x00000003)

class FDCAN_GlobalTypeDef(PeripheralBase):

    def __init__(self, base):
        super().__init__(base)
        self.CREL = FDCAN_Global_CREL(base + 0x0)
        self.ENDN = FDCAN_Global_ENDN(base + 0x4)
        self.DBTP = FDCAN_Global_DBTP(base + 0xC)
        self.TEST = FDCAN_Global_TEST(base + 0x10)
        self.RWD = FDCAN_Global_RWD(base + 0x14)
        self.CCCR = FDCAN_Global_CCCR(base + 0x18)
        self.NBTP = FDCAN_Global_NBTP(base + 0x1C)
        self.TSCC = FDCAN_Global_TSCC(base + 0x20)
        self.TSCV = FDCAN_Global_TSCV(base + 0x24)
        self.TOCC = FDCAN_Global_TOCC(base + 0x28)
        self.TOCV = FDCAN_Global_TOCV(base + 0x2C)
        self.ECR = FDCAN_Global_ECR(base + 0x40)
        self.PSR = FDCAN_Global_PSR(base + 0x44)
        self.TDCR = FDCAN_Global_TDCR(base + 0x48)
        self.IR = FDCAN_Global_IR(base + 0x50)
        self.IE = FDCAN_Global_IE(base + 0x54)
        self.ILS = FDCAN_Global_ILS(base + 0x58)
        self.ILE = FDCAN_Global_ILE(base + 0x5C)
        self.RXGFC = FDCAN_Global_RXGFC(base + 0x80)
        self.XIDAM = FDCAN_Global_XIDAM(base + 0x84)
        self.HPMS = FDCAN_Global_HPMS(base + 0x88)
        self.RXF0S = FDCAN_Global_RXF0S(base + 0x90)
        self.RXF0A = FDCAN_Global_RXF0A(base + 0x94)
        self.RXF1S = FDCAN_Global_RXF1S(base + 0x98)
        self.RXF1A = FDCAN_Global_RXF1A(base + 0x9C)
        self.TXBC = FDCAN_Global_TXBC(base + 0xC0)
        self.TXFQS = FDCAN_Global_TXFQS(base + 0xC4)
        self.TXBRP = FDCAN_Global_TXBRP(base + 0xC8)
        self.TXBAR = FDCAN_Global_TXBAR(base + 0xCC)
        self.TXBCR = FDCAN_Global_TXBCR(base + 0xD0)
        self.TXBTO = FDCAN_Global_TXBTO(base + 0xD4)
        self.TXBCF = FDCAN_Global_TXBCF(base + 0xD8)
        self.TXBTIE = FDCAN_Global_TXBTIE(base + 0xDC)
        self.TXBCIE = FDCAN_Global_TXBCIE(base + 0xE0)
        self.TXEFS = FDCAN_Global_TXEFS(base + 0xE4)
        self.TXEFA = FDCAN_Global_TXEFA(base + 0xE8)

FDCAN1 = FDCAN_GlobalTypeDef(0x40006400)
FDCAN2 = FDCAN_GlobalTypeDef(0x40006800)
FDCAN3 = FDCAN_GlobalTypeDef(0x40006C00)

class FDCAN_Config_CKDIV(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.PDIV = BitField(self, 0x0000000F)

class FDCAN_Config_TypeDef(PeripheralBase):

    def __init__(self, base):
        super().__init__(base)
        self.CKDIV = FDCAN_Config_CKDIV(base + 0x0)

FDCAN_CONFIG = FDCAN_Config_TypeDef(0x40006500)

class COMP_CSR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.EN = BitField(self, 0x00000001)
        self.INMSEL = BitField(self, 0x000000F0)
        self.INPSEL = BitField(self, 0x00000100)
        self.POLARITY = BitField(self, 0x00008000)
        self.HYST = BitField(self, 0x00070000)
        self.BLANKING = BitField(self, 0x00380000)
        self.BRGEN = BitField(self, 0x00400000)
        self.SCALEN = BitField(self, 0x00800000)
        self.VALUE = BitField(self, 0x40000000)
        self.LOCK = BitField(self, 0x80000000)

class COMP_TypeDef(PeripheralBase):

    def __init__(self, base):
        super().__init__(base)
        self.CSR = COMP_CSR(base + 0x0)

COMP1 = COMP_TypeDef(0x40010200)
COMP2 = COMP_TypeDef(0x40010204)
COMP3 = COMP_TypeDef(0x40010208)
COMP4 = COMP_TypeDef(0x4001020C)
COMP5 = COMP_TypeDef(0x40010210)
COMP6 = COMP_TypeDef(0x40010214)
COMP7 = COMP_TypeDef(0x40010218)

class CRC_DR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.DR = BitField(self, 0xFFFFFFFF)

class CRC_IDR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.IDR = BitField(self, 0xFFFFFFFF)

class CRC_CR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.RESET = BitField(self, 0x00000001)
        self.POLYSIZE = BitField(self, 0x00000018)
        self.REV_IN = BitField(self, 0x00000060)
        self.REV_OUT = BitField(self, 0x00000080)

class CRC_INIT(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.INIT = BitField(self, 0xFFFFFFFF)

class CRC_POL(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.POL = BitField(self, 0xFFFFFFFF)

class CRC_TypeDef(PeripheralBase):

    def __init__(self, base):
        super().__init__(base)
        self.DR = CRC_DR(base + 0x0)
        self.IDR = CRC_IDR(base + 0x4)
        self.CR = CRC_CR(base + 0x8)
        self.INIT = CRC_INIT(base + 0x10)
        self.POL = CRC_POL(base + 0x14)

CRC = CRC_TypeDef(0x40023000)

class CRS_CR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.SYNCOKIE = BitField(self, 0x00000001)
        self.SYNCWARNIE = BitField(self, 0x00000002)
        self.ERRIE = BitField(self, 0x00000004)
        self.ESYNCIE = BitField(self, 0x00000008)
        self.CEN = BitField(self, 0x00000020)
        self.AUTOTRIMEN = BitField(self, 0x00000040)
        self.SWSYNC = BitField(self, 0x00000080)
        self.TRIM = BitField(self, 0x00007F00)

class CRS_CFGR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.RELOAD = BitField(self, 0x0000FFFF)
        self.FELIM = BitField(self, 0x00FF0000)
        self.SYNCDIV = BitField(self, 0x07000000)
        self.SYNCSRC = BitField(self, 0x30000000)
        self.SYNCPOL = BitField(self, 0x80000000)

class CRS_ISR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.SYNCOKF = BitField(self, 0x00000001)
        self.SYNCWARNF = BitField(self, 0x00000002)
        self.ERRF = BitField(self, 0x00000004)
        self.ESYNCF = BitField(self, 0x00000008)
        self.SYNCERR = BitField(self, 0x00000100)
        self.SYNCMISS = BitField(self, 0x00000200)
        self.TRIMOVF = BitField(self, 0x00000400)
        self.FEDIR = BitField(self, 0x00008000)
        self.FECAP = BitField(self, 0xFFFF0000)

class CRS_ICR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.SYNCOKC = BitField(self, 0x00000001)
        self.SYNCWARNC = BitField(self, 0x00000002)
        self.ERRC = BitField(self, 0x00000004)
        self.ESYNCC = BitField(self, 0x00000008)

class CRS_TypeDef(PeripheralBase):

    def __init__(self, base):
        super().__init__(base)
        self.CR = CRS_CR(base + 0x0)
        self.CFGR = CRS_CFGR(base + 0x4)
        self.ISR = CRS_ISR(base + 0x8)
        self.ICR = CRS_ICR(base + 0xC)

CRS = CRS_TypeDef(0x40002000)

class DAC_CR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.EN1 = BitField(self, 0x00000001)
        self.TEN1 = BitField(self, 0x00000002)
        self.TSEL1 = BitField(self, 0x0000003C)
        self.WAVE1 = BitField(self, 0x000000C0)
        self.MAMP1 = BitField(self, 0x00000F00)
        self.DMAEN1 = BitField(self, 0x00001000)
        self.DMAUDRIE1 = BitField(self, 0x00002000)
        self.CEN1 = BitField(self, 0x00004000)
        self.HFSEL = BitField(self, 0x00008000)
        self.EN2 = BitField(self, 0x00010000)
        self.TEN2 = BitField(self, 0x00020000)
        self.TSEL2 = BitField(self, 0x003C0000)
        self.WAVE2 = BitField(self, 0x00C00000)
        self.MAMP2 = BitField(self, 0x0F000000)
        self.DMAEN2 = BitField(self, 0x10000000)
        self.DMAUDRIE2 = BitField(self, 0x20000000)
        self.CEN2 = BitField(self, 0x40000000)

class DAC_SWTRIGR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.SWTRIG1 = BitField(self, 0x00000001)
        self.SWTRIG2 = BitField(self, 0x00000002)
        self.SWTRIGB1 = BitField(self, 0x00010000)
        self.SWTRIGB2 = BitField(self, 0x00020000)

class DAC_DHR12R1(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.DACC1DHR = BitField(self, 0x00000FFF)
        self.DACC1DHRB = BitField(self, 0x0FFF0000)

class DAC_DHR12L1(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.DACC1DHR = BitField(self, 0x0000FFF0)
        self.DACC1DHRB = BitField(self, 0xFFF00000)

class DAC_DHR8R1(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.DACC1DHR = BitField(self, 0x000000FF)
        self.DACC1DHRB = BitField(self, 0x0000FF00)

class DAC_DHR12R2(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.DACC2DHR = BitField(self, 0x00000FFF)
        self.DACC2DHRB = BitField(self, 0x0FFF0000)

class DAC_DHR12L2(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.DACC2DHR = BitField(self, 0x0000FFF0)
        self.DACC2DHRB = BitField(self, 0xFFF00000)

class DAC_DHR8R2(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.DACC2DHR = BitField(self, 0x000000FF)
        self.DACC2DHRB = BitField(self, 0x0000FF00)

class DAC_DHR12RD(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.DACC1DHR = BitField(self, 0x00000FFF)
        self.DACC2DHR = BitField(self, 0x0FFF0000)

class DAC_DHR12LD(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.DACC1DHR = BitField(self, 0x0000FFF0)
        self.DACC2DHR = BitField(self, 0xFFF00000)

class DAC_DHR8RD(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.DACC1DHR = BitField(self, 0x000000FF)
        self.DACC2DHR = BitField(self, 0x0000FF00)

class DAC_DOR1(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.DACC1DOR = BitField(self, 0x00000FFF)
        self.DACC1DORB = BitField(self, 0x0FFF0000)

class DAC_DOR2(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.DACC2DOR = BitField(self, 0x00000FFF)
        self.DACC2DORB = BitField(self, 0x0FFF0000)

class DAC_SR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.DAC1RDY = BitField(self, 0x00000800)
        self.DORSTAT1 = BitField(self, 0x00001000)
        self.DMAUDR1 = BitField(self, 0x00002000)
        self.CAL_FLAG1 = BitField(self, 0x00004000)
        self.BWST1 = BitField(self, 0x00008000)
        self.DAC2RDY = BitField(self, 0x08000000)
        self.DORSTAT2 = BitField(self, 0x10000000)
        self.DMAUDR2 = BitField(self, 0x20000000)
        self.CAL_FLAG2 = BitField(self, 0x40000000)
        self.BWST2 = BitField(self, 0x80000000)

class DAC_CCR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.OTRIM1 = BitField(self, 0x0000001F)
        self.OTRIM2 = BitField(self, 0x001F0000)

class DAC_MCR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.MODE1 = BitField(self, 0x00000007)
        self.DMADOUBLE1 = BitField(self, 0x00000100)
        self.SINFORMAT1 = BitField(self, 0x00000200)
        self.HFSEL = BitField(self, 0x0000C000)
        self.MODE2 = BitField(self, 0x00070000)
        self.DMADOUBLE2 = BitField(self, 0x01000000)
        self.SINFORMAT2 = BitField(self, 0x02000000)

class DAC_SHSR1(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.TSAMPLE1 = BitField(self, 0x000003FF)

class DAC_SHSR2(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.TSAMPLE2 = BitField(self, 0x000003FF)

class DAC_SHHR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.THOLD1 = BitField(self, 0x000003FF)
        self.THOLD2 = BitField(self, 0x03FF0000)

class DAC_SHRR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.TREFRESH1 = BitField(self, 0x000000FF)
        self.TREFRESH2 = BitField(self, 0x00FF0000)

class DAC_STR1(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.STRSTDATA1 = BitField(self, 0x00000FFF)
        self.STDIR1 = BitField(self, 0x00001000)
        self.STINCDATA1 = BitField(self, 0xFFFF0000)

class DAC_STR2(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.STRSTDATA2 = BitField(self, 0x00000FFF)
        self.STDIR2 = BitField(self, 0x00001000)
        self.STINCDATA2 = BitField(self, 0xFFFF0000)

class DAC_STMODR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.STRSTTRIGSEL1 = BitField(self, 0x0000000F)
        self.STINCTRIGSEL1 = BitField(self, 0x00000F00)
        self.STRSTTRIGSEL2 = BitField(self, 0x000F0000)
        self.STINCTRIGSEL2 = BitField(self, 0x0F000000)

class DAC_TypeDef(PeripheralBase):

    def __init__(self, base):
        super().__init__(base)
        self.CR = DAC_CR(base + 0x0)
        self.SWTRIGR = DAC_SWTRIGR(base + 0x4)
        self.DHR12R1 = DAC_DHR12R1(base + 0x8)
        self.DHR12L1 = DAC_DHR12L1(base + 0xC)
        self.DHR8R1 = DAC_DHR8R1(base + 0x10)
        self.DHR12R2 = DAC_DHR12R2(base + 0x14)
        self.DHR12L2 = DAC_DHR12L2(base + 0x18)
        self.DHR8R2 = DAC_DHR8R2(base + 0x1C)
        self.DHR12RD = DAC_DHR12RD(base + 0x20)
        self.DHR12LD = DAC_DHR12LD(base + 0x24)
        self.DHR8RD = DAC_DHR8RD(base + 0x28)
        self.DOR1 = DAC_DOR1(base + 0x2C)
        self.DOR2 = DAC_DOR2(base + 0x30)
        self.SR = DAC_SR(base + 0x34)
        self.CCR = DAC_CCR(base + 0x38)
        self.MCR = DAC_MCR(base + 0x3C)
        self.SHSR1 = DAC_SHSR1(base + 0x40)
        self.SHSR2 = DAC_SHSR2(base + 0x44)
        self.SHHR = DAC_SHHR(base + 0x48)
        self.SHRR = DAC_SHRR(base + 0x4C)
        self.STR1 = DAC_STR1(base + 0x58)
        self.STR2 = DAC_STR2(base + 0x5C)
        self.STMODR = DAC_STMODR(base + 0x60)

DAC = DAC_TypeDef(0x50000800)
DAC1 = DAC_TypeDef(0x50000800)
DAC2 = DAC_TypeDef(0x50000C00)
DAC3 = DAC_TypeDef(0x50001000)
DAC4 = DAC_TypeDef(0x50001400)

class DBGMCU_IDCODE(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.DEV_ID = BitField(self, 0x00000FFF)
        self.REV_ID = BitField(self, 0xFFFF0000)

class DBGMCU_CR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.DBG_SLEEP = BitField(self, 0x00000001)
        self.DBG_STOP = BitField(self, 0x00000002)
        self.DBG_STANDBY = BitField(self, 0x00000004)
        self.TRACE_IOEN = BitField(self, 0x00000020)
        self.TRACE_MODE = BitField(self, 0x000000C0)

class DBGMCU_APB1FZR1(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.DBG_TIM2_STOP = BitField(self, 0x00000001)
        self.DBG_TIM3_STOP = BitField(self, 0x00000002)
        self.DBG_TIM4_STOP = BitField(self, 0x00000004)
        self.DBG_TIM5_STOP = BitField(self, 0x00000008)
        self.DBG_TIM6_STOP = BitField(self, 0x00000010)
        self.DBG_TIM7_STOP = BitField(self, 0x00000020)
        self.DBG_RTC_STOP = BitField(self, 0x00000400)
        self.DBG_WWDG_STOP = BitField(self, 0x00000800)
        self.DBG_IWDG_STOP = BitField(self, 0x00001000)
        self.DBG_I2C1_STOP = BitField(self, 0x00200000)
        self.DBG_I2C2_STOP = BitField(self, 0x00400000)
        self.DBG_I2C3_STOP = BitField(self, 0x40000000)
        self.DBG_LPTIM1_STOP = BitField(self, 0x80000000)

class DBGMCU_APB1FZR2(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.DBG_I2C4_STOP = BitField(self, 0x00000002)

class DBGMCU_APB2FZ(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.DBG_TIM1_STOP = BitField(self, 0x00000800)
        self.DBG_TIM8_STOP = BitField(self, 0x00002000)
        self.DBG_TIM15_STOP = BitField(self, 0x00010000)
        self.DBG_TIM16_STOP = BitField(self, 0x00020000)
        self.DBG_TIM17_STOP = BitField(self, 0x00040000)
        self.DBG_TIM20_STOP = BitField(self, 0x00100000)
        self.DBG_HRTIM1_STOP = BitField(self, 0x04000000)

class DBGMCU_TypeDef(PeripheralBase):

    def __init__(self, base):
        super().__init__(base)
        self.IDCODE = DBGMCU_IDCODE(base + 0x0)
        self.CR = DBGMCU_CR(base + 0x4)
        self.APB1FZR1 = DBGMCU_APB1FZR1(base + 0x8)
        self.APB1FZR2 = DBGMCU_APB1FZR2(base + 0xC)
        self.APB2FZ = DBGMCU_APB2FZ(base + 0x10)

DBGMCU = DBGMCU_TypeDef(0xE0042000)

class DMA_Channel_CCR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.EN = BitField(self, 0x00000001)
        self.TCIE = BitField(self, 0x00000002)
        self.HTIE = BitField(self, 0x00000004)
        self.TEIE = BitField(self, 0x00000008)
        self.DIR = BitField(self, 0x00000010)
        self.CIRC = BitField(self, 0x00000020)
        self.PINC = BitField(self, 0x00000040)
        self.MINC = BitField(self, 0x00000080)
        self.PSIZE = BitField(self, 0x00000300)
        self.MSIZE = BitField(self, 0x00000C00)
        self.PL = BitField(self, 0x00003000)
        self.MEM2MEM = BitField(self, 0x00004000)

class DMA_Channel_CNDTR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.NDT = BitField(self, 0x0000FFFF)

class DMA_Channel_CPAR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.PA = BitField(self, 0xFFFFFFFF)

class DMA_Channel_CMAR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.MA = BitField(self, 0xFFFFFFFF)

class DMA_Channel_TypeDef(PeripheralBase):

    def __init__(self, base):
        super().__init__(base)
        self.CCR = DMA_Channel_CCR(base + 0x0)
        self.CNDTR = DMA_Channel_CNDTR(base + 0x4)
        self.CPAR = DMA_Channel_CPAR(base + 0x8)
        self.CMAR = DMA_Channel_CMAR(base + 0xC)

DMA1_Channel1 = DMA_Channel_TypeDef(0x40020008)
DMA1_Channel2 = DMA_Channel_TypeDef(0x4002001C)
DMA1_Channel3 = DMA_Channel_TypeDef(0x40020030)
DMA1_Channel4 = DMA_Channel_TypeDef(0x40020044)
DMA1_Channel5 = DMA_Channel_TypeDef(0x40020058)
DMA1_Channel6 = DMA_Channel_TypeDef(0x4002006C)
DMA1_Channel7 = DMA_Channel_TypeDef(0x40020080)
DMA1_Channel8 = DMA_Channel_TypeDef(0x40020094)
DMA2_Channel1 = DMA_Channel_TypeDef(0x40020408)
DMA2_Channel2 = DMA_Channel_TypeDef(0x4002041C)
DMA2_Channel3 = DMA_Channel_TypeDef(0x40020430)
DMA2_Channel4 = DMA_Channel_TypeDef(0x40020444)
DMA2_Channel5 = DMA_Channel_TypeDef(0x40020458)
DMA2_Channel6 = DMA_Channel_TypeDef(0x4002046C)
DMA2_Channel7 = DMA_Channel_TypeDef(0x40020480)
DMA2_Channel8 = DMA_Channel_TypeDef(0x40020494)

class DMA_ISR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.GIF1 = BitField(self, 0x00000001)
        self.TCIF1 = BitField(self, 0x00000002)
        self.HTIF1 = BitField(self, 0x00000004)
        self.TEIF1 = BitField(self, 0x00000008)
        self.GIF2 = BitField(self, 0x00000010)
        self.TCIF2 = BitField(self, 0x00000020)
        self.HTIF2 = BitField(self, 0x00000040)
        self.TEIF2 = BitField(self, 0x00000080)
        self.GIF3 = BitField(self, 0x00000100)
        self.TCIF3 = BitField(self, 0x00000200)
        self.HTIF3 = BitField(self, 0x00000400)
        self.TEIF3 = BitField(self, 0x00000800)
        self.GIF4 = BitField(self, 0x00001000)
        self.TCIF4 = BitField(self, 0x00002000)
        self.HTIF4 = BitField(self, 0x00004000)
        self.TEIF4 = BitField(self, 0x00008000)
        self.GIF5 = BitField(self, 0x00010000)
        self.TCIF5 = BitField(self, 0x00020000)
        self.HTIF5 = BitField(self, 0x00040000)
        self.TEIF5 = BitField(self, 0x00080000)
        self.GIF6 = BitField(self, 0x00100000)
        self.TCIF6 = BitField(self, 0x00200000)
        self.HTIF6 = BitField(self, 0x00400000)
        self.TEIF6 = BitField(self, 0x00800000)
        self.GIF7 = BitField(self, 0x01000000)
        self.TCIF7 = BitField(self, 0x02000000)
        self.HTIF7 = BitField(self, 0x04000000)
        self.TEIF7 = BitField(self, 0x08000000)
        self.GIF8 = BitField(self, 0x10000000)
        self.TCIF8 = BitField(self, 0x20000000)
        self.HTIF8 = BitField(self, 0x40000000)
        self.TEIF8 = BitField(self, 0x80000000)

class DMA_IFCR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.CGIF1 = BitField(self, 0x00000001)
        self.CTCIF1 = BitField(self, 0x00000002)
        self.CHTIF1 = BitField(self, 0x00000004)
        self.CTEIF1 = BitField(self, 0x00000008)
        self.CGIF2 = BitField(self, 0x00000010)
        self.CTCIF2 = BitField(self, 0x00000020)
        self.CHTIF2 = BitField(self, 0x00000040)
        self.CTEIF2 = BitField(self, 0x00000080)
        self.CGIF3 = BitField(self, 0x00000100)
        self.CTCIF3 = BitField(self, 0x00000200)
        self.CHTIF3 = BitField(self, 0x00000400)
        self.CTEIF3 = BitField(self, 0x00000800)
        self.CGIF4 = BitField(self, 0x00001000)
        self.CTCIF4 = BitField(self, 0x00002000)
        self.CHTIF4 = BitField(self, 0x00004000)
        self.CTEIF4 = BitField(self, 0x00008000)
        self.CGIF5 = BitField(self, 0x00010000)
        self.CTCIF5 = BitField(self, 0x00020000)
        self.CHTIF5 = BitField(self, 0x00040000)
        self.CTEIF5 = BitField(self, 0x00080000)
        self.CGIF6 = BitField(self, 0x00100000)
        self.CTCIF6 = BitField(self, 0x00200000)
        self.CHTIF6 = BitField(self, 0x00400000)
        self.CTEIF6 = BitField(self, 0x00800000)
        self.CGIF7 = BitField(self, 0x01000000)
        self.CTCIF7 = BitField(self, 0x02000000)
        self.CHTIF7 = BitField(self, 0x04000000)
        self.CTEIF7 = BitField(self, 0x08000000)
        self.CGIF8 = BitField(self, 0x10000000)
        self.CTCIF8 = BitField(self, 0x20000000)
        self.CHTIF8 = BitField(self, 0x40000000)
        self.CTEIF8 = BitField(self, 0x80000000)

class DMA_TypeDef(PeripheralBase):

    def __init__(self, base):
        super().__init__(base)
        self.ISR = DMA_ISR(base + 0x0)
        self.IFCR = DMA_IFCR(base + 0x4)

DMA1 = DMA_TypeDef(0x40020000)
DMA2 = DMA_TypeDef(0x40020400)

class DMAMUX_Channel_CCR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.DMAREQ_ID = BitField(self, 0x000000FF)
        self.SOIE = BitField(self, 0x00000100)
        self.EGE = BitField(self, 0x00000200)
        self.SE = BitField(self, 0x00010000)
        self.SPOL = BitField(self, 0x00060000)
        self.NBREQ = BitField(self, 0x00F80000)
        self.SYNC_ID = BitField(self, 0x1F000000)

class DMAMUX_Channel_TypeDef(PeripheralBase):

    def __init__(self, base):
        super().__init__(base)
        self.CCR = DMAMUX_Channel_CCR(base + 0x0)

DMAMUX1 = DMAMUX_Channel_TypeDef(0x40020800)
DMAMUX1_Channel0 = DMAMUX_Channel_TypeDef(0x40020800)
DMAMUX1_Channel1 = DMAMUX_Channel_TypeDef(0x40020804)
DMAMUX1_Channel2 = DMAMUX_Channel_TypeDef(0x40020808)
DMAMUX1_Channel3 = DMAMUX_Channel_TypeDef(0x4002080C)
DMAMUX1_Channel4 = DMAMUX_Channel_TypeDef(0x40020810)
DMAMUX1_Channel5 = DMAMUX_Channel_TypeDef(0x40020814)
DMAMUX1_Channel6 = DMAMUX_Channel_TypeDef(0x40020818)
DMAMUX1_Channel7 = DMAMUX_Channel_TypeDef(0x4002081C)
DMAMUX1_Channel8 = DMAMUX_Channel_TypeDef(0x40020820)
DMAMUX1_Channel9 = DMAMUX_Channel_TypeDef(0x40020824)
DMAMUX1_Channel10 = DMAMUX_Channel_TypeDef(0x40020828)
DMAMUX1_Channel11 = DMAMUX_Channel_TypeDef(0x4002082C)
DMAMUX1_Channel12 = DMAMUX_Channel_TypeDef(0x40020830)
DMAMUX1_Channel13 = DMAMUX_Channel_TypeDef(0x40020834)
DMAMUX1_Channel14 = DMAMUX_Channel_TypeDef(0x40020838)
DMAMUX1_Channel15 = DMAMUX_Channel_TypeDef(0x4002083C)

class DMAMUX_ChannelStatus_CSR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.SOF0 = BitField(self, 0x00000001)
        self.SOF1 = BitField(self, 0x00000002)
        self.SOF2 = BitField(self, 0x00000004)
        self.SOF3 = BitField(self, 0x00000008)
        self.SOF4 = BitField(self, 0x00000010)
        self.SOF5 = BitField(self, 0x00000020)
        self.SOF6 = BitField(self, 0x00000040)
        self.SOF7 = BitField(self, 0x00000080)
        self.SOF8 = BitField(self, 0x00000100)
        self.SOF9 = BitField(self, 0x00000200)
        self.SOF10 = BitField(self, 0x00000400)
        self.SOF11 = BitField(self, 0x00000800)
        self.SOF12 = BitField(self, 0x00001000)
        self.SOF13 = BitField(self, 0x00002000)
        self.SOF14 = BitField(self, 0x00004000)
        self.SOF15 = BitField(self, 0x00008000)

class DMAMUX_ChannelStatus_CFR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.CSOF0 = BitField(self, 0x00000001)
        self.CSOF1 = BitField(self, 0x00000002)
        self.CSOF2 = BitField(self, 0x00000004)
        self.CSOF3 = BitField(self, 0x00000008)
        self.CSOF4 = BitField(self, 0x00000010)
        self.CSOF5 = BitField(self, 0x00000020)
        self.CSOF6 = BitField(self, 0x00000040)
        self.CSOF7 = BitField(self, 0x00000080)
        self.CSOF8 = BitField(self, 0x00000100)
        self.CSOF9 = BitField(self, 0x00000200)
        self.CSOF10 = BitField(self, 0x00000400)
        self.CSOF11 = BitField(self, 0x00000800)
        self.CSOF12 = BitField(self, 0x00001000)
        self.CSOF13 = BitField(self, 0x00002000)
        self.CSOF14 = BitField(self, 0x00004000)
        self.CSOF15 = BitField(self, 0x00008000)

class DMAMUX_ChannelStatus_TypeDef(PeripheralBase):

    def __init__(self, base):
        super().__init__(base)
        self.CSR = DMAMUX_ChannelStatus_CSR(base + 0x0)
        self.CFR = DMAMUX_ChannelStatus_CFR(base + 0x4)

DMAMUX1_ChannelStatus = DMAMUX_ChannelStatus_TypeDef(0x40020880)

class DMAMUX_RequestGen_RGCR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.SIG_ID = BitField(self, 0x0000001F)
        self.OIE = BitField(self, 0x00000100)
        self.GE = BitField(self, 0x00010000)
        self.GPOL = BitField(self, 0x00060000)
        self.GNBREQ = BitField(self, 0x00F80000)

class DMAMUX_RequestGen_TypeDef(PeripheralBase):

    def __init__(self, base):
        super().__init__(base)
        self.RGCR = DMAMUX_RequestGen_RGCR(base + 0x0)

DMAMUX1_RequestGenerator0 = DMAMUX_RequestGen_TypeDef(0x40020900)
DMAMUX1_RequestGenerator1 = DMAMUX_RequestGen_TypeDef(0x40020904)
DMAMUX1_RequestGenerator2 = DMAMUX_RequestGen_TypeDef(0x40020908)
DMAMUX1_RequestGenerator3 = DMAMUX_RequestGen_TypeDef(0x4002090C)

class DMAMUX_RequestGenStatus_RGSR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.OF0 = BitField(self, 0x00000001)
        self.OF1 = BitField(self, 0x00000002)
        self.OF2 = BitField(self, 0x00000004)
        self.OF3 = BitField(self, 0x00000008)

class DMAMUX_RequestGenStatus_RGCFR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.COF0 = BitField(self, 0x00000001)
        self.COF1 = BitField(self, 0x00000002)
        self.COF2 = BitField(self, 0x00000004)
        self.COF3 = BitField(self, 0x00000008)

class DMAMUX_RequestGenStatus_TypeDef(PeripheralBase):

    def __init__(self, base):
        super().__init__(base)
        self.RGSR = DMAMUX_RequestGenStatus_RGSR(base + 0x0)
        self.RGCFR = DMAMUX_RequestGenStatus_RGCFR(base + 0x4)

DMAMUX1_RequestGenStatus = DMAMUX_RequestGenStatus_TypeDef(0x40020940)

class EXTI_IMR1(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.IM0 = BitField(self, 0x00000001)
        self.IM1 = BitField(self, 0x00000002)
        self.IM2 = BitField(self, 0x00000004)
        self.IM3 = BitField(self, 0x00000008)
        self.IM4 = BitField(self, 0x00000010)
        self.IM5 = BitField(self, 0x00000020)
        self.IM6 = BitField(self, 0x00000040)
        self.IM7 = BitField(self, 0x00000080)
        self.IM8 = BitField(self, 0x00000100)
        self.IM9 = BitField(self, 0x00000200)
        self.IM10 = BitField(self, 0x00000400)
        self.IM11 = BitField(self, 0x00000800)
        self.IM12 = BitField(self, 0x00001000)
        self.IM13 = BitField(self, 0x00002000)
        self.IM14 = BitField(self, 0x00004000)
        self.IM15 = BitField(self, 0x00008000)
        self.IM16 = BitField(self, 0x00010000)
        self.IM17 = BitField(self, 0x00020000)
        self.IM18 = BitField(self, 0x00040000)
        self.IM19 = BitField(self, 0x00080000)
        self.IM20 = BitField(self, 0x00100000)
        self.IM21 = BitField(self, 0x00200000)
        self.IM22 = BitField(self, 0x00400000)
        self.IM23 = BitField(self, 0x00800000)
        self.IM24 = BitField(self, 0x01000000)
        self.IM25 = BitField(self, 0x02000000)
        self.IM26 = BitField(self, 0x04000000)
        self.IM27 = BitField(self, 0x08000000)
        self.IM28 = BitField(self, 0x10000000)
        self.IM29 = BitField(self, 0x20000000)
        self.IM30 = BitField(self, 0x40000000)
        self.IM31 = BitField(self, 0x80000000)
        self.IM = BitField(self, 0xFFFFFFFF)

class EXTI_EMR1(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.EM0 = BitField(self, 0x00000001)
        self.EM1 = BitField(self, 0x00000002)
        self.EM2 = BitField(self, 0x00000004)
        self.EM3 = BitField(self, 0x00000008)
        self.EM4 = BitField(self, 0x00000010)
        self.EM5 = BitField(self, 0x00000020)
        self.EM6 = BitField(self, 0x00000040)
        self.EM7 = BitField(self, 0x00000080)
        self.EM8 = BitField(self, 0x00000100)
        self.EM9 = BitField(self, 0x00000200)
        self.EM10 = BitField(self, 0x00000400)
        self.EM11 = BitField(self, 0x00000800)
        self.EM12 = BitField(self, 0x00001000)
        self.EM13 = BitField(self, 0x00002000)
        self.EM14 = BitField(self, 0x00004000)
        self.EM15 = BitField(self, 0x00008000)
        self.EM16 = BitField(self, 0x00010000)
        self.EM17 = BitField(self, 0x00020000)
        self.EM18 = BitField(self, 0x00040000)
        self.EM19 = BitField(self, 0x00080000)
        self.EM20 = BitField(self, 0x00100000)
        self.EM21 = BitField(self, 0x00200000)
        self.EM22 = BitField(self, 0x00400000)
        self.EM23 = BitField(self, 0x00800000)
        self.EM24 = BitField(self, 0x01000000)
        self.EM25 = BitField(self, 0x02000000)
        self.EM26 = BitField(self, 0x04000000)
        self.EM27 = BitField(self, 0x08000000)
        self.EM28 = BitField(self, 0x10000000)
        self.EM29 = BitField(self, 0x20000000)
        self.EM30 = BitField(self, 0x40000000)
        self.EM31 = BitField(self, 0x80000000)

class EXTI_RTSR1(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.RT0 = BitField(self, 0x00000001)
        self.RT1 = BitField(self, 0x00000002)
        self.RT2 = BitField(self, 0x00000004)
        self.RT3 = BitField(self, 0x00000008)
        self.RT4 = BitField(self, 0x00000010)
        self.RT5 = BitField(self, 0x00000020)
        self.RT6 = BitField(self, 0x00000040)
        self.RT7 = BitField(self, 0x00000080)
        self.RT8 = BitField(self, 0x00000100)
        self.RT9 = BitField(self, 0x00000200)
        self.RT10 = BitField(self, 0x00000400)
        self.RT11 = BitField(self, 0x00000800)
        self.RT12 = BitField(self, 0x00001000)
        self.RT13 = BitField(self, 0x00002000)
        self.RT14 = BitField(self, 0x00004000)
        self.RT15 = BitField(self, 0x00008000)
        self.RT16 = BitField(self, 0x00010000)
        self.RT17 = BitField(self, 0x00020000)
        self.RT19 = BitField(self, 0x00080000)
        self.RT20 = BitField(self, 0x00100000)
        self.RT21 = BitField(self, 0x00200000)
        self.RT22 = BitField(self, 0x00400000)
        self.RT29 = BitField(self, 0x20000000)
        self.RT30 = BitField(self, 0x40000000)
        self.RT31 = BitField(self, 0x80000000)

class EXTI_FTSR1(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.FT0 = BitField(self, 0x00000001)
        self.FT1 = BitField(self, 0x00000002)
        self.FT2 = BitField(self, 0x00000004)
        self.FT3 = BitField(self, 0x00000008)
        self.FT4 = BitField(self, 0x00000010)
        self.FT5 = BitField(self, 0x00000020)
        self.FT6 = BitField(self, 0x00000040)
        self.FT7 = BitField(self, 0x00000080)
        self.FT8 = BitField(self, 0x00000100)
        self.FT9 = BitField(self, 0x00000200)
        self.FT10 = BitField(self, 0x00000400)
        self.FT11 = BitField(self, 0x00000800)
        self.FT12 = BitField(self, 0x00001000)
        self.FT13 = BitField(self, 0x00002000)
        self.FT14 = BitField(self, 0x00004000)
        self.FT15 = BitField(self, 0x00008000)
        self.FT16 = BitField(self, 0x00010000)
        self.FT17 = BitField(self, 0x00020000)
        self.FT19 = BitField(self, 0x00080000)
        self.FT20 = BitField(self, 0x00100000)
        self.FT21 = BitField(self, 0x00200000)
        self.FT22 = BitField(self, 0x00400000)
        self.FT29 = BitField(self, 0x20000000)
        self.FT30 = BitField(self, 0x40000000)
        self.FT31 = BitField(self, 0x80000000)

class EXTI_SWIER1(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.SWI0 = BitField(self, 0x00000001)
        self.SWI1 = BitField(self, 0x00000002)
        self.SWI2 = BitField(self, 0x00000004)
        self.SWI3 = BitField(self, 0x00000008)
        self.SWI4 = BitField(self, 0x00000010)
        self.SWI5 = BitField(self, 0x00000020)
        self.SWI6 = BitField(self, 0x00000040)
        self.SWI7 = BitField(self, 0x00000080)
        self.SWI8 = BitField(self, 0x00000100)
        self.SWI9 = BitField(self, 0x00000200)
        self.SWI10 = BitField(self, 0x00000400)
        self.SWI11 = BitField(self, 0x00000800)
        self.SWI12 = BitField(self, 0x00001000)
        self.SWI13 = BitField(self, 0x00002000)
        self.SWI14 = BitField(self, 0x00004000)
        self.SWI15 = BitField(self, 0x00008000)
        self.SWI16 = BitField(self, 0x00010000)
        self.SWI17 = BitField(self, 0x00020000)
        self.SWI19 = BitField(self, 0x00080000)
        self.SWI20 = BitField(self, 0x00100000)
        self.SWI21 = BitField(self, 0x00200000)
        self.SWI22 = BitField(self, 0x00400000)
        self.SWI29 = BitField(self, 0x20000000)
        self.SWI30 = BitField(self, 0x40000000)
        self.SWI31 = BitField(self, 0x80000000)

class EXTI_PR1(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.PIF0 = BitField(self, 0x00000001)
        self.PIF1 = BitField(self, 0x00000002)
        self.PIF2 = BitField(self, 0x00000004)
        self.PIF3 = BitField(self, 0x00000008)
        self.PIF4 = BitField(self, 0x00000010)
        self.PIF5 = BitField(self, 0x00000020)
        self.PIF6 = BitField(self, 0x00000040)
        self.PIF7 = BitField(self, 0x00000080)
        self.PIF8 = BitField(self, 0x00000100)
        self.PIF9 = BitField(self, 0x00000200)
        self.PIF10 = BitField(self, 0x00000400)
        self.PIF11 = BitField(self, 0x00000800)
        self.PIF12 = BitField(self, 0x00001000)
        self.PIF13 = BitField(self, 0x00002000)
        self.PIF14 = BitField(self, 0x00004000)
        self.PIF15 = BitField(self, 0x00008000)
        self.PIF16 = BitField(self, 0x00010000)
        self.PIF17 = BitField(self, 0x00020000)
        self.PIF19 = BitField(self, 0x00080000)
        self.PIF20 = BitField(self, 0x00100000)
        self.PIF21 = BitField(self, 0x00200000)
        self.PIF22 = BitField(self, 0x00400000)
        self.PIF29 = BitField(self, 0x20000000)
        self.PIF30 = BitField(self, 0x40000000)
        self.PIF31 = BitField(self, 0x80000000)

class EXTI_IMR2(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.IM32 = BitField(self, 0x00000001)
        self.IM33 = BitField(self, 0x00000002)
        self.IM34 = BitField(self, 0x00000004)
        self.IM35 = BitField(self, 0x00000008)
        self.IM36 = BitField(self, 0x00000010)
        self.IM37 = BitField(self, 0x00000020)
        self.IM38 = BitField(self, 0x00000040)
        self.IM39 = BitField(self, 0x00000080)
        self.IM40 = BitField(self, 0x00000100)
        self.IM41 = BitField(self, 0x00000200)
        self.IM42 = BitField(self, 0x00000400)
        self.IM = BitField(self, 0x000007FF)

class EXTI_EMR2(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.EM32 = BitField(self, 0x00000001)
        self.EM33 = BitField(self, 0x00000002)
        self.EM34 = BitField(self, 0x00000004)
        self.EM35 = BitField(self, 0x00000008)
        self.EM36 = BitField(self, 0x00000010)
        self.EM37 = BitField(self, 0x00000020)
        self.EM38 = BitField(self, 0x00000040)
        self.EM39 = BitField(self, 0x00000080)
        self.EM40 = BitField(self, 0x00000100)
        self.EM41 = BitField(self, 0x00000200)
        self.EM42 = BitField(self, 0x00000400)
        self.EM = BitField(self, 0x000007FF)

class EXTI_RTSR2(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.RT32 = BitField(self, 0x00000001)
        self.RT33 = BitField(self, 0x00000002)
        self.RT38 = BitField(self, 0x00000040)
        self.RT39 = BitField(self, 0x00000080)
        self.RT40 = BitField(self, 0x00000100)
        self.RT41 = BitField(self, 0x00000200)

class EXTI_FTSR2(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.FT32 = BitField(self, 0x00000001)
        self.FT33 = BitField(self, 0x00000002)
        self.FT38 = BitField(self, 0x00000040)
        self.FT39 = BitField(self, 0x00000080)
        self.FT40 = BitField(self, 0x00000100)
        self.FT41 = BitField(self, 0x00000200)

class EXTI_SWIER2(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.SWI32 = BitField(self, 0x00000001)
        self.SWI33 = BitField(self, 0x00000002)
        self.SWI38 = BitField(self, 0x00000040)
        self.SWI39 = BitField(self, 0x00000080)
        self.SWI40 = BitField(self, 0x00000100)
        self.SWI41 = BitField(self, 0x00000200)

class EXTI_PR2(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.PIF32 = BitField(self, 0x00000001)
        self.PIF33 = BitField(self, 0x00000002)
        self.PIF38 = BitField(self, 0x00000040)
        self.PIF39 = BitField(self, 0x00000080)
        self.PIF40 = BitField(self, 0x00000100)
        self.PIF41 = BitField(self, 0x00000200)

class EXTI_TypeDef(PeripheralBase):

    def __init__(self, base):
        super().__init__(base)
        self.IMR1 = EXTI_IMR1(base + 0x0)
        self.EMR1 = EXTI_EMR1(base + 0x4)
        self.RTSR1 = EXTI_RTSR1(base + 0x8)
        self.FTSR1 = EXTI_FTSR1(base + 0xC)
        self.SWIER1 = EXTI_SWIER1(base + 0x10)
        self.PR1 = EXTI_PR1(base + 0x14)
        self.IMR2 = EXTI_IMR2(base + 0x20)
        self.EMR2 = EXTI_EMR2(base + 0x24)
        self.RTSR2 = EXTI_RTSR2(base + 0x28)
        self.FTSR2 = EXTI_FTSR2(base + 0x2C)
        self.SWIER2 = EXTI_SWIER2(base + 0x30)
        self.PR2 = EXTI_PR2(base + 0x34)

EXTI = EXTI_TypeDef(0x40010400)

class FLASH_ACR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.LATENCY = BitField(self, 0x0000000F)
        self.PRFTEN = BitField(self, 0x00000100)
        self.ICEN = BitField(self, 0x00000200)
        self.DCEN = BitField(self, 0x00000400)
        self.ICRST = BitField(self, 0x00000800)
        self.DCRST = BitField(self, 0x00001000)
        self.RUN_PD = BitField(self, 0x00002000)
        self.SLEEP_PD = BitField(self, 0x00004000)
        self.DBG_SWEN = BitField(self, 0x00040000)

class FLASH_PDKEYR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)

class FLASH_KEYR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)

class FLASH_OPTKEYR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)

class FLASH_SR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.EOP = BitField(self, 0x00000001)
        self.OPERR = BitField(self, 0x00000002)
        self.PROGERR = BitField(self, 0x00000008)
        self.WRPERR = BitField(self, 0x00000010)
        self.PGAERR = BitField(self, 0x00000020)
        self.SIZERR = BitField(self, 0x00000040)
        self.PGSERR = BitField(self, 0x00000080)
        self.MISERR = BitField(self, 0x00000100)
        self.FASTERR = BitField(self, 0x00000200)
        self.RDERR = BitField(self, 0x00004000)
        self.OPTVERR = BitField(self, 0x00008000)
        self.BSY = BitField(self, 0x00010000)

class FLASH_CR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.PG = BitField(self, 0x00000001)
        self.PER = BitField(self, 0x00000002)
        self.MER1 = BitField(self, 0x00000004)
        self.PNB = BitField(self, 0x000003F8)
        self.BKER = BitField(self, 0x00000800)
        self.MER2 = BitField(self, 0x00008000)
        self.STRT = BitField(self, 0x00010000)
        self.OPTSTRT = BitField(self, 0x00020000)
        self.FSTPG = BitField(self, 0x00040000)
        self.EOPIE = BitField(self, 0x01000000)
        self.ERRIE = BitField(self, 0x02000000)
        self.RDERRIE = BitField(self, 0x04000000)
        self.OBL_LAUNCH = BitField(self, 0x08000000)
        self.SEC_PROT1 = BitField(self, 0x10000000)
        self.SEC_PROT2 = BitField(self, 0x20000000)
        self.OPTLOCK = BitField(self, 0x40000000)
        self.LOCK = BitField(self, 0x80000000)

class FLASH_ECCR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.ADDR_ECC = BitField(self, 0x0007FFFF)
        self.BK_ECC = BitField(self, 0x00200000)
        self.SYSF_ECC = BitField(self, 0x00400000)
        self.ECCIE = BitField(self, 0x01000000)
        self.ECCC2 = BitField(self, 0x10000000)
        self.ECCD2 = BitField(self, 0x20000000)
        self.ECCC = BitField(self, 0x40000000)
        self.ECCD = BitField(self, 0x80000000)

class FLASH_OPTR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.RDP = BitField(self, 0x000000FF)
        self.BOR_LEV = BitField(self, 0x00000700)
        self.nRST_STOP = BitField(self, 0x00001000)
        self.nRST_STDBY = BitField(self, 0x00002000)
        self.nRST_SHDW = BitField(self, 0x00004000)
        self.IWDG_SW = BitField(self, 0x00010000)
        self.IWDG_STOP = BitField(self, 0x00020000)
        self.IWDG_STDBY = BitField(self, 0x00040000)
        self.WWDG_SW = BitField(self, 0x00080000)
        self.BFB2 = BitField(self, 0x00100000)
        self.DBANK = BitField(self, 0x00400000)
        self.nBOOT1 = BitField(self, 0x00800000)
        self.SRAM_PE = BitField(self, 0x01000000)
        self.CCMSRAM_RST = BitField(self, 0x02000000)
        self.nSWBOOT0 = BitField(self, 0x04000000)
        self.nBOOT0 = BitField(self, 0x08000000)
        self.NRST_MODE = BitField(self, 0x30000000)
        self.IRHEN = BitField(self, 0x40000000)

class FLASH_PCROP1SR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.PCROP1_STRT = BitField(self, 0x00007FFF)

class FLASH_PCROP1ER(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.PCROP1_END = BitField(self, 0x00007FFF)
        self.PCROP_RDP = BitField(self, 0x80000000)

class FLASH_WRP1AR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.WRP1A_STRT = BitField(self, 0x0000007F)
        self.WRP1A_END = BitField(self, 0x007F0000)

class FLASH_WRP1BR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.WRP1B_STRT = BitField(self, 0x0000007F)
        self.WRP1B_END = BitField(self, 0x007F0000)

class FLASH_PCROP2SR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.PCROP2_STRT = BitField(self, 0x00007FFF)

class FLASH_PCROP2ER(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.PCROP2_END = BitField(self, 0x00007FFF)

class FLASH_WRP2AR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.WRP2A_STRT = BitField(self, 0x0000007F)
        self.WRP2A_END = BitField(self, 0x007F0000)

class FLASH_WRP2BR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.WRP2B_STRT = BitField(self, 0x0000007F)
        self.WRP2B_END = BitField(self, 0x007F0000)

class FLASH_SEC1R(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.SEC_SIZE1 = BitField(self, 0x000000FF)
        self.BOOT_LOCK = BitField(self, 0x00010000)

class FLASH_SEC2R(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.SEC_SIZE2 = BitField(self, 0x000000FF)

class FLASH_TypeDef(PeripheralBase):

    def __init__(self, base):
        super().__init__(base)
        self.ACR = FLASH_ACR(base + 0x0)
        self.PDKEYR = FLASH_PDKEYR(base + 0x4)
        self.KEYR = FLASH_KEYR(base + 0x8)
        self.OPTKEYR = FLASH_OPTKEYR(base + 0xC)
        self.SR = FLASH_SR(base + 0x10)
        self.CR = FLASH_CR(base + 0x14)
        self.ECCR = FLASH_ECCR(base + 0x18)
        self.OPTR = FLASH_OPTR(base + 0x20)
        self.PCROP1SR = FLASH_PCROP1SR(base + 0x24)
        self.PCROP1ER = FLASH_PCROP1ER(base + 0x28)
        self.WRP1AR = FLASH_WRP1AR(base + 0x2C)
        self.WRP1BR = FLASH_WRP1BR(base + 0x30)
        self.PCROP2SR = FLASH_PCROP2SR(base + 0x44)
        self.PCROP2ER = FLASH_PCROP2ER(base + 0x48)
        self.WRP2AR = FLASH_WRP2AR(base + 0x4C)
        self.WRP2BR = FLASH_WRP2BR(base + 0x50)
        self.SEC1R = FLASH_SEC1R(base + 0x70)
        self.SEC2R = FLASH_SEC2R(base + 0x74)

FLASH = FLASH_TypeDef(0x40022000)

class FMAC_X1BUFCFG(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.X1_BASE = BitField(self, 0x000000FF)
        self.X1_BUF_SIZE = BitField(self, 0x0000FF00)
        self.FULL_WM = BitField(self, 0x03000000)

class FMAC_X2BUFCFG(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.X2_BASE = BitField(self, 0x000000FF)
        self.X2_BUF_SIZE = BitField(self, 0x0000FF00)

class FMAC_YBUFCFG(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.Y_BASE = BitField(self, 0x000000FF)
        self.Y_BUF_SIZE = BitField(self, 0x0000FF00)
        self.EMPTY_WM = BitField(self, 0x03000000)

class FMAC_PARAM(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.P = BitField(self, 0x000000FF)
        self.Q = BitField(self, 0x0000FF00)
        self.R = BitField(self, 0x00FF0000)
        self.FUNC = BitField(self, 0x7F000000)
        self.START = BitField(self, 0x80000000)

class FMAC_CR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.RIEN = BitField(self, 0x00000001)
        self.WIEN = BitField(self, 0x00000002)
        self.OVFLIEN = BitField(self, 0x00000004)
        self.UNFLIEN = BitField(self, 0x00000008)
        self.SATIEN = BitField(self, 0x00000010)
        self.DMAREN = BitField(self, 0x00000100)
        self.DMAWEN = BitField(self, 0x00000200)
        self.CLIPEN = BitField(self, 0x00008000)
        self.RESET = BitField(self, 0x00010000)

class FMAC_SR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.YEMPTY = BitField(self, 0x00000001)
        self.X1FULL = BitField(self, 0x00000002)
        self.OVFL = BitField(self, 0x00000100)
        self.UNFL = BitField(self, 0x00000200)
        self.SAT = BitField(self, 0x00000400)

class FMAC_WDATA(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.WDATA = BitField(self, 0x0000FFFF)

class FMAC_RDATA(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.RDATA = BitField(self, 0x0000FFFF)

class FMAC_TypeDef(PeripheralBase):

    def __init__(self, base):
        super().__init__(base)
        self.X1BUFCFG = FMAC_X1BUFCFG(base + 0x0)
        self.X2BUFCFG = FMAC_X2BUFCFG(base + 0x4)
        self.YBUFCFG = FMAC_YBUFCFG(base + 0x8)
        self.PARAM = FMAC_PARAM(base + 0xC)
        self.CR = FMAC_CR(base + 0x10)
        self.SR = FMAC_SR(base + 0x14)
        self.WDATA = FMAC_WDATA(base + 0x18)
        self.RDATA = FMAC_RDATA(base + 0x1C)

FMAC = FMAC_TypeDef(0x40021400)

class FMC_Bank1_BTCR0(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)

class FMC_Bank1_BTCR1(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)

class FMC_Bank1_BTCR2(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)

class FMC_Bank1_BTCR3(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)

class FMC_Bank1_BTCR4(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)

class FMC_Bank1_BTCR5(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)

class FMC_Bank1_BTCR6(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)

class FMC_Bank1_BTCR7(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)

class FMC_Bank1_PCSCNTR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.CSCOUNT = BitField(self, 0x0000FFFF)
        self.CNTB1EN = BitField(self, 0x00010000)
        self.CNTB2EN = BitField(self, 0x00020000)
        self.CNTB3EN = BitField(self, 0x00040000)
        self.CNTB4EN = BitField(self, 0x00080000)

class FMC_Bank1_TypeDef(PeripheralBase):

    def __init__(self, base):
        super().__init__(base)
        self.BTCR0 = FMC_Bank1_BTCR0(base + 0x0)
        self.BTCR1 = FMC_Bank1_BTCR1(base + 0x4)
        self.BTCR2 = FMC_Bank1_BTCR2(base + 0x8)
        self.BTCR3 = FMC_Bank1_BTCR3(base + 0xC)
        self.BTCR4 = FMC_Bank1_BTCR4(base + 0x10)
        self.BTCR5 = FMC_Bank1_BTCR5(base + 0x14)
        self.BTCR6 = FMC_Bank1_BTCR6(base + 0x18)
        self.BTCR7 = FMC_Bank1_BTCR7(base + 0x1C)
        self.PCSCNTR = FMC_Bank1_PCSCNTR(base + 0x20)

FMC_Bank1_R = FMC_Bank1_TypeDef(0xA0000000)

class FMC_Bank1E_BWTR0(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.ADDSET = BitField(self, 0x0000000F)
        self.ADDHLD = BitField(self, 0x000000F0)
        self.DATAST = BitField(self, 0x0000FF00)
        self.BUSTURN = BitField(self, 0x000F0000)
        self.ACCMOD = BitField(self, 0x30000000)
        self.DATAHLD = BitField(self, 0xC0000000)

class FMC_Bank1E_BWTR1(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)

class FMC_Bank1E_BWTR2(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)

class FMC_Bank1E_BWTR3(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)

class FMC_Bank1E_BWTR4(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)

class FMC_Bank1E_BWTR5(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)

class FMC_Bank1E_BWTR6(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)

class FMC_Bank1E_TypeDef(PeripheralBase):

    def __init__(self, base):
        super().__init__(base)
        self.BWTR0 = FMC_Bank1E_BWTR0(base + 0x0)
        self.BWTR1 = FMC_Bank1E_BWTR1(base + 0x4)
        self.BWTR2 = FMC_Bank1E_BWTR2(base + 0x8)
        self.BWTR3 = FMC_Bank1E_BWTR3(base + 0xC)
        self.BWTR4 = FMC_Bank1E_BWTR4(base + 0x10)
        self.BWTR5 = FMC_Bank1E_BWTR5(base + 0x14)
        self.BWTR6 = FMC_Bank1E_BWTR6(base + 0x18)

FMC_Bank1E_R = FMC_Bank1E_TypeDef(0xA0000104)

class FMC_Bank3_PCR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.PWAITEN = BitField(self, 0x00000002)
        self.PBKEN = BitField(self, 0x00000004)
        self.PTYP = BitField(self, 0x00000008)
        self.PWID = BitField(self, 0x00000030)
        self.ECCEN = BitField(self, 0x00000040)
        self.TCLR = BitField(self, 0x00001E00)
        self.TAR = BitField(self, 0x0001E000)
        self.ECCPS = BitField(self, 0x000E0000)

class FMC_Bank3_SR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.IRS = BitField(self, 0x00000001)
        self.ILS = BitField(self, 0x00000002)
        self.IFS = BitField(self, 0x00000004)
        self.IREN = BitField(self, 0x00000008)
        self.ILEN = BitField(self, 0x00000010)
        self.IFEN = BitField(self, 0x00000020)
        self.FEMPT = BitField(self, 0x00000040)

class FMC_Bank3_PMEM(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.MEMSET = BitField(self, 0x000000FF)
        self.MEMWAIT = BitField(self, 0x0000FF00)
        self.MEMHOLD = BitField(self, 0x00FF0000)
        self.MEMHIZ = BitField(self, 0xFF000000)

class FMC_Bank3_PATT(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.ATTSET = BitField(self, 0x000000FF)
        self.ATTWAIT = BitField(self, 0x0000FF00)
        self.ATTHOLD = BitField(self, 0x00FF0000)
        self.ATTHIZ = BitField(self, 0xFF000000)

class FMC_Bank3_ECCR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.ECC = BitField(self, 0xFFFFFFFF)

class FMC_Bank3_TypeDef(PeripheralBase):

    def __init__(self, base):
        super().__init__(base)
        self.PCR = FMC_Bank3_PCR(base + 0x0)
        self.SR = FMC_Bank3_SR(base + 0x4)
        self.PMEM = FMC_Bank3_PMEM(base + 0x8)
        self.PATT = FMC_Bank3_PATT(base + 0xC)
        self.ECCR = FMC_Bank3_ECCR(base + 0x14)

FMC_Bank3_R = FMC_Bank3_TypeDef(0xA0000080)

class GPIO_MODER(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.MODE0 = BitField(self, 0x00000003)
        self.MODE1 = BitField(self, 0x0000000C)
        self.MODE2 = BitField(self, 0x00000030)
        self.MODE3 = BitField(self, 0x000000C0)
        self.MODE4 = BitField(self, 0x00000300)
        self.MODE5 = BitField(self, 0x00000C00)
        self.MODE6 = BitField(self, 0x00003000)
        self.MODE7 = BitField(self, 0x0000C000)
        self.MODE8 = BitField(self, 0x00030000)
        self.MODE9 = BitField(self, 0x000C0000)
        self.MODE10 = BitField(self, 0x00300000)
        self.MODE11 = BitField(self, 0x00C00000)
        self.MODE12 = BitField(self, 0x03000000)
        self.MODE13 = BitField(self, 0x0C000000)
        self.MODE14 = BitField(self, 0x30000000)
        self.MODE15 = BitField(self, 0xC0000000)

class GPIO_OTYPER(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.OT0 = BitField(self, 0x00000001)
        self.OT1 = BitField(self, 0x00000002)
        self.OT2 = BitField(self, 0x00000004)
        self.OT3 = BitField(self, 0x00000008)
        self.OT4 = BitField(self, 0x00000010)
        self.OT5 = BitField(self, 0x00000020)
        self.OT6 = BitField(self, 0x00000040)
        self.OT7 = BitField(self, 0x00000080)
        self.OT8 = BitField(self, 0x00000100)
        self.OT9 = BitField(self, 0x00000200)
        self.OT10 = BitField(self, 0x00000400)
        self.OT11 = BitField(self, 0x00000800)
        self.OT12 = BitField(self, 0x00001000)
        self.OT13 = BitField(self, 0x00002000)
        self.OT14 = BitField(self, 0x00004000)
        self.OT15 = BitField(self, 0x00008000)

class GPIO_OSPEEDR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.OSPEED0 = BitField(self, 0x00000003)
        self.OSPEED1 = BitField(self, 0x0000000C)
        self.OSPEED2 = BitField(self, 0x00000030)
        self.OSPEED3 = BitField(self, 0x000000C0)
        self.OSPEED4 = BitField(self, 0x00000300)
        self.OSPEED5 = BitField(self, 0x00000C00)
        self.OSPEED6 = BitField(self, 0x00003000)
        self.OSPEED7 = BitField(self, 0x0000C000)
        self.OSPEED8 = BitField(self, 0x00030000)
        self.OSPEED9 = BitField(self, 0x000C0000)
        self.OSPEED10 = BitField(self, 0x00300000)
        self.OSPEED11 = BitField(self, 0x00C00000)
        self.OSPEED12 = BitField(self, 0x03000000)
        self.OSPEED13 = BitField(self, 0x0C000000)
        self.OSPEED14 = BitField(self, 0x30000000)
        self.OSPEED15 = BitField(self, 0xC0000000)

class GPIO_PUPDR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.PUPD0 = BitField(self, 0x00000003)
        self.PUPD1 = BitField(self, 0x0000000C)
        self.PUPD2 = BitField(self, 0x00000030)
        self.PUPD3 = BitField(self, 0x000000C0)
        self.PUPD4 = BitField(self, 0x00000300)
        self.PUPD5 = BitField(self, 0x00000C00)
        self.PUPD6 = BitField(self, 0x00003000)
        self.PUPD7 = BitField(self, 0x0000C000)
        self.PUPD8 = BitField(self, 0x00030000)
        self.PUPD9 = BitField(self, 0x000C0000)
        self.PUPD10 = BitField(self, 0x00300000)
        self.PUPD11 = BitField(self, 0x00C00000)
        self.PUPD12 = BitField(self, 0x03000000)
        self.PUPD13 = BitField(self, 0x0C000000)
        self.PUPD14 = BitField(self, 0x30000000)
        self.PUPD15 = BitField(self, 0xC0000000)

class GPIO_IDR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.ID0 = BitField(self, 0x00000001)
        self.ID1 = BitField(self, 0x00000002)
        self.ID2 = BitField(self, 0x00000004)
        self.ID3 = BitField(self, 0x00000008)
        self.ID4 = BitField(self, 0x00000010)
        self.ID5 = BitField(self, 0x00000020)
        self.ID6 = BitField(self, 0x00000040)
        self.ID7 = BitField(self, 0x00000080)
        self.ID8 = BitField(self, 0x00000100)
        self.ID9 = BitField(self, 0x00000200)
        self.ID10 = BitField(self, 0x00000400)
        self.ID11 = BitField(self, 0x00000800)
        self.ID12 = BitField(self, 0x00001000)
        self.ID13 = BitField(self, 0x00002000)
        self.ID14 = BitField(self, 0x00004000)
        self.ID15 = BitField(self, 0x00008000)

class GPIO_ODR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.OD0 = BitField(self, 0x00000001)
        self.OD1 = BitField(self, 0x00000002)
        self.OD2 = BitField(self, 0x00000004)
        self.OD3 = BitField(self, 0x00000008)
        self.OD4 = BitField(self, 0x00000010)
        self.OD5 = BitField(self, 0x00000020)
        self.OD6 = BitField(self, 0x00000040)
        self.OD7 = BitField(self, 0x00000080)
        self.OD8 = BitField(self, 0x00000100)
        self.OD9 = BitField(self, 0x00000200)
        self.OD10 = BitField(self, 0x00000400)
        self.OD11 = BitField(self, 0x00000800)
        self.OD12 = BitField(self, 0x00001000)
        self.OD13 = BitField(self, 0x00002000)
        self.OD14 = BitField(self, 0x00004000)
        self.OD15 = BitField(self, 0x00008000)

class GPIO_BSRR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.BS0 = BitField(self, 0x00000001)
        self.BS1 = BitField(self, 0x00000002)
        self.BS2 = BitField(self, 0x00000004)
        self.BS3 = BitField(self, 0x00000008)
        self.BS4 = BitField(self, 0x00000010)
        self.BS5 = BitField(self, 0x00000020)
        self.BS6 = BitField(self, 0x00000040)
        self.BS7 = BitField(self, 0x00000080)
        self.BS8 = BitField(self, 0x00000100)
        self.BS9 = BitField(self, 0x00000200)
        self.BS10 = BitField(self, 0x00000400)
        self.BS11 = BitField(self, 0x00000800)
        self.BS12 = BitField(self, 0x00001000)
        self.BS13 = BitField(self, 0x00002000)
        self.BS14 = BitField(self, 0x00004000)
        self.BS15 = BitField(self, 0x00008000)
        self.BR0 = BitField(self, 0x00010000)
        self.BR1 = BitField(self, 0x00020000)
        self.BR2 = BitField(self, 0x00040000)
        self.BR3 = BitField(self, 0x00080000)
        self.BR4 = BitField(self, 0x00100000)
        self.BR5 = BitField(self, 0x00200000)
        self.BR6 = BitField(self, 0x00400000)
        self.BR7 = BitField(self, 0x00800000)
        self.BR8 = BitField(self, 0x01000000)
        self.BR9 = BitField(self, 0x02000000)
        self.BR10 = BitField(self, 0x04000000)
        self.BR11 = BitField(self, 0x08000000)
        self.BR12 = BitField(self, 0x10000000)
        self.BR13 = BitField(self, 0x20000000)
        self.BR14 = BitField(self, 0x40000000)
        self.BR15 = BitField(self, 0x80000000)

class GPIO_LCKR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.LCK0 = BitField(self, 0x00000001)
        self.LCK1 = BitField(self, 0x00000002)
        self.LCK2 = BitField(self, 0x00000004)
        self.LCK3 = BitField(self, 0x00000008)
        self.LCK4 = BitField(self, 0x00000010)
        self.LCK5 = BitField(self, 0x00000020)
        self.LCK6 = BitField(self, 0x00000040)
        self.LCK7 = BitField(self, 0x00000080)
        self.LCK8 = BitField(self, 0x00000100)
        self.LCK9 = BitField(self, 0x00000200)
        self.LCK10 = BitField(self, 0x00000400)
        self.LCK11 = BitField(self, 0x00000800)
        self.LCK12 = BitField(self, 0x00001000)
        self.LCK13 = BitField(self, 0x00002000)
        self.LCK14 = BitField(self, 0x00004000)
        self.LCK15 = BitField(self, 0x00008000)
        self.LCKK = BitField(self, 0x00010000)

class GPIO_AFRL(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.AFSEL0 = BitField(self, 0x0000000F)
        self.AFSEL1 = BitField(self, 0x000000F0)
        self.AFSEL2 = BitField(self, 0x00000F00)
        self.AFSEL3 = BitField(self, 0x0000F000)
        self.AFSEL4 = BitField(self, 0x000F0000)
        self.AFSEL5 = BitField(self, 0x00F00000)
        self.AFSEL6 = BitField(self, 0x0F000000)
        self.AFSEL7 = BitField(self, 0xF0000000)

class GPIO_AFRH(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.AFSEL8 = BitField(self, 0x0000000F)
        self.AFSEL9 = BitField(self, 0x000000F0)
        self.AFSEL10 = BitField(self, 0x00000F00)
        self.AFSEL11 = BitField(self, 0x0000F000)
        self.AFSEL12 = BitField(self, 0x000F0000)
        self.AFSEL13 = BitField(self, 0x00F00000)
        self.AFSEL14 = BitField(self, 0x0F000000)
        self.AFSEL15 = BitField(self, 0xF0000000)

class GPIO_BRR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.BR0 = BitField(self, 0x00000001)
        self.BR1 = BitField(self, 0x00000002)
        self.BR2 = BitField(self, 0x00000004)
        self.BR3 = BitField(self, 0x00000008)
        self.BR4 = BitField(self, 0x00000010)
        self.BR5 = BitField(self, 0x00000020)
        self.BR6 = BitField(self, 0x00000040)
        self.BR7 = BitField(self, 0x00000080)
        self.BR8 = BitField(self, 0x00000100)
        self.BR9 = BitField(self, 0x00000200)
        self.BR10 = BitField(self, 0x00000400)
        self.BR11 = BitField(self, 0x00000800)
        self.BR12 = BitField(self, 0x00001000)
        self.BR13 = BitField(self, 0x00002000)
        self.BR14 = BitField(self, 0x00004000)
        self.BR15 = BitField(self, 0x00008000)

class GPIO_TypeDef(PeripheralBase):

    def __init__(self, base):
        super().__init__(base)
        self.MODER = GPIO_MODER(base + 0x0)
        self.OTYPER = GPIO_OTYPER(base + 0x4)
        self.OSPEEDR = GPIO_OSPEEDR(base + 0x8)
        self.PUPDR = GPIO_PUPDR(base + 0xC)
        self.IDR = GPIO_IDR(base + 0x10)
        self.ODR = GPIO_ODR(base + 0x14)
        self.BSRR = GPIO_BSRR(base + 0x18)
        self.LCKR = GPIO_LCKR(base + 0x1C)
        self.AFRL = GPIO_AFRL(base + 0x20)
        self.AFRH = GPIO_AFRH(base + 0x24)
        self.BRR = GPIO_BRR(base + 0x28)

GPIOA = GPIO_TypeDef(0x48000000)
GPIOB = GPIO_TypeDef(0x48000400)
GPIOC = GPIO_TypeDef(0x48000800)
GPIOD = GPIO_TypeDef(0x48000C00)
GPIOE = GPIO_TypeDef(0x48001000)
GPIOF = GPIO_TypeDef(0x48001400)
GPIOG = GPIO_TypeDef(0x48001800)

class I2C_CR1(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.PE = BitField(self, 0x00000001)
        self.TXIE = BitField(self, 0x00000002)
        self.RXIE = BitField(self, 0x00000004)
        self.ADDRIE = BitField(self, 0x00000008)
        self.NACKIE = BitField(self, 0x00000010)
        self.STOPIE = BitField(self, 0x00000020)
        self.TCIE = BitField(self, 0x00000040)
        self.ERRIE = BitField(self, 0x00000080)
        self.DNF = BitField(self, 0x00000F00)
        self.ANFOFF = BitField(self, 0x00001000)
        self.SWRST = BitField(self, 0x00002000)
        self.TXDMAEN = BitField(self, 0x00004000)
        self.RXDMAEN = BitField(self, 0x00008000)
        self.SBC = BitField(self, 0x00010000)
        self.NOSTRETCH = BitField(self, 0x00020000)
        self.WUPEN = BitField(self, 0x00040000)
        self.GCEN = BitField(self, 0x00080000)
        self.SMBHEN = BitField(self, 0x00100000)
        self.SMBDEN = BitField(self, 0x00200000)
        self.ALERTEN = BitField(self, 0x00400000)
        self.PECEN = BitField(self, 0x00800000)

class I2C_CR2(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.SADD = BitField(self, 0x000003FF)
        self.RD_WRN = BitField(self, 0x00000400)
        self.ADD10 = BitField(self, 0x00000800)
        self.HEAD10R = BitField(self, 0x00001000)
        self.START = BitField(self, 0x00002000)
        self.STOP = BitField(self, 0x00004000)
        self.NACK = BitField(self, 0x00008000)
        self.NBYTES = BitField(self, 0x00FF0000)
        self.RELOAD = BitField(self, 0x01000000)
        self.AUTOEND = BitField(self, 0x02000000)
        self.PECBYTE = BitField(self, 0x04000000)

class I2C_OAR1(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.OA1 = BitField(self, 0x000003FF)
        self.OA1MODE = BitField(self, 0x00000400)
        self.OA1EN = BitField(self, 0x00008000)

class I2C_OAR2(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.OA2 = BitField(self, 0x000000FE)
        self.OA2MSK = BitField(self, 0x00000700)
        self.OA2MASK01 = BitField(self, 0x00000100)
        self.OA2MASK02 = BitField(self, 0x00000200)
        self.OA2MASK03 = BitField(self, 0x00000300)
        self.OA2MASK04 = BitField(self, 0x00000400)
        self.OA2MASK05 = BitField(self, 0x00000500)
        self.OA2MASK06 = BitField(self, 0x00000600)
        self.OA2MASK07 = BitField(self, 0x00000700)
        self.OA2EN = BitField(self, 0x00008000)

class I2C_TIMINGR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.SCLL = BitField(self, 0x000000FF)
        self.SCLH = BitField(self, 0x0000FF00)
        self.SDADEL = BitField(self, 0x000F0000)
        self.SCLDEL = BitField(self, 0x00F00000)
        self.PRESC = BitField(self, 0xF0000000)

class I2C_TIMEOUTR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.TIMEOUTA = BitField(self, 0x00000FFF)
        self.TIDLE = BitField(self, 0x00001000)
        self.TIMOUTEN = BitField(self, 0x00008000)
        self.TIMEOUTB = BitField(self, 0x0FFF0000)
        self.TEXTEN = BitField(self, 0x80000000)

class I2C_ISR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.TXE = BitField(self, 0x00000001)
        self.TXIS = BitField(self, 0x00000002)
        self.RXNE = BitField(self, 0x00000004)
        self.ADDR = BitField(self, 0x00000008)
        self.NACKF = BitField(self, 0x00000010)
        self.STOPF = BitField(self, 0x00000020)
        self.TC = BitField(self, 0x00000040)
        self.TCR = BitField(self, 0x00000080)
        self.BERR = BitField(self, 0x00000100)
        self.ARLO = BitField(self, 0x00000200)
        self.OVR = BitField(self, 0x00000400)
        self.PECERR = BitField(self, 0x00000800)
        self.TIMEOUT = BitField(self, 0x00001000)
        self.ALERT = BitField(self, 0x00002000)
        self.BUSY = BitField(self, 0x00008000)
        self.DIR = BitField(self, 0x00010000)
        self.ADDCODE = BitField(self, 0x00FE0000)

class I2C_ICR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.ADDRCF = BitField(self, 0x00000008)
        self.NACKCF = BitField(self, 0x00000010)
        self.STOPCF = BitField(self, 0x00000020)
        self.BERRCF = BitField(self, 0x00000100)
        self.ARLOCF = BitField(self, 0x00000200)
        self.OVRCF = BitField(self, 0x00000400)
        self.PECCF = BitField(self, 0x00000800)
        self.TIMOUTCF = BitField(self, 0x00001000)
        self.ALERTCF = BitField(self, 0x00002000)

class I2C_PECR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.PEC = BitField(self, 0x000000FF)

class I2C_RXDR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.RXDATA = BitField(self, 0x000000FF)

class I2C_TXDR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.TXDATA = BitField(self, 0x000000FF)

class I2C_TypeDef(PeripheralBase):

    def __init__(self, base):
        super().__init__(base)
        self.CR1 = I2C_CR1(base + 0x0)
        self.CR2 = I2C_CR2(base + 0x4)
        self.OAR1 = I2C_OAR1(base + 0x8)
        self.OAR2 = I2C_OAR2(base + 0xC)
        self.TIMINGR = I2C_TIMINGR(base + 0x10)
        self.TIMEOUTR = I2C_TIMEOUTR(base + 0x14)
        self.ISR = I2C_ISR(base + 0x18)
        self.ICR = I2C_ICR(base + 0x1C)
        self.PECR = I2C_PECR(base + 0x20)
        self.RXDR = I2C_RXDR(base + 0x24)
        self.TXDR = I2C_TXDR(base + 0x28)

I2C1 = I2C_TypeDef(0x40005400)
I2C2 = I2C_TypeDef(0x40005800)
I2C3 = I2C_TypeDef(0x40007800)
I2C4 = I2C_TypeDef(0x40008400)

class IWDG_KR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.KEY = BitField(self, 0x0000FFFF)

class IWDG_PR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.PR = BitField(self, 0x00000007)

class IWDG_RLR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.RL = BitField(self, 0x00000FFF)

class IWDG_SR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.PVU = BitField(self, 0x00000001)
        self.RVU = BitField(self, 0x00000002)
        self.WVU = BitField(self, 0x00000004)

class IWDG_WINR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.WIN = BitField(self, 0x00000FFF)

class IWDG_TypeDef(PeripheralBase):

    def __init__(self, base):
        super().__init__(base)
        self.KR = IWDG_KR(base + 0x0)
        self.PR = IWDG_PR(base + 0x4)
        self.RLR = IWDG_RLR(base + 0x8)
        self.SR = IWDG_SR(base + 0xC)
        self.WINR = IWDG_WINR(base + 0x10)

IWDG = IWDG_TypeDef(0x40003000)

class LPTIM_ISR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.CMPM = BitField(self, 0x00000001)
        self.ARRM = BitField(self, 0x00000002)
        self.EXTTRIG = BitField(self, 0x00000004)
        self.CMPOK = BitField(self, 0x00000008)
        self.ARROK = BitField(self, 0x00000010)
        self.UP = BitField(self, 0x00000020)
        self.DOWN = BitField(self, 0x00000040)

class LPTIM_ICR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.CMPMCF = BitField(self, 0x00000001)
        self.ARRMCF = BitField(self, 0x00000002)
        self.EXTTRIGCF = BitField(self, 0x00000004)
        self.CMPOKCF = BitField(self, 0x00000008)
        self.ARROKCF = BitField(self, 0x00000010)
        self.UPCF = BitField(self, 0x00000020)
        self.DOWNCF = BitField(self, 0x00000040)

class LPTIM_IER(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.CMPMIE = BitField(self, 0x00000001)
        self.ARRMIE = BitField(self, 0x00000002)
        self.EXTTRIGIE = BitField(self, 0x00000004)
        self.CMPOKIE = BitField(self, 0x00000008)
        self.ARROKIE = BitField(self, 0x00000010)
        self.UPIE = BitField(self, 0x00000020)
        self.DOWNIE = BitField(self, 0x00000040)

class LPTIM_CFGR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.CKSEL = BitField(self, 0x00000001)
        self.CKPOL = BitField(self, 0x00000006)
        self.CKFLT = BitField(self, 0x00000018)
        self.TRGFLT = BitField(self, 0x000000C0)
        self.PRESC = BitField(self, 0x00000E00)
        self.TRIGSEL = BitField(self, 0x2000E000)
        self.TRIGEN = BitField(self, 0x00060000)
        self.TIMOUT = BitField(self, 0x00080000)
        self.WAVE = BitField(self, 0x00100000)
        self.WAVPOL = BitField(self, 0x00200000)
        self.PRELOAD = BitField(self, 0x00400000)
        self.COUNTMODE = BitField(self, 0x00800000)
        self.ENC = BitField(self, 0x01000000)

class LPTIM_CR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.ENABLE = BitField(self, 0x00000001)
        self.SNGSTRT = BitField(self, 0x00000002)
        self.CNTSTRT = BitField(self, 0x00000004)
        self.COUNTRST = BitField(self, 0x00000008)
        self.RSTARE = BitField(self, 0x00000010)

class LPTIM_CMP(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.CMP = BitField(self, 0x0000FFFF)

class LPTIM_ARR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.ARR = BitField(self, 0x0000FFFF)

class LPTIM_CNT(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.CNT = BitField(self, 0x0000FFFF)

class LPTIM_OR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.IN1 = BitField(self, 0x0000000D)
        self.IN2 = BitField(self, 0x00000032)

class LPTIM_TypeDef(PeripheralBase):

    def __init__(self, base):
        super().__init__(base)
        self.ISR = LPTIM_ISR(base + 0x0)
        self.ICR = LPTIM_ICR(base + 0x4)
        self.IER = LPTIM_IER(base + 0x8)
        self.CFGR = LPTIM_CFGR(base + 0xC)
        self.CR = LPTIM_CR(base + 0x10)
        self.CMP = LPTIM_CMP(base + 0x14)
        self.ARR = LPTIM_ARR(base + 0x18)
        self.CNT = LPTIM_CNT(base + 0x1C)
        self.OR = LPTIM_OR(base + 0x20)

LPTIM1 = LPTIM_TypeDef(0x40007C00)

class OPAMP_CSR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.OPAMPxEN = BitField(self, 0x00000001)
        self.FORCEVP = BitField(self, 0x00000002)
        self.VPSEL = BitField(self, 0x0000000C)
        self.USERTRIM = BitField(self, 0x00000010)
        self.VMSEL = BitField(self, 0x00000060)
        self.HIGHSPEEDEN = BitField(self, 0x00000080)
        self.OPAMPINTEN = BitField(self, 0x00000100)
        self.CALON = BitField(self, 0x00000800)
        self.CALSEL = BitField(self, 0x00003000)
        self.PGGAIN = BitField(self, 0x0007C000)
        self.TRIMOFFSETP = BitField(self, 0x00F80000)
        self.TRIMOFFSETN = BitField(self, 0x1F000000)
        self.OUTCAL = BitField(self, 0x40000000)
        self.LOCK = BitField(self, 0x80000000)

class OPAMP_TCMR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.VMSSEL = BitField(self, 0x00000001)
        self.VPSSEL = BitField(self, 0x00000006)
        self.T1CMEN = BitField(self, 0x00000008)
        self.T8CMEN = BitField(self, 0x00000010)
        self.T20CMEN = BitField(self, 0x00000020)
        self.LOCK = BitField(self, 0x80000000)

class OPAMP_TypeDef(PeripheralBase):

    def __init__(self, base):
        super().__init__(base)
        self.CSR = OPAMP_CSR(base + 0x0)
        self.TCMR = OPAMP_TCMR(base + 0x18)

OPAMP = OPAMP_TypeDef(0x40010300)
OPAMP1 = OPAMP_TypeDef(0x40010300)
OPAMP2 = OPAMP_TypeDef(0x40010304)
OPAMP3 = OPAMP_TypeDef(0x40010308)
OPAMP4 = OPAMP_TypeDef(0x4001030C)
OPAMP5 = OPAMP_TypeDef(0x40010310)
OPAMP6 = OPAMP_TypeDef(0x40010314)

class PWR_CR1(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.LPR = BitField(self, 0x00004000)
        self.VOS = BitField(self, 0x00000600)
        self.DBP = BitField(self, 0x00000100)
        self.LPMS = BitField(self, 0x00000007)
        self.LPMS_STOP1 = BitField(self, 0x00000001)
        self.LPMS_STANDBY = BitField(self, 0x00000003)
        self.LPMS_SHUTDOWN = BitField(self, 0x00000004)

class PWR_CR2(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.PVME = BitField(self, 0x000000F0)
        self.PVME4 = BitField(self, 0x00000080)
        self.PVME3 = BitField(self, 0x00000040)
        self.PVME2 = BitField(self, 0x00000020)
        self.PVME1 = BitField(self, 0x00000010)
        self.PLS = BitField(self, 0x0000000E)
        self.PLS_LEV1 = BitField(self, 0x00000002)
        self.PLS_LEV2 = BitField(self, 0x00000004)
        self.PLS_LEV3 = BitField(self, 0x00000006)
        self.PLS_LEV4 = BitField(self, 0x00000008)
        self.PLS_LEV5 = BitField(self, 0x0000000A)
        self.PLS_LEV6 = BitField(self, 0x0000000C)
        self.PLS_LEV7 = BitField(self, 0x0000000E)
        self.PVDE = BitField(self, 0x00000001)

class PWR_CR3(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.EIWF = BitField(self, 0x00008000)
        self.UCPD_DBDIS = BitField(self, 0x00004000)
        self.UCPD_STDBY = BitField(self, 0x00002000)
        self.APC = BitField(self, 0x00000400)
        self.RRS = BitField(self, 0x00000100)
        self.EWUP5 = BitField(self, 0x00000010)
        self.EWUP4 = BitField(self, 0x00000008)
        self.EWUP3 = BitField(self, 0x00000004)
        self.EWUP2 = BitField(self, 0x00000002)
        self.EWUP1 = BitField(self, 0x00000001)
        self.EWUP = BitField(self, 0x0000001F)

class PWR_CR4(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.VBRS = BitField(self, 0x00000200)
        self.VBE = BitField(self, 0x00000100)
        self.WP5 = BitField(self, 0x00000010)
        self.WP4 = BitField(self, 0x00000008)
        self.WP3 = BitField(self, 0x00000004)
        self.WP2 = BitField(self, 0x00000002)
        self.WP1 = BitField(self, 0x00000001)

class PWR_SR1(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.WUFI = BitField(self, 0x00008000)
        self.SBF = BitField(self, 0x00000100)
        self.WUF = BitField(self, 0x0000001F)
        self.WUF5 = BitField(self, 0x00000010)
        self.WUF4 = BitField(self, 0x00000008)
        self.WUF3 = BitField(self, 0x00000004)
        self.WUF2 = BitField(self, 0x00000002)
        self.WUF1 = BitField(self, 0x00000001)

class PWR_SR2(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.PVMO4 = BitField(self, 0x00008000)
        self.PVMO3 = BitField(self, 0x00004000)
        self.PVMO2 = BitField(self, 0x00002000)
        self.PVMO1 = BitField(self, 0x00001000)
        self.PVDO = BitField(self, 0x00000800)
        self.VOSF = BitField(self, 0x00000400)
        self.REGLPF = BitField(self, 0x00000200)
        self.REGLPS = BitField(self, 0x00000100)

class PWR_SCR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.CSBF = BitField(self, 0x00000100)
        self.CWUF = BitField(self, 0x0000001F)
        self.CWUF5 = BitField(self, 0x00000010)
        self.CWUF4 = BitField(self, 0x00000008)
        self.CWUF3 = BitField(self, 0x00000004)
        self.CWUF2 = BitField(self, 0x00000002)
        self.CWUF1 = BitField(self, 0x00000001)

class PWR_PUCRA(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.PA15 = BitField(self, 0x00008000)
        self.PA13 = BitField(self, 0x00002000)
        self.PA12 = BitField(self, 0x00001000)
        self.PA11 = BitField(self, 0x00000800)
        self.PA10 = BitField(self, 0x00000400)
        self.PA9 = BitField(self, 0x00000200)
        self.PA8 = BitField(self, 0x00000100)
        self.PA7 = BitField(self, 0x00000080)
        self.PA6 = BitField(self, 0x00000040)
        self.PA5 = BitField(self, 0x00000020)
        self.PA4 = BitField(self, 0x00000010)
        self.PA3 = BitField(self, 0x00000008)
        self.PA2 = BitField(self, 0x00000004)
        self.PA1 = BitField(self, 0x00000002)
        self.PA0 = BitField(self, 0x00000001)

class PWR_PDCRA(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.PA14 = BitField(self, 0x00004000)
        self.PA12 = BitField(self, 0x00001000)
        self.PA11 = BitField(self, 0x00000800)
        self.PA10 = BitField(self, 0x00000400)
        self.PA9 = BitField(self, 0x00000200)
        self.PA8 = BitField(self, 0x00000100)
        self.PA7 = BitField(self, 0x00000080)
        self.PA6 = BitField(self, 0x00000040)
        self.PA5 = BitField(self, 0x00000020)
        self.PA4 = BitField(self, 0x00000010)
        self.PA3 = BitField(self, 0x00000008)
        self.PA2 = BitField(self, 0x00000004)
        self.PA1 = BitField(self, 0x00000002)
        self.PA0 = BitField(self, 0x00000001)

class PWR_PUCRB(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.PB15 = BitField(self, 0x00008000)
        self.PB14 = BitField(self, 0x00004000)
        self.PB13 = BitField(self, 0x00002000)
        self.PB12 = BitField(self, 0x00001000)
        self.PB11 = BitField(self, 0x00000800)
        self.PB10 = BitField(self, 0x00000400)
        self.PB9 = BitField(self, 0x00000200)
        self.PB8 = BitField(self, 0x00000100)
        self.PB7 = BitField(self, 0x00000080)
        self.PB6 = BitField(self, 0x00000040)
        self.PB5 = BitField(self, 0x00000020)
        self.PB4 = BitField(self, 0x00000010)
        self.PB3 = BitField(self, 0x00000008)
        self.PB2 = BitField(self, 0x00000004)
        self.PB1 = BitField(self, 0x00000002)
        self.PB0 = BitField(self, 0x00000001)

class PWR_PDCRB(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.PB15 = BitField(self, 0x00008000)
        self.PB14 = BitField(self, 0x00004000)
        self.PB13 = BitField(self, 0x00002000)
        self.PB12 = BitField(self, 0x00001000)
        self.PB11 = BitField(self, 0x00000800)
        self.PB10 = BitField(self, 0x00000400)
        self.PB9 = BitField(self, 0x00000200)
        self.PB8 = BitField(self, 0x00000100)
        self.PB7 = BitField(self, 0x00000080)
        self.PB6 = BitField(self, 0x00000040)
        self.PB5 = BitField(self, 0x00000020)
        self.PB3 = BitField(self, 0x00000008)
        self.PB2 = BitField(self, 0x00000004)
        self.PB1 = BitField(self, 0x00000002)
        self.PB0 = BitField(self, 0x00000001)

class PWR_PUCRC(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.PC15 = BitField(self, 0x00008000)
        self.PC14 = BitField(self, 0x00004000)
        self.PC13 = BitField(self, 0x00002000)
        self.PC12 = BitField(self, 0x00001000)
        self.PC11 = BitField(self, 0x00000800)
        self.PC10 = BitField(self, 0x00000400)
        self.PC9 = BitField(self, 0x00000200)
        self.PC8 = BitField(self, 0x00000100)
        self.PC7 = BitField(self, 0x00000080)
        self.PC6 = BitField(self, 0x00000040)
        self.PC5 = BitField(self, 0x00000020)
        self.PC4 = BitField(self, 0x00000010)
        self.PC3 = BitField(self, 0x00000008)
        self.PC2 = BitField(self, 0x00000004)
        self.PC1 = BitField(self, 0x00000002)
        self.PC0 = BitField(self, 0x00000001)

class PWR_PDCRC(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.PC15 = BitField(self, 0x00008000)
        self.PC14 = BitField(self, 0x00004000)
        self.PC13 = BitField(self, 0x00002000)
        self.PC12 = BitField(self, 0x00001000)
        self.PC11 = BitField(self, 0x00000800)
        self.PC10 = BitField(self, 0x00000400)
        self.PC9 = BitField(self, 0x00000200)
        self.PC8 = BitField(self, 0x00000100)
        self.PC7 = BitField(self, 0x00000080)
        self.PC6 = BitField(self, 0x00000040)
        self.PC5 = BitField(self, 0x00000020)
        self.PC4 = BitField(self, 0x00000010)
        self.PC3 = BitField(self, 0x00000008)
        self.PC2 = BitField(self, 0x00000004)
        self.PC1 = BitField(self, 0x00000002)
        self.PC0 = BitField(self, 0x00000001)

class PWR_PUCRD(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.PD15 = BitField(self, 0x00008000)
        self.PD14 = BitField(self, 0x00004000)
        self.PD13 = BitField(self, 0x00002000)
        self.PD12 = BitField(self, 0x00001000)
        self.PD11 = BitField(self, 0x00000800)
        self.PD10 = BitField(self, 0x00000400)
        self.PD9 = BitField(self, 0x00000200)
        self.PD8 = BitField(self, 0x00000100)
        self.PD7 = BitField(self, 0x00000080)
        self.PD6 = BitField(self, 0x00000040)
        self.PD5 = BitField(self, 0x00000020)
        self.PD4 = BitField(self, 0x00000010)
        self.PD3 = BitField(self, 0x00000008)
        self.PD2 = BitField(self, 0x00000004)
        self.PD1 = BitField(self, 0x00000002)
        self.PD0 = BitField(self, 0x00000001)

class PWR_PDCRD(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.PD15 = BitField(self, 0x00008000)
        self.PD14 = BitField(self, 0x00004000)
        self.PD13 = BitField(self, 0x00002000)
        self.PD12 = BitField(self, 0x00001000)
        self.PD11 = BitField(self, 0x00000800)
        self.PD10 = BitField(self, 0x00000400)
        self.PD9 = BitField(self, 0x00000200)
        self.PD8 = BitField(self, 0x00000100)
        self.PD7 = BitField(self, 0x00000080)
        self.PD6 = BitField(self, 0x00000040)
        self.PD5 = BitField(self, 0x00000020)
        self.PD4 = BitField(self, 0x00000010)
        self.PD3 = BitField(self, 0x00000008)
        self.PD2 = BitField(self, 0x00000004)
        self.PD1 = BitField(self, 0x00000002)
        self.PD0 = BitField(self, 0x00000001)

class PWR_PUCRE(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.PE15 = BitField(self, 0x00008000)
        self.PE14 = BitField(self, 0x00004000)
        self.PE13 = BitField(self, 0x00002000)
        self.PE12 = BitField(self, 0x00001000)
        self.PE11 = BitField(self, 0x00000800)
        self.PE10 = BitField(self, 0x00000400)
        self.PE9 = BitField(self, 0x00000200)
        self.PE8 = BitField(self, 0x00000100)
        self.PE7 = BitField(self, 0x00000080)
        self.PE6 = BitField(self, 0x00000040)
        self.PE5 = BitField(self, 0x00000020)
        self.PE4 = BitField(self, 0x00000010)
        self.PE3 = BitField(self, 0x00000008)
        self.PE2 = BitField(self, 0x00000004)
        self.PE1 = BitField(self, 0x00000002)
        self.PE0 = BitField(self, 0x00000001)

class PWR_PDCRE(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.PE15 = BitField(self, 0x00008000)
        self.PE14 = BitField(self, 0x00004000)
        self.PE13 = BitField(self, 0x00002000)
        self.PE12 = BitField(self, 0x00001000)
        self.PE11 = BitField(self, 0x00000800)
        self.PE10 = BitField(self, 0x00000400)
        self.PE9 = BitField(self, 0x00000200)
        self.PE8 = BitField(self, 0x00000100)
        self.PE7 = BitField(self, 0x00000080)
        self.PE6 = BitField(self, 0x00000040)
        self.PE5 = BitField(self, 0x00000020)
        self.PE4 = BitField(self, 0x00000010)
        self.PE3 = BitField(self, 0x00000008)
        self.PE2 = BitField(self, 0x00000004)
        self.PE1 = BitField(self, 0x00000002)
        self.PE0 = BitField(self, 0x00000001)

class PWR_PUCRF(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.PF15 = BitField(self, 0x00008000)
        self.PF14 = BitField(self, 0x00004000)
        self.PF13 = BitField(self, 0x00002000)
        self.PF12 = BitField(self, 0x00001000)
        self.PF11 = BitField(self, 0x00000800)
        self.PF10 = BitField(self, 0x00000400)
        self.PF9 = BitField(self, 0x00000200)
        self.PF8 = BitField(self, 0x00000100)
        self.PF7 = BitField(self, 0x00000080)
        self.PF6 = BitField(self, 0x00000040)
        self.PF5 = BitField(self, 0x00000020)
        self.PF4 = BitField(self, 0x00000010)
        self.PF3 = BitField(self, 0x00000008)
        self.PF2 = BitField(self, 0x00000004)
        self.PF1 = BitField(self, 0x00000002)
        self.PF0 = BitField(self, 0x00000001)

class PWR_PDCRF(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.PF15 = BitField(self, 0x00008000)
        self.PF14 = BitField(self, 0x00004000)
        self.PF13 = BitField(self, 0x00002000)
        self.PF12 = BitField(self, 0x00001000)
        self.PF11 = BitField(self, 0x00000800)
        self.PF10 = BitField(self, 0x00000400)
        self.PF9 = BitField(self, 0x00000200)
        self.PF8 = BitField(self, 0x00000100)
        self.PF7 = BitField(self, 0x00000080)
        self.PF6 = BitField(self, 0x00000040)
        self.PF5 = BitField(self, 0x00000020)
        self.PF4 = BitField(self, 0x00000010)
        self.PF3 = BitField(self, 0x00000008)
        self.PF2 = BitField(self, 0x00000004)
        self.PF1 = BitField(self, 0x00000002)
        self.PF0 = BitField(self, 0x00000001)

class PWR_PUCRG(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.PG15 = BitField(self, 0x00008000)
        self.PG14 = BitField(self, 0x00004000)
        self.PG13 = BitField(self, 0x00002000)
        self.PG12 = BitField(self, 0x00001000)
        self.PG11 = BitField(self, 0x00000800)
        self.PG10 = BitField(self, 0x00000400)
        self.PG9 = BitField(self, 0x00000200)
        self.PG8 = BitField(self, 0x00000100)
        self.PG7 = BitField(self, 0x00000080)
        self.PG6 = BitField(self, 0x00000040)
        self.PG5 = BitField(self, 0x00000020)
        self.PG4 = BitField(self, 0x00000010)
        self.PG3 = BitField(self, 0x00000008)
        self.PG2 = BitField(self, 0x00000004)
        self.PG1 = BitField(self, 0x00000002)
        self.PG0 = BitField(self, 0x00000001)

class PWR_PDCRG(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.PG10 = BitField(self, 0x00000400)
        self.PG9 = BitField(self, 0x00000200)
        self.PG8 = BitField(self, 0x00000100)
        self.PG7 = BitField(self, 0x00000080)
        self.PG6 = BitField(self, 0x00000040)
        self.PG5 = BitField(self, 0x00000020)
        self.PG4 = BitField(self, 0x00000010)
        self.PG3 = BitField(self, 0x00000008)
        self.PG2 = BitField(self, 0x00000004)
        self.PG1 = BitField(self, 0x00000002)
        self.PG0 = BitField(self, 0x00000001)

class PWR_CR5(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.R1MODE = BitField(self, 0x00000100)

class PWR_TypeDef(PeripheralBase):

    def __init__(self, base):
        super().__init__(base)
        self.CR1 = PWR_CR1(base + 0x0)
        self.CR2 = PWR_CR2(base + 0x4)
        self.CR3 = PWR_CR3(base + 0x8)
        self.CR4 = PWR_CR4(base + 0xC)
        self.SR1 = PWR_SR1(base + 0x10)
        self.SR2 = PWR_SR2(base + 0x14)
        self.SCR = PWR_SCR(base + 0x18)
        self.PUCRA = PWR_PUCRA(base + 0x20)
        self.PDCRA = PWR_PDCRA(base + 0x24)
        self.PUCRB = PWR_PUCRB(base + 0x28)
        self.PDCRB = PWR_PDCRB(base + 0x2C)
        self.PUCRC = PWR_PUCRC(base + 0x30)
        self.PDCRC = PWR_PDCRC(base + 0x34)
        self.PUCRD = PWR_PUCRD(base + 0x38)
        self.PDCRD = PWR_PDCRD(base + 0x3C)
        self.PUCRE = PWR_PUCRE(base + 0x40)
        self.PDCRE = PWR_PDCRE(base + 0x44)
        self.PUCRF = PWR_PUCRF(base + 0x48)
        self.PDCRF = PWR_PDCRF(base + 0x4C)
        self.PUCRG = PWR_PUCRG(base + 0x50)
        self.PDCRG = PWR_PDCRG(base + 0x54)
        self.CR5 = PWR_CR5(base + 0x80)

PWR = PWR_TypeDef(0x40007000)

class QUADSPI_CR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.EN = BitField(self, 0x00000001)
        self.ABORT = BitField(self, 0x00000002)
        self.DMAEN = BitField(self, 0x00000004)
        self.TCEN = BitField(self, 0x00000008)
        self.SSHIFT = BitField(self, 0x00000010)
        self.DFM = BitField(self, 0x00000040)
        self.FSEL = BitField(self, 0x00000080)
        self.FTHRES = BitField(self, 0x00000F00)
        self.TEIE = BitField(self, 0x00010000)
        self.TCIE = BitField(self, 0x00020000)
        self.FTIE = BitField(self, 0x00040000)
        self.SMIE = BitField(self, 0x00080000)
        self.TOIE = BitField(self, 0x00100000)
        self.APMS = BitField(self, 0x00400000)
        self.PMM = BitField(self, 0x00800000)
        self.PRESCALER = BitField(self, 0xFF000000)

class QUADSPI_DCR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.CKMODE = BitField(self, 0x00000001)
        self.CSHT = BitField(self, 0x00000700)
        self.FSIZE = BitField(self, 0x001F0000)

class QUADSPI_SR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.TEF = BitField(self, 0x00000001)
        self.TCF = BitField(self, 0x00000002)
        self.FTF = BitField(self, 0x00000004)
        self.SMF = BitField(self, 0x00000008)
        self.TOF = BitField(self, 0x00000010)
        self.BUSY = BitField(self, 0x00000020)
        self.FLEVEL = BitField(self, 0x00001F00)

class QUADSPI_FCR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.CTEF = BitField(self, 0x00000001)
        self.CTCF = BitField(self, 0x00000002)
        self.CSMF = BitField(self, 0x00000008)
        self.CTOF = BitField(self, 0x00000010)

class QUADSPI_DLR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.DL = BitField(self, 0xFFFFFFFF)

class QUADSPI_CCR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.INSTRUCTION = BitField(self, 0x000000FF)
        self.IMODE = BitField(self, 0x00000300)
        self.ADMODE = BitField(self, 0x00000C00)
        self.ADSIZE = BitField(self, 0x00003000)
        self.ABMODE = BitField(self, 0x0000C000)
        self.ABSIZE = BitField(self, 0x00030000)
        self.DCYC = BitField(self, 0x007C0000)
        self.DMODE = BitField(self, 0x03000000)
        self.FMODE = BitField(self, 0x0C000000)
        self.SIOO = BitField(self, 0x10000000)
        self.DHHC = BitField(self, 0x40000000)
        self.DDRM = BitField(self, 0x80000000)

class QUADSPI_AR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.ADDRESS = BitField(self, 0xFFFFFFFF)

class QUADSPI_ABR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.ALTERNATE = BitField(self, 0xFFFFFFFF)

class QUADSPI_DR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.DATA = BitField(self, 0xFFFFFFFF)

class QUADSPI_PSMKR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.MASK = BitField(self, 0xFFFFFFFF)

class QUADSPI_PSMAR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.MATCH = BitField(self, 0xFFFFFFFF)

class QUADSPI_PIR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.INTERVAL = BitField(self, 0x0000FFFF)

class QUADSPI_LPTR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.TIMEOUT = BitField(self, 0x0000FFFF)

class QUADSPI_TypeDef(PeripheralBase):

    def __init__(self, base):
        super().__init__(base)
        self.CR = QUADSPI_CR(base + 0x0)
        self.DCR = QUADSPI_DCR(base + 0x4)
        self.SR = QUADSPI_SR(base + 0x8)
        self.FCR = QUADSPI_FCR(base + 0xC)
        self.DLR = QUADSPI_DLR(base + 0x10)
        self.CCR = QUADSPI_CCR(base + 0x14)
        self.AR = QUADSPI_AR(base + 0x18)
        self.ABR = QUADSPI_ABR(base + 0x1C)
        self.DR = QUADSPI_DR(base + 0x20)
        self.PSMKR = QUADSPI_PSMKR(base + 0x24)
        self.PSMAR = QUADSPI_PSMAR(base + 0x28)
        self.PIR = QUADSPI_PIR(base + 0x2C)
        self.LPTR = QUADSPI_LPTR(base + 0x30)

QUADSPI = QUADSPI_TypeDef(0xA0001000)

class RCC_CR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.HSION = BitField(self, 0x00000100)
        self.HSIKERON = BitField(self, 0x00000200)
        self.HSIRDY = BitField(self, 0x00000400)
        self.HSEON = BitField(self, 0x00010000)
        self.HSERDY = BitField(self, 0x00020000)
        self.HSEBYP = BitField(self, 0x00040000)
        self.CSSON = BitField(self, 0x00080000)
        self.PLLON = BitField(self, 0x01000000)
        self.PLLRDY = BitField(self, 0x02000000)

class RCC_ICSCR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.HSICAL = BitField(self, 0x00FF0000)
        self.HSITRIM = BitField(self, 0x7F000000)

class RCC_CFGR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.SW = BitField(self, 0x00000003)
        self.SWS = BitField(self, 0x0000000C)
        self.HPRE = BitField(self, 0x000000F0)
        self.PPRE1 = BitField(self, 0x00000700)
        self.PPRE2 = BitField(self, 0x00003800)
        self.MCOSEL = BitField(self, 0x0F000000)
        self.MCOPRE = BitField(self, 0x70000000)

class RCC_PLLCFGR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.PLLSRC = BitField(self, 0x00000003)
        self.PLLSRC_HSI = BitField(self, 0x00000002)
        self.PLLSRC_HSE = BitField(self, 0x00000003)
        self.PLLM = BitField(self, 0x000000F0)
        self.PLLN = BitField(self, 0x00007F00)
        self.PLLPEN = BitField(self, 0x00010000)
        self.PLLP = BitField(self, 0x00020000)
        self.PLLQEN = BitField(self, 0x00100000)
        self.PLLQ = BitField(self, 0x00600000)
        self.PLLREN = BitField(self, 0x01000000)
        self.PLLR = BitField(self, 0x06000000)
        self.PLLPDIV = BitField(self, 0xF8000000)

class RCC_CIER(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.LSIRDYIE = BitField(self, 0x00000001)
        self.LSERDYIE = BitField(self, 0x00000002)
        self.HSIRDYIE = BitField(self, 0x00000008)
        self.HSERDYIE = BitField(self, 0x00000010)
        self.PLLRDYIE = BitField(self, 0x00000020)
        self.LSECSSIE = BitField(self, 0x00000200)
        self.HSI48RDYIE = BitField(self, 0x00000400)

class RCC_CIFR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.LSIRDYF = BitField(self, 0x00000001)
        self.LSERDYF = BitField(self, 0x00000002)
        self.HSIRDYF = BitField(self, 0x00000008)
        self.HSERDYF = BitField(self, 0x00000010)
        self.PLLRDYF = BitField(self, 0x00000020)
        self.CSSF = BitField(self, 0x00000100)
        self.LSECSSF = BitField(self, 0x00000200)
        self.HSI48RDYF = BitField(self, 0x00000400)

class RCC_CICR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.LSIRDYC = BitField(self, 0x00000001)
        self.LSERDYC = BitField(self, 0x00000002)
        self.HSIRDYC = BitField(self, 0x00000008)
        self.HSERDYC = BitField(self, 0x00000010)
        self.PLLRDYC = BitField(self, 0x00000020)
        self.CSSC = BitField(self, 0x00000100)
        self.LSECSSC = BitField(self, 0x00000200)
        self.HSI48RDYC = BitField(self, 0x00000400)

class RCC_AHB1RSTR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.DMA1RST = BitField(self, 0x00000001)
        self.DMA2RST = BitField(self, 0x00000002)
        self.DMAMUX1RST = BitField(self, 0x00000004)
        self.CORDICRST = BitField(self, 0x00000008)
        self.FMACRST = BitField(self, 0x00000010)
        self.FLASHRST = BitField(self, 0x00000100)
        self.CRCRST = BitField(self, 0x00001000)

class RCC_AHB2RSTR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.GPIOARST = BitField(self, 0x00000001)
        self.GPIOBRST = BitField(self, 0x00000002)
        self.GPIOCRST = BitField(self, 0x00000004)
        self.GPIODRST = BitField(self, 0x00000008)
        self.GPIOERST = BitField(self, 0x00000010)
        self.GPIOFRST = BitField(self, 0x00000020)
        self.GPIOGRST = BitField(self, 0x00000040)
        self.ADC12RST = BitField(self, 0x00002000)
        self.ADC345RST = BitField(self, 0x00004000)
        self.DAC1RST = BitField(self, 0x00010000)
        self.DAC2RST = BitField(self, 0x00020000)
        self.DAC3RST = BitField(self, 0x00040000)
        self.DAC4RST = BitField(self, 0x00080000)
        self.RNGRST = BitField(self, 0x04000000)

class RCC_AHB3RSTR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.FMCRST = BitField(self, 0x00000001)
        self.QSPIRST = BitField(self, 0x00000100)

class RCC_APB1RSTR1(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.TIM2RST = BitField(self, 0x00000001)
        self.TIM3RST = BitField(self, 0x00000002)
        self.TIM4RST = BitField(self, 0x00000004)
        self.TIM5RST = BitField(self, 0x00000008)
        self.TIM6RST = BitField(self, 0x00000010)
        self.TIM7RST = BitField(self, 0x00000020)
        self.CRSRST = BitField(self, 0x00000100)
        self.SPI2RST = BitField(self, 0x00004000)
        self.SPI3RST = BitField(self, 0x00008000)
        self.USART2RST = BitField(self, 0x00020000)
        self.USART3RST = BitField(self, 0x00040000)
        self.UART4RST = BitField(self, 0x00080000)
        self.UART5RST = BitField(self, 0x00100000)
        self.I2C1RST = BitField(self, 0x00200000)
        self.I2C2RST = BitField(self, 0x00400000)
        self.USBRST = BitField(self, 0x00800000)
        self.FDCANRST = BitField(self, 0x02000000)
        self.PWRRST = BitField(self, 0x10000000)
        self.I2C3RST = BitField(self, 0x40000000)
        self.LPTIM1RST = BitField(self, 0x80000000)

class RCC_APB1RSTR2(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.LPUART1RST = BitField(self, 0x00000001)
        self.I2C4RST = BitField(self, 0x00000002)
        self.UCPD1RST = BitField(self, 0x00000100)

class RCC_APB2RSTR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.SYSCFGRST = BitField(self, 0x00000001)
        self.TIM1RST = BitField(self, 0x00000800)
        self.SPI1RST = BitField(self, 0x00001000)
        self.TIM8RST = BitField(self, 0x00002000)
        self.USART1RST = BitField(self, 0x00004000)
        self.SPI4RST = BitField(self, 0x00008000)
        self.TIM15RST = BitField(self, 0x00010000)
        self.TIM16RST = BitField(self, 0x00020000)
        self.TIM17RST = BitField(self, 0x00040000)
        self.TIM20RST = BitField(self, 0x00100000)
        self.SAI1RST = BitField(self, 0x00200000)
        self.HRTIM1RST = BitField(self, 0x04000000)

class RCC_AHB1ENR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.DMA1EN = BitField(self, 0x00000001)
        self.DMA2EN = BitField(self, 0x00000002)
        self.DMAMUX1EN = BitField(self, 0x00000004)
        self.CORDICEN = BitField(self, 0x00000008)
        self.FMACEN = BitField(self, 0x00000010)
        self.FLASHEN = BitField(self, 0x00000100)
        self.CRCEN = BitField(self, 0x00001000)

class RCC_AHB2ENR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.GPIOAEN = BitField(self, 0x00000001)
        self.GPIOBEN = BitField(self, 0x00000002)
        self.GPIOCEN = BitField(self, 0x00000004)
        self.GPIODEN = BitField(self, 0x00000008)
        self.GPIOEEN = BitField(self, 0x00000010)
        self.GPIOFEN = BitField(self, 0x00000020)
        self.GPIOGEN = BitField(self, 0x00000040)
        self.ADC12EN = BitField(self, 0x00002000)
        self.ADC345EN = BitField(self, 0x00004000)
        self.DAC1EN = BitField(self, 0x00010000)
        self.DAC2EN = BitField(self, 0x00020000)
        self.DAC3EN = BitField(self, 0x00040000)
        self.DAC4EN = BitField(self, 0x00080000)
        self.RNGEN = BitField(self, 0x04000000)

class RCC_AHB3ENR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.FMCEN = BitField(self, 0x00000001)
        self.QSPIEN = BitField(self, 0x00000100)

class RCC_APB1ENR1(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.TIM2EN = BitField(self, 0x00000001)
        self.TIM3EN = BitField(self, 0x00000002)
        self.TIM4EN = BitField(self, 0x00000004)
        self.TIM5EN = BitField(self, 0x00000008)
        self.TIM6EN = BitField(self, 0x00000010)
        self.TIM7EN = BitField(self, 0x00000020)
        self.CRSEN = BitField(self, 0x00000100)
        self.RTCAPBEN = BitField(self, 0x00000400)
        self.WWDGEN = BitField(self, 0x00000800)
        self.SPI2EN = BitField(self, 0x00004000)
        self.SPI3EN = BitField(self, 0x00008000)
        self.USART2EN = BitField(self, 0x00020000)
        self.USART3EN = BitField(self, 0x00040000)
        self.UART4EN = BitField(self, 0x00080000)
        self.UART5EN = BitField(self, 0x00100000)
        self.I2C1EN = BitField(self, 0x00200000)
        self.I2C2EN = BitField(self, 0x00400000)
        self.USBEN = BitField(self, 0x00800000)
        self.FDCANEN = BitField(self, 0x02000000)
        self.PWREN = BitField(self, 0x10000000)
        self.I2C3EN = BitField(self, 0x40000000)
        self.LPTIM1EN = BitField(self, 0x80000000)

class RCC_APB1ENR2(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.LPUART1EN = BitField(self, 0x00000001)
        self.I2C4EN = BitField(self, 0x00000002)
        self.UCPD1EN = BitField(self, 0x00000100)

class RCC_APB2ENR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.SYSCFGEN = BitField(self, 0x00000001)
        self.TIM1EN = BitField(self, 0x00000800)
        self.SPI1EN = BitField(self, 0x00001000)
        self.TIM8EN = BitField(self, 0x00002000)
        self.USART1EN = BitField(self, 0x00004000)
        self.SPI4EN = BitField(self, 0x00008000)
        self.TIM15EN = BitField(self, 0x00010000)
        self.TIM16EN = BitField(self, 0x00020000)
        self.TIM17EN = BitField(self, 0x00040000)
        self.TIM20EN = BitField(self, 0x00100000)
        self.SAI1EN = BitField(self, 0x00200000)
        self.HRTIM1EN = BitField(self, 0x04000000)

class RCC_AHB1SMENR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.DMA1SMEN = BitField(self, 0x00000001)
        self.DMA2SMEN = BitField(self, 0x00000002)
        self.DMAMUX1SMEN = BitField(self, 0x00000004)
        self.CORDICSMEN = BitField(self, 0x00000008)
        self.FMACSMEN = BitField(self, 0x00000010)
        self.FLASHSMEN = BitField(self, 0x00000100)
        self.SRAM1SMEN = BitField(self, 0x00000200)
        self.CRCSMEN = BitField(self, 0x00001000)

class RCC_AHB2SMENR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.GPIOASMEN = BitField(self, 0x00000001)
        self.GPIOBSMEN = BitField(self, 0x00000002)
        self.GPIOCSMEN = BitField(self, 0x00000004)
        self.GPIODSMEN = BitField(self, 0x00000008)
        self.GPIOESMEN = BitField(self, 0x00000010)
        self.GPIOFSMEN = BitField(self, 0x00000020)
        self.GPIOGSMEN = BitField(self, 0x00000040)
        self.CCMSRAMSMEN = BitField(self, 0x00000200)
        self.SRAM2SMEN = BitField(self, 0x00000400)
        self.ADC12SMEN = BitField(self, 0x00002000)
        self.ADC345SMEN = BitField(self, 0x00004000)
        self.DAC1SMEN = BitField(self, 0x00010000)
        self.DAC2SMEN = BitField(self, 0x00020000)
        self.DAC3SMEN = BitField(self, 0x00040000)
        self.DAC4SMEN = BitField(self, 0x00080000)
        self.RNGSMEN = BitField(self, 0x04000000)

class RCC_AHB3SMENR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.FMCSMEN = BitField(self, 0x00000001)
        self.QSPISMEN = BitField(self, 0x00000100)

class RCC_APB1SMENR1(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.TIM2SMEN = BitField(self, 0x00000001)
        self.TIM3SMEN = BitField(self, 0x00000002)
        self.TIM4SMEN = BitField(self, 0x00000004)
        self.TIM5SMEN = BitField(self, 0x00000008)
        self.TIM6SMEN = BitField(self, 0x00000010)
        self.TIM7SMEN = BitField(self, 0x00000020)
        self.CRSSMEN = BitField(self, 0x00000100)
        self.RTCAPBSMEN = BitField(self, 0x00000400)
        self.WWDGSMEN = BitField(self, 0x00000800)
        self.SPI2SMEN = BitField(self, 0x00004000)
        self.SPI3SMEN = BitField(self, 0x00008000)
        self.USART2SMEN = BitField(self, 0x00020000)
        self.USART3SMEN = BitField(self, 0x00040000)
        self.UART4SMEN = BitField(self, 0x00080000)
        self.UART5SMEN = BitField(self, 0x00100000)
        self.I2C1SMEN = BitField(self, 0x00200000)
        self.I2C2SMEN = BitField(self, 0x00400000)
        self.USBSMEN = BitField(self, 0x00800000)
        self.FDCANSMEN = BitField(self, 0x02000000)
        self.PWRSMEN = BitField(self, 0x10000000)
        self.I2C3SMEN = BitField(self, 0x40000000)
        self.LPTIM1SMEN = BitField(self, 0x80000000)

class RCC_APB1SMENR2(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.LPUART1SMEN = BitField(self, 0x00000001)
        self.I2C4SMEN = BitField(self, 0x00000002)
        self.UCPD1SMEN = BitField(self, 0x00000100)

class RCC_APB2SMENR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.SYSCFGSMEN = BitField(self, 0x00000001)
        self.TIM1SMEN = BitField(self, 0x00000800)
        self.SPI1SMEN = BitField(self, 0x00001000)
        self.TIM8SMEN = BitField(self, 0x00002000)
        self.USART1SMEN = BitField(self, 0x00004000)
        self.SPI4SMEN = BitField(self, 0x00008000)
        self.TIM15SMEN = BitField(self, 0x00010000)
        self.TIM16SMEN = BitField(self, 0x00020000)
        self.TIM17SMEN = BitField(self, 0x00040000)
        self.TIM20SMEN = BitField(self, 0x00100000)
        self.SAI1SMEN = BitField(self, 0x00200000)
        self.HRTIM1SMEN = BitField(self, 0x04000000)

class RCC_CCIPR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.USART1SEL = BitField(self, 0x00000003)
        self.USART2SEL = BitField(self, 0x0000000C)
        self.USART3SEL = BitField(self, 0x00000030)
        self.UART4SEL = BitField(self, 0x000000C0)
        self.UART5SEL = BitField(self, 0x00000300)
        self.LPUART1SEL = BitField(self, 0x00000C00)
        self.I2C1SEL = BitField(self, 0x00003000)
        self.I2C2SEL = BitField(self, 0x0000C000)
        self.I2C3SEL = BitField(self, 0x00030000)
        self.LPTIM1SEL = BitField(self, 0x000C0000)
        self.SAI1SEL = BitField(self, 0x00300000)
        self.I2S23SEL = BitField(self, 0x00C00000)
        self.FDCANSEL = BitField(self, 0x03000000)
        self.CLK48SEL = BitField(self, 0x0C000000)
        self.ADC12SEL = BitField(self, 0x30000000)
        self.ADC345SEL = BitField(self, 0xC0000000)

class RCC_BDCR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.LSEON = BitField(self, 0x00000001)
        self.LSERDY = BitField(self, 0x00000002)
        self.LSEBYP = BitField(self, 0x00000004)
        self.LSEDRV = BitField(self, 0x00000018)
        self.LSECSSON = BitField(self, 0x00000020)
        self.LSECSSD = BitField(self, 0x00000040)
        self.RTCSEL = BitField(self, 0x00000300)
        self.RTCEN = BitField(self, 0x00008000)
        self.BDRST = BitField(self, 0x00010000)
        self.LSCOEN = BitField(self, 0x01000000)
        self.LSCOSEL = BitField(self, 0x02000000)

class RCC_CSR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.LSION = BitField(self, 0x00000001)
        self.LSIRDY = BitField(self, 0x00000002)
        self.RMVF = BitField(self, 0x00800000)
        self.OBLRSTF = BitField(self, 0x02000000)
        self.PINRSTF = BitField(self, 0x04000000)
        self.BORRSTF = BitField(self, 0x08000000)
        self.SFTRSTF = BitField(self, 0x10000000)
        self.IWDGRSTF = BitField(self, 0x20000000)
        self.WWDGRSTF = BitField(self, 0x40000000)
        self.LPWRRSTF = BitField(self, 0x80000000)

class RCC_CRRCR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.HSI48ON = BitField(self, 0x00000001)
        self.HSI48RDY = BitField(self, 0x00000002)
        self.HSI48CAL = BitField(self, 0x0000FF80)

class RCC_CCIPR2(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.I2C4SEL = BitField(self, 0x00000003)
        self.QSPISEL = BitField(self, 0x00300000)

class RCC_TypeDef(PeripheralBase):

    def __init__(self, base):
        super().__init__(base)
        self.CR = RCC_CR(base + 0x0)
        self.ICSCR = RCC_ICSCR(base + 0x4)
        self.CFGR = RCC_CFGR(base + 0x8)
        self.PLLCFGR = RCC_PLLCFGR(base + 0xC)
        self.CIER = RCC_CIER(base + 0x18)
        self.CIFR = RCC_CIFR(base + 0x1C)
        self.CICR = RCC_CICR(base + 0x20)
        self.AHB1RSTR = RCC_AHB1RSTR(base + 0x28)
        self.AHB2RSTR = RCC_AHB2RSTR(base + 0x2C)
        self.AHB3RSTR = RCC_AHB3RSTR(base + 0x30)
        self.APB1RSTR1 = RCC_APB1RSTR1(base + 0x38)
        self.APB1RSTR2 = RCC_APB1RSTR2(base + 0x3C)
        self.APB2RSTR = RCC_APB2RSTR(base + 0x40)
        self.AHB1ENR = RCC_AHB1ENR(base + 0x48)
        self.AHB2ENR = RCC_AHB2ENR(base + 0x4C)
        self.AHB3ENR = RCC_AHB3ENR(base + 0x50)
        self.APB1ENR1 = RCC_APB1ENR1(base + 0x58)
        self.APB1ENR2 = RCC_APB1ENR2(base + 0x5C)
        self.APB2ENR = RCC_APB2ENR(base + 0x60)
        self.AHB1SMENR = RCC_AHB1SMENR(base + 0x68)
        self.AHB2SMENR = RCC_AHB2SMENR(base + 0x6C)
        self.AHB3SMENR = RCC_AHB3SMENR(base + 0x70)
        self.APB1SMENR1 = RCC_APB1SMENR1(base + 0x78)
        self.APB1SMENR2 = RCC_APB1SMENR2(base + 0x7C)
        self.APB2SMENR = RCC_APB2SMENR(base + 0x80)
        self.CCIPR = RCC_CCIPR(base + 0x88)
        self.BDCR = RCC_BDCR(base + 0x90)
        self.CSR = RCC_CSR(base + 0x94)
        self.CRRCR = RCC_CRRCR(base + 0x98)
        self.CCIPR2 = RCC_CCIPR2(base + 0x9C)

RCC = RCC_TypeDef(0x40021000)

class RTC_TR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.PM = BitField(self, 0x00400000)
        self.HT = BitField(self, 0x00300000)
        self.HU = BitField(self, 0x000F0000)
        self.MNT = BitField(self, 0x00007000)
        self.MNU = BitField(self, 0x00000F00)
        self.ST = BitField(self, 0x00000070)
        self.SU = BitField(self, 0x0000000F)

class RTC_DR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.YT = BitField(self, 0x00F00000)
        self.YU = BitField(self, 0x000F0000)
        self.WDU = BitField(self, 0x0000E000)
        self.MT = BitField(self, 0x00001000)
        self.MU = BitField(self, 0x00000F00)
        self.DT = BitField(self, 0x00000030)
        self.DU = BitField(self, 0x0000000F)

class RTC_SSR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.SS = BitField(self, 0x0000FFFF)

class RTC_ICSR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.RECALPF = BitField(self, 0x00010000)
        self.INIT = BitField(self, 0x00000080)
        self.INITF = BitField(self, 0x00000040)
        self.RSF = BitField(self, 0x00000020)
        self.INITS = BitField(self, 0x00000010)
        self.SHPF = BitField(self, 0x00000008)
        self.WUTWF = BitField(self, 0x00000004)
        self.ALRBWF = BitField(self, 0x00000002)
        self.ALRAWF = BitField(self, 0x00000001)

class RTC_PRER(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.PREDIV_A = BitField(self, 0x007F0000)
        self.PREDIV_S = BitField(self, 0x00007FFF)

class RTC_WUTR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.WUT = BitField(self, 0x0000FFFF)

class RTC_CR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.OUT2EN = BitField(self, 0x80000000)
        self.TAMPALRM_TYPE = BitField(self, 0x40000000)
        self.TAMPALRM_PU = BitField(self, 0x20000000)
        self.TAMPOE = BitField(self, 0x04000000)
        self.TAMPTS = BitField(self, 0x02000000)
        self.ITSE = BitField(self, 0x01000000)
        self.COE = BitField(self, 0x00800000)
        self.OSEL = BitField(self, 0x00600000)
        self.POL = BitField(self, 0x00100000)
        self.COSEL = BitField(self, 0x00080000)
        self.BKP = BitField(self, 0x00040000)
        self.SUB1H = BitField(self, 0x00020000)
        self.ADD1H = BitField(self, 0x00010000)
        self.TSIE = BitField(self, 0x00008000)
        self.WUTIE = BitField(self, 0x00004000)
        self.ALRBIE = BitField(self, 0x00002000)
        self.ALRAIE = BitField(self, 0x00001000)
        self.TSE = BitField(self, 0x00000800)
        self.WUTE = BitField(self, 0x00000400)
        self.ALRBE = BitField(self, 0x00000200)
        self.ALRAE = BitField(self, 0x00000100)
        self.FMT = BitField(self, 0x00000040)
        self.BYPSHAD = BitField(self, 0x00000020)
        self.REFCKON = BitField(self, 0x00000010)
        self.TSEDGE = BitField(self, 0x00000008)
        self.WUCKSEL = BitField(self, 0x00000007)

class RTC_WPR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.KEY = BitField(self, 0x000000FF)

class RTC_CALR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.CALP = BitField(self, 0x00008000)
        self.CALW8 = BitField(self, 0x00004000)
        self.CALW16 = BitField(self, 0x00002000)
        self.CALM = BitField(self, 0x000001FF)

class RTC_SHIFTR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.SUBFS = BitField(self, 0x00007FFF)
        self.ADD1S = BitField(self, 0x80000000)

class RTC_TSTR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.PM = BitField(self, 0x00400000)
        self.HT = BitField(self, 0x00300000)
        self.HU = BitField(self, 0x000F0000)
        self.MNT = BitField(self, 0x00007000)
        self.MNU = BitField(self, 0x00000F00)
        self.ST = BitField(self, 0x00000070)
        self.SU = BitField(self, 0x0000000F)

class RTC_TSDR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.WDU = BitField(self, 0x0000E000)
        self.MT = BitField(self, 0x00001000)
        self.MU = BitField(self, 0x00000F00)
        self.DT = BitField(self, 0x00000030)
        self.DU = BitField(self, 0x0000000F)

class RTC_TSSSR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.SS = BitField(self, 0x0000FFFF)

class RTC_ALRMAR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.MSK4 = BitField(self, 0x80000000)
        self.WDSEL = BitField(self, 0x40000000)
        self.DT = BitField(self, 0x30000000)
        self.DU = BitField(self, 0x0F000000)
        self.MSK3 = BitField(self, 0x00800000)
        self.PM = BitField(self, 0x00400000)
        self.HT = BitField(self, 0x00300000)
        self.HU = BitField(self, 0x000F0000)
        self.MSK2 = BitField(self, 0x00008000)
        self.MNT = BitField(self, 0x00007000)
        self.MNU = BitField(self, 0x00000F00)
        self.MSK1 = BitField(self, 0x00000080)
        self.ST = BitField(self, 0x00000070)
        self.SU = BitField(self, 0x0000000F)

class RTC_ALRMASSR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.MASKSS = BitField(self, 0x0F000000)
        self.SS = BitField(self, 0x00007FFF)

class RTC_ALRMBR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.MSK4 = BitField(self, 0x80000000)
        self.WDSEL = BitField(self, 0x40000000)
        self.DT = BitField(self, 0x30000000)
        self.DU = BitField(self, 0x0F000000)
        self.MSK3 = BitField(self, 0x00800000)
        self.PM = BitField(self, 0x00400000)
        self.HT = BitField(self, 0x00300000)
        self.HU = BitField(self, 0x000F0000)
        self.MSK2 = BitField(self, 0x00008000)
        self.MNT = BitField(self, 0x00007000)
        self.MNU = BitField(self, 0x00000F00)
        self.MSK1 = BitField(self, 0x00000080)
        self.ST = BitField(self, 0x00000070)
        self.SU = BitField(self, 0x0000000F)

class RTC_ALRMBSSR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.MASKSS = BitField(self, 0x0F000000)
        self.SS = BitField(self, 0x00007FFF)

class RTC_SR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.ITSF = BitField(self, 0x00000020)
        self.TSOVF = BitField(self, 0x00000010)
        self.TSF = BitField(self, 0x00000008)
        self.WUTF = BitField(self, 0x00000004)
        self.ALRBF = BitField(self, 0x00000002)
        self.ALRAF = BitField(self, 0x00000001)

class RTC_MISR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.ITSMF = BitField(self, 0x00000020)
        self.TSOVMF = BitField(self, 0x00000010)
        self.TSMF = BitField(self, 0x00000008)
        self.WUTMF = BitField(self, 0x00000004)
        self.ALRBMF = BitField(self, 0x00000002)
        self.ALRAMF = BitField(self, 0x00000001)

class RTC_SCR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.CITSF = BitField(self, 0x00000020)
        self.CTSOVF = BitField(self, 0x00000010)
        self.CTSF = BitField(self, 0x00000008)
        self.CWUTF = BitField(self, 0x00000004)
        self.CALRBF = BitField(self, 0x00000002)
        self.CALRAF = BitField(self, 0x00000001)

class RTC_TypeDef(PeripheralBase):

    def __init__(self, base):
        super().__init__(base)
        self.TR = RTC_TR(base + 0x0)
        self.DR = RTC_DR(base + 0x4)
        self.SSR = RTC_SSR(base + 0x8)
        self.ICSR = RTC_ICSR(base + 0xC)
        self.PRER = RTC_PRER(base + 0x10)
        self.WUTR = RTC_WUTR(base + 0x14)
        self.CR = RTC_CR(base + 0x18)
        self.WPR = RTC_WPR(base + 0x24)
        self.CALR = RTC_CALR(base + 0x28)
        self.SHIFTR = RTC_SHIFTR(base + 0x2C)
        self.TSTR = RTC_TSTR(base + 0x30)
        self.TSDR = RTC_TSDR(base + 0x34)
        self.TSSSR = RTC_TSSSR(base + 0x38)
        self.ALRMAR = RTC_ALRMAR(base + 0x40)
        self.ALRMASSR = RTC_ALRMASSR(base + 0x44)
        self.ALRMBR = RTC_ALRMBR(base + 0x48)
        self.ALRMBSSR = RTC_ALRMBSSR(base + 0x4C)
        self.SR = RTC_SR(base + 0x50)
        self.MISR = RTC_MISR(base + 0x54)
        self.SCR = RTC_SCR(base + 0x5C)

RTC = RTC_TypeDef(0x40002800)

class TAMP_CR1(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.TAMP1E = BitField(self, 0x00000001)
        self.TAMP2E = BitField(self, 0x00000002)
        self.TAMP3E = BitField(self, 0x00000004)
        self.ITAMP3E = BitField(self, 0x00040000)
        self.ITAMP4E = BitField(self, 0x00080000)
        self.ITAMP5E = BitField(self, 0x00100000)
        self.ITAMP6E = BitField(self, 0x00200000)

class TAMP_CR2(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.TAMP1NOERASE = BitField(self, 0x00000001)
        self.TAMP2NOERASE = BitField(self, 0x00000002)
        self.TAMP3NOERASE = BitField(self, 0x00000004)
        self.TAMP1MF = BitField(self, 0x00010000)
        self.TAMP2MF = BitField(self, 0x00020000)
        self.TAMP3MF = BitField(self, 0x00040000)
        self.TAMP1TRG = BitField(self, 0x01000000)
        self.TAMP2TRG = BitField(self, 0x02000000)
        self.TAMP3TRG = BitField(self, 0x04000000)

class TAMP_FLTCR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.TAMPFREQ = BitField(self, 0x00000007)
        self.TAMPFLT = BitField(self, 0x00000018)
        self.TAMPPRCH = BitField(self, 0x00000060)
        self.TAMPPUDIS = BitField(self, 0x00000080)

class TAMP_IER(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.TAMP1IE = BitField(self, 0x00000001)
        self.TAMP2IE = BitField(self, 0x00000002)
        self.TAMP3IE = BitField(self, 0x00000004)
        self.ITAMP3IE = BitField(self, 0x00040000)
        self.ITAMP4IE = BitField(self, 0x00080000)
        self.ITAMP5IE = BitField(self, 0x00100000)
        self.ITAMP6IE = BitField(self, 0x00200000)

class TAMP_SR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.TAMP1F = BitField(self, 0x00000001)
        self.TAMP2F = BitField(self, 0x00000002)
        self.TAMP3F = BitField(self, 0x00000004)
        self.ITAMP3F = BitField(self, 0x00040000)
        self.ITAMP4F = BitField(self, 0x00080000)
        self.ITAMP5F = BitField(self, 0x00100000)
        self.ITAMP6F = BitField(self, 0x00200000)

class TAMP_MISR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.TAMP1MF = BitField(self, 0x00000001)
        self.TAMP2MF = BitField(self, 0x00000002)
        self.TAMP3MF = BitField(self, 0x00000004)
        self.ITAMP3MF = BitField(self, 0x00040000)
        self.ITAMP4MF = BitField(self, 0x00080000)
        self.ITAMP5MF = BitField(self, 0x00100000)
        self.ITAMP6MF = BitField(self, 0x00200000)

class TAMP_SCR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.CTAMP1F = BitField(self, 0x00000001)
        self.CTAMP2F = BitField(self, 0x00000002)
        self.CTAMP3F = BitField(self, 0x00000004)
        self.CITAMP3F = BitField(self, 0x00040000)
        self.CITAMP4F = BitField(self, 0x00080000)
        self.CITAMP5F = BitField(self, 0x00100000)
        self.CITAMP6F = BitField(self, 0x00200000)

class TAMP_BKP0R(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.BKP0R = BitField(self, 0xFFFFFFFF)

class TAMP_BKP1R(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.BKP1R = BitField(self, 0xFFFFFFFF)

class TAMP_BKP2R(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.BKP2R = BitField(self, 0xFFFFFFFF)

class TAMP_BKP3R(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.BKP3R = BitField(self, 0xFFFFFFFF)

class TAMP_BKP4R(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.BKP4R = BitField(self, 0xFFFFFFFF)

class TAMP_BKP5R(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.BKP5R = BitField(self, 0xFFFFFFFF)

class TAMP_BKP6R(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.BKP6R = BitField(self, 0xFFFFFFFF)

class TAMP_BKP7R(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.BKP7R = BitField(self, 0xFFFFFFFF)

class TAMP_BKP8R(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.BKP8R = BitField(self, 0xFFFFFFFF)

class TAMP_BKP9R(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.BKP9R = BitField(self, 0xFFFFFFFF)

class TAMP_BKP10R(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.BKP10R = BitField(self, 0xFFFFFFFF)

class TAMP_BKP11R(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.BKP11R = BitField(self, 0xFFFFFFFF)

class TAMP_BKP12R(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.BKP12R = BitField(self, 0xFFFFFFFF)

class TAMP_BKP13R(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.BKP13R = BitField(self, 0xFFFFFFFF)

class TAMP_BKP14R(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.BKP14R = BitField(self, 0xFFFFFFFF)

class TAMP_BKP15R(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.BKP15R = BitField(self, 0xFFFFFFFF)

class TAMP_BKP16R(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.BKP16R = BitField(self, 0xFFFFFFFF)

class TAMP_BKP17R(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.BKP17R = BitField(self, 0xFFFFFFFF)

class TAMP_BKP18R(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.BKP18R = BitField(self, 0xFFFFFFFF)

class TAMP_BKP19R(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.BKP19R = BitField(self, 0xFFFFFFFF)

class TAMP_BKP20R(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.BKP20R = BitField(self, 0xFFFFFFFF)

class TAMP_BKP21R(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.BKP21R = BitField(self, 0xFFFFFFFF)

class TAMP_BKP22R(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.BKP22R = BitField(self, 0xFFFFFFFF)

class TAMP_BKP23R(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.BKP23R = BitField(self, 0xFFFFFFFF)

class TAMP_BKP24R(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.BKP24R = BitField(self, 0xFFFFFFFF)

class TAMP_BKP25R(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.BKP25R = BitField(self, 0xFFFFFFFF)

class TAMP_BKP26R(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.BKP26R = BitField(self, 0xFFFFFFFF)

class TAMP_BKP27R(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.BKP27R = BitField(self, 0xFFFFFFFF)

class TAMP_BKP28R(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.BKP28R = BitField(self, 0xFFFFFFFF)

class TAMP_BKP29R(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.BKP29R = BitField(self, 0xFFFFFFFF)

class TAMP_BKP30R(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.BKP30R = BitField(self, 0xFFFFFFFF)

class TAMP_BKP31R(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.BKP31R = BitField(self, 0xFFFFFFFF)

class TAMP_TypeDef(PeripheralBase):

    def __init__(self, base):
        super().__init__(base)
        self.CR1 = TAMP_CR1(base + 0x0)
        self.CR2 = TAMP_CR2(base + 0x4)
        self.FLTCR = TAMP_FLTCR(base + 0xC)
        self.IER = TAMP_IER(base + 0x2C)
        self.SR = TAMP_SR(base + 0x30)
        self.MISR = TAMP_MISR(base + 0x34)
        self.SCR = TAMP_SCR(base + 0x3C)
        self.BKP0R = TAMP_BKP0R(base + 0x100)
        self.BKP1R = TAMP_BKP1R(base + 0x104)
        self.BKP2R = TAMP_BKP2R(base + 0x108)
        self.BKP3R = TAMP_BKP3R(base + 0x10C)
        self.BKP4R = TAMP_BKP4R(base + 0x110)
        self.BKP5R = TAMP_BKP5R(base + 0x114)
        self.BKP6R = TAMP_BKP6R(base + 0x118)
        self.BKP7R = TAMP_BKP7R(base + 0x11C)
        self.BKP8R = TAMP_BKP8R(base + 0x120)
        self.BKP9R = TAMP_BKP9R(base + 0x124)
        self.BKP10R = TAMP_BKP10R(base + 0x128)
        self.BKP11R = TAMP_BKP11R(base + 0x12C)
        self.BKP12R = TAMP_BKP12R(base + 0x130)
        self.BKP13R = TAMP_BKP13R(base + 0x134)
        self.BKP14R = TAMP_BKP14R(base + 0x138)
        self.BKP15R = TAMP_BKP15R(base + 0x13C)
        self.BKP16R = TAMP_BKP16R(base + 0x140)
        self.BKP17R = TAMP_BKP17R(base + 0x144)
        self.BKP18R = TAMP_BKP18R(base + 0x148)
        self.BKP19R = TAMP_BKP19R(base + 0x14C)
        self.BKP20R = TAMP_BKP20R(base + 0x150)
        self.BKP21R = TAMP_BKP21R(base + 0x154)
        self.BKP22R = TAMP_BKP22R(base + 0x158)
        self.BKP23R = TAMP_BKP23R(base + 0x15C)
        self.BKP24R = TAMP_BKP24R(base + 0x160)
        self.BKP25R = TAMP_BKP25R(base + 0x164)
        self.BKP26R = TAMP_BKP26R(base + 0x168)
        self.BKP27R = TAMP_BKP27R(base + 0x16C)
        self.BKP28R = TAMP_BKP28R(base + 0x170)
        self.BKP29R = TAMP_BKP29R(base + 0x174)
        self.BKP30R = TAMP_BKP30R(base + 0x178)
        self.BKP31R = TAMP_BKP31R(base + 0x17C)

TAMP = TAMP_TypeDef(0x40002400)

class SAI_PDMCR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.PDMEN = BitField(self, 0x00000001)
        self.MICNBR = BitField(self, 0x00000030)
        self.CKEN1 = BitField(self, 0x00000100)
        self.CKEN2 = BitField(self, 0x00000200)
        self.CKEN3 = BitField(self, 0x00000400)
        self.CKEN4 = BitField(self, 0x00000800)

class SAI_PDMDLY(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.DLYM1L = BitField(self, 0x00000007)
        self.DLYM1R = BitField(self, 0x00000070)
        self.DLYM2L = BitField(self, 0x00000700)
        self.DLYM2R = BitField(self, 0x00007000)
        self.DLYM3L = BitField(self, 0x00070000)
        self.DLYM3R = BitField(self, 0x00700000)
        self.DLYM4L = BitField(self, 0x07000000)
        self.DLYM4R = BitField(self, 0x70000000)

class SAI_TypeDef(PeripheralBase):

    def __init__(self, base):
        super().__init__(base)
        self.PDMCR = SAI_PDMCR(base + 0x44)
        self.PDMDLY = SAI_PDMDLY(base + 0x48)

SAI1 = SAI_TypeDef(0x40015400)

class SAI_Block_CR1(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.MODE = BitField(self, 0x00000003)
        self.PRTCFG = BitField(self, 0x0000000C)
        self.DS = BitField(self, 0x000000E0)
        self.LSBFIRST = BitField(self, 0x00000100)
        self.CKSTR = BitField(self, 0x00000200)
        self.SYNCEN = BitField(self, 0x00000C00)
        self.MONO = BitField(self, 0x00001000)
        self.OUTDRIV = BitField(self, 0x00002000)
        self.SAIEN = BitField(self, 0x00010000)
        self.DMAEN = BitField(self, 0x00020000)
        self.NODIV = BitField(self, 0x00080000)
        self.MCKDIV = BitField(self, 0x03F00000)
        self.OSR = BitField(self, 0x04000000)
        self.MCKEN = BitField(self, 0x08000000)

class SAI_Block_CR2(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.FTH = BitField(self, 0x00000007)
        self.FFLUSH = BitField(self, 0x00000008)
        self.TRIS = BitField(self, 0x00000010)
        self.MUTE = BitField(self, 0x00000020)
        self.MUTEVAL = BitField(self, 0x00000040)
        self.MUTECNT = BitField(self, 0x00001F80)
        self.CPL = BitField(self, 0x00002000)
        self.COMP = BitField(self, 0x0000C000)

class SAI_Block_FRCR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.FRL = BitField(self, 0x000000FF)
        self.FSALL = BitField(self, 0x00007F00)
        self.FSDEF = BitField(self, 0x00010000)
        self.FSPOL = BitField(self, 0x00020000)
        self.FSOFF = BitField(self, 0x00040000)

class SAI_Block_SLOTR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.FBOFF = BitField(self, 0x0000001F)
        self.SLOTSZ = BitField(self, 0x000000C0)
        self.NBSLOT = BitField(self, 0x00000F00)
        self.SLOTEN = BitField(self, 0xFFFF0000)

class SAI_Block_IMR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.OVRUDRIE = BitField(self, 0x00000001)
        self.MUTEDETIE = BitField(self, 0x00000002)
        self.WCKCFGIE = BitField(self, 0x00000004)
        self.FREQIE = BitField(self, 0x00000008)
        self.CNRDYIE = BitField(self, 0x00000010)
        self.AFSDETIE = BitField(self, 0x00000020)
        self.LFSDETIE = BitField(self, 0x00000040)

class SAI_Block_SR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.OVRUDR = BitField(self, 0x00000001)
        self.MUTEDET = BitField(self, 0x00000002)
        self.WCKCFG = BitField(self, 0x00000004)
        self.FREQ = BitField(self, 0x00000008)
        self.CNRDY = BitField(self, 0x00000010)
        self.AFSDET = BitField(self, 0x00000020)
        self.LFSDET = BitField(self, 0x00000040)
        self.FLVL = BitField(self, 0x00070000)

class SAI_Block_CLRFR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.COVRUDR = BitField(self, 0x00000001)
        self.CMUTEDET = BitField(self, 0x00000002)
        self.CWCKCFG = BitField(self, 0x00000004)
        self.CFREQ = BitField(self, 0x00000008)
        self.CCNRDY = BitField(self, 0x00000010)
        self.CAFSDET = BitField(self, 0x00000020)
        self.CLFSDET = BitField(self, 0x00000040)

class SAI_Block_DR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.DATA = BitField(self, 0xFFFFFFFF)

class SAI_Block_TypeDef(PeripheralBase):

    def __init__(self, base):
        super().__init__(base)
        self.CR1 = SAI_Block_CR1(base + 0x0)
        self.CR2 = SAI_Block_CR2(base + 0x4)
        self.FRCR = SAI_Block_FRCR(base + 0x8)
        self.SLOTR = SAI_Block_SLOTR(base + 0xC)
        self.IMR = SAI_Block_IMR(base + 0x10)
        self.SR = SAI_Block_SR(base + 0x14)
        self.CLRFR = SAI_Block_CLRFR(base + 0x18)
        self.DR = SAI_Block_DR(base + 0x1C)

SAI1_Block_A = SAI_Block_TypeDef(0x40015404)
SAI1_Block_B = SAI_Block_TypeDef(0x40015424)

class SPI_CR1(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.CPHA = BitField(self, 0x00000001)
        self.CPOL = BitField(self, 0x00000002)
        self.MSTR = BitField(self, 0x00000004)
        self.BR = BitField(self, 0x00000038)
        self.SPE = BitField(self, 0x00000040)
        self.LSBFIRST = BitField(self, 0x00000080)
        self.SSI = BitField(self, 0x00000100)
        self.SSM = BitField(self, 0x00000200)
        self.RXONLY = BitField(self, 0x00000400)
        self.CRCL = BitField(self, 0x00000800)
        self.CRCNEXT = BitField(self, 0x00001000)
        self.CRCEN = BitField(self, 0x00002000)
        self.BIDIOE = BitField(self, 0x00004000)
        self.BIDIMODE = BitField(self, 0x00008000)

class SPI_CR2(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.RXDMAEN = BitField(self, 0x00000001)
        self.TXDMAEN = BitField(self, 0x00000002)
        self.SSOE = BitField(self, 0x00000004)
        self.NSSP = BitField(self, 0x00000008)
        self.FRF = BitField(self, 0x00000010)
        self.ERRIE = BitField(self, 0x00000020)
        self.RXNEIE = BitField(self, 0x00000040)
        self.TXEIE = BitField(self, 0x00000080)
        self.DS = BitField(self, 0x00000F00)
        self.FRXTH = BitField(self, 0x00001000)
        self.LDMARX = BitField(self, 0x00002000)
        self.LDMATX = BitField(self, 0x00004000)

class SPI_SR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.RXNE = BitField(self, 0x00000001)
        self.TXE = BitField(self, 0x00000002)
        self.CHSIDE = BitField(self, 0x00000004)
        self.UDR = BitField(self, 0x00000008)
        self.CRCERR = BitField(self, 0x00000010)
        self.MODF = BitField(self, 0x00000020)
        self.OVR = BitField(self, 0x00000040)
        self.BSY = BitField(self, 0x00000080)
        self.FRE = BitField(self, 0x00000100)
        self.FRLVL = BitField(self, 0x00000600)
        self.FTLVL = BitField(self, 0x00001800)

class SPI_DR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.DR = BitField(self, 0x0000FFFF)

class SPI_CRCPR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.CRCPOLY = BitField(self, 0x0000FFFF)

class SPI_RXCRCR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.RXCRC = BitField(self, 0x0000FFFF)

class SPI_TXCRCR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.TXCRC = BitField(self, 0x0000FFFF)

class SPI_I2SCFGR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.CHLEN = BitField(self, 0x00000001)
        self.DATLEN = BitField(self, 0x00000006)
        self.CKPOL = BitField(self, 0x00000008)
        self.I2SSTD = BitField(self, 0x00000030)
        self.PCMSYNC = BitField(self, 0x00000080)
        self.I2SCFG = BitField(self, 0x00000300)
        self.I2SE = BitField(self, 0x00000400)
        self.I2SMOD = BitField(self, 0x00000800)
        self.ASTRTEN = BitField(self, 0x00001000)

class SPI_I2SPR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.I2SDIV = BitField(self, 0x000000FF)
        self.ODD = BitField(self, 0x00000100)
        self.MCKOE = BitField(self, 0x00000200)

class SPI_TypeDef(PeripheralBase):

    def __init__(self, base):
        super().__init__(base)
        self.CR1 = SPI_CR1(base + 0x0)
        self.CR2 = SPI_CR2(base + 0x4)
        self.SR = SPI_SR(base + 0x8)
        self.DR = SPI_DR(base + 0xC)
        self.CRCPR = SPI_CRCPR(base + 0x10)
        self.RXCRCR = SPI_RXCRCR(base + 0x14)
        self.TXCRCR = SPI_TXCRCR(base + 0x18)
        self.I2SCFGR = SPI_I2SCFGR(base + 0x1C)
        self.I2SPR = SPI_I2SPR(base + 0x20)

SPI2 = SPI_TypeDef(0x40003800)
SPI3 = SPI_TypeDef(0x40003C00)
SPI1 = SPI_TypeDef(0x40013000)
SPI4 = SPI_TypeDef(0x40013C00)

class SYSCFG_MEMRMP(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.MEM_MODE = BitField(self, 0x00000007)
        self.FB_MODE = BitField(self, 0x00000100)

class SYSCFG_CFGR1(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.BOOSTEN = BitField(self, 0x00000100)
        self.ANASWVDD = BitField(self, 0x00000200)
        self.I2C_PB6_FMP = BitField(self, 0x00010000)
        self.I2C_PB7_FMP = BitField(self, 0x00020000)
        self.I2C_PB8_FMP = BitField(self, 0x00040000)
        self.I2C_PB9_FMP = BitField(self, 0x00080000)
        self.I2C1_FMP = BitField(self, 0x00100000)
        self.I2C2_FMP = BitField(self, 0x00200000)
        self.I2C3_FMP = BitField(self, 0x00400000)
        self.I2C4_FMP = BitField(self, 0x00800000)

class SYSCFG_EXTICR1(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.EXTI0 = BitField(self, 0x00000007)
        self.EXTI1 = BitField(self, 0x00000070)
        self.EXTI2 = BitField(self, 0x00000700)
        self.EXTI3 = BitField(self, 0x00007000)

class SYSCFG_EXTICR2(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.EXTI4 = BitField(self, 0x00000007)
        self.EXTI5 = BitField(self, 0x00000070)
        self.EXTI6 = BitField(self, 0x00000700)
        self.EXTI7 = BitField(self, 0x00007000)

class SYSCFG_EXTICR3(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.EXTI8 = BitField(self, 0x00000007)
        self.EXTI9 = BitField(self, 0x00000070)
        self.EXTI10 = BitField(self, 0x00000700)
        self.EXTI11 = BitField(self, 0x00007000)

class SYSCFG_EXTICR4(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.EXTI12 = BitField(self, 0x00000007)
        self.EXTI13 = BitField(self, 0x00000070)
        self.EXTI14 = BitField(self, 0x00000700)
        self.EXTI15 = BitField(self, 0x00007000)

class SYSCFG_SCSR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.CCMER = BitField(self, 0x00000001)
        self.CCMBSY = BitField(self, 0x00000002)

class SYSCFG_CFGR2(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.CLL = BitField(self, 0x00000001)
        self.SPL = BitField(self, 0x00000002)
        self.PVDL = BitField(self, 0x00000004)
        self.ECCL = BitField(self, 0x00000008)
        self.SPF = BitField(self, 0x00000100)

class SYSCFG_SWPR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.PAGE0 = BitField(self, 0x00000001)
        self.PAGE1 = BitField(self, 0x00000002)
        self.PAGE2 = BitField(self, 0x00000004)
        self.PAGE3 = BitField(self, 0x00000008)
        self.PAGE4 = BitField(self, 0x00000010)
        self.PAGE5 = BitField(self, 0x00000020)
        self.PAGE6 = BitField(self, 0x00000040)
        self.PAGE7 = BitField(self, 0x00000080)
        self.PAGE8 = BitField(self, 0x00000100)
        self.PAGE9 = BitField(self, 0x00000200)
        self.PAGE10 = BitField(self, 0x00000400)
        self.PAGE11 = BitField(self, 0x00000800)
        self.PAGE12 = BitField(self, 0x00001000)
        self.PAGE13 = BitField(self, 0x00002000)
        self.PAGE14 = BitField(self, 0x00004000)
        self.PAGE15 = BitField(self, 0x00008000)
        self.PAGE16 = BitField(self, 0x00010000)
        self.PAGE17 = BitField(self, 0x00020000)
        self.PAGE18 = BitField(self, 0x00040000)
        self.PAGE19 = BitField(self, 0x00080000)
        self.PAGE20 = BitField(self, 0x00100000)
        self.PAGE21 = BitField(self, 0x00200000)
        self.PAGE22 = BitField(self, 0x00400000)
        self.PAGE23 = BitField(self, 0x00800000)
        self.PAGE24 = BitField(self, 0x01000000)
        self.PAGE25 = BitField(self, 0x02000000)
        self.PAGE26 = BitField(self, 0x04000000)
        self.PAGE27 = BitField(self, 0x08000000)
        self.PAGE28 = BitField(self, 0x10000000)
        self.PAGE29 = BitField(self, 0x20000000)
        self.PAGE30 = BitField(self, 0x40000000)
        self.PAGE31 = BitField(self, 0x80000000)

class SYSCFG_SKR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.KEY = BitField(self, 0x000000FF)

class SYSCFG_TypeDef(PeripheralBase):

    def __init__(self, base):
        super().__init__(base)
        self.MEMRMP = SYSCFG_MEMRMP(base + 0x0)
        self.CFGR1 = SYSCFG_CFGR1(base + 0x4)
        self.EXTICR1 = SYSCFG_EXTICR1(base + 0x8)
        self.EXTICR2 = SYSCFG_EXTICR2(base + 0xC)
        self.EXTICR3 = SYSCFG_EXTICR3(base + 0x10)
        self.EXTICR4 = SYSCFG_EXTICR4(base + 0x14)
        self.SCSR = SYSCFG_SCSR(base + 0x18)
        self.CFGR2 = SYSCFG_CFGR2(base + 0x1C)
        self.SWPR = SYSCFG_SWPR(base + 0x20)
        self.SKR = SYSCFG_SKR(base + 0x24)

SYSCFG = SYSCFG_TypeDef(0x40010000)

class TIM_CR1(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.CEN = BitField(self, 0x00000001)
        self.UDIS = BitField(self, 0x00000002)
        self.URS = BitField(self, 0x00000004)
        self.OPM = BitField(self, 0x00000008)
        self.DIR = BitField(self, 0x00000010)
        self.CMS = BitField(self, 0x00000060)
        self.ARPE = BitField(self, 0x00000080)
        self.CKD = BitField(self, 0x00000300)
        self.UIFREMAP = BitField(self, 0x00000800)
        self.DITHEN = BitField(self, 0x00001000)

class TIM_CR2(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.CCPC = BitField(self, 0x00000001)
        self.CCUS = BitField(self, 0x00000004)
        self.CCDS = BitField(self, 0x00000008)
        self.MMS = BitField(self, 0x02000070)
        self.TI1S = BitField(self, 0x00000080)
        self.OIS1 = BitField(self, 0x00000100)
        self.OIS1N = BitField(self, 0x00000200)
        self.OIS2 = BitField(self, 0x00000400)
        self.OIS2N = BitField(self, 0x00000800)
        self.OIS3 = BitField(self, 0x00001000)
        self.OIS3N = BitField(self, 0x00002000)
        self.OIS4 = BitField(self, 0x00004000)
        self.OIS4N = BitField(self, 0x00008000)
        self.OIS5 = BitField(self, 0x00010000)
        self.OIS6 = BitField(self, 0x00040000)
        self.MMS2 = BitField(self, 0x00F00000)

class TIM_SMCR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.SMS = BitField(self, 0x00010007)
        self.OCCS = BitField(self, 0x00000008)
        self.TS = BitField(self, 0x00300070)
        self.MSM = BitField(self, 0x00000080)
        self.ETF = BitField(self, 0x00000F00)
        self.ETPS = BitField(self, 0x00003000)
        self.ECE = BitField(self, 0x00004000)
        self.ETP = BitField(self, 0x00008000)
        self.SMSPE = BitField(self, 0x01000000)
        self.SMSPS = BitField(self, 0x02000000)

class TIM_DIER(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.UIE = BitField(self, 0x00000001)
        self.CC1IE = BitField(self, 0x00000002)
        self.CC2IE = BitField(self, 0x00000004)
        self.CC3IE = BitField(self, 0x00000008)
        self.CC4IE = BitField(self, 0x00000010)
        self.COMIE = BitField(self, 0x00000020)
        self.TIE = BitField(self, 0x00000040)
        self.BIE = BitField(self, 0x00000080)
        self.UDE = BitField(self, 0x00000100)
        self.CC1DE = BitField(self, 0x00000200)
        self.CC2DE = BitField(self, 0x00000400)
        self.CC3DE = BitField(self, 0x00000800)
        self.CC4DE = BitField(self, 0x00001000)
        self.COMDE = BitField(self, 0x00002000)
        self.TDE = BitField(self, 0x00004000)
        self.IDXIE = BitField(self, 0x00100000)
        self.DIRIE = BitField(self, 0x00200000)
        self.IERRIE = BitField(self, 0x00400000)
        self.TERRIE = BitField(self, 0x00800000)

class TIM_SR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.UIF = BitField(self, 0x00000001)
        self.CC1IF = BitField(self, 0x00000002)
        self.CC2IF = BitField(self, 0x00000004)
        self.CC3IF = BitField(self, 0x00000008)
        self.CC4IF = BitField(self, 0x00000010)
        self.COMIF = BitField(self, 0x00000020)
        self.TIF = BitField(self, 0x00000040)
        self.BIF = BitField(self, 0x00000080)
        self.B2IF = BitField(self, 0x00000100)
        self.CC1OF = BitField(self, 0x00000200)
        self.CC2OF = BitField(self, 0x00000400)
        self.CC3OF = BitField(self, 0x00000800)
        self.CC4OF = BitField(self, 0x00001000)
        self.SBIF = BitField(self, 0x00002000)
        self.CC5IF = BitField(self, 0x00010000)
        self.CC6IF = BitField(self, 0x00020000)
        self.IDXF = BitField(self, 0x00100000)
        self.DIRF = BitField(self, 0x00200000)
        self.IERRF = BitField(self, 0x00400000)
        self.TERRF = BitField(self, 0x00800000)

class TIM_EGR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.UG = BitField(self, 0x00000001)
        self.CC1G = BitField(self, 0x00000002)
        self.CC2G = BitField(self, 0x00000004)
        self.CC3G = BitField(self, 0x00000008)
        self.CC4G = BitField(self, 0x00000010)
        self.COMG = BitField(self, 0x00000020)
        self.TG = BitField(self, 0x00000040)
        self.BG = BitField(self, 0x00000080)
        self.B2G = BitField(self, 0x00000100)

class TIM_CCMR1(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.CC1S = BitField(self, 0x00000003)
        self.OC1FE = BitField(self, 0x00000004)
        self.OC1PE = BitField(self, 0x00000008)
        self.OC1M = BitField(self, 0x00010070)
        self.OC1CE = BitField(self, 0x00000080)
        self.CC2S = BitField(self, 0x00000300)
        self.OC2FE = BitField(self, 0x00000400)
        self.OC2PE = BitField(self, 0x00000800)
        self.OC2M = BitField(self, 0x01007000)
        self.OC2CE = BitField(self, 0x00008000)
        self.IC1PSC = BitField(self, 0x0000000C)
        self.IC1F = BitField(self, 0x000000F0)
        self.IC2PSC = BitField(self, 0x00000C00)
        self.IC2F = BitField(self, 0x0000F000)

class TIM_CCMR2(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.CC3S = BitField(self, 0x00000003)
        self.OC3FE = BitField(self, 0x00000004)
        self.OC3PE = BitField(self, 0x00000008)
        self.OC3M = BitField(self, 0x00010070)
        self.OC3CE = BitField(self, 0x00000080)
        self.CC4S = BitField(self, 0x00000300)
        self.OC4FE = BitField(self, 0x00000400)
        self.OC4PE = BitField(self, 0x00000800)
        self.OC4M = BitField(self, 0x01007000)
        self.OC4CE = BitField(self, 0x00008000)
        self.IC3PSC = BitField(self, 0x0000000C)
        self.IC3F = BitField(self, 0x000000F0)
        self.IC4PSC = BitField(self, 0x00000C00)
        self.IC4F = BitField(self, 0x0000F000)

class TIM_CCER(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.CC1E = BitField(self, 0x00000001)
        self.CC1P = BitField(self, 0x00000002)
        self.CC1NE = BitField(self, 0x00000004)
        self.CC1NP = BitField(self, 0x00000008)
        self.CC2E = BitField(self, 0x00000010)
        self.CC2P = BitField(self, 0x00000020)
        self.CC2NE = BitField(self, 0x00000040)
        self.CC2NP = BitField(self, 0x00000080)
        self.CC3E = BitField(self, 0x00000100)
        self.CC3P = BitField(self, 0x00000200)
        self.CC3NE = BitField(self, 0x00000400)
        self.CC3NP = BitField(self, 0x00000800)
        self.CC4E = BitField(self, 0x00001000)
        self.CC4P = BitField(self, 0x00002000)
        self.CC4NE = BitField(self, 0x00004000)
        self.CC4NP = BitField(self, 0x00008000)
        self.CC5E = BitField(self, 0x00010000)
        self.CC5P = BitField(self, 0x00020000)
        self.CC6E = BitField(self, 0x00100000)
        self.CC6P = BitField(self, 0x00200000)

class TIM_CNT(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.CNT = BitField(self, 0xFFFFFFFF)
        self.UIFCPY = BitField(self, 0x80000000)

class TIM_PSC(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.PSC = BitField(self, 0x0000FFFF)

class TIM_ARR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.ARR = BitField(self, 0xFFFFFFFF)

class TIM_RCR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.REP = BitField(self, 0x0000FFFF)

class TIM_CCR1(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.CCR1 = BitField(self, 0x0000FFFF)

class TIM_CCR2(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.CCR2 = BitField(self, 0x0000FFFF)

class TIM_CCR3(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.CCR3 = BitField(self, 0x0000FFFF)

class TIM_CCR4(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.CCR4 = BitField(self, 0x0000FFFF)

class TIM_BDTR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.DTG = BitField(self, 0x000000FF)
        self.LOCK = BitField(self, 0x00000300)
        self.OSSI = BitField(self, 0x00000400)
        self.OSSR = BitField(self, 0x00000800)
        self.BKE = BitField(self, 0x00001000)
        self.BKP = BitField(self, 0x00002000)
        self.AOE = BitField(self, 0x00004000)
        self.MOE = BitField(self, 0x00008000)
        self.BKF = BitField(self, 0x000F0000)
        self.BK2F = BitField(self, 0x00F00000)
        self.BK2E = BitField(self, 0x01000000)
        self.BK2P = BitField(self, 0x02000000)
        self.BKDSRM = BitField(self, 0x04000000)
        self.BK2DSRM = BitField(self, 0x08000000)
        self.BKBID = BitField(self, 0x10000000)
        self.BK2BID = BitField(self, 0x20000000)

class TIM_CCR5(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.CCR5 = BitField(self, 0xFFFFFFFF)
        self.GC5C1 = BitField(self, 0x20000000)
        self.GC5C2 = BitField(self, 0x40000000)
        self.GC5C3 = BitField(self, 0x80000000)

class TIM_CCR6(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.CCR6 = BitField(self, 0x0000FFFF)

class TIM_CCMR3(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.OC5FE = BitField(self, 0x00000004)
        self.OC5PE = BitField(self, 0x00000008)
        self.OC5M = BitField(self, 0x00010070)
        self.OC5CE = BitField(self, 0x00000080)
        self.OC6FE = BitField(self, 0x00000400)
        self.OC6PE = BitField(self, 0x00000800)
        self.OC6M = BitField(self, 0x01007000)
        self.OC6CE = BitField(self, 0x00008000)

class TIM_DTR2(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.DTGF = BitField(self, 0x000000FF)
        self.DTAE = BitField(self, 0x00010000)
        self.DTPE = BitField(self, 0x00020000)

class TIM_ECR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.IE = BitField(self, 0x00000001)
        self.IDIR = BitField(self, 0x00000006)
        self.FIDX = BitField(self, 0x00000020)
        self.IPOS = BitField(self, 0x000000C0)
        self.PW = BitField(self, 0x00FF0000)
        self.PWPRSC = BitField(self, 0x07000000)

class TIM_TISEL(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.TI1SEL = BitField(self, 0x0000000F)
        self.TI2SEL = BitField(self, 0x00000F00)
        self.TI3SEL = BitField(self, 0x000F0000)
        self.TI4SEL = BitField(self, 0x0F000000)

class TIM_AF1(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.BKINE = BitField(self, 0x00000001)
        self.BKCMP1E = BitField(self, 0x00000002)
        self.BKCMP2E = BitField(self, 0x00000004)
        self.BKCMP3E = BitField(self, 0x00000008)
        self.BKCMP4E = BitField(self, 0x00000010)
        self.BKCMP5E = BitField(self, 0x00000020)
        self.BKCMP6E = BitField(self, 0x00000040)
        self.BKCMP7E = BitField(self, 0x00000080)
        self.BKINP = BitField(self, 0x00000200)
        self.BKCMP1P = BitField(self, 0x00000400)
        self.BKCMP2P = BitField(self, 0x00000800)
        self.BKCMP3P = BitField(self, 0x00001000)
        self.BKCMP4P = BitField(self, 0x00002000)
        self.ETRSEL = BitField(self, 0x0003C000)

class TIM_AF2(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.BK2INE = BitField(self, 0x00000001)
        self.BK2CMP1E = BitField(self, 0x00000002)
        self.BK2CMP2E = BitField(self, 0x00000004)
        self.BK2CMP3E = BitField(self, 0x00000008)
        self.BK2CMP4E = BitField(self, 0x00000010)
        self.BK2CMP5E = BitField(self, 0x00000020)
        self.BK2CMP6E = BitField(self, 0x00000040)
        self.BK2CMP7E = BitField(self, 0x00000080)
        self.BK2INP = BitField(self, 0x00000200)
        self.BK2CMP1P = BitField(self, 0x00000400)
        self.BK2CMP2P = BitField(self, 0x00000800)
        self.BK2CMP3P = BitField(self, 0x00001000)
        self.BK2CMP4P = BitField(self, 0x00002000)
        self.OCRSEL = BitField(self, 0x00070000)

class TIM_OR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.HSE32EN = BitField(self, 0x00000001)

class TIM_DCR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.DBA = BitField(self, 0x0000001F)
        self.DBL = BitField(self, 0x00001F00)

class TIM_DMAR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.DMAB = BitField(self, 0xFFFFFFFF)

class TIM_TypeDef(PeripheralBase):

    def __init__(self, base):
        super().__init__(base)
        self.CR1 = TIM_CR1(base + 0x0)
        self.CR2 = TIM_CR2(base + 0x4)
        self.SMCR = TIM_SMCR(base + 0x8)
        self.DIER = TIM_DIER(base + 0xC)
        self.SR = TIM_SR(base + 0x10)
        self.EGR = TIM_EGR(base + 0x14)
        self.CCMR1 = TIM_CCMR1(base + 0x18)
        self.CCMR2 = TIM_CCMR2(base + 0x1C)
        self.CCER = TIM_CCER(base + 0x20)
        self.CNT = TIM_CNT(base + 0x24)
        self.PSC = TIM_PSC(base + 0x28)
        self.ARR = TIM_ARR(base + 0x2C)
        self.RCR = TIM_RCR(base + 0x30)
        self.CCR1 = TIM_CCR1(base + 0x34)
        self.CCR2 = TIM_CCR2(base + 0x38)
        self.CCR3 = TIM_CCR3(base + 0x3C)
        self.CCR4 = TIM_CCR4(base + 0x40)
        self.BDTR = TIM_BDTR(base + 0x44)
        self.CCR5 = TIM_CCR5(base + 0x48)
        self.CCR6 = TIM_CCR6(base + 0x4C)
        self.CCMR3 = TIM_CCMR3(base + 0x50)
        self.DTR2 = TIM_DTR2(base + 0x54)
        self.ECR = TIM_ECR(base + 0x58)
        self.TISEL = TIM_TISEL(base + 0x5C)
        self.AF1 = TIM_AF1(base + 0x60)
        self.AF2 = TIM_AF2(base + 0x64)
        self.OR = TIM_OR(base + 0x68)
        self.DCR = TIM_DCR(base + 0x3DC)
        self.DMAR = TIM_DMAR(base + 0x3E0)

TIM2 = TIM_TypeDef(0x40000000)
TIM3 = TIM_TypeDef(0x40000400)
TIM4 = TIM_TypeDef(0x40000800)
TIM5 = TIM_TypeDef(0x40000C00)
TIM6 = TIM_TypeDef(0x40001000)
TIM7 = TIM_TypeDef(0x40001400)
TIM1 = TIM_TypeDef(0x40012C00)
TIM8 = TIM_TypeDef(0x40013400)
TIM15 = TIM_TypeDef(0x40014000)
TIM16 = TIM_TypeDef(0x40014400)
TIM17 = TIM_TypeDef(0x40014800)
TIM20 = TIM_TypeDef(0x40015000)

class USART_CR1(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.UE = BitField(self, 0x00000001)
        self.UESM = BitField(self, 0x00000002)
        self.RE = BitField(self, 0x00000004)
        self.TE = BitField(self, 0x00000008)
        self.IDLEIE = BitField(self, 0x00000010)
        self.RXNEIE = BitField(self, 0x00000020)
        self.RXNEIE_RXFNEIE = BitField(self, 0x00000020)
        self.TCIE = BitField(self, 0x00000040)
        self.TXEIE = BitField(self, 0x00000080)
        self.TXEIE_TXFNFIE = BitField(self, 0x00000080)
        self.PEIE = BitField(self, 0x00000100)
        self.PS = BitField(self, 0x00000200)
        self.PCE = BitField(self, 0x00000400)
        self.WAKE = BitField(self, 0x00000800)
        self.M = BitField(self, 0x10001000)
        self.M0 = BitField(self, 0x00001000)
        self.MME = BitField(self, 0x00002000)
        self.CMIE = BitField(self, 0x00004000)
        self.OVER8 = BitField(self, 0x00008000)
        self.DEDT = BitField(self, 0x001F0000)
        self.DEAT = BitField(self, 0x03E00000)
        self.RTOIE = BitField(self, 0x04000000)
        self.EOBIE = BitField(self, 0x08000000)
        self.M1 = BitField(self, 0x10000000)
        self.FIFOEN = BitField(self, 0x20000000)
        self.TXFEIE = BitField(self, 0x40000000)
        self.RXFFIE = BitField(self, 0x80000000)

class USART_CR2(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.SLVEN = BitField(self, 0x00000001)
        self.DIS_NSS = BitField(self, 0x00000008)
        self.ADDM7 = BitField(self, 0x00000010)
        self.LBDL = BitField(self, 0x00000020)
        self.LBDIE = BitField(self, 0x00000040)
        self.LBCL = BitField(self, 0x00000100)
        self.CPHA = BitField(self, 0x00000200)
        self.CPOL = BitField(self, 0x00000400)
        self.CLKEN = BitField(self, 0x00000800)
        self.STOP = BitField(self, 0x00003000)
        self.LINEN = BitField(self, 0x00004000)
        self.SWAP = BitField(self, 0x00008000)
        self.RXINV = BitField(self, 0x00010000)
        self.TXINV = BitField(self, 0x00020000)
        self.DATAINV = BitField(self, 0x00040000)
        self.MSBFIRST = BitField(self, 0x00080000)
        self.ABREN = BitField(self, 0x00100000)
        self.ABRMODE = BitField(self, 0x00600000)
        self.RTOEN = BitField(self, 0x00800000)
        self.ADD = BitField(self, 0xFF000000)

class USART_CR3(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.EIE = BitField(self, 0x00000001)
        self.IREN = BitField(self, 0x00000002)
        self.IRLP = BitField(self, 0x00000004)
        self.HDSEL = BitField(self, 0x00000008)
        self.NACK = BitField(self, 0x00000010)
        self.SCEN = BitField(self, 0x00000020)
        self.DMAR = BitField(self, 0x00000040)
        self.DMAT = BitField(self, 0x00000080)
        self.RTSE = BitField(self, 0x00000100)
        self.CTSE = BitField(self, 0x00000200)
        self.CTSIE = BitField(self, 0x00000400)
        self.ONEBIT = BitField(self, 0x00000800)
        self.OVRDIS = BitField(self, 0x00001000)
        self.DDRE = BitField(self, 0x00002000)
        self.DEM = BitField(self, 0x00004000)
        self.DEP = BitField(self, 0x00008000)
        self.SCARCNT = BitField(self, 0x000E0000)
        self.WUS = BitField(self, 0x00300000)
        self.WUFIE = BitField(self, 0x00400000)
        self.TXFTIE = BitField(self, 0x00800000)
        self.TCBGTIE = BitField(self, 0x01000000)
        self.RXFTCFG = BitField(self, 0x0E000000)
        self.RXFTIE = BitField(self, 0x10000000)
        self.TXFTCFG = BitField(self, 0xE0000000)

class USART_BRR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.LPUART = BitField(self, 0x000FFFFF)
        self.BRR = BitField(self, 0x0000FFFF)

class USART_GTPR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.PSC = BitField(self, 0x000000FF)
        self.GT = BitField(self, 0x0000FF00)

class USART_RTOR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.RTO = BitField(self, 0x00FFFFFF)
        self.BLEN = BitField(self, 0xFF000000)

class USART_RQR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.ABRRQ = BitField(self, 0x00000001)
        self.SBKRQ = BitField(self, 0x00000002)
        self.MMRQ = BitField(self, 0x00000004)
        self.RXFRQ = BitField(self, 0x00000008)
        self.TXFRQ = BitField(self, 0x00000010)

class USART_ISR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.PE = BitField(self, 0x00000001)
        self.FE = BitField(self, 0x00000002)
        self.NE = BitField(self, 0x00000004)
        self.ORE = BitField(self, 0x00000008)
        self.IDLE = BitField(self, 0x00000010)
        self.RXNE = BitField(self, 0x00000020)
        self.RXNE_RXFNE = BitField(self, 0x00000020)
        self.TC = BitField(self, 0x00000040)
        self.TXE = BitField(self, 0x00000080)
        self.TXE_TXFNF = BitField(self, 0x00000080)
        self.LBDF = BitField(self, 0x00000100)
        self.CTSIF = BitField(self, 0x00000200)
        self.CTS = BitField(self, 0x00000400)
        self.RTOF = BitField(self, 0x00000800)
        self.EOBF = BitField(self, 0x00001000)
        self.UDR = BitField(self, 0x00002000)
        self.ABRE = BitField(self, 0x00004000)
        self.ABRF = BitField(self, 0x00008000)
        self.BUSY = BitField(self, 0x00010000)
        self.CMF = BitField(self, 0x00020000)
        self.SBKF = BitField(self, 0x00040000)
        self.RWU = BitField(self, 0x00080000)
        self.WUF = BitField(self, 0x00100000)
        self.TEACK = BitField(self, 0x00200000)
        self.REACK = BitField(self, 0x00400000)
        self.TXFE = BitField(self, 0x00800000)
        self.RXFF = BitField(self, 0x01000000)
        self.TCBGT = BitField(self, 0x02000000)
        self.RXFT = BitField(self, 0x04000000)
        self.TXFT = BitField(self, 0x08000000)

class USART_ICR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.PECF = BitField(self, 0x00000001)
        self.FECF = BitField(self, 0x00000002)
        self.NECF = BitField(self, 0x00000004)
        self.ORECF = BitField(self, 0x00000008)
        self.IDLECF = BitField(self, 0x00000010)
        self.TXFECF = BitField(self, 0x00000020)
        self.TCCF = BitField(self, 0x00000040)
        self.TCBGTCF = BitField(self, 0x00000080)
        self.LBDCF = BitField(self, 0x00000100)
        self.CTSCF = BitField(self, 0x00000200)
        self.RTOCF = BitField(self, 0x00000800)
        self.EOBCF = BitField(self, 0x00001000)
        self.UDRCF = BitField(self, 0x00002000)
        self.CMCF = BitField(self, 0x00020000)
        self.WUCF = BitField(self, 0x00100000)

class USART_RDR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.RDR = BitField(self, 0x000001FF)

class USART_TDR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.TDR = BitField(self, 0x000001FF)

class USART_PRESC(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.PRESCALER = BitField(self, 0x0000000F)

class USART_TypeDef(PeripheralBase):

    def __init__(self, base):
        super().__init__(base)
        self.CR1 = USART_CR1(base + 0x0)
        self.CR2 = USART_CR2(base + 0x4)
        self.CR3 = USART_CR3(base + 0x8)
        self.BRR = USART_BRR(base + 0xC)
        self.GTPR = USART_GTPR(base + 0x10)
        self.RTOR = USART_RTOR(base + 0x14)
        self.RQR = USART_RQR(base + 0x18)
        self.ISR = USART_ISR(base + 0x1C)
        self.ICR = USART_ICR(base + 0x20)
        self.RDR = USART_RDR(base + 0x24)
        self.TDR = USART_TDR(base + 0x28)
        self.PRESC = USART_PRESC(base + 0x2C)

USART2 = USART_TypeDef(0x40004400)
USART3 = USART_TypeDef(0x40004800)
UART4 = USART_TypeDef(0x40004C00)
UART5 = USART_TypeDef(0x40005000)
LPUART1 = USART_TypeDef(0x40008000)
USART1 = USART_TypeDef(0x40013800)

class USB_EP0R(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)

class USB_EP1R(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)

class USB_EP2R(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)

class USB_EP3R(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)

class USB_EP4R(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)

class USB_EP5R(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)

class USB_EP6R(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)

class USB_EP7R(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)

class USB_CNTR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)

class USB_ISTR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)

class USB_FNR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)

class USB_DADDR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)

class USB_BTABLE(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)

class USB_LPMCSR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)

class USB_BCDR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)

class USB_TypeDef(PeripheralBase):

    def __init__(self, base):
        super().__init__(base)
        self.EP0R = USB_EP0R(base + 0x0)
        self.EP1R = USB_EP1R(base + 0x4)
        self.EP2R = USB_EP2R(base + 0x8)
        self.EP3R = USB_EP3R(base + 0xC)
        self.EP4R = USB_EP4R(base + 0x10)
        self.EP5R = USB_EP5R(base + 0x14)
        self.EP6R = USB_EP6R(base + 0x18)
        self.EP7R = USB_EP7R(base + 0x1C)
        self.CNTR = USB_CNTR(base + 0x40)
        self.ISTR = USB_ISTR(base + 0x44)
        self.FNR = USB_FNR(base + 0x48)
        self.DADDR = USB_DADDR(base + 0x4C)
        self.BTABLE = USB_BTABLE(base + 0x50)
        self.LPMCSR = USB_LPMCSR(base + 0x54)
        self.BCDR = USB_BCDR(base + 0x58)

USB = USB_TypeDef(0x40005C00)

class VREFBUF_CSR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.ENVR = BitField(self, 0x00000001)
        self.HIZ = BitField(self, 0x00000002)
        self.VRR = BitField(self, 0x00000008)
        self.VRS = BitField(self, 0x00000030)

class VREFBUF_CCR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.TRIM = BitField(self, 0x0000003F)

class VREFBUF_TypeDef(PeripheralBase):

    def __init__(self, base):
        super().__init__(base)
        self.CSR = VREFBUF_CSR(base + 0x0)
        self.CCR = VREFBUF_CCR(base + 0x4)

VREFBUF = VREFBUF_TypeDef(0x40010030)

class WWDG_CR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.T = BitField(self, 0x0000007F)
        self.WDGA = BitField(self, 0x00000080)

class WWDG_CFR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.W = BitField(self, 0x0000007F)
        self.WDGTB = BitField(self, 0x00003800)
        self.EWI = BitField(self, 0x00000200)

class WWDG_SR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.EWIF = BitField(self, 0x00000001)

class WWDG_TypeDef(PeripheralBase):

    def __init__(self, base):
        super().__init__(base)
        self.CR = WWDG_CR(base + 0x0)
        self.CFR = WWDG_CFR(base + 0x4)
        self.SR = WWDG_SR(base + 0x8)

WWDG = WWDG_TypeDef(0x40002C00)

class RNG_CR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.RNGEN = BitField(self, 0x00000004)
        self.IE = BitField(self, 0x00000008)
        self.CED = BitField(self, 0x00000020)

class RNG_SR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.DRDY = BitField(self, 0x00000001)
        self.CECS = BitField(self, 0x00000002)
        self.SECS = BitField(self, 0x00000004)
        self.CEIS = BitField(self, 0x00000020)
        self.SEIS = BitField(self, 0x00000040)

class RNG_DR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)

class RNG_TypeDef(PeripheralBase):

    def __init__(self, base):
        super().__init__(base)
        self.CR = RNG_CR(base + 0x0)
        self.SR = RNG_SR(base + 0x4)
        self.DR = RNG_DR(base + 0x8)

RNG = RNG_TypeDef(0x50060800)

class CORDIC_CSR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.FUNC = BitField(self, 0x0000000F)
        self.PRECISION = BitField(self, 0x000000F0)
        self.SCALE = BitField(self, 0x00000700)
        self.IEN = BitField(self, 0x00010000)
        self.DMAREN = BitField(self, 0x00020000)
        self.DMAWEN = BitField(self, 0x00040000)
        self.NRES = BitField(self, 0x00080000)
        self.NARGS = BitField(self, 0x00100000)
        self.RESSIZE = BitField(self, 0x00200000)
        self.ARGSIZE = BitField(self, 0x00400000)
        self.RRDY = BitField(self, 0x80000000)

class CORDIC_WDATA(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.ARG = BitField(self, 0xFFFFFFFF)

class CORDIC_RDATA(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.RES = BitField(self, 0xFFFFFFFF)

class CORDIC_TypeDef(PeripheralBase):

    def __init__(self, base):
        super().__init__(base)
        self.CSR = CORDIC_CSR(base + 0x0)
        self.WDATA = CORDIC_WDATA(base + 0x4)
        self.RDATA = CORDIC_RDATA(base + 0x8)

CORDIC = CORDIC_TypeDef(0x40020C00)

class UCPD_CFG1(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.HBITCLKDIV = BitField(self, 0x0000003F)
        self.IFRGAP = BitField(self, 0x000007C0)
        self.TRANSWIN = BitField(self, 0x0000F800)
        self.PSC_UCPDCLK = BitField(self, 0x000E0000)
        self.RXORDSETEN = BitField(self, 0x1FF00000)
        self.TXDMAEN = BitField(self, 0x20000000)
        self.RXDMAEN = BitField(self, 0x40000000)
        self.UCPDEN = BitField(self, 0x80000000)

class UCPD_CFG2(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.RXFILTDIS = BitField(self, 0x00000001)
        self.RXFILT2N3 = BitField(self, 0x00000002)
        self.FORCECLK = BitField(self, 0x00000004)
        self.WUPEN = BitField(self, 0x00000008)

class UCPD_CR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.TXMODE = BitField(self, 0x00000003)
        self.TXSEND = BitField(self, 0x00000004)
        self.TXHRST = BitField(self, 0x00000008)
        self.RXMODE = BitField(self, 0x00000010)
        self.PHYRXEN = BitField(self, 0x00000020)
        self.PHYCCSEL = BitField(self, 0x00000040)
        self.ANASUBMODE = BitField(self, 0x00000180)
        self.ANAMODE = BitField(self, 0x00000200)
        self.CCENABLE = BitField(self, 0x00000C00)
        self.FRSRXEN = BitField(self, 0x00010000)
        self.FRSTX = BitField(self, 0x00020000)
        self.RDCH = BitField(self, 0x00040000)
        self.CC1TCDIS = BitField(self, 0x00100000)
        self.CC2TCDIS = BitField(self, 0x00200000)

class UCPD_IMR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.TXISIE = BitField(self, 0x00000001)
        self.TXMSGDISCIE = BitField(self, 0x00000002)
        self.TXMSGSENTIE = BitField(self, 0x00000004)
        self.TXMSGABTIE = BitField(self, 0x00000008)
        self.HRSTDISCIE = BitField(self, 0x00000010)
        self.HRSTSENTIE = BitField(self, 0x00000020)
        self.TXUNDIE = BitField(self, 0x00000040)
        self.RXNEIE = BitField(self, 0x00000100)
        self.RXORDDETIE = BitField(self, 0x00000200)
        self.RXHRSTDETIE = BitField(self, 0x00000400)
        self.RXOVRIE = BitField(self, 0x00000800)
        self.RXMSGENDIE = BitField(self, 0x00001000)
        self.TYPECEVT1IE = BitField(self, 0x00004000)
        self.TYPECEVT2IE = BitField(self, 0x00008000)
        self.FRSEVTIE = BitField(self, 0x00100000)

class UCPD_SR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.TXIS = BitField(self, 0x00000001)
        self.TXMSGDISC = BitField(self, 0x00000002)
        self.TXMSGSENT = BitField(self, 0x00000004)
        self.TXMSGABT = BitField(self, 0x00000008)
        self.HRSTDISC = BitField(self, 0x00000010)
        self.HRSTSENT = BitField(self, 0x00000020)
        self.TXUND = BitField(self, 0x00000040)
        self.RXNE = BitField(self, 0x00000100)
        self.RXORDDET = BitField(self, 0x00000200)
        self.RXHRSTDET = BitField(self, 0x00000400)
        self.RXOVR = BitField(self, 0x00000800)
        self.RXMSGEND = BitField(self, 0x00001000)
        self.RXERR = BitField(self, 0x00002000)
        self.TYPECEVT1 = BitField(self, 0x00004000)
        self.TYPECEVT2 = BitField(self, 0x00008000)
        self.TYPEC_VSTATE_CC1 = BitField(self, 0x00030000)
        self.TYPEC_VSTATE_CC2 = BitField(self, 0x000C0000)
        self.FRSEVT = BitField(self, 0x00100000)

class UCPD_ICR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.TXMSGDISCCF = BitField(self, 0x00000002)
        self.TXMSGSENTCF = BitField(self, 0x00000004)
        self.TXMSGABTCF = BitField(self, 0x00000008)
        self.HRSTDISCCF = BitField(self, 0x00000010)
        self.HRSTSENTCF = BitField(self, 0x00000020)
        self.TXUNDCF = BitField(self, 0x00000040)
        self.RXORDDETCF = BitField(self, 0x00000200)
        self.RXHRSTDETCF = BitField(self, 0x00000400)
        self.RXOVRCF = BitField(self, 0x00000800)
        self.RXMSGENDCF = BitField(self, 0x00001000)
        self.TYPECEVT1CF = BitField(self, 0x00004000)
        self.TYPECEVT2CF = BitField(self, 0x00008000)
        self.FRSEVTCF = BitField(self, 0x00100000)

class UCPD_TX_ORDSET(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)

class UCPD_TX_PAYSZ(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)

class UCPD_TXDR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.TXDATA = BitField(self, 0x000000FF)

class UCPD_RX_ORDSET(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)

class UCPD_RX_PAYSZ(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)

class UCPD_RXDR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.RXDATA = BitField(self, 0x000000FF)

class UCPD_RX_ORDEXT1(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)

class UCPD_RX_ORDEXT2(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)

class UCPD_TypeDef(PeripheralBase):

    def __init__(self, base):
        super().__init__(base)
        self.CFG1 = UCPD_CFG1(base + 0x0)
        self.CFG2 = UCPD_CFG2(base + 0x4)
        self.CR = UCPD_CR(base + 0xC)
        self.IMR = UCPD_IMR(base + 0x10)
        self.SR = UCPD_SR(base + 0x14)
        self.ICR = UCPD_ICR(base + 0x18)
        self.TX_ORDSET = UCPD_TX_ORDSET(base + 0x1C)
        self.TX_PAYSZ = UCPD_TX_PAYSZ(base + 0x20)
        self.TXDR = UCPD_TXDR(base + 0x24)
        self.RX_ORDSET = UCPD_RX_ORDSET(base + 0x28)
        self.RX_PAYSZ = UCPD_RX_PAYSZ(base + 0x2C)
        self.RXDR = UCPD_RXDR(base + 0x30)
        self.RX_ORDEXT1 = UCPD_RX_ORDEXT1(base + 0x34)
        self.RX_ORDEXT2 = UCPD_RX_ORDEXT2(base + 0x38)

UCPD1 = UCPD_TypeDef(0x4000A000)

class HRTIM_Master_MCR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.CK_PSC = BitField(self, 0x00000007)
        self.CONT = BitField(self, 0x00000008)
        self.RETRIG = BitField(self, 0x00000010)
        self.HALF = BitField(self, 0x00000020)
        self.INTLVD = BitField(self, 0x000000C0)
        self.SYNC_IN = BitField(self, 0x00000300)
        self.SYNCRSTM = BitField(self, 0x00000400)
        self.SYNCSTRTM = BitField(self, 0x00000800)
        self.SYNC_OUT = BitField(self, 0x00003000)
        self.SYNC_SRC = BitField(self, 0x0000C000)
        self.MCEN = BitField(self, 0x00010000)
        self.TACEN = BitField(self, 0x00020000)
        self.TBCEN = BitField(self, 0x00040000)
        self.TCCEN = BitField(self, 0x00080000)
        self.TDCEN = BitField(self, 0x00100000)
        self.TECEN = BitField(self, 0x00200000)
        self.TFCEN = BitField(self, 0x00400000)
        self.DACSYNC = BitField(self, 0x06000000)
        self.PREEN = BitField(self, 0x08000000)
        self.MREPU = BitField(self, 0x20000000)
        self.BRSTDMA = BitField(self, 0xC0000000)

class HRTIM_Master_MISR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.MCMP1 = BitField(self, 0x00000001)
        self.MCMP2 = BitField(self, 0x00000002)
        self.MCMP3 = BitField(self, 0x00000004)
        self.MCMP4 = BitField(self, 0x00000008)
        self.MREP = BitField(self, 0x00000010)
        self.SYNC = BitField(self, 0x00000020)
        self.MUPD = BitField(self, 0x00000040)

class HRTIM_Master_MICR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.MCMP1 = BitField(self, 0x00000001)
        self.MCMP2 = BitField(self, 0x00000002)
        self.MCMP3 = BitField(self, 0x00000004)
        self.MCMP4 = BitField(self, 0x00000008)
        self.MREP = BitField(self, 0x00000010)
        self.SYNC = BitField(self, 0x00000020)
        self.MUPD = BitField(self, 0x00000040)

class HRTIM_Master_MDIER(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.MCMP1IE = BitField(self, 0x00000001)
        self.MCMP2IE = BitField(self, 0x00000002)
        self.MCMP3IE = BitField(self, 0x00000004)
        self.MCMP4IE = BitField(self, 0x00000008)
        self.MREPIE = BitField(self, 0x00000010)
        self.SYNCIE = BitField(self, 0x00000020)
        self.MUPDIE = BitField(self, 0x00000040)
        self.MCMP1DE = BitField(self, 0x00010000)
        self.MCMP2DE = BitField(self, 0x00020000)
        self.MCMP3DE = BitField(self, 0x00040000)
        self.MCMP4DE = BitField(self, 0x00080000)
        self.MREPDE = BitField(self, 0x00100000)
        self.SYNCDE = BitField(self, 0x00200000)
        self.MUPDDE = BitField(self, 0x00400000)

class HRTIM_Master_MCNTR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.MCNTR = BitField(self, 0x0000FFFF)

class HRTIM_Master_MPER(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.MPER = BitField(self, 0x0000FFFF)

class HRTIM_Master_MREP(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.MREP = BitField(self, 0x000000FF)

class HRTIM_Master_MCMP1R(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.MCMP1R = BitField(self, 0x0000FFFF)

class HRTIM_Master_MCMP2R(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.MCMP2R = BitField(self, 0x0000FFFF)

class HRTIM_Master_MCMP3R(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.MCMP3R = BitField(self, 0x0000FFFF)

class HRTIM_Master_MCMP4R(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.MCMP4R = BitField(self, 0x0000FFFF)

class HRTIM_Master_TypeDef(PeripheralBase):

    def __init__(self, base):
        super().__init__(base)
        self.MCR = HRTIM_Master_MCR(base + 0x0)
        self.MISR = HRTIM_Master_MISR(base + 0x4)
        self.MICR = HRTIM_Master_MICR(base + 0x8)
        self.MDIER = HRTIM_Master_MDIER(base + 0xC)
        self.MCNTR = HRTIM_Master_MCNTR(base + 0x10)
        self.MPER = HRTIM_Master_MPER(base + 0x14)
        self.MREP = HRTIM_Master_MREP(base + 0x18)
        self.MCMP1R = HRTIM_Master_MCMP1R(base + 0x1C)
        self.MCMP2R = HRTIM_Master_MCMP2R(base + 0x24)
        self.MCMP3R = HRTIM_Master_MCMP3R(base + 0x28)
        self.MCMP4R = HRTIM_Master_MCMP4R(base + 0x2C)


class HRTIM_Timerx_TIMxCR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.CK_PSC = BitField(self, 0x00000007)
        self.CONT = BitField(self, 0x00000008)
        self.RETRIG = BitField(self, 0x00000010)
        self.HALF = BitField(self, 0x00000020)
        self.PSHPLL = BitField(self, 0x00000040)
        self.INTLVD = BitField(self, 0x00000180)
        self.RSYNCU = BitField(self, 0x00000200)
        self.SYNCRST = BitField(self, 0x00000400)
        self.SYNCSTRT = BitField(self, 0x00000800)
        self.DELCMP2 = BitField(self, 0x00003000)
        self.DELCMP4 = BitField(self, 0x0000C000)
        self.TFU = BitField(self, 0x00010000)
        self.TREPU = BitField(self, 0x00020000)
        self.TRSTU = BitField(self, 0x00040000)
        self.TAU = BitField(self, 0x00080000)
        self.TBU = BitField(self, 0x00100000)
        self.TCU = BitField(self, 0x00200000)
        self.TDU = BitField(self, 0x00400000)
        self.TEU = BitField(self, 0x00800000)
        self.MSTU = BitField(self, 0x01000000)
        self.DACSYNC = BitField(self, 0x06000000)
        self.PREEN = BitField(self, 0x08000000)
        self.UPDGAT = BitField(self, 0xF0000000)

class HRTIM_Timerx_TIMxISR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.CMP1 = BitField(self, 0x00000001)
        self.CMP2 = BitField(self, 0x00000002)
        self.CMP3 = BitField(self, 0x00000004)
        self.CMP4 = BitField(self, 0x00000008)
        self.REP = BitField(self, 0x00000010)
        self.UPD = BitField(self, 0x00000040)
        self.CPT1 = BitField(self, 0x00000080)
        self.CPT2 = BitField(self, 0x00000100)
        self.SET1 = BitField(self, 0x00000200)
        self.RST1 = BitField(self, 0x00000400)
        self.SET2 = BitField(self, 0x00000800)
        self.RST2 = BitField(self, 0x00001000)
        self.RST = BitField(self, 0x00002000)
        self.DLYPRT = BitField(self, 0x00004000)
        self.CPPSTAT = BitField(self, 0x00010000)
        self.IPPSTAT = BitField(self, 0x00020000)
        self.O1STAT = BitField(self, 0x00040000)
        self.O2STAT = BitField(self, 0x00080000)
        self.O1CPY = BitField(self, 0x00100000)
        self.O2CPY = BitField(self, 0x00200000)

class HRTIM_Timerx_TIMxICR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.CMP1C = BitField(self, 0x00000001)
        self.CMP2C = BitField(self, 0x00000002)
        self.CMP3C = BitField(self, 0x00000004)
        self.CMP4C = BitField(self, 0x00000008)
        self.REPC = BitField(self, 0x00000010)
        self.UPDC = BitField(self, 0x00000040)
        self.CPT1C = BitField(self, 0x00000080)
        self.CPT2C = BitField(self, 0x00000100)
        self.SET1C = BitField(self, 0x00000200)
        self.RST1C = BitField(self, 0x00000400)
        self.SET2C = BitField(self, 0x00000800)
        self.RST2C = BitField(self, 0x00001000)
        self.RSTC = BitField(self, 0x00002000)
        self.DLYPRTC = BitField(self, 0x00004000)

class HRTIM_Timerx_TIMxDIER(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.CMP1IE = BitField(self, 0x00000001)
        self.CMP2IE = BitField(self, 0x00000002)
        self.CMP3IE = BitField(self, 0x00000004)
        self.CMP4IE = BitField(self, 0x00000008)
        self.REPIE = BitField(self, 0x00000010)
        self.UPDIE = BitField(self, 0x00000040)
        self.CPT1IE = BitField(self, 0x00000080)
        self.CPT2IE = BitField(self, 0x00000100)
        self.SET1IE = BitField(self, 0x00000200)
        self.RST1IE = BitField(self, 0x00000400)
        self.SET2IE = BitField(self, 0x00000800)
        self.RST2IE = BitField(self, 0x00001000)
        self.RSTIE = BitField(self, 0x00002000)
        self.DLYPRTIE = BitField(self, 0x00004000)
        self.CMP1DE = BitField(self, 0x00010000)
        self.CMP2DE = BitField(self, 0x00020000)
        self.CMP3DE = BitField(self, 0x00040000)
        self.CMP4DE = BitField(self, 0x00080000)
        self.REPDE = BitField(self, 0x00100000)
        self.UPDDE = BitField(self, 0x00400000)
        self.CPT1DE = BitField(self, 0x00800000)
        self.CPT2DE = BitField(self, 0x01000000)
        self.SET1DE = BitField(self, 0x02000000)
        self.RST1DE = BitField(self, 0x04000000)
        self.SET2DE = BitField(self, 0x08000000)
        self.RST2DE = BitField(self, 0x10000000)
        self.RSTDE = BitField(self, 0x20000000)
        self.DLYPRTDE = BitField(self, 0x40000000)

class HRTIM_Timerx_CNTxR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.CNTR = BitField(self, 0x0000FFFF)

class HRTIM_Timerx_PERxR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.PER = BitField(self, 0x0000FFFF)

class HRTIM_Timerx_REPxR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.REP = BitField(self, 0x000000FF)

class HRTIM_Timerx_CMP1xR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.CMP1R = BitField(self, 0x0000FFFF)

class HRTIM_Timerx_CMP1CxR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.CMP1CR = BitField(self, 0x0000FFFF)

class HRTIM_Timerx_CMP2xR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.CMP2R = BitField(self, 0x0000FFFF)

class HRTIM_Timerx_CMP3xR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.CMP3R = BitField(self, 0x0000FFFF)

class HRTIM_Timerx_CMP4xR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.CMP4R = BitField(self, 0x0000FFFF)

class HRTIM_Timerx_CPT1xR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.CPT1R = BitField(self, 0x0000FFFF)
        self.DIR = BitField(self, 0x00010000)

class HRTIM_Timerx_CPT2xR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.CPT2R = BitField(self, 0x0000FFFF)
        self.DIR = BitField(self, 0x00010000)

class HRTIM_Timerx_DTxR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.DTR = BitField(self, 0x000001FF)
        self.SDTR = BitField(self, 0x00000200)
        self.DTPRSC = BitField(self, 0x00001C00)
        self.DTRSLK = BitField(self, 0x00004000)
        self.DTRLK = BitField(self, 0x00008000)
        self.DTF = BitField(self, 0x01FF0000)
        self.SDTF = BitField(self, 0x02000000)
        self.DTFSLK = BitField(self, 0x40000000)
        self.DTFLK = BitField(self, 0x80000000)

class HRTIM_Timerx_SETx1R(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.SST = BitField(self, 0x00000001)
        self.RESYNC = BitField(self, 0x00000002)
        self.PER = BitField(self, 0x00000004)
        self.CMP1 = BitField(self, 0x00000008)
        self.CMP2 = BitField(self, 0x00000010)
        self.CMP3 = BitField(self, 0x00000020)
        self.CMP4 = BitField(self, 0x00000040)
        self.MSTPER = BitField(self, 0x00000080)
        self.MSTCMP1 = BitField(self, 0x00000100)
        self.MSTCMP2 = BitField(self, 0x00000200)
        self.MSTCMP3 = BitField(self, 0x00000400)
        self.MSTCMP4 = BitField(self, 0x00000800)
        self.TIMEVNT1 = BitField(self, 0x00001000)
        self.TIMEVNT2 = BitField(self, 0x00002000)
        self.TIMEVNT3 = BitField(self, 0x00004000)
        self.TIMEVNT4 = BitField(self, 0x00008000)
        self.TIMEVNT5 = BitField(self, 0x00010000)
        self.TIMEVNT6 = BitField(self, 0x00020000)
        self.TIMEVNT7 = BitField(self, 0x00040000)
        self.TIMEVNT8 = BitField(self, 0x00080000)
        self.TIMEVNT9 = BitField(self, 0x00100000)
        self.EXTVNT1 = BitField(self, 0x00200000)
        self.EXTVNT2 = BitField(self, 0x00400000)
        self.EXTVNT3 = BitField(self, 0x00800000)
        self.EXTVNT4 = BitField(self, 0x01000000)
        self.EXTVNT5 = BitField(self, 0x02000000)
        self.EXTVNT6 = BitField(self, 0x04000000)
        self.EXTVNT7 = BitField(self, 0x08000000)
        self.EXTVNT8 = BitField(self, 0x10000000)
        self.EXTVNT9 = BitField(self, 0x20000000)
        self.EXTVNT10 = BitField(self, 0x40000000)
        self.UPDATE = BitField(self, 0x80000000)

class HRTIM_Timerx_RSTx1R(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.SRT = BitField(self, 0x00000001)
        self.RESYNC = BitField(self, 0x00000002)
        self.PER = BitField(self, 0x00000004)
        self.CMP1 = BitField(self, 0x00000008)
        self.CMP2 = BitField(self, 0x00000010)
        self.CMP3 = BitField(self, 0x00000020)
        self.CMP4 = BitField(self, 0x00000040)
        self.MSTPER = BitField(self, 0x00000080)
        self.MSTCMP1 = BitField(self, 0x00000100)
        self.MSTCMP2 = BitField(self, 0x00000200)
        self.MSTCMP3 = BitField(self, 0x00000400)
        self.MSTCMP4 = BitField(self, 0x00000800)
        self.TIMEVNT1 = BitField(self, 0x00001000)
        self.TIMEVNT2 = BitField(self, 0x00002000)
        self.TIMEVNT3 = BitField(self, 0x00004000)
        self.TIMEVNT4 = BitField(self, 0x00008000)
        self.TIMEVNT5 = BitField(self, 0x00010000)
        self.TIMEVNT6 = BitField(self, 0x00020000)
        self.TIMEVNT7 = BitField(self, 0x00040000)
        self.TIMEVNT8 = BitField(self, 0x00080000)
        self.TIMEVNT9 = BitField(self, 0x00100000)
        self.EXTVNT1 = BitField(self, 0x00200000)
        self.EXTVNT2 = BitField(self, 0x00400000)
        self.EXTVNT3 = BitField(self, 0x00800000)
        self.EXTVNT4 = BitField(self, 0x01000000)
        self.EXTVNT5 = BitField(self, 0x02000000)
        self.EXTVNT6 = BitField(self, 0x04000000)
        self.EXTVNT7 = BitField(self, 0x08000000)
        self.EXTVNT8 = BitField(self, 0x10000000)
        self.EXTVNT9 = BitField(self, 0x20000000)
        self.EXTVNT10 = BitField(self, 0x40000000)
        self.UPDATE = BitField(self, 0x80000000)

class HRTIM_Timerx_SETx2R(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.SST = BitField(self, 0x00000001)
        self.RESYNC = BitField(self, 0x00000002)
        self.PER = BitField(self, 0x00000004)
        self.CMP1 = BitField(self, 0x00000008)
        self.CMP2 = BitField(self, 0x00000010)
        self.CMP3 = BitField(self, 0x00000020)
        self.CMP4 = BitField(self, 0x00000040)
        self.MSTPER = BitField(self, 0x00000080)
        self.MSTCMP1 = BitField(self, 0x00000100)
        self.MSTCMP2 = BitField(self, 0x00000200)
        self.MSTCMP3 = BitField(self, 0x00000400)
        self.MSTCMP4 = BitField(self, 0x00000800)
        self.TIMEVNT1 = BitField(self, 0x00001000)
        self.TIMEVNT2 = BitField(self, 0x00002000)
        self.TIMEVNT3 = BitField(self, 0x00004000)
        self.TIMEVNT4 = BitField(self, 0x00008000)
        self.TIMEVNT5 = BitField(self, 0x00010000)
        self.TIMEVNT6 = BitField(self, 0x00020000)
        self.TIMEVNT7 = BitField(self, 0x00040000)
        self.TIMEVNT8 = BitField(self, 0x00080000)
        self.TIMEVNT9 = BitField(self, 0x00100000)
        self.EXTVNT1 = BitField(self, 0x00200000)
        self.EXTVNT2 = BitField(self, 0x00400000)
        self.EXTVNT3 = BitField(self, 0x00800000)
        self.EXTVNT4 = BitField(self, 0x01000000)
        self.EXTVNT5 = BitField(self, 0x02000000)
        self.EXTVNT6 = BitField(self, 0x04000000)
        self.EXTVNT7 = BitField(self, 0x08000000)
        self.EXTVNT8 = BitField(self, 0x10000000)
        self.EXTVNT9 = BitField(self, 0x20000000)
        self.EXTVNT10 = BitField(self, 0x40000000)
        self.UPDATE = BitField(self, 0x80000000)

class HRTIM_Timerx_RSTx2R(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.SRT = BitField(self, 0x00000001)
        self.RESYNC = BitField(self, 0x00000002)
        self.PER = BitField(self, 0x00000004)
        self.CMP1 = BitField(self, 0x00000008)
        self.CMP2 = BitField(self, 0x00000010)
        self.CMP3 = BitField(self, 0x00000020)
        self.CMP4 = BitField(self, 0x00000040)
        self.MSTPER = BitField(self, 0x00000080)
        self.MSTCMP1 = BitField(self, 0x00000100)
        self.MSTCMP2 = BitField(self, 0x00000200)
        self.MSTCMP3 = BitField(self, 0x00000400)
        self.MSTCMP4 = BitField(self, 0x00000800)
        self.TIMEVNT1 = BitField(self, 0x00001000)
        self.TIMEVNT2 = BitField(self, 0x00002000)
        self.TIMEVNT3 = BitField(self, 0x00004000)
        self.TIMEVNT4 = BitField(self, 0x00008000)
        self.TIMEVNT5 = BitField(self, 0x00010000)
        self.TIMEVNT6 = BitField(self, 0x00020000)
        self.TIMEVNT7 = BitField(self, 0x00040000)
        self.TIMEVNT8 = BitField(self, 0x00080000)
        self.TIMEVNT9 = BitField(self, 0x00100000)
        self.EXTVNT1 = BitField(self, 0x00200000)
        self.EXTVNT2 = BitField(self, 0x00400000)
        self.EXTVNT3 = BitField(self, 0x00800000)
        self.EXTVNT4 = BitField(self, 0x01000000)
        self.EXTVNT5 = BitField(self, 0x02000000)
        self.EXTVNT6 = BitField(self, 0x04000000)
        self.EXTVNT7 = BitField(self, 0x08000000)
        self.EXTVNT8 = BitField(self, 0x10000000)
        self.EXTVNT9 = BitField(self, 0x20000000)
        self.EXTVNT10 = BitField(self, 0x40000000)
        self.UPDATE = BitField(self, 0x80000000)

class HRTIM_Timerx_EEFxR1(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.EE1LTCH = BitField(self, 0x00000001)
        self.EE1FLTR = BitField(self, 0x0000001E)
        self.EE2LTCH = BitField(self, 0x00000040)
        self.EE2FLTR = BitField(self, 0x00000780)
        self.EE3LTCH = BitField(self, 0x00001000)
        self.EE3FLTR = BitField(self, 0x0001E000)
        self.EE4LTCH = BitField(self, 0x00040000)
        self.EE4FLTR = BitField(self, 0x00780000)
        self.EE5LTCH = BitField(self, 0x01000000)
        self.EE5FLTR = BitField(self, 0x1E000000)

class HRTIM_Timerx_EEFxR2(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.EE6LTCH = BitField(self, 0x00000001)
        self.EE6FLTR = BitField(self, 0x0000001E)
        self.EE7LTCH = BitField(self, 0x00000040)
        self.EE7FLTR = BitField(self, 0x00000780)
        self.EE8LTCH = BitField(self, 0x00001000)
        self.EE8FLTR = BitField(self, 0x0001E000)
        self.EE9LTCH = BitField(self, 0x00040000)
        self.EE9FLTR = BitField(self, 0x00780000)
        self.EE10LTCH = BitField(self, 0x01000000)
        self.EE10FLTR = BitField(self, 0x1E000000)

class HRTIM_Timerx_RSTxR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.TIMFCMP1 = BitField(self, 0x00000001)
        self.UPDATE = BitField(self, 0x00000002)
        self.CMP2 = BitField(self, 0x00000004)
        self.CMP4 = BitField(self, 0x00000008)
        self.MSTPER = BitField(self, 0x00000010)
        self.MSTCMP1 = BitField(self, 0x00000020)
        self.MSTCMP2 = BitField(self, 0x00000040)
        self.MSTCMP3 = BitField(self, 0x00000080)
        self.MSTCMP4 = BitField(self, 0x00000100)
        self.EXTEVNT1 = BitField(self, 0x00000200)
        self.EXTEVNT2 = BitField(self, 0x00000400)
        self.EXTEVNT3 = BitField(self, 0x00000800)
        self.EXTEVNT4 = BitField(self, 0x00001000)
        self.EXTEVNT5 = BitField(self, 0x00002000)
        self.EXTEVNT6 = BitField(self, 0x00004000)
        self.EXTEVNT7 = BitField(self, 0x00008000)
        self.EXTEVNT8 = BitField(self, 0x00010000)
        self.EXTEVNT9 = BitField(self, 0x00020000)
        self.EXTEVNT10 = BitField(self, 0x00040000)
        self.TIMBCMP1 = BitField(self, 0x00080000)
        self.TIMBCMP2 = BitField(self, 0x00100000)
        self.TIMBCMP4 = BitField(self, 0x00200000)
        self.TIMCCMP1 = BitField(self, 0x00400000)
        self.TIMCCMP2 = BitField(self, 0x00800000)
        self.TIMCCMP4 = BitField(self, 0x01000000)
        self.TIMDCMP1 = BitField(self, 0x02000000)
        self.TIMDCMP2 = BitField(self, 0x04000000)
        self.TIMDCMP4 = BitField(self, 0x08000000)
        self.TIMECMP1 = BitField(self, 0x10000000)
        self.TIMECMP2 = BitField(self, 0x20000000)
        self.TIMECMP4 = BitField(self, 0x40000000)
        self.TIMFCMP2 = BitField(self, 0x80000000)

class HRTIM_Timerx_CHPxR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.CARFRQ = BitField(self, 0x0000000F)
        self.CARDTY = BitField(self, 0x00000070)
        self.STRPW = BitField(self, 0x00000780)

class HRTIM_Timerx_CPT1xCR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.SWCPT = BitField(self, 0x00000001)
        self.UPDCPT = BitField(self, 0x00000002)
        self.EXEV1CPT = BitField(self, 0x00000004)
        self.EXEV2CPT = BitField(self, 0x00000008)
        self.EXEV3CPT = BitField(self, 0x00000010)
        self.EXEV4CPT = BitField(self, 0x00000020)
        self.EXEV5CPT = BitField(self, 0x00000040)
        self.EXEV6CPT = BitField(self, 0x00000080)
        self.EXEV7CPT = BitField(self, 0x00000100)
        self.EXEV8CPT = BitField(self, 0x00000200)
        self.EXEV9CPT = BitField(self, 0x00000400)
        self.EXEV10CPT = BitField(self, 0x00000800)
        self.TF1SET = BitField(self, 0x00000001)
        self.TF1RST = BitField(self, 0x00000002)
        self.TIMFCMP1 = BitField(self, 0x00000004)
        self.TIMFCMP2 = BitField(self, 0x00000008)
        self.TA1SET = BitField(self, 0x00001000)
        self.TA1RST = BitField(self, 0x00002000)
        self.TIMACMP1 = BitField(self, 0x00004000)
        self.TIMACMP2 = BitField(self, 0x00008000)
        self.TB1SET = BitField(self, 0x00010000)
        self.TB1RST = BitField(self, 0x00020000)
        self.TIMBCMP1 = BitField(self, 0x00040000)
        self.TIMBCMP2 = BitField(self, 0x00080000)
        self.TC1SET = BitField(self, 0x00100000)
        self.TC1RST = BitField(self, 0x00200000)
        self.TIMCCMP1 = BitField(self, 0x00400000)
        self.TIMCCMP2 = BitField(self, 0x00800000)
        self.TD1SET = BitField(self, 0x01000000)
        self.TD1RST = BitField(self, 0x02000000)
        self.TIMDCMP1 = BitField(self, 0x04000000)
        self.TIMDCMP2 = BitField(self, 0x08000000)
        self.TE1SET = BitField(self, 0x10000000)
        self.TE1RST = BitField(self, 0x20000000)
        self.TIMECMP1 = BitField(self, 0x40000000)
        self.TIMECMP2 = BitField(self, 0x80000000)

class HRTIM_Timerx_CPT2xCR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.SWCPT = BitField(self, 0x00000001)
        self.UPDCPT = BitField(self, 0x00000002)
        self.EXEV1CPT = BitField(self, 0x00000004)
        self.EXEV2CPT = BitField(self, 0x00000008)
        self.EXEV3CPT = BitField(self, 0x00000010)
        self.EXEV4CPT = BitField(self, 0x00000020)
        self.EXEV5CPT = BitField(self, 0x00000040)
        self.EXEV6CPT = BitField(self, 0x00000080)
        self.EXEV7CPT = BitField(self, 0x00000100)
        self.EXEV8CPT = BitField(self, 0x00000200)
        self.EXEV9CPT = BitField(self, 0x00000400)
        self.EXEV10CPT = BitField(self, 0x00000800)
        self.TF1SET = BitField(self, 0x00000001)
        self.TF1RST = BitField(self, 0x00000002)
        self.TIMFCMP1 = BitField(self, 0x00000004)
        self.TIMFCMP2 = BitField(self, 0x00000008)
        self.TA1SET = BitField(self, 0x00001000)
        self.TA1RST = BitField(self, 0x00002000)
        self.TIMACMP1 = BitField(self, 0x00004000)
        self.TIMACMP2 = BitField(self, 0x00008000)
        self.TB1SET = BitField(self, 0x00010000)
        self.TB1RST = BitField(self, 0x00020000)
        self.TIMBCMP1 = BitField(self, 0x00040000)
        self.TIMBCMP2 = BitField(self, 0x00080000)
        self.TC1SET = BitField(self, 0x00100000)
        self.TC1RST = BitField(self, 0x00200000)
        self.TIMCCMP1 = BitField(self, 0x00400000)
        self.TIMCCMP2 = BitField(self, 0x00800000)
        self.TD1SET = BitField(self, 0x01000000)
        self.TD1RST = BitField(self, 0x02000000)
        self.TIMDCMP1 = BitField(self, 0x04000000)
        self.TIMDCMP2 = BitField(self, 0x08000000)
        self.TE1SET = BitField(self, 0x10000000)
        self.TE1RST = BitField(self, 0x20000000)
        self.TIMECMP1 = BitField(self, 0x40000000)
        self.TIMECMP2 = BitField(self, 0x80000000)

class HRTIM_Timerx_OUTxR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.POL1 = BitField(self, 0x00000002)
        self.IDLM1 = BitField(self, 0x00000004)
        self.IDLES1 = BitField(self, 0x00000008)
        self.FAULT1 = BitField(self, 0x00000030)
        self.CHP1 = BitField(self, 0x00000040)
        self.DIDL1 = BitField(self, 0x00000080)
        self.DTEN = BitField(self, 0x00000100)
        self.DLYPRTEN = BitField(self, 0x00000200)
        self.DLYPRT = BitField(self, 0x00001C00)
        self.BIAR = BitField(self, 0x00004000)
        self.POL2 = BitField(self, 0x00020000)
        self.IDLM2 = BitField(self, 0x00040000)
        self.IDLES2 = BitField(self, 0x00080000)
        self.FAULT2 = BitField(self, 0x00300000)
        self.CHP2 = BitField(self, 0x00400000)
        self.DIDL2 = BitField(self, 0x00800000)

class HRTIM_Timerx_FLTxR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.FLT1EN = BitField(self, 0x00000001)
        self.FLT2EN = BitField(self, 0x00000002)
        self.FLT3EN = BitField(self, 0x00000004)
        self.FLT4EN = BitField(self, 0x00000008)
        self.FLT5EN = BitField(self, 0x00000010)
        self.FLT6EN = BitField(self, 0x00000020)
        self.FLTLCK = BitField(self, 0x80000000)

class HRTIM_Timerx_TIMxCR2(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.DCDE = BitField(self, 0x00000001)
        self.DCDS = BitField(self, 0x00000002)
        self.DCDR = BitField(self, 0x00000004)
        self.UDM = BitField(self, 0x00000010)
        self.ROM = BitField(self, 0x000000C0)
        self.OUTROM = BitField(self, 0x00000300)
        self.ADROM = BitField(self, 0x00000C00)
        self.BMROM = BitField(self, 0x00003000)
        self.FEROM = BitField(self, 0x0000C000)
        self.GTCMP1 = BitField(self, 0x00010000)
        self.GTCMP3 = BitField(self, 0x00020000)
        self.TRGHLF = BitField(self, 0x00100000)

class HRTIM_Timerx_EEFxR3(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.EEVACE = BitField(self, 0x00000001)
        self.EEVACRES = BitField(self, 0x00000002)
        self.EEVARSTM = BitField(self, 0x00000004)
        self.EEVASEL = BitField(self, 0x000000F0)
        self.EEVACNT = BitField(self, 0x00003F00)
        self.EEVBCE = BitField(self, 0x00010000)
        self.EEVBCRES = BitField(self, 0x00020000)
        self.EEVBRSTM = BitField(self, 0x00040000)
        self.EEVBSEL = BitField(self, 0x00F00000)
        self.EEVBCNT = BitField(self, 0x3F000000)

class HRTIM_Timerx_TypeDef(PeripheralBase):

    def __init__(self, base):
        super().__init__(base)
        self.TIMxCR = HRTIM_Timerx_TIMxCR(base + 0x0)
        self.TIMxISR = HRTIM_Timerx_TIMxISR(base + 0x4)
        self.TIMxICR = HRTIM_Timerx_TIMxICR(base + 0x8)
        self.TIMxDIER = HRTIM_Timerx_TIMxDIER(base + 0xC)
        self.CNTxR = HRTIM_Timerx_CNTxR(base + 0x10)
        self.PERxR = HRTIM_Timerx_PERxR(base + 0x14)
        self.REPxR = HRTIM_Timerx_REPxR(base + 0x18)
        self.CMP1xR = HRTIM_Timerx_CMP1xR(base + 0x1C)
        self.CMP1CxR = HRTIM_Timerx_CMP1CxR(base + 0x20)
        self.CMP2xR = HRTIM_Timerx_CMP2xR(base + 0x24)
        self.CMP3xR = HRTIM_Timerx_CMP3xR(base + 0x28)
        self.CMP4xR = HRTIM_Timerx_CMP4xR(base + 0x2C)
        self.CPT1xR = HRTIM_Timerx_CPT1xR(base + 0x30)
        self.CPT2xR = HRTIM_Timerx_CPT2xR(base + 0x34)
        self.DTxR = HRTIM_Timerx_DTxR(base + 0x38)
        self.SETx1R = HRTIM_Timerx_SETx1R(base + 0x3C)
        self.RSTx1R = HRTIM_Timerx_RSTx1R(base + 0x40)
        self.SETx2R = HRTIM_Timerx_SETx2R(base + 0x44)
        self.RSTx2R = HRTIM_Timerx_RSTx2R(base + 0x48)
        self.EEFxR1 = HRTIM_Timerx_EEFxR1(base + 0x4C)
        self.EEFxR2 = HRTIM_Timerx_EEFxR2(base + 0x50)
        self.RSTxR = HRTIM_Timerx_RSTxR(base + 0x54)
        self.CHPxR = HRTIM_Timerx_CHPxR(base + 0x58)
        self.CPT1xCR = HRTIM_Timerx_CPT1xCR(base + 0x5C)
        self.CPT2xCR = HRTIM_Timerx_CPT2xCR(base + 0x60)
        self.OUTxR = HRTIM_Timerx_OUTxR(base + 0x64)
        self.FLTxR = HRTIM_Timerx_FLTxR(base + 0x68)
        self.TIMxCR2 = HRTIM_Timerx_TIMxCR2(base + 0x6C)
        self.EEFxR3 = HRTIM_Timerx_EEFxR3(base + 0x70)

HRTIM1_TIMA = HRTIM_Timerx_TypeDef(0x40016880)
HRTIM1_TIMB = HRTIM_Timerx_TypeDef(0x40016900)
HRTIM1_TIMC = HRTIM_Timerx_TypeDef(0x40016980)
HRTIM1_TIMD = HRTIM_Timerx_TypeDef(0x40016A00)
HRTIM1_TIME = HRTIM_Timerx_TypeDef(0x40016A80)
HRTIM1_TIMF = HRTIM_Timerx_TypeDef(0x40016B00)

class HRTIM_Common_CR1(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.MUDIS = BitField(self, 0x00000001)
        self.TAUDIS = BitField(self, 0x00000002)
        self.TBUDIS = BitField(self, 0x00000004)
        self.TCUDIS = BitField(self, 0x00000008)
        self.TDUDIS = BitField(self, 0x00000010)
        self.TEUDIS = BitField(self, 0x00000020)
        self.TFUDIS = BitField(self, 0x00000040)
        self.ADC1USRC = BitField(self, 0x00070000)
        self.ADC2USRC = BitField(self, 0x00380000)
        self.ADC3USRC = BitField(self, 0x01C00000)
        self.ADC4USRC = BitField(self, 0x0E000000)

class HRTIM_Common_CR2(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.MSWU = BitField(self, 0x00000001)
        self.TASWU = BitField(self, 0x00000002)
        self.TBSWU = BitField(self, 0x00000004)
        self.TCSWU = BitField(self, 0x00000008)
        self.TDSWU = BitField(self, 0x00000010)
        self.TESWU = BitField(self, 0x00000020)
        self.TFSWU = BitField(self, 0x00000040)
        self.MRST = BitField(self, 0x00000100)
        self.TARST = BitField(self, 0x00000200)
        self.TBRST = BitField(self, 0x00000400)
        self.TCRST = BitField(self, 0x00000800)
        self.TDRST = BitField(self, 0x00001000)
        self.TERST = BitField(self, 0x00002000)
        self.TFRST = BitField(self, 0x00004000)
        self.SWPA = BitField(self, 0x00010000)
        self.SWPB = BitField(self, 0x00020000)
        self.SWPC = BitField(self, 0x00040000)
        self.SWPD = BitField(self, 0x00080000)
        self.SWPE = BitField(self, 0x00100000)
        self.SWPF = BitField(self, 0x00200000)

class HRTIM_Common_ISR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.FLT1 = BitField(self, 0x00000001)
        self.FLT2 = BitField(self, 0x00000002)
        self.FLT3 = BitField(self, 0x00000004)
        self.FLT4 = BitField(self, 0x00000008)
        self.FLT5 = BitField(self, 0x00000010)
        self.SYSFLT = BitField(self, 0x00000020)
        self.FLT6 = BitField(self, 0x00000040)
        self.DLLRDY = BitField(self, 0x00010000)
        self.BMPER = BitField(self, 0x00020000)

class HRTIM_Common_ICR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.FLT1C = BitField(self, 0x00000001)
        self.FLT2C = BitField(self, 0x00000002)
        self.FLT3C = BitField(self, 0x00000004)
        self.FLT4C = BitField(self, 0x00000008)
        self.FLT5C = BitField(self, 0x00000010)
        self.SYSFLTC = BitField(self, 0x00000020)
        self.FLT6C = BitField(self, 0x00000040)
        self.DLLRDYC = BitField(self, 0x00010000)
        self.BMPERC = BitField(self, 0x00020000)

class HRTIM_Common_IER(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.FLT1 = BitField(self, 0x00000001)
        self.FLT2 = BitField(self, 0x00000002)
        self.FLT3 = BitField(self, 0x00000004)
        self.FLT4 = BitField(self, 0x00000008)
        self.FLT5 = BitField(self, 0x00000010)
        self.SYSFLT = BitField(self, 0x00000020)
        self.FLT6 = BitField(self, 0x00000040)
        self.DLLRDY = BitField(self, 0x00010000)
        self.BMPER = BitField(self, 0x00020000)

class HRTIM_Common_OENR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.TA1OEN = BitField(self, 0x00000001)
        self.TA2OEN = BitField(self, 0x00000002)
        self.TB1OEN = BitField(self, 0x00000004)
        self.TB2OEN = BitField(self, 0x00000008)
        self.TC1OEN = BitField(self, 0x00000010)
        self.TC2OEN = BitField(self, 0x00000020)
        self.TD1OEN = BitField(self, 0x00000040)
        self.TD2OEN = BitField(self, 0x00000080)
        self.TE1OEN = BitField(self, 0x00000100)
        self.TE2OEN = BitField(self, 0x00000200)
        self.TF1OEN = BitField(self, 0x00000400)
        self.TF2OEN = BitField(self, 0x00000800)

class HRTIM_Common_ODISR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.TA1ODIS = BitField(self, 0x00000001)
        self.TA2ODIS = BitField(self, 0x00000002)
        self.TB1ODIS = BitField(self, 0x00000004)
        self.TB2ODIS = BitField(self, 0x00000008)
        self.TC1ODIS = BitField(self, 0x00000010)
        self.TC2ODIS = BitField(self, 0x00000020)
        self.TD1ODIS = BitField(self, 0x00000040)
        self.TD2ODIS = BitField(self, 0x00000080)
        self.TE1ODIS = BitField(self, 0x00000100)
        self.TE2ODIS = BitField(self, 0x00000200)
        self.TF1ODIS = BitField(self, 0x00000400)
        self.TF2ODIS = BitField(self, 0x00000800)

class HRTIM_Common_ODSR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.TA1ODS = BitField(self, 0x00000001)
        self.TA2ODS = BitField(self, 0x00000002)
        self.TB1ODS = BitField(self, 0x00000004)
        self.TB2ODS = BitField(self, 0x00000008)
        self.TC1ODS = BitField(self, 0x00000010)
        self.TC2ODS = BitField(self, 0x00000020)
        self.TD1ODS = BitField(self, 0x00000040)
        self.TD2ODS = BitField(self, 0x00000080)
        self.TE1ODS = BitField(self, 0x00000100)
        self.TE2ODS = BitField(self, 0x00000200)
        self.TF1ODS = BitField(self, 0x00000400)
        self.TF2ODS = BitField(self, 0x00000800)

class HRTIM_Common_BMCR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.BME = BitField(self, 0x00000001)
        self.BMOM = BitField(self, 0x00000002)
        self.BMCLK = BitField(self, 0x0000003C)
        self.BMPRSC = BitField(self, 0x000003C0)
        self.BMPREN = BitField(self, 0x00000400)
        self.MTBM = BitField(self, 0x00010000)
        self.TABM = BitField(self, 0x00020000)
        self.TBBM = BitField(self, 0x00040000)
        self.TCBM = BitField(self, 0x00080000)
        self.TDBM = BitField(self, 0x00100000)
        self.TEBM = BitField(self, 0x00200000)
        self.TFBM = BitField(self, 0x00400000)
        self.BMSTAT = BitField(self, 0x80000000)

class HRTIM_Common_BMTRGR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.SW = BitField(self, 0x00000001)
        self.MSTRST = BitField(self, 0x00000002)
        self.MSTREP = BitField(self, 0x00000004)
        self.MSTCMP1 = BitField(self, 0x00000008)
        self.MSTCMP2 = BitField(self, 0x00000010)
        self.MSTCMP3 = BitField(self, 0x00000020)
        self.MSTCMP4 = BitField(self, 0x00000040)
        self.TARST = BitField(self, 0x00000080)
        self.TAREP = BitField(self, 0x00000100)
        self.TACMP1 = BitField(self, 0x00000200)
        self.TACMP2 = BitField(self, 0x00000400)
        self.TBRST = BitField(self, 0x00000800)
        self.TBREP = BitField(self, 0x00001000)
        self.TBCMP1 = BitField(self, 0x00002000)
        self.TBCMP2 = BitField(self, 0x00004000)
        self.TCRST = BitField(self, 0x00008000)
        self.TCREP = BitField(self, 0x00010000)
        self.TCCMP1 = BitField(self, 0x00020000)
        self.TFRST = BitField(self, 0x00040000)
        self.TDRST = BitField(self, 0x00080000)
        self.TDREP = BitField(self, 0x00100000)
        self.TFREP = BitField(self, 0x00200000)
        self.TDCMP2 = BitField(self, 0x00400000)
        self.TFCMP1 = BitField(self, 0x00800000)
        self.TEREP = BitField(self, 0x01000000)
        self.TECMP1 = BitField(self, 0x02000000)
        self.TECMP2 = BitField(self, 0x04000000)
        self.TAEEV7 = BitField(self, 0x08000000)
        self.TDEEV8 = BitField(self, 0x10000000)
        self.EEV7 = BitField(self, 0x20000000)
        self.EEV8 = BitField(self, 0x40000000)
        self.OCHPEV = BitField(self, 0x80000000)

class HRTIM_Common_BMCMPR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.BMCMPR = BitField(self, 0x0000FFFF)

class HRTIM_Common_BMPER(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.BMPER = BitField(self, 0x0000FFFF)

class HRTIM_Common_EECR1(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.EE1SRC = BitField(self, 0x00000003)
        self.EE1POL = BitField(self, 0x00000004)
        self.EE1SNS = BitField(self, 0x00000018)
        self.EE1FAST = BitField(self, 0x00000020)
        self.EE2SRC = BitField(self, 0x000000C0)
        self.EE2POL = BitField(self, 0x00000100)
        self.EE2SNS = BitField(self, 0x00000600)
        self.EE2FAST = BitField(self, 0x00000800)
        self.EE3SRC = BitField(self, 0x00003000)
        self.EE3POL = BitField(self, 0x00004000)
        self.EE3SNS = BitField(self, 0x00018000)
        self.EE3FAST = BitField(self, 0x00020000)
        self.EE4SRC = BitField(self, 0x000C0000)
        self.EE4POL = BitField(self, 0x00100000)
        self.EE4SNS = BitField(self, 0x00600000)
        self.EE4FAST = BitField(self, 0x00800000)
        self.EE5SRC = BitField(self, 0x03000000)
        self.EE5POL = BitField(self, 0x04000000)
        self.EE5SNS = BitField(self, 0x18000000)
        self.EE5FAST = BitField(self, 0x20000000)

class HRTIM_Common_EECR2(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.EE6SRC = BitField(self, 0x00000003)
        self.EE6POL = BitField(self, 0x00000004)
        self.EE6SNS = BitField(self, 0x00000018)
        self.EE7SRC = BitField(self, 0x000000C0)
        self.EE7POL = BitField(self, 0x00000100)
        self.EE7SNS = BitField(self, 0x00000600)
        self.EE8SRC = BitField(self, 0x00003000)
        self.EE8POL = BitField(self, 0x00004000)
        self.EE8SNS = BitField(self, 0x00018000)
        self.EE9SRC = BitField(self, 0x000C0000)
        self.EE9POL = BitField(self, 0x00100000)
        self.EE9SNS = BitField(self, 0x00600000)
        self.EE10SRC = BitField(self, 0x03000000)
        self.EE10POL = BitField(self, 0x04000000)
        self.EE10SNS = BitField(self, 0x18000000)

class HRTIM_Common_EECR3(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.EE6F = BitField(self, 0x0000000F)
        self.EE7F = BitField(self, 0x000003C0)
        self.EE8F = BitField(self, 0x0000F000)
        self.EE9F = BitField(self, 0x003C0000)
        self.EE10F = BitField(self, 0x0F000000)
        self.EEVSD = BitField(self, 0xC0000000)

class HRTIM_Common_ADC1R(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.AD1MC1 = BitField(self, 0x00000001)
        self.AD1MC2 = BitField(self, 0x00000002)
        self.AD1MC3 = BitField(self, 0x00000004)
        self.AD1MC4 = BitField(self, 0x00000008)
        self.AD1MPER = BitField(self, 0x00000010)
        self.AD1EEV1 = BitField(self, 0x00000020)
        self.AD1EEV2 = BitField(self, 0x00000040)
        self.AD1EEV3 = BitField(self, 0x00000080)
        self.AD1EEV4 = BitField(self, 0x00000100)
        self.AD1EEV5 = BitField(self, 0x00000200)
        self.AD1TFC2 = BitField(self, 0x00000400)
        self.AD1TAC3 = BitField(self, 0x00000800)
        self.AD1TAC4 = BitField(self, 0x00001000)
        self.AD1TAPER = BitField(self, 0x00002000)
        self.AD1TARST = BitField(self, 0x00004000)
        self.AD1TFC3 = BitField(self, 0x00008000)
        self.AD1TBC3 = BitField(self, 0x00010000)
        self.AD1TBC4 = BitField(self, 0x00020000)
        self.AD1TBPER = BitField(self, 0x00040000)
        self.AD1TBRST = BitField(self, 0x00080000)
        self.AD1TFC4 = BitField(self, 0x00100000)
        self.AD1TCC3 = BitField(self, 0x00200000)
        self.AD1TCC4 = BitField(self, 0x00400000)
        self.AD1TCPER = BitField(self, 0x00800000)
        self.AD1TFPER = BitField(self, 0x01000000)
        self.AD1TDC3 = BitField(self, 0x02000000)
        self.AD1TDC4 = BitField(self, 0x04000000)
        self.AD1TDPER = BitField(self, 0x08000000)
        self.AD1TFRST = BitField(self, 0x10000000)
        self.AD1TEC3 = BitField(self, 0x20000000)
        self.AD1TEC4 = BitField(self, 0x40000000)
        self.AD1TEPER = BitField(self, 0x80000000)

class HRTIM_Common_ADC2R(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.AD2MC1 = BitField(self, 0x00000001)
        self.AD2MC2 = BitField(self, 0x00000002)
        self.AD2MC3 = BitField(self, 0x00000004)
        self.AD2MC4 = BitField(self, 0x00000008)
        self.AD2MPER = BitField(self, 0x00000010)
        self.AD2EEV6 = BitField(self, 0x00000020)
        self.AD2EEV7 = BitField(self, 0x00000040)
        self.AD2EEV8 = BitField(self, 0x00000080)
        self.AD2EEV9 = BitField(self, 0x00000100)
        self.AD2EEV10 = BitField(self, 0x00000200)
        self.AD2TAC2 = BitField(self, 0x00000400)
        self.AD2TFC2 = BitField(self, 0x00000800)
        self.AD2TAC4 = BitField(self, 0x00001000)
        self.AD2TAPER = BitField(self, 0x00002000)
        self.AD2TBC2 = BitField(self, 0x00004000)
        self.AD2TFC3 = BitField(self, 0x00008000)
        self.AD2TBC4 = BitField(self, 0x00010000)
        self.AD2TBPER = BitField(self, 0x00020000)
        self.AD2TCC2 = BitField(self, 0x00040000)
        self.AD2TFC4 = BitField(self, 0x00080000)
        self.AD2TCC4 = BitField(self, 0x00100000)
        self.AD2TCPER = BitField(self, 0x00200000)
        self.AD2TCRST = BitField(self, 0x00400000)
        self.AD2TDC2 = BitField(self, 0x00800000)
        self.AD2TFPER = BitField(self, 0x01000000)
        self.AD2TDC4 = BitField(self, 0x02000000)
        self.AD2TDPER = BitField(self, 0x04000000)
        self.AD2TDRST = BitField(self, 0x08000000)
        self.AD2TEC2 = BitField(self, 0x10000000)
        self.AD2TEC3 = BitField(self, 0x20000000)
        self.AD2TEC4 = BitField(self, 0x40000000)
        self.AD2TERST = BitField(self, 0x80000000)

class HRTIM_Common_ADC3R(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.AD3MC1 = BitField(self, 0x00000001)
        self.AD3MC2 = BitField(self, 0x00000002)
        self.AD3MC3 = BitField(self, 0x00000004)
        self.AD3MC4 = BitField(self, 0x00000008)
        self.AD3MPER = BitField(self, 0x00000010)
        self.AD3EEV1 = BitField(self, 0x00000020)
        self.AD3EEV2 = BitField(self, 0x00000040)
        self.AD3EEV3 = BitField(self, 0x00000080)
        self.AD3EEV4 = BitField(self, 0x00000100)
        self.AD3EEV5 = BitField(self, 0x00000200)
        self.AD3TFC2 = BitField(self, 0x00000400)
        self.AD3TAC3 = BitField(self, 0x00000800)
        self.AD3TAC4 = BitField(self, 0x00001000)
        self.AD3TAPER = BitField(self, 0x00002000)
        self.AD3TARST = BitField(self, 0x00004000)
        self.AD3TFC3 = BitField(self, 0x00008000)
        self.AD3TBC3 = BitField(self, 0x00010000)
        self.AD3TBC4 = BitField(self, 0x00020000)
        self.AD3TBPER = BitField(self, 0x00040000)
        self.AD3TBRST = BitField(self, 0x00080000)
        self.AD3TFC4 = BitField(self, 0x00100000)
        self.AD3TCC3 = BitField(self, 0x00200000)
        self.AD3TCC4 = BitField(self, 0x00400000)
        self.AD3TCPER = BitField(self, 0x00800000)
        self.AD3TFPER = BitField(self, 0x01000000)
        self.AD3TDC3 = BitField(self, 0x02000000)
        self.AD3TDC4 = BitField(self, 0x04000000)
        self.AD3TDPER = BitField(self, 0x08000000)
        self.AD3TFRST = BitField(self, 0x10000000)
        self.AD3TEC3 = BitField(self, 0x20000000)
        self.AD3TEC4 = BitField(self, 0x40000000)
        self.AD3TEPER = BitField(self, 0x80000000)

class HRTIM_Common_ADC4R(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.AD4MC1 = BitField(self, 0x00000001)
        self.AD4MC2 = BitField(self, 0x00000002)
        self.AD4MC3 = BitField(self, 0x00000004)
        self.AD4MC4 = BitField(self, 0x00000008)
        self.AD4MPER = BitField(self, 0x00000010)
        self.AD4EEV6 = BitField(self, 0x00000020)
        self.AD4EEV7 = BitField(self, 0x00000040)
        self.AD4EEV8 = BitField(self, 0x00000080)
        self.AD4EEV9 = BitField(self, 0x00000100)
        self.AD4EEV10 = BitField(self, 0x00000200)
        self.AD4TAC2 = BitField(self, 0x00000400)
        self.AD4TFC2 = BitField(self, 0x00000800)
        self.AD4TAC4 = BitField(self, 0x00001000)
        self.AD4TAPER = BitField(self, 0x00002000)
        self.AD4TBC2 = BitField(self, 0x00004000)
        self.AD4TFC3 = BitField(self, 0x00008000)
        self.AD4TBC4 = BitField(self, 0x00010000)
        self.AD4TBPER = BitField(self, 0x00020000)
        self.AD4TCC2 = BitField(self, 0x00040000)
        self.AD4TFC4 = BitField(self, 0x00080000)
        self.AD4TCC4 = BitField(self, 0x00100000)
        self.AD4TCPER = BitField(self, 0x00200000)
        self.AD4TCRST = BitField(self, 0x00400000)
        self.AD4TDC2 = BitField(self, 0x00800000)
        self.AD4TFPER = BitField(self, 0x01000000)
        self.AD4TDC4 = BitField(self, 0x02000000)
        self.AD4TDPER = BitField(self, 0x04000000)
        self.AD4TDRST = BitField(self, 0x08000000)
        self.AD4TEC2 = BitField(self, 0x10000000)
        self.AD4TEC3 = BitField(self, 0x20000000)
        self.AD4TEC4 = BitField(self, 0x40000000)
        self.AD4TERST = BitField(self, 0x80000000)

class HRTIM_Common_DLLCR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.CAL = BitField(self, 0x00000001)
        self.CALEN = BitField(self, 0x00000002)
        self.CALRTE = BitField(self, 0x0000000C)

class HRTIM_Common_FLTINR1(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.FLT1E = BitField(self, 0x00000001)
        self.FLT1P = BitField(self, 0x00000002)
        self.FLT1SRC_0 = BitField(self, 0x00000004)
        self.FLT1F = BitField(self, 0x00000078)
        self.FLT1LCK = BitField(self, 0x00000080)
        self.FLT2E = BitField(self, 0x00000100)
        self.FLT2P = BitField(self, 0x00000200)
        self.FLT2SRC_0 = BitField(self, 0x00000400)
        self.FLT2F = BitField(self, 0x00007800)
        self.FLT2LCK = BitField(self, 0x00008000)
        self.FLT3E = BitField(self, 0x00010000)
        self.FLT3P = BitField(self, 0x00020000)
        self.FLT3SRC_0 = BitField(self, 0x00040000)
        self.FLT3F = BitField(self, 0x00780000)
        self.FLT3LCK = BitField(self, 0x00800000)
        self.FLT4E = BitField(self, 0x01000000)
        self.FLT4P = BitField(self, 0x02000000)
        self.FLT4SRC_0 = BitField(self, 0x04000000)
        self.FLT4F = BitField(self, 0x78000000)
        self.FLT4LCK = BitField(self, 0x80000000)

class HRTIM_Common_FLTINR2(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.FLT5E = BitField(self, 0x00000001)
        self.FLT5P = BitField(self, 0x00000002)
        self.FLT5SRC_0 = BitField(self, 0x00000004)
        self.FLT5F = BitField(self, 0x00000078)
        self.FLT5LCK = BitField(self, 0x00000080)
        self.FLT6E = BitField(self, 0x00000100)
        self.FLT6P = BitField(self, 0x00000200)
        self.FLT6SRC_0 = BitField(self, 0x00000400)
        self.FLT6F = BitField(self, 0x00007800)
        self.FLT6LCK = BitField(self, 0x00008000)
        self.FLT1SRC_1 = BitField(self, 0x00010000)
        self.FLT2SRC_1 = BitField(self, 0x00020000)
        self.FLT3SRC_1 = BitField(self, 0x00040000)
        self.FLT4SRC_1 = BitField(self, 0x00080000)
        self.FLT5SRC_1 = BitField(self, 0x00100000)
        self.FLT6SRC_1 = BitField(self, 0x00200000)
        self.FLTSD = BitField(self, 0x03000000)

class HRTIM_Common_BDMUPR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.MCR = BitField(self, 0x00000001)
        self.MICR = BitField(self, 0x00000002)
        self.MDIER = BitField(self, 0x00000004)
        self.MCNT = BitField(self, 0x00000008)
        self.MPER = BitField(self, 0x00000010)
        self.MREP = BitField(self, 0x00000020)
        self.MCMP1 = BitField(self, 0x00000040)
        self.MCMP2 = BitField(self, 0x00000080)
        self.MCMP3 = BitField(self, 0x00000100)
        self.MCMP4 = BitField(self, 0x00000200)

class HRTIM_Common_BDTAUPR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)

class HRTIM_Common_BDTBUPR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)

class HRTIM_Common_BDTCUPR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)

class HRTIM_Common_BDTDUPR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)

class HRTIM_Common_BDTEUPR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)

class HRTIM_Common_BDMADR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.BDMADR = BitField(self, 0xFFFFFFFF)

class HRTIM_Common_BDTFUPR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)

class HRTIM_Common_ADCER(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.AD5TRG = BitField(self, 0x0000001F)
        self.AD6TRG = BitField(self, 0x000003E0)
        self.AD7TRG = BitField(self, 0x00007C00)
        self.AD8TRG = BitField(self, 0x001F0000)
        self.AD9TRG = BitField(self, 0x03E00000)
        self.AD10TRG = BitField(self, 0x7C000000)

class HRTIM_Common_ADCUR(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.AD5USRC = BitField(self, 0x00000007)
        self.AD6USRC = BitField(self, 0x00000070)
        self.AD7USRC = BitField(self, 0x00000700)
        self.AD8USRC = BitField(self, 0x00007000)
        self.AD9USRC = BitField(self, 0x00070000)
        self.AD10USRC = BitField(self, 0x00700000)

class HRTIM_Common_ADCPS1(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.AD1PSC = BitField(self, 0x0000001F)
        self.AD2PSC = BitField(self, 0x000007C0)
        self.AD3PSC = BitField(self, 0x0001F000)
        self.AD4PSC = BitField(self, 0x007C0000)
        self.AD5PSC = BitField(self, 0x1F000000)

class HRTIM_Common_ADCPS2(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.AD6PSC = BitField(self, 0x0000001F)
        self.AD7PSC = BitField(self, 0x000007C0)
        self.AD8PSC = BitField(self, 0x0001F000)
        self.AD9PSC = BitField(self, 0x007C0000)
        self.AD10PSC = BitField(self, 0x1F000000)

class HRTIM_Common_FLTINR3(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.FLT1BLKE = BitField(self, 0x00000001)
        self.FLT1BLKS = BitField(self, 0x00000002)
        self.FLT1CNT = BitField(self, 0x0000003C)
        self.FLT1CRES = BitField(self, 0x00000040)
        self.FLT1RSTM = BitField(self, 0x00000080)
        self.FLT2BLKE = BitField(self, 0x00000100)
        self.FLT2BLKS = BitField(self, 0x00000200)
        self.FLT2CNT = BitField(self, 0x00003C00)
        self.FLT2CRES = BitField(self, 0x00004000)
        self.FLT2RSTM = BitField(self, 0x00008000)
        self.FLT3BLKE = BitField(self, 0x00010000)
        self.FLT3BLKS = BitField(self, 0x00020000)
        self.FLT3CNT = BitField(self, 0x003C0000)
        self.FLT3CRES = BitField(self, 0x00400000)
        self.FLT3RSTM = BitField(self, 0x00800000)
        self.FLT4BLKE = BitField(self, 0x01000000)
        self.FLT4BLKS = BitField(self, 0x02000000)
        self.FLT4CNT = BitField(self, 0x3C000000)
        self.FLT4CRES = BitField(self, 0x40000000)
        self.FLT4RSTM = BitField(self, 0x80000000)

class HRTIM_Common_FLTINR4(RegisterBase):
    
    def __init__(self, address):
        super().__init__(address)
        self.FLT5BLKE = BitField(self, 0x00000001)
        self.FLT5BLKS = BitField(self, 0x00000002)
        self.FLT5CNT = BitField(self, 0x0000003C)
        self.FLT5CRES = BitField(self, 0x00000040)
        self.FLT5RSTM = BitField(self, 0x00000080)
        self.FLT6BLKE = BitField(self, 0x00000100)
        self.FLT6BLKS = BitField(self, 0x00000200)
        self.FLT6CNT = BitField(self, 0x00003C00)
        self.FLT6CRES = BitField(self, 0x00004000)
        self.FLT6RSTM = BitField(self, 0x00008000)

class HRTIM_Common_TypeDef(PeripheralBase):

    def __init__(self, base):
        super().__init__(base)
        self.CR1 = HRTIM_Common_CR1(base + 0x0)
        self.CR2 = HRTIM_Common_CR2(base + 0x4)
        self.ISR = HRTIM_Common_ISR(base + 0x8)
        self.ICR = HRTIM_Common_ICR(base + 0xC)
        self.IER = HRTIM_Common_IER(base + 0x10)
        self.OENR = HRTIM_Common_OENR(base + 0x14)
        self.ODISR = HRTIM_Common_ODISR(base + 0x18)
        self.ODSR = HRTIM_Common_ODSR(base + 0x1C)
        self.BMCR = HRTIM_Common_BMCR(base + 0x20)
        self.BMTRGR = HRTIM_Common_BMTRGR(base + 0x24)
        self.BMCMPR = HRTIM_Common_BMCMPR(base + 0x28)
        self.BMPER = HRTIM_Common_BMPER(base + 0x2C)
        self.EECR1 = HRTIM_Common_EECR1(base + 0x30)
        self.EECR2 = HRTIM_Common_EECR2(base + 0x34)
        self.EECR3 = HRTIM_Common_EECR3(base + 0x38)
        self.ADC1R = HRTIM_Common_ADC1R(base + 0x3C)
        self.ADC2R = HRTIM_Common_ADC2R(base + 0x40)
        self.ADC3R = HRTIM_Common_ADC3R(base + 0x44)
        self.ADC4R = HRTIM_Common_ADC4R(base + 0x48)
        self.DLLCR = HRTIM_Common_DLLCR(base + 0x4C)
        self.FLTINR1 = HRTIM_Common_FLTINR1(base + 0x50)
        self.FLTINR2 = HRTIM_Common_FLTINR2(base + 0x54)
        self.BDMUPR = HRTIM_Common_BDMUPR(base + 0x58)
        self.BDTAUPR = HRTIM_Common_BDTAUPR(base + 0x5C)
        self.BDTBUPR = HRTIM_Common_BDTBUPR(base + 0x60)
        self.BDTCUPR = HRTIM_Common_BDTCUPR(base + 0x64)
        self.BDTDUPR = HRTIM_Common_BDTDUPR(base + 0x68)
        self.BDTEUPR = HRTIM_Common_BDTEUPR(base + 0x6C)
        self.BDMADR = HRTIM_Common_BDMADR(base + 0x70)
        self.BDTFUPR = HRTIM_Common_BDTFUPR(base + 0x74)
        self.ADCER = HRTIM_Common_ADCER(base + 0x78)
        self.ADCUR = HRTIM_Common_ADCUR(base + 0x7C)
        self.ADCPS1 = HRTIM_Common_ADCPS1(base + 0x80)
        self.ADCPS2 = HRTIM_Common_ADCPS2(base + 0x84)
        self.FLTINR3 = HRTIM_Common_FLTINR3(base + 0x88)
        self.FLTINR4 = HRTIM_Common_FLTINR4(base + 0x8C)

HRTIM1_COMMON = HRTIM_Common_TypeDef(0x40016B80)

