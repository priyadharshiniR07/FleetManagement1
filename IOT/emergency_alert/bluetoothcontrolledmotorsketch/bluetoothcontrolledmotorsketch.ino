#include <SoftwareSerial.h>
SoftwareSerial BT(0, 1); // RX, TX
char c;
int m1 = D2;
int m2 = D4;
int m3 = D5;
int m4 = D6;

void setup() {
  // put your setup code here, to run once:
pinMode(m1,OUTPUT);
pinMode(m2,OUTPUT);
pinMode(m3,OUTPUT);
pinMode(m4,OUTPUT);
Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
if (Serial.available()){
    c = Serial.read();
    Serial.println(c);

    if(c=='a')
    {
  digitalWrite(m1,HIGH);
  digitalWrite(m2,LOW);
  digitalWrite(m3,HIGH);
  digitalWrite(m4,LOW);

  Serial.println("ROBOT WILL BE FORWARD");
      delay(500);
    }
    if(c=='b')
    {
  digitalWrite(m1,LOW);
  digitalWrite(m2,HIGH);
  digitalWrite(m3,LOW);
  digitalWrite(m4,HIGH);

  Serial.println("ROBOT WILL BE BACKWARD");
      delay(500);
    }
    if(c=='c')
    {
  digitalWrite(m1,HIGH);
  digitalWrite(m2,LOW);
  digitalWrite(m3,LOW);
  digitalWrite(m4,LOW);

  Serial.println("ROBOT WILL BE RIGHT");
      delay(500);
    }
}
}
