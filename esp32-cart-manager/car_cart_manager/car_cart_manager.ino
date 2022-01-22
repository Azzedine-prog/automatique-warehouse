/*
  SimpleMQTTClient.ino
  The purpose of this exemple is to illustrate a simple handling of MQTT and Wifi connection.
  Once it connects successfully to a Wifi network and a MQTT broker, it subscribe to a topic and send a message to it.
  It will also send a message delayed 5 seconds later.
*/

#include "EspMQTTClient.h"
int liste_of_items[20];
int trigPin = 27;      // trig pin of HC-SR04
int echoPin = 14;     // Echo pin of HC-SR04

int revleft4 = 33;       //REVerse motion of Left motor
int fwdleft5 = 32;       //ForWarD motion of Left motor
int revright6 = 25;      //REVerse motion of Right motor
int fwdright7 = 26;      //ForWarD motion of Right motor
int step_;
long duration, distance;
void moveforward();
void movebackward();
void moveright();
void moveleft();
void stop_();
long distance_();
EspMQTTClient client(
  "HOME",
  "ButGoogle1",
  "192.168.1.111",  // MQTT Broker server ip
  "TestClient",     // Client name that uniquely identify your device
  1883              // The MQTT port, default to 1883. this line can be omitted
);
String received_from_raspberry,done_text,number_text;
int number = 0;
char Start,transmission_complete,start_collecting;
int i =0,done=0;
void setup()
{
  delay(random(500,2000));   // delay for random time
  //Serial.begin(9600);
  pinMode(revleft4, OUTPUT);      // set Motor pins as output
  pinMode(fwdleft5, OUTPUT);
  pinMode(revright6, OUTPUT);
  pinMode(fwdright7, OUTPUT);
  
  pinMode(trigPin, OUTPUT);         // set trig pin as output
  pinMode(echoPin, INPUT);          //set echo pin as input to capture reflected waves
  Serial.begin(115200);

  // Optional functionalities of EspMQTTClient
  client.enableDebuggingMessages(); // Enable debugging messages sent to serial output
  client.enableHTTPWebUpdater(); // Enable the web updater. User and password default to values of MQTTUsername and MQTTPassword. These can be overridded with enableHTTPWebUpdater("user", "password").
  client.enableOTA(); // Enable OTA (Over The Air) updates. Password defaults to MQTTPassword. Port is the default OTA port. Can be overridden with enableOTA("password", port).
  client.enableLastWillMessage("TestClient/lastwill", "I am going offline");  // You can activate the retain flag by setting the third parameter to true
  
}

// This function is called once everything is connected (Wifi and MQTT)
// WARNING : YOU MUST IMPLEMENT IT IF YOU USE EspMQTTClient
void onConnectionEstablished()
{
  // Subscribe to "mytopic/test" and display received message to Serial
  client.subscribe("from/done", [](const String & payload) {
    done_text = payload;
    done = done_text.toInt();
  });
  client.subscribe("from/raspberry", [](const String & payload) {
    number_text = payload;
    number = number_text.toInt();
  });
  // Subscribe to "mytopic/wildcardtest/#" and display received message to Serial
  /*client.subscribe("mytopic/wildcardtest/#", [](const String & topic, const String & payload) {
    Serial.println("(From wildcard) topic: " + topic + ", payload: " + payload);
  });*/

  // Publish a message to "mytopic/test"
  //client.publish("mytopic/test", "This is a message"); // You can activate the retain flag by setting the third parameter to true
  //for(int i = 0;i<45;i++){
  client.publish("esp/ismail", "lwafix");
  //client.subscribe("from/raspberry", onTestMessageReceived);
  //  delay(100);
  //}
  // Execute delayed instructions
  /*client.executeDelayed(1 * 1000, []() {
    client.publish("esp/ismail", "This is a message resent 1 second later");
  });*/
}
void onTestMessageReceived(const String& message) {

}

void loop()
{
  client.loop();
  movebackward();
  delay(2000);
  stop_();
  delay(2000);
}

void moveforward(){
    digitalWrite(fwdright7, LOW);      //movebackword         
    digitalWrite(revright6, HIGH);
    digitalWrite(fwdleft5, LOW);                                
    digitalWrite(revleft4, HIGH);
  }
void stop_(){
    digitalWrite(fwdright7, LOW);  //Stop                
    digitalWrite(revright6, LOW);
    digitalWrite(fwdleft5, LOW);                                
    digitalWrite(revleft4, LOW); 
  }
void movebackward(){
    digitalWrite(fwdright7, HIGH);      //moveforward        
    digitalWrite(revright6, LOW);
    digitalWrite(fwdleft5, HIGH);                                
    digitalWrite(revleft4, LOW);
  }
void moveright(){
    digitalWrite(fwdright7, LOW);      //moveright         
    digitalWrite(revright6, HIGH);
    digitalWrite(fwdleft5, LOW);                                
    digitalWrite(revleft4, LOW);
  }
void moveleft(){
    digitalWrite(fwdright7, LOW);      //moveleft       
    digitalWrite(revright6, HIGH);
    digitalWrite(fwdleft5, LOW);                                
    digitalWrite(revleft4, LOW);
  }
long distance_(){
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);   
  digitalWrite(trigPin, LOW);     // send waves for 10 us
  //delayMicroseconds(10);
  duration = pulseIn(echoPin, HIGH); // receive reflected waves
  distance = duration / 58.2;   // convert to distance
  delay(10);
//  if(distance > 500)
//    return distance_();
  return distance;
  }
void goforward(int x){
  while((distance_()-x )< 1){
    moveforward();
    Serial.print(x);
    }
  stop_();
  }
void gobackward(int x){
    while((distance_()-x)> 1){
    movebackward();
    Serial.print(x);
    }
  stop_();
  }
