#include <ESP8266WiFi.h>
#include <WiFiUdp.h>

#include <Wire.h>
#include <SPI.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BME280.h>

#define BME_SCK 13
#define BME_MISO 12
#define BME_MOSI 11
#define BME_CS 10

Adafruit_BME280 bme;

#include <DNSServer.h>
#include <ESP8266WebServer.h>
#include <WiFiManager.h>

unsigned int localPort = 8888;
char  ReplyBuffer[255] = "50";

const int TemperatureNumReadings = 120;
int TempTemperatureNumReadings = 0;
int TemperatureReadings[TemperatureNumReadings];
int TemperatureReadIndex = 0;
int TemperatureTotal = 0;
int TemperatureAverage = 0;

WiFiUDP Udp;

String ZoneNumber;
const char* ServerZoneChoice;
const char* TempZoneNumber = 0;

void setup() {
  Serial.begin(115200);
  bme.begin();

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

  Udp.begin(localPort);
}

void loop() {
  Udp.beginPacket("255.255.255.255", 8888);
  //--------------------------- DATA LOAD --------------------------------
  TemperatureTotal = TemperatureTotal - TemperatureReadings[TemperatureReadIndex];
  TemperatureReadings[TemperatureReadIndex] = ((((bme.readTemperature()) * 1.8) + 32));
  TemperatureTotal = TemperatureTotal + TemperatureReadings[TemperatureReadIndex];
  TemperatureReadIndex = TemperatureReadIndex + 1;
  if (TemperatureReadIndex >= TemperatureNumReadings) {
    TemperatureReadIndex = 0;
  }
  if (TempTemperatureNumReadings < TemperatureNumReadings) {
    TempTemperatureNumReadings++;
    TemperatureAverage = TemperatureTotal / TempTemperatureNumReadings;
  } else {
    TemperatureAverage = TemperatureTotal / TemperatureNumReadings;
  }
  //----------------------------------------------------------------------
  strcpy (ReplyBuffer, itoa(TemperatureAverage, ReplyBuffer, 10));
  Udp.write(ReplyBuffer);
  Udp.endPacket();
  delay(250);
}
