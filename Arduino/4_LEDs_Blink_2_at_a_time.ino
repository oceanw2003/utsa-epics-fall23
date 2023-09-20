
int led_pin1 = 13;
int led_pin2 = 13;
int led_pin3 = 13;
int led_pin4 = 13;
 int blink_duration1 = 1000;

 void setup()  {}

void loop() {
 

  digitalWrite (13,HIGH);
  delay (blink_duration1);
  pinMode (13, led_pin1);
  digitalWrite (13,LOW);
  delay (blink_duration1);

}