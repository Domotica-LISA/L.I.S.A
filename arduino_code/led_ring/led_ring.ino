#include <Adafruit_NeoPixel.h>

#define PIN 6
Adafruit_NeoPixel ring = Adafruit_NeoPixel(8, PIN, NEO_GRB + NEO_KHZ800);

int i=0;
int a=7;  

void setup() {
  // put your setup code here, to run once:
  ring.begin();
  ring.show();
}

void loop() {
  // put your main code here, to run repeatedly:
    ring.setPixelColor(i, ring.Color(0, 0, 30)); // .Color(RED[0-255], GREEN[0-255], BLUE[0-255]);
    ring.setPixelColor(i-1, ring.Color(0, 0, 0)); // .Color(RED[0-255], GREEN[0-255], BLUE[0-255]);
    ring.setPixelColor(a, ring.Color(30, 0, 0)); // .Color(RED[0-255], GREEN[0-255], BLUE[0-255]);
    ring.setPixelColor(a+1, ring.Color(0, 0, 0)); // .Color(RED[0-255], GREEN[0-255], BLUE[0-255]);
    //ring.setBrightness(30); // .setBrightness([0-255]);
    ring.show();
    
    i++;
    a--;
    if(i >= ring.numPixels()) {
      i=0;
      ring.setPixelColor(7, ring.Color(0, 0, 0));
    }
    if(a<0) {
      a=7;
    }
    delay(100);
}
