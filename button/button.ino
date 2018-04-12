#define B_IN 2

#define ZzZz 7

void setup(){
  Serial.begin(9600);
  pinMode(B_IN, INPUT);
}



void loop(){
  int b;
  char c;
  //read pot voltages
  b = !digitalRead(B_IN);
  
  if(Serial.available()>0){
    c = Serial.read();
    if (c == 'p')
      Serial.println(b);
  }
}
