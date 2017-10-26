
/*
 Stepper Motor Control - one revolution
 This program drives a unipolar or bipolar stepper motor.
 The motor is attached to digital pins 8 - 11 of the Arduino.
 The motor should revolve one revolution in one direction, then
 one revolution in the other direction.
 Created 11 Mar. 2007
 Modified 30 Nov. 2009
 by Tom Igoe
 */

#include <Stepper.h>
#define TURN_LEFT 0
#define TURN_RIGHT 1

const int stepsPerRevolution = 200;  // change this to fit the number of steps per revolution

// for your motor

// initialize the stepper library on pins 8 through 11:
Stepper myStepper(stepsPerRevolution, 8, 9, 10, 11);

void setup() {
  // set the speed at 60 rpm:
  myStepper.setSpeed(60);
  // initialize the serial port:
  Serial.begin(9600);
}

void loop() {
  // step one revolution  in one direction:
  //myStepper.step(200);
  while(Serial.available())
  {
    int direction = Serial.read();
    int step_num;
    Serial.print(direction);
    delay(50);
    switch(direction)
    {
      case TURN_LEFT :
        step_num = Serial.read();
        Serial.println(step_num);
        myStepper.step(-25*step_num); //왼쪽으로 -25*step_num*1.8도 만큼 회전
        Serial.write(1);
        break;
        
      case TURN_RIGHT :
        step_num = Serial.read();
        Serial.println(step_num);
        myStepper.step(25*step_num);  //오른쪽으로 25*step_num*1.8도 만큼 회전
        Serial.write(1);
        break;
    }
  }
}
