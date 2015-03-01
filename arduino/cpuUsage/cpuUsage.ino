String inString = " ";
int cpuUsage;
int pwm = 0;
byte pin = 3;

void setup() {
  Serial.begin(9600);
  Serial.println("Initialisation...");
  pinMode(pin, OUTPUT);
}

void loop() {
  if (pwm < cpuUsage) {
    pwm++;
  }
  else if (pwm > cpuUsage) {
    pwm--;
  }
  analogWrite(pin, pwm);
  delay(30);
}

void serialEvent() {
	int inChar;
	while(Serial.available() > 0){
	    inChar = Serial.read();
	    if(isDigit(inChar)){
	        inString += (char)inChar;
	    }
	    if(inChar == '\n'){
	        cpuUsage = inString.toInt();
	        Serial.print(cpuUsage);
                cpuUsage = map(cpuUsage, 0, 100, 0, 255);
                Serial.print("  ");
                Serial.println(cpuUsage);
	        inString = " ";
	    }
	}
}
