void setup() {

 
  Serial.begin(9600);
  pinMode(LED_BUILTIN, OUTPUT);
 

}

void loop() {

 String message = Serial.readStringUntil('\n');

 if (message == "ON")
 {
  digitalWrite(LED_BUILTIN, HIGH);
  
 }
 if (message == "OFF")
 {
  digitalWrite(LED_BUILTIN, LOW);
 }
 
 /*digitalWrite(LED_BUILTIN, HIGH); //turn the led on (high is the voltage level)
 delay(500);                      
 digitalWrite(LED_BUILTIN, LOW);  // turns the led off (low voltage causes it to go off)
 delay(500);*/

 
}
