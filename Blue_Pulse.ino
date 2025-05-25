#include <SoftwareSerial.h>
SoftwareSerial BT(10, 11); // RX, TX

bool modoDemo = true;

void setup() {
  Serial.begin(9600);
  BT.begin(9600);
}

void loop() {
  if (BT.available()) {
    String cmd = BT.readStringUntil('\n');
    cmd.trim();
    if (cmd == "DEMO") modoDemo = true;
    else if (cmd == "REAL") modoDemo = false;
  }

  int value;
  if (modoDemo) {
    float base = 512 + 30 * sin(millis() / 500.0);
    float ruido = random(-5, 6);
    value = constrain(base + ruido, 0, 1023);
  } else {
    value = analogRead(A0);
  }

  BT.println(value);
  delay(50);
}
