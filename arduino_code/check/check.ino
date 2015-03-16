#include <Adafruit_TiCoServo.h>
#include <Adafruit_NeoPixel.h>

Adafruit_TiCoServo baseServo;

int pirPin = 3;    //the digital pin connected to the PIR sensor's output
int pirPin2 = 2;
int ledPin = 7;

float pos = 90.0;

Adafruit_NeoPixel ring = Adafruit_NeoPixel(8, ledPin, NEO_GRB + NEO_KHZ800);

/////////////////////////////
//SETUP
void setup(){
  Serial.begin(9600);
  pinMode(pirPin, INPUT);
  pinMode(pirPin2, INPUT);
  baseServo.attach(9);
  ring.begin();
}

////////////////////////////
//LOOP
void loop() {
  if(digitalRead(pirPin) == HIGH){
    for(int a=0; a<8; a++) {
      if(a<4 && a>0) {
        ring.setPixelColor(a, ring.Color(0,15,0));
      } else {
        ring.setPixelColor(a, ring.Color(15,15,15));
      }
      ring.show();
    }
    pos+=0.005;
  } else if(digitalRead(pirPin2) == HIGH) {
    for(int b=0; b<8; b++) {
      if(b<8 && b>4) {
        ring.setPixelColor(b, ring.Color(0,15,0));
      } else {
        ring.setPixelColor(b, ring.Color(15,15,15));
      }
      ring.show();
    }
    pos-=0.005;
  } else {
    clearLed();
  }
  if(pos>180) pos=180;
  if(pos<0) pos=0;
  baseServo.write(pos);
}

void clearLed() {
  for(int c=0; c<8; c++) {
    ring.setPixelColor(c, ring.Color(15,15,15));
    ring.show();
  }
}
