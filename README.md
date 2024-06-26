# SerialRegister

An interactive MCU register accessor through UART

Currently supporting STM32G4 only

## Usage

### In MCU

1. Create a project based on `SerialRegister.ioc`
   - If you want to create a project from scratch, remember to correctly configure USART, DMA and their interrupts
2. Add `uart_reg.h` to includes and `uart_reg.cpp` to sources
3. Call `uart_init()`
4. Remerber that handlers are invoked in USART interrupts, so don't use `HAL_Delay` in handlers

### In Jupyter
1. `from g474 import *`
2. Type the register name just like writing C (with `->` replaced by `.`), e.g. `TIM1.CNT`
3. For reading, just type the name and press `Shift+Enter`, it will print a table like the register description in Reference Manual; for writing, just make an assignment
4. You can access the whole register or bit fields, e.g. `TIM1.CR1.CEN = 1`, which will be converted to a read-modify-write access; don't use operators like `|=`

## Future Plans
1. Generating register map from SVD file
2. Eliminating UART and DMA configurations in STM32CubeMX - rewrite the framework with register access
3. Adding 8- and 16-bit accessors to registers, and shortening UART transmissions

