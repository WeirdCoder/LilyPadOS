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
  int val = None;
  if (val == None || val != digitalRead(3)){
    val = digitalRead(3); 
    
    if (val == HIGH){
      Serial.write("ON");
      Serial.println("000"); //healthy
    }
  
    else if (val == LOW){
      Serial.write("OFF");
      Serial.println("000"); //healthy
    }
  
    else{
      Serial.println("003"); //Something is wrong with the detection circuit
    }
  }
  
  else{}

  if (Serial.available()){
    int i = Serial.read();
    
    if (i == "00"){
      digitalWrite(2, LOW); 
      magnetServo.write(1);
      Serial.println("000"); //healthy
    }
    
    else if (i == "01"){
      digitalWrite(2, LOW); 
      magnetServo.write(90);
      Serial.println("000"); //healthy
    }
    
    else if (i == "10"){
      digitalWrite(2, HIGH); 
      magnetServo.write(1);
      Serial.println("000"); //healthy
    }
    
    else if (i == "11"){
      digitalWrite(2, HIGH); 
      magnetServo.write(HIGH);
      Serial.println("000"); //healthy
    }
  
    else{
      Serial.println("002"); //Something is wrong with the RPi Communication
    }  
  }
  delay(50); 
}
