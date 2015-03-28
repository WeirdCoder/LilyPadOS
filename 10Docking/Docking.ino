#include <Servo.h>

Servo magnetServo;

void setup(){
  Serial.begin(9600);
  pinMode(2, OUTPUT); //relays for LED
  pinMode(3, INPUT) //dock detection circuit
  magnetServo.attach(9);
  magnetServo.write(1);
  digitalWrite(2, LOW);
}

void loop(){
  
  if (digitalRead(3) == HIGH){
    Serial.write("ON");
    Serial.println("Healthy");
  }
  
  else if (digitalRead(3) == LOW){
    Serial.write("OFF");
    Serial.println("Healthy");
  }
  
  else{
    Serial.println("Something is wrong with the detection circuit");
  }
  
  if (Serial.available()){
    int i = Serial.read();
    
    if (i == "00"){
      digitalWrite(2, LOW); 
      magnetServo.write(1);
      Serial.println("Healthy");
    }
    
    else if (i == "01"){
      digitalWrite(2, LOW); 
      magnetServo.write(90);
      Serial.println("Healthy");
    }
    
    else if (i == "10"){
      digitalWrite(2, HIGH); 
      magnetServo.write(1);
      Serial.println("Healthy");
    }
    
    else if (i == "11"){
      digitalWrite(2, HIGH); 
      magnetServo.write(HIGH);
      Serial.println("Healthy");
    }
  
    else{
      Serial.println("Something is wrong with the RPi Communication");
    }  
  }
  delay(50); 
}
