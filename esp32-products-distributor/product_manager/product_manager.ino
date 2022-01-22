#include <ESP32_Servo.h>
#include "EspMQTTClient.h"
Servo servo1,servo2; 
char servo1_pin = 12,servo2_pin = 14;
char prev_ang;
EspMQTTClient client(
  "HOME",
  "ButGoogle1",
  "192.168.1.111",  // MQTT Broker server ip
  "TestClient",     // Client name that uniquely identify your device
  1883              // The MQTT port, default to 1883. this line can be omitted
);
int max_angle = 120;
String received_from_raspberry;
char Start,transmission_complete,start_collecting;
int number = 0;
void setup() {
   delay(random(500,2000));   // delay for random time
  // put your setup code here, to run once:
servo1.attach(servo1_pin);
servo2.attach(servo2_pin);
servo2.write(0);
servo1.write(0);
Serial.begin(115200);
  // Optional functionalities of EspMQTTClient
  client.enableDebuggingMessages(); // Enable debugging messages sent to serial output
  client.enableHTTPWebUpdater(); // Enable the web updater. User and password default to values of MQTTUsername and MQTTPassword. These can be overridded with enableHTTPWebUpdater("user", "password").
  client.enableOTA(); // Enable OTA (Over The Air) updates. Password defaults to MQTTPassword. Port is the default OTA port. Can be overridden with enableOTA("password", port).
  client.enableLastWillMessage("TestClient/lastwill", "I am going offline servo");  // You can activate the retain flag by setting the third parameter to true
  Serial.println("from setup");
}
// This function is called once everything is connected (Wifi and MQTT)
// WARNING : YOU MUST IMPLEMENT IT IF YOU USE EspMQTTClient
void onConnectionEstablished()
{
  /*// Subscribe to "mytopic/test" and display received message to Serial
  client.subscribe("mytopic/test", [](const String & payload) {
    Serial.println(payload);
  });*/

  // Subscribe to "mytopic/wildcardtest/#" and display received message to Serial
  client.subscribe("from/product", [](const String & topic, const String & message) {
    Serial.println("message received: " + message);
  received_from_raspberry = message;
  number = received_from_raspberry.toInt();
  if(Start == 1 && received_from_raspberry != "" && received_from_raspberry != "875"){
    Serial.println("second step");
    number = received_from_raspberry.toInt();
    //Serial.println(received_from_raspberry);
    //Serial.println(number);
    }
  });

  // Publish a message to "mytopic/test"
  //client.publish("mytopic/test", "This is a message"); // You can activate the retain flag by setting the third parameter to true
  //for(int i = 0;i<45;i++){
  client.publish("esp/ismail", "lwafix servo");
  client.subscribe("from/product", onTestMessageReceived);
  //  delay(100);
  //}
  // Execute delayed instructions
  /*client.executeDelayed(1 * 1000, []() {
    client.publish("esp/ismail", "This is a message resent 1 second later");
  });*/
}
void onTestMessageReceived(const String& message) {
  
}
void loop() {
  client.loop();
  // put your main code here, to run repeatedly:
 //Serial.println(number);
  if(number ==1){
    int i;
    for(i=0;i<max_angle;i++){
    servo1.write(i);
    Serial.println(i);
    delay(10);
      }
    delay(5000);
    for(i=max_angle;i>0;i--){
    servo1.write(i);
    Serial.println(i);
    delay(10);
      }
    number=0;
    client.publish("from/done", "1");
    }
  if(number ==2){
    int i;
    number=0;
    for(i=0;i<max_angle;i++){
    servo2.write(i);
    Serial.println(i);
    delay(10);
      }
    delay(5000);
    for(i=max_angle;i>0;i--){
    servo2.write(i);
    Serial.println(i);
    delay(10);
      }
      client.publish("from/done", "1");
    }
  
}
//void set_angle1(char angle){
//  Serial.println(angle);
//  int i=0;
//  if(prev_ang<=angle){
//for(i=prev_ang;i<angle;i++){
//servo1.write(i);
//Serial.println(i);
//delay(10);
//}
//  }
//  else if(prev_ang>angle){
//for(i=angle;i<prev_ang;i++){
//servo1.write(i);
//Serial.println(i);
//delay(10);
//}
//  }
//else if(angle == 0){
//  set_angle1(1);
//  servo1.write(0);
//  }
//prev_ang = angle;
//delay(5);
//}
//void set_angle2(char angle){
//  Serial.println(angle);
//  int i=0;
//  if(prev_ang<=angle){
//for(i=prev_ang;i<angle;i++){
//servo2.write(i);
//Serial.println(i);
//delay(10);
//}
//  }
//  else if(prev_ang>angle){
//for(i=angle;i<prev_ang;i++){
//servo2.write(i);
//Serial.println(i);
//delay(10);
//}
//  }
//else if(angle == 0){
//  set_angle2(1);
//  servo2.write(0);
//  }
//prev_ang = angle;
//delay(5);
//}
