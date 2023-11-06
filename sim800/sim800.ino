#include <SoftwareSerial.h>

SoftwareSerial sim800l(2, 3);  // RX, TX

void setup() {
  Serial.begin(9600);
  sim800l.begin(9600);
  // sim800l.println("AT");

}

void loop() {
  delay(1000);
  String response = "";
  char c = sim800l.read();
  response += c;
  Serial.println(response);

}

