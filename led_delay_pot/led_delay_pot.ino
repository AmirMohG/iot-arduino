// const int greenLED = 2; 
// const int yellowLED = 3; 
// const int redLED = 4; 
// const int tempSensor = A0; 
const int redPin = 9; 
const int greenPin = 10; 
const int bluePin = 11; 
const int tempPin = A0; 
void setup() { 
  pinMode(redPin, OUTPUT); 
  pinMode(greenPin, OUTPUT); 
  pinMode(bluePin, OUTPUT); 
  Serial.begin(9600); 
} 
 
 
 
void loop() { 
 
 
  int rawValue = analogRead(A2); 
  Serial.println(rawValue * 10); 
  delay(rawValue * 10 /2 + 250); 
   digitalWrite(bluePin, HIGH); 
  delay(rawValue * 10 /2 + 250); 
  digitalWrite(bluePin, LOW); 
 
 
 
  
}