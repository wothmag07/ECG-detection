const float analogInPin = A0;

void setup() {
  // put your setup code here, to run once:
pinMode(10,INPUT);
pinMode(11,INPUT);
Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
float voltage;
if(digitalRead(11) == 1 || digitalRead(10) == 1)
{
}
else
{
  voltage = analogRead(analogInPin) ;
  String voltageToSend = String(voltage);
  Serial.println(voltageToSend);
  delay(0.01);
}
}
