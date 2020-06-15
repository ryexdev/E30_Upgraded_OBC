#include <ESP8266WiFi.h>
#include <WiFiUdp.h>

#include <Wire.h>
#include <SPI.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BME280.h>

#include "OLED.h"

#include <DNSServer.h>
#include <ESP8266WebServer.h>
#include <WiFiManager.h>

OLED display(D4, D5);

unsigned int localPort = 8888;
char  ReplyBuffer[255] = "50";

WiFiUDP Udp;

String ZoneNumber;
const char* ServerZoneChoice;
const char* TempZoneNumber = 0;

void setup() {
  Serial.begin(115200);
  pinMode(D2, OUTPUT);
  digitalWrite(D2, LOW);
  delay(50);
  digitalWrite(D2, HIGH);
  display.begin();
  display.print("Connecting");
  WiFiManager wifiManager;
  wifiManager.setTimeout(180);
  WiFiManagerParameter custom_text_Setup2("Sensor Number");
  WiFiManagerParameter custom_Zone_Number("ZoneNumber", "Sensor Number (1,2,3,4...)", ServerZoneChoice, 40);
  wifiManager.addParameter(&custom_text_Setup2);
  wifiManager.addParameter(&custom_Zone_Number);
  TempZoneNumber = custom_Zone_Number.getValue();
  for (int Size = 0; TempZoneNumber[Size] != '\0'; Size++) {
    ZoneNumber = ZoneNumber + TempZoneNumber[Size];
  }
  if (!wifiManager.autoConnect("AutoConnectAP")) {
    delay(3000);
    ESP.reset();
    delay(5000);
  }
  display.print("Connected!");
  Udp.begin(localPort);
}

void loop() {
  int x = 1;
  for (int i = 0; i > -1; i = i + x) {
    Udp.beginPacket("255.255.255.255", 8888);
    if (i == 100)
      x = -1;
    strcpy (ReplyBuffer, itoa( i, ReplyBuffer, 10 ));
    Udp.write(ReplyBuffer);
    Udp.endPacket();
    delay(250);
  }
}
