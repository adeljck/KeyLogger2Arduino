#include <Keyboard.h>
#include <HID.h>
void setup() {
  Keyboard.begin();
  delay(1000);
{{ code }}
  delay(1000);
  Keyboard.end();
}
void loop() {
  Serial.println("Running......");
  delay(1000);
}