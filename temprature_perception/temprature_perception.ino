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
  delay(1001); 
  int tempReading = analogRead(tempPin); 
  float temp = tempReading * 0.48828125; 
  Serial.println(temp); 
if (temp < 25) { 
  digitalWrite(redPin, LOW); 
  digitalWrite(greenPin, LOW); 
  digitalWrite(bluePin, HIGH); 
} else if (temp >= 25 && temp <= 44) { 
  digitalWrite(redPin, LOW); 
  digitalWrite(greenPin, HIGH); 
  digitalWrite(bluePin, LOW); 
} else { 
  digitalWrite(redPin, HIGH); 
  digitalWrite(greenPin, LOW); 
  digitalWrite(bluePin, LOW); 
  } 
}