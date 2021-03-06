#include <Servo.h>

Servo magnetServo;
int val = 2;

void setup(){
  Serial.begin(9600);
  pinMode(2, OUTPUT); //relays for LED
  pinMode(3, INPUT); //dock detection circuit
  magnetServo.attach(9);
  magnetServo.write(1);
  digitalWrite(2, LOW);
}

void loop(){
  if (val == 2){
    val = digitalRead(3);
  }
  
  else if (val != digitalRead(3)){
    val = digitalRead(3); 
    
    if (val == HIGH){
      Serial.println("ON");
      Serial.println("000"); //healthy
    }
  
    else if (val == LOW){
      Serial.println("OFF");
      Serial.println("000"); //healthy
    }
  
    else{
      Serial.println("003"); //Something is wrong with the detection circuit
    }
  }
  
  else{}

  if (Serial.available()){
    char i = Serial.read();
    
    if (i == '0'){
      digitalWrite(2, LOW); 
      magnetServo.write(20);
      Serial.println("000"); //healthy
    }
    
    else if (i == '1'){
      digitalWrite(2, LOW); 
      magnetServo.write(30);
      Serial.println("000"); //healthy
    }
    
    else if (i == '2'){
      digitalWrite(2, HIGH); 
      magnetServo.write(40);
      Serial.println("000"); //healthy
    }
    
    else if (i == '3'){
      digitalWrite(2, HIGH); 
      magnetServo.write(60);
      Serial.println("000"); //healthy
    }
  
    else{
      Serial.println("002"); //Something is wrong with the RPi Communication
    }  
  }
  delay(50); 
}
