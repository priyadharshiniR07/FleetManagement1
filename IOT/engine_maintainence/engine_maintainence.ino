// Pin Definitions
const int vibrationPin = 2;     // SW-420 Digital Output
const int tempPin = A0;         // LM35 Analog Output
const int gasPin = A1;          // MQ Gas Sensor Analog Output

void setup() {
  Serial.begin(9600);
  pinMode(vibrationPin, INPUT);
  Serial.println("Engine Maintenance Module Started");
}

void loop() {
  // Vibration
  int vibrationStatus = digitalRead(vibrationPin);
  if (vibrationStatus == LOW) {
    Serial.println("Vibration Detected!");
  } else {
    Serial.println("No Vibration.");
  }

  // Temperature (LM35: 10mV/°C, Analog read: 0-1023 → 0-5V)
  int tempReading = analogRead(tempPin);
  float voltage = tempReading * (5.0 / 1023.0);
  float temperatureC = voltage * 100; // LM35 output: 10mV per degree
  Serial.print("Temperature: ");
  Serial.print(temperatureC);
  Serial.println(" °C");

  // Gas Level (MQ Sensor)
  int gasLevel = analogRead(gasPin);
  Serial.print("Gas Sensor Value: ");
  Serial.println(gasLevel);

  Serial.println("-----------------------------");
  delay(1000);  // 1 second delay
}
