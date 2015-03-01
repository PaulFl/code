int input;
unsigned long int time;
boolean state = false;

void setup() {
  Serial.begin(9600);
  Serial.println("Initialisation...");
  pinMode(13, OUTPUT);
  time = millis();
}

void loop() {
  if ((millis() - time) > 500) {
    time = millis();
    state = !state;
    digitalWrite(13, state);
    Serial.println(state);
  }
}

void serialEvent() {
  input = Serial.readStringUntil('\n').toInt();
  while(Serial.available()) {
    Serial.read();
  }
  Serial.print("Input: ");
  Serial.println(input);
}
  
  
