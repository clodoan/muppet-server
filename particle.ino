// Basic demo for accelerometer readings from Adafruit LIS3DH

#include <Wire.h>
#include <SPI.h>
#include <Adafruit_LIS3DH.h>
#include <Adafruit_Sensor.h>

#include <neopixel.h>
#include "Particle.h"
#include <time.h>

// Used for software SPI
#define LIS3DH_CLK 13
#define LIS3DH_MISO 12
#define LIS3DH_MOSI 11
// Used for hardware & software SPI
#define LIS3DH_CS 10

// IMPORTANT: Set pixel COUNT, PIN and TYPE
#define PIXEL_PIN D3
#define PIXEL_COUNT 32
#define PIXEL_TYPE WS2812B
#define BRIGHTNESS 250 // 0 - 255


Adafruit_LIS3DH lis = Adafruit_LIS3DH();
Adafruit_NeoPixel strip(PIXEL_COUNT, PIXEL_PIN, PIXEL_TYPE);

#if defined(ARDUINO_ARCH_SAMD)
   #define Serial SerialUSB
#endif

// servo
// Servo myservo;
// int pos = 0;

void setup(void) {
    strip.setBrightness(BRIGHTNESS);
    strip.begin();
    strip.show();

    // Particle.variable('bump', bump);
    // myservo.attach(D3);
    #ifndef ESP8266
        while (!Serial);     // will pause Zero, Leonardo, etc until serial console opens
    #endif

    Serial.begin(9600);
    Serial.println("LIS3DH test!");

    if (! lis.begin(0x18)) {   // change this to 0x19 for alternative i2c address
        Serial.println("Couldnt start");
        while (1);
    }
    Serial.println("LIS3DH found!");

    lis.setRange(LIS3DH_RANGE_4_G);   // 2, 4, 8 or 16 G!

    Serial.print("Range = "); Serial.print(2 << lis.getRange());
    Serial.println("G");

    Spark.function("led",moodToggle);
}


void colorAll(uint32_t c, uint8_t wait, uint8_t start, uint8_t end) {
  uint16_t i;

  for(i=start; i<=end; i++) {
    strip.setPixelColor(i, c);
  }
  strip.show();
  delay(wait);
}

void loop() {

//   bump = false;
  lis.read();      // get X Y and Z data at once
  // Then print out the raw data
  Serial.print("X:  "); Serial.print(lis.x);
  Serial.print("  \tY:  "); Serial.print(lis.y);
  Serial.print("  \tZ:  "); Serial.print(lis.z);

  /* Or....get a new sensor event, normalized */
  sensors_event_t event;
  lis.getEvent(&event);

  /* Display the results (acceleration is measured in m/s^2) */
//   Serial.print("\t\tX: "); Serial.print(event.acceleration.x);
//   Serial.print(" \tY: "); Serial.print(event.acceleration.y);
//   Serial.print(" \tZ: "); Serial.print(event.acceleration.z);
//   Serial.println(" m/s^2 ");

  Serial.println();
    if ((lis.y/1000) > 7) {
        // bump = true;
        Particle.publish ("bump", "ouch", PUBLIC);
    }

    if ((lis.y/1000) < -7) {
        // bump = true;
        Particle.publish ("bump", "ouch", PUBLIC);
    }

    if ((lis.z/1000) > 7) {
        // bump = true;
        Particle.publish ("bump", "ouch", PUBLIC);
    }

    if ((lis.z/1000) < -7) {
        // bump = true;
        Particle.publish ("bump", "ouch", PUBLIC);
    }

    if ((lis.x/1000) > 7) {
        // bump = true;
        Particle.publish ("bump", "ouch", PUBLIC);
    }

    if ((lis.x/1000) < -7) {
        // bump = true;
        Particle.publish ("bump", "ouch", PUBLIC);
    }
  delay(600);

}


int moodToggle(String command) {

    if (command=="2") {
        Particle.publish("mood", "2", PUBLIC);
        colorAll(strip.Color(255, 255, 0), 50, 0, 59);
        // pos = 180;
        // myservo.write(pos);
        return 2;
    }

    else if (command=="1") {
        Particle.publish("mood", "1", PUBLIC);
        colorAll(strip.Color(0, 0, 255), 50, 0, 59);
        // pos = 90;
        // myservo.write(pos);
        return 1;
    }

     else if (command=="0") {
        Particle.publish("mood", "0", PUBLIC);
        colorAll(strip.Color(255, 0, 127), 50, 0, 59);
        // pos = 0;
        // myservo.write(pos);
        return 0;
    }

    else {
        return -1;
    }
}
