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
  delay(rawValue * 10 / 2); 
  digitalWrite(bluePin, HIGH); 
  delay(1500); 
  digitalWrite(bluePin, LOW); 
  delay(rawValue * 10 / 2 + 250); 
 
 
 
  
}