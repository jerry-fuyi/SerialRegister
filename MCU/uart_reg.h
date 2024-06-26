/*
 * uart_reg.h
 *
 *  Created on: Jun 27, 2024
 *      Author: JerryFu
 */

#ifndef INC_UART_REG_H_
#define INC_UART_REG_H_

#ifdef __cplusplus
extern "C" {
#endif

void uart_init();

void uart_transmit(const uint8_t* data, size_t size);

void uart_register_handler(const char*, void(*)(uint8_t*, size_t));

#ifdef __cplusplus
}
#endif

#endif /* INC_UART_REG_H_ */
