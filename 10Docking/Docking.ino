#include <Servo.h>

Servo magnetServo;

void setup(){
  Serial.begin(9600);
  pinMode(2, OUTPUT); //relays for LED
  magnetServo.attach(9);
  magnetServo.write(1);
  digitalWrite(2, LOW);
}

void loop(){
  
  if (Serial.available()){
    int i = Serial.read();
    if (i-48){
      digitalWrite(2, HIGH); 
      magnetServo.write(90);
      Serial.write("ON");
    }
    
    else{
      digitalWrite(2, LOW);
      magnetServo.write(1);
      Serial.write("OFF");
    }
  
  }
  delay(50); 
}
