

/* Obstacle Avoiding Robot Using Ultrasonic Sensor and Arduino uno
 *  www.blackkeyhole.com
 */

int trigPin = 27;      // trig pin of HC-SR04
int echoPin = 14;     // Echo pin of HC-SR04

int revleft4 = 33;       //REVerse motion of Left motor
int fwdleft5 = 32;       //ForWarD motion of Left motor
int revright6 = 25;      //REVerse motion of Right motor
int fwdright7 = 26;      //ForWarD motion of Right motor

long duration, distance;
void moveforward();
void movebackward();
void moveright();
void moveleft();
void stop_();
void setup() {
  
  delay(random(500,2000));   // delay for random time
  Serial.begin(9600);
  pinMode(revleft4, OUTPUT);      // set Motor pins as output
  pinMode(fwdleft5, OUTPUT);
  pinMode(revright6, OUTPUT);
  pinMode(fwdright7, OUTPUT);
  
  pinMode(trigPin, OUTPUT);         // set trig pin as output
  pinMode(echoPin, INPUT);          //set echo pin as input to capture reflected waves
  //Serial.begin(115200);
  Serial.println("khdama");
}

void loop(){
  Serial.println("ha7na floop tani");
  movebackward();
  Serial.println("backward");
  delay(2000);
  moveforward();
  Serial.println("forward");
  //Serial.println(distance_());
//  go(30);
  delay(500);
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
  //if(distance > 500)
    //return distance_();
  return distance;
  }
void go(int x){
  while(distance_() < x){
    moveforward();
    }
  stop_();
  while(distance_() > x){
    movebackward();
    }
  stop_();
  }
