#include <SoftwareSerial.h>
SoftwareSerial Sim800(2,3);
float temp_sen_pin = A0;
float temperature = 0;
void setup()
{
  Sim800.begin(9600);               // the GPRS baud rate   
  Serial.begin(9600);    
}
 
void loop()
{
      temperature = analogRead(temp_sen_pin);
      temperature = temperature * (5.0 / 1024.0);
      temperature = temperature * 100;
      Serial.print("Temperature = ");
      Serial.print(temperature);
      Serial.println("°C");
      delay(100);     
      
  if (Sim800.available())
    Serial.write(Sim800.read());
 
  Sim800.println("AT");
  delay(1000);
 
  Sim800.println("AT+CPIN?");
  delay(1000);
 
  Sim800.println("AT+CREG?");
  delay(1000);
 
  Sim800.println("AT+CGATT?");
  delay(1000);
 
  Sim800.println("AT+CIPSHUT");
  delay(1000);
 
  Sim800.println("AT+CIPSTATUS");
  delay(1000);
 
  Sim800.println("AT+CIPMUX=0");
  delay(1000);
  Display_feedback();
 
  Sim800.println("AT+CSTT=\"mtnirancell\"");//start task and setting the APN,
  delay(1000);
 
  Display_feedback();
  Sim800.println("AT+CIICR");//bring up wireless connection
  delay(1000);

  Display_feedback();
 
  Sim800.println("AT+CIFSR");//get local IP adress
  delay(1000);

  Display_feedback();
 
  Sim800.println("AT+CIPSPRT=0");
  delay(1000);

  Display_feedback();
  
  Sim800.println("AT+CIPSTART=\"TCP\",\"api.thingspeak.com\",\"80\"");//start up the connection
  delay(2000);

  Display_feedback();

  Sim800.println("AT+CIPSEND");//begin send data to remote server
  delay(1000);
  
  Display_feedback();
  String str="GET https://api.thingspeak.com/update?api_key=4LMSMLNCOF9WMUEK&field1=" + String(temperature);
  // String str="GET https://bpms.rso-co.ir/aaaaaaaaaaaaaaaaaaaaa" + String(temperature);


  Serial.println(str);
  Sim800.println(str);//begin send data to remote server
  
  delay(1000);
   
  Display_feedback();
 
  Sim800.println((char)26);//sending
  delay(2000);//waitting for reply, important! the time is base on the condition of internet 
  Sim800.println();
 
  Display_feedback();
 
  Sim800.println("AT+CIPSHUT");//close the connection
  delay(100);
  
  Display_feedback();
} 
void Display_feedback()
{
  while(Sim800.available()!=0)
  Serial.write(Sim800.read());
  delay(2000); 
  
}
