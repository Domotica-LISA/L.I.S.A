void setup() {
  Serial.begin(9600);
}

void loop() {
  while(Serial.available() > 0) {
      int headpos = Serial.parseInt();
      int rotationpos = Serial.parseInt();
      int armpos = Serial.parseInt();
      int basepos = Serial.parseInt();
      
      Serial.println(headpos);
      Serial.println(rotationpos);
      Serial.println(armpos);
      Serial.println(basepos);
  }
}
