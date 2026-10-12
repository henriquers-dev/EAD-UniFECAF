#include <Arduino.h>

// Colocar a declaração de funções:
const char* VERSION = "1.0.0";

void setup() {
    Serial.begin(115200);
    delay(1000);

    Serial.println("Firmware ORIGINAL de laboratorio");
    Serial.print("Versao: ");
    Serial.println(VERSION);
}

void loop() {
    delay(5000);
}
