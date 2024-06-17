#include <LiquidCrystal_I2C.h>
#include <DHT.h>

// Definições dos pinos dos sensores e componentes
#define DHTPIN 2
#define DHTTYPE DHT22
#define LDRPIN A0
#define POTPIN A1
#define TRIGPIN 7
#define ECHOPIN 6
#define BTN_NEXT 8
#define BTN_PREV 9

// Inicialização dos componentes
DHT dht(DHTPIN, DHTTYPE);
LiquidCrystal_I2C lcd(0x27, 16, 2);

// Variável para armazenar o estado atual da tela
int currentScreen = 0;
int numScreens = 4;

void setup() {
  // Inicialização da comunicação serial
  Serial.begin(9600);
  
  // Inicialização dos pinos
  pinMode(LDRPIN, INPUT);
  pinMode(POTPIN, INPUT);
  pinMode(TRIGPIN, OUTPUT);
  pinMode(ECHOPIN, INPUT);
  pinMode(BTN_NEXT, INPUT_PULLUP);
  pinMode(BTN_PREV, INPUT_PULLUP);

  // Inicialização do DHT
  dht.begin();
  
  // Inicialização do LCD
  lcd.init();
  lcd.backlight();
}

void loop() {
  // Verifica se os botões foram pressionados
  if (digitalRead(BTN_NEXT) == LOW) {
    currentScreen = (currentScreen + 1) % numScreens;
    delay(200); // Debounce
  }
  if (digitalRead(BTN_PREV) == LOW) {
    currentScreen = (currentScreen - 1 + numScreens) % numScreens;
    delay(200); // Debounce
  }

  // Leitura da temperatura e umidade do sensor DHT
  float temperature = dht.readTemperature();
  float humidity = dht.readHumidity();

  // Leitura da luminosidade do sensor LDR
  int ldrValue = analogRead(LDRPIN);

  // Leitura do valor do potenciômetro
  int potValue = map(analogRead(POTPIN), 0, 1023, 0, 320);

  // Leitura do sensor de proximidade
  long duration, distance;
  digitalWrite(TRIGPIN, LOW);
  delayMicroseconds(2);
  digitalWrite(TRIGPIN, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIGPIN, LOW);
  duration = pulseIn(ECHOPIN, HIGH);
  distance = (duration / 2) / 29.1;

  // Limpa a tela do LCD
  lcd.clear();

  // Exibe os dados no LCD com base na tela atual
  switch (currentScreen) {
    case 0:
      lcd.setCursor(0, 0);
      lcd.print("Temp: ");
      lcd.print(temperature);
      lcd.print("C");
      lcd.setCursor(0, 1);
      lcd.print("Hum: ");
      lcd.print(humidity);
      lcd.print("%");
      break;
    case 1:
      lcd.setCursor(0, 0);
      lcd.print("LDR: ");
      lcd.print(ldrValue);
      break;
    case 2:
      lcd.setCursor(0, 0);
      lcd.print("Vel: ");
      lcd.print(potValue);
      lcd.print(" Km/h");
      break;
    case 3:
      lcd.setCursor(0, 0);
      lcd.print("Dist: ");
      lcd.print(distance);
      lcd.print(" m");
      break;
  }

  // Exibição dos dados adicionais no Serial Monitor
  Serial.print("LDR: ");
  Serial.print(ldrValue);
  Serial.print(" | Vel: ");
  Serial.print(potValue);
  Serial.print(" Km/h | Dist: ");
  Serial.print(distance);
  Serial.print(" m");
  Serial.print(" | Temp: ");
  Serial.print(temperature);
  Serial.print("C | Hum: ");
  Serial.print(humidity);
  Serial.println("%");

  // Espera de 1 segundo antes da próxima leitura
  delay(1000);
}
