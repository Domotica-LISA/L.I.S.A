#include <Servo.h>

Servo headServo;  // create servo object to control a servo
Servo lowerArmServo;  // create servo object to control a servo
Servo upperArmServo;  // create servo object to control a servo
Servo baseServo;  // create servo object to control a servo

int pos = 0;
char val;    // variable to read the value from the analog pin
int value[5];
char statusvalue[10];
int index;
int soundSensorLeft = A0;
int soundSensorRight = A1;
int soundSensorLeftValue = 0;
int soundSensorRightValue = 0;

const int ledPin = 13;

void setup() {
  pinMode(ledPin, OUTPUT);
  Serial.begin(9600);
  //initServos();
  initSensors();
}

void initServos() {
  headServo.attach(8);  // attaches the servo on pin 9 to the servo object
  lowerArmServo.attach(9);  // attaches the servo on pin 9 to the servo object
  upperArmServo.attach(10);  // attaches the servo on pin 9 to the servo object
  baseServo.attach(11);  // attaches the servo on pin 9 to the servo object
    
  //baseServo.write(45);
  //headServo.write(45);
  //lowerArmServo.write(45);
  //upperArmServo.write(45);
}

void initSensors() {
  pinMode(soundSensorRight, INPUT);
  pinMode(soundSensorLeft, INPUT);
  //digitalWrite(soundSensorRight, HIGH);
  //digitalWrite(soundSensorLeft, HIGH);
}
  
void loop() {
  //baseServo.write(random(0,180));
  //headServo.write(random(30,150));
  //lowerArmServo.write(random(60,120));
  //upperArmServo.write(random(0,180));
  soundSensorLeftValue = analogRead(soundSensorLeft);
  soundSensorRightValue = analogRead(soundSensorRight);
  Serial.print("Left: ");
  Serial.print(soundSensorLeftValue);
  Serial.print("     Right: ");
  Serial.print(soundSensorRightValue);
  Serial.println();
  delay(100);
}

/*
  digitalWrite(ledPin, HIGH);
  soundSensorRightValue = analogRead(soundSensorRight);
  soundSensorLeftValue = analogRead(soundSensorLeft);
  index = 100;
  int a=0;
  byte b=0;
  while(Serial.available()) {
    if(index >= 100) {
        value[a] = 0;
    }
    val = Serial.read();
    Serial.println(val);
    if(val == 44) {
      for(int c=0;c<10;c++) {
        statusvalue[c] = 0;
      }
      a++;
      index = 100;
    } else if(a<4) {
      val -= 48;
      value[a] += val * index;
      index = index / 10;
      Serial.println(value[a]);
    } else {
      statusvalue[b] = val;
      b++;
    }
  }
  if(strcmp(statusvalue,"detected") == 0) {
    followUser();
  } else if(strcmp(statusvalue,"searching") == 0) {
    seekUser();
  } else {
    waiting();
  }
}

void waiting() {
  
}

void seekUser() {
  if(soundSensorRightValue > soundSensorLeftValue) {
    pos = 90 + ((soundSensorRightValue - soundSensorLeftValue) * 0.3515625);
    baseServo.write(pos);
    //Serial.write(pos);
  } else if(soundSensorRightValue < soundSensorLeftValue) {
    pos = 90 + ((soundSensorRightValue - soundSensorLeftValue) * 0.3515625);
    baseServo.write(pos);
    //Serial.write(pos);
  } else {
    pos = 90 + ((soundSensorRightValue - soundSensorLeftValue) * 0.3515625);
    baseServo.write(pos);
    //Serial.write(pos);
  }
}

void followUser() {
  headServo.write(value[0]);                  // sets the servo position according to the scaled value 
  lowerArmServo.write(value[1]);                  // sets the servo position according to the scaled value
  upperArmServo.write(value[2]);                  // sets the servo position according to the scaled value
  baseServo.write(value[3]);                  // sets the servo position according to the scaled value
  //delay(150); 
} 
*/
