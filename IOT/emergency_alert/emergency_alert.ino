#include <Wire.h>
#include <MPU6050.h>

MPU6050 mpu;

void setup() {
  Serial.begin(9600);
  Wire.begin();
  
  Serial.println("Initializing MPU6050...");
  mpu.initialize();

  if (mpu.testConnection()) {
    Serial.println("MPU6050 connected successfully.");
  } else {
    Serial.println("MPU6050 connection failed.");
    while (1);
  }
}

void loop() {
  int16_t ax, ay, az;
  int16_t gx, gy, gz;

  // Get raw accelerometer and gyroscope data
  mpu.getMotion6(&ax, &ay, &az, &gx, &gy, &gz);

  Serial.print("Accel X: "); Serial.print(ax);
  Serial.print(" | Y: "); Serial.print(ay);
  Serial.print(" | Z: "); Serial.print(az);
  Serial.print(" || Gyro X: "); Serial.print(gx);
  Serial.print(" | Y: "); Serial.print(gy);
  Serial.print(" | Z: "); Serial.println(gz);

  // Detect crash/movement threshold (adjust as needed)
  if (abs(ax) > 15000 || abs(ay) > 15000 || abs(az) > 20000) {
    Serial.println("⚠️ Emergency Alert: Sudden Movement Detected!");
    // You can trigger a buzzer or send signal here
  }

  delay(500);
}
