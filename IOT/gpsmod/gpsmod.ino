#include <SoftwareSerial.h>
#include <TinyGPS++.h>

// GPS module connected to Arduino pins 4 (RX) and 3 (TX)
SoftwareSerial gpsSerial(4, 3); // RX, TX
TinyGPSPlus gps;

void setup() {
  Serial.begin(9600);       // Serial Monitor
  gpsSerial.begin(9600);    // GPS module baud rate
  Serial.println("GPS Module Initialized");
}

void loop() {
  while (gpsSerial.available() > 0) {
    gps.encode(gpsSerial.read());

    if (gps.location.isUpdated()) {
      Serial.print("Latitude: ");
      Serial.println(gps.location.lat(), 6);
      Serial.print("Longitude: ");
      Serial.println(gps.location.lng(), 6);
    }
  }
}
