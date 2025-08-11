const int trigPin = 9;
const int echoPin = 8;
const int tankHeight = 30; // in cm (change to your tank's actual height)

void setup() {
  Serial.begin(9600);
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
}

void loop() {
  long duration;
  float distance, fuelLevel, fuelPercentage;

  // Trigger the sensor
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  // Measure echo duration
  duration = pulseIn(echoPin, HIGH);
  distance = duration * 0.034 / 2; // cm

  // Calculate fuel level (from bottom)
  fuelLevel = tankHeight - distance;
  if (fuelLevel < 0) fuelLevel = 0;
  if (fuelLevel > tankHeight) fuelLevel = tankHeight;

  // Calculate fuel percentage
  fuelPercentage = (fuelLevel / tankHeight) * 100;

  // Print results
  Serial.print("Fuel Level: ");
  Serial.print(fuelLevel);
  Serial.print(" cm | ");
  Serial.print("Fuel Percentage: ");
  Serial.print(fuelPercentage);
  Serial.println(" %");

  delay(1000); // Update every second
}
