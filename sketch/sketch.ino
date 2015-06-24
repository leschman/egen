#include <Servo.h>

Servo servo; //create servo object.

int pos = 0;             // Postion of Servo.
boolean countUp = true;  // track if pos is going up or down.
int delayCount = 0;
const int delayClosed = 333;//delay at pos 0, (~5 seconds)
const int delayOpen = 0;//delay when open


int firstSensor = 0;    // first analog sensor
int secondSensor = 0;   // second analog sensor
int thirdSensor = 0;    // digital sensor
int inByte = 0;         // incoming serial byte
int voltage = 0;

void setup()
{
  // start serial port at 9600 bps:
  Serial.begin(9600);
  pinMode(3, OUTPUT);   // set pin 3 to supply voltage. 
  digitalWrite(3, HIGH); // put voltage on the pin.
  pinMode(A3, INPUT);   // analog read on pin A3.
  
  servo.attach(8); //attach the servo to pin 8.

  
  establishContact();  // send a byte to establish contact until receiver responds 
}

void loop()
{
 
  if (Serial.available() > 0) {
    
    //collect and send the voltage data.
    voltage = analogRead(A3);
    Serial.println(voltage, BIN);

    
    //servo control. 
    servo.write(pos);
  
    if(countUp){                    // if pos should move up.
      if(delayCount >= delayClosed){  // and the 
        pos++;
        if(pos >= 85){
          countUp = false;
          delayCount = 0;
        }
      }
    }else{  
      if(delayCount >= delayOpen){
        pos--;
        if(pos <=0){
          countUp = true;
          delayCount = 0;
        }
      }
    }
    
    // delay 15ms for servo to move,
    // a delay of 10ms was needed to let the ADC recover.
    delayCount++;
    delay(15);
                   
 }
}
void establishContact() {
  while (Serial.available() <= 0) {
    Serial.print('A');   // send a capital A
    delay(300);
  }
}

