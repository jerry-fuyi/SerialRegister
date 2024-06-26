/*
 * uart_reg.c
 *
 *  Created on: Jun 27, 2024
 *      Author: JerryFu
 */

#include "main.h"

extern UART_HandleTypeDef huart2;
extern DMA_HandleTypeDef hdma_usart2_rx;
extern CRC_HandleTypeDef hcrc;

UART_HandleTypeDef* huart_reg = &huart2;
DMA_HandleTypeDef* hdma_rx = &hdma_usart2_rx;

#include "uart_reg.h"

#include <cstring>
#include <string>
#include <map>

static void uart_receive_start();
static void reg_read_handler(uint8_t* data, size_t size);
static void reg_write_handler(uint8_t* data, size_t size);

static uint8_t rx_buf[520];

void uart_init()
{
  uart_register_handler("RDR", reg_read_handler);
  uart_register_handler("WRR", reg_write_handler);

  uart_receive_start();
}

void uart_transmit(const uint8_t* data, size_t size)
{
  uint8_t tx_buf[4] = {0x55, 0xA5,
      (uint8_t)(size & 0xFF), (uint8_t)(size >> 8)};
  HAL_UART_Transmit(huart_reg, tx_buf, 4, 10);
  uint16_t crc = HAL_CRC_Calculate(&hcrc, (uint32_t*)data, size);
  HAL_UART_Transmit(huart_reg, data, size, size+1);
  tx_buf[0] = crc & 0xFF;
  tx_buf[1] = crc >> 8;
  HAL_UART_Transmit(huart_reg, tx_buf, 2, 10);
}

static std::map<std::string, void(*)(uint8_t*, size_t)> handler_map;

void uart_register_handler(const char* cmd, void(*cb)(uint8_t*, size_t))
{
  handler_map[cmd] = cb;
}

static int uart_manager(uint8_t* begin, uint8_t* end)
{
  if (end - begin < 8)
    return -1;

  if (*begin++ != 0x55)
    return -1;
  if (*begin++ != 0xA5)
    return -1;

  int size = *begin++;
  size += *begin++ << 8;

  if (size > end - begin + 2 || size < 2)
    return -1;

  int crc = begin[size] + (begin[size+1] << 8);
  int calc = HAL_CRC_Calculate(&hcrc, (uint32_t*)begin, size);
  if (calc != crc)
    return -1;

  end = begin + size;
  auto p = begin;
  for (; p != end; ++p)
  {
    if (*p == ':')
      break;
  }

  if (p != end)
  {
    std::string cmd(begin, p);
    auto it = handler_map.find(cmd);
    if (it != handler_map.end())
    {
      ++p;
      it->second(p, end-p);
    }
  }

  return size + 6;
}

void HAL_UARTEx_RxEventCallback(UART_HandleTypeDef *huart, uint16_t Size)
{
  if (huart != huart_reg)
    return;

  auto end = rx_buf + Size;
  for (auto* p = rx_buf; p < end; )
  {
    int res = uart_manager(p, end);
    if (res < 0)
      break;
    p += res;
  }

  uart_receive_start();
}

static void uart_receive_start()
{
  HAL_UARTEx_ReceiveToIdle_DMA(huart_reg, rx_buf, sizeof(rx_buf)/sizeof(*rx_buf));
  hdma_rx->Instance->CCR &= ~DMA_CCR_HTIE;
}

static void reg_read_handler(uint8_t* data, size_t size)
{
  if (size != 4)
    return;

  uint32_t addr = *(uint32_t*)data;
  volatile uint32_t* reg = (volatile uint32_t*)addr;
  uint32_t value = *reg;
  uart_transmit((uint8_t*)&value, 4);
}

static void reg_write_handler(uint8_t* data, size_t size)
{
  if (size != 12)
    return;

  uint32_t addr = *(uint32_t*)data;
  volatile uint32_t* reg = (volatile uint32_t*)addr;
  uint32_t value = *(uint32_t*)(data+4);
  uint32_t mask = *(uint32_t*)(data+8);

  *reg = (*reg & ~mask) | value;
}

