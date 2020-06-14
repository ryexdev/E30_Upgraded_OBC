#include <ESP8266WiFi.h>
#include <WiFiUdp.h>
#include <Wire.h>
#include "OLED.h"

#include <DNSServer.h>
#include <ESP8266WebServer.h>
#include <WiFiManager.h>

OLED display(D4, D5);

unsigned int localPort = 8888;
char  ReplyBuffer[255] = "50";

WiFiUDP Udp;

void setup() {
  pinMode(D2, OUTPUT);
  digitalWrite(D2, LOW);
  delay(50);
  digitalWrite(D2, HIGH);
  display.begin();
  display.print("Connecting");

  WiFiManager wifiManager;
  wifiManager.setTimeout(180);
  if (!wifiManager.autoConnect("AutoConnectAP")) {
    delay(3000);
    ESP.reset();
    delay(5000);
  }
  display.print("Connected!");
  Udp.begin(localPort);
}

void loop() {
  Udp.beginPacket("255.255.255.255", 8888);
  Udp.write(ReplyBuffer);
  Udp.endPacket();
  strcpy (ReplyBuffer, "75");
  delay(250);
  Udp.beginPacket("255.255.255.255", 8888);
  Udp.write(ReplyBuffer);
  Udp.endPacket();
  strcpy (ReplyBuffer, "25");
  delay(250);
}
