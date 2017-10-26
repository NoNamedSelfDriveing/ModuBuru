/*
 * StepperMotorTest.c
 *
 * Created: 2017-10-25 13:50:16
 * Author : Skj
 */ 

/*
*	�� ���� ���
*	ATmega128 PE0(RX0) - Arduino Digital 1(TX)
*	ATmega128 PE1(TX0) - Arduino Digital 0(RX)
*/

#define F_CPU 16000000

#include <avr/io.h>
#include <avr/interrupt.h>
#include <util/delay.h>

#define TURN_LEFT 0
#define TURN_RIGHT 1

//�Ƶ��̳�κ��� uart ���� �Ǿ����� üũ�ϴ� �÷���
volatile uint8_t arduino_receive_flag = 0;
volatile uint8_t arduino_receive_data = 0;

void uart_init();
void uart_send_byte(unsigned char byte);
void turn_step_motor(char direction, char turn_cycle);

//UART ���� ���ͷ�Ʈ
ISR(USART0_RX_vect)
{
	arduino_receive_flag = 1;
	arduino_receive_data = UDR0;
}

int main(void)
{
	cli();
   uart_init();
    DDRD = 0xFF;		// ������
	sei();
	
	PORTD = 0xFF;
	turn_step_motor(TURN_RIGHT, 8);		//���������� 360�� ȸ��
	_delay_ms(500);
	turn_step_motor(TURN_LEFT, 8);	//�������� 360�� ȸ��
	_delay_ms(500);
	PORTD = 0x00;
	while(1);
	/*while(1)
	{
		turn_step_motor(TURN_RIGHT, 3);
		
	}*/
}

void uart_init()
{
	 //uart �ۼ��� ��� ����
	 UCSR0A = 0x00;
	 UCSR0B = 0x98;
	 UCSR0C = 0x06;
	 
	 //Baud rate ����
	 UBRR0H = 0x00;
	 UBRR0L = 0x67;	//103, 9600 Baud rate
}

void uart_send_byte(unsigned char byte)
{
	while(!(UCSR0A & (1<<UDRE0)));
	UDR0 = byte;
}

//���� ���� ������ �Լ�. ���� : direction : ����(TURN_RIGHT, TURN LEFT), turn_cycle : ȸ�� Ƚ��
void turn_step_motor(char direction, char turn_cycle)
{
	int i;
	uart_send_byte(direction);	//���� ����
	uart_send_byte(turn_cycle);	//ȸ���� ����
	//while(!(arduino_receive_flag));
	//arduino_receive_flag = 0;
}
