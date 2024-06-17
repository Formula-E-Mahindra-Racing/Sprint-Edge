# Sprint 1 - Edge Computing

## Integrantes 👋
<ul>
    <li>Gabriel Barros (RM556309)</li>  
    <li>João Marcelo Furtado Romero (RM555199)</li>
    <li>Kayky Silva Stiliano (RM555148)</li>
    <li>Pedro Henrique Bizzo de Santana (RM557263)</li>
    <li>Pedro Henrique Mendes (RM555332)</li>
</ul>
 
<img src="https://github.com/Formula-E-Mahindra-Racing/Sprint1-Edge/blob/main/arduino-sketch.png" alt="print do circuito Arduino/printscreen Arduino circuit"/>

Link da simulação no <a href="https://wokwi.com/projects/400451221044858881">Wokwi</a>

## Instruções
O Wokwi está com um bug onde se você da uma certa quantidade de zoom algumas funcionalidades não irão aparecer no display.

## Explicação do Projeto 📖
Este projeto é um sistema de monitoramento ambiental para a Fórmula E que utiliza um microcontrolador Arduino para ler dados de vários sensores e exibi-los em um display LCD e também no Monitor Serial do computador. Os componentes principais incluem:
<br>
- Sensor de Temperatura e Umidade (DHT22): Este sensor é usado para medir a temperatura e a umidade do ambiente.
- Sensor de Luminosidade (LDR): Este sensor mede a intensidade da luz ambiente.
- Potenciômetro: Este componente é usado para simular uma entrada de velocidade.
- Sensor de Proximidade Ultrassônico: Utilizado para medir a distância até um objeto próximo.
- Display LCD com Interface I2C: Um display de cristal líquido usado para exibir os dados coletados pelos sensores.
- Botões de Controle: São utilizados dois botões para navegar entre as diferentes telas de exibição no display LCD.
<br>
O funcionamento do sistema é o seguinte:
<ul>
    <li>O código no Arduino é responsável por inicializar os componentes, ler os valores dos sensores em intervalos regulares e exibir esses valores no display LCD.</li>
    <li>O usuário pode navegar entre diferentes telas de informações usando os botões de controle, permitindo a visualização dos dados de temperatura/umidade, luminosidade, velocidade simulada e distância medida.</li>
    <li>Além da exibição no display LCD, os valores lidos pelos sensores também são enviados para o Monitor Serial do computador, proporcionando uma forma alternativa de visualização e monitoramento.</li>
</ul>
<br>
 
## Componentes 🛠️
<ul>
    <li>1x Placa Arduino Uno</li>
    <li>1x Breadboard</li>
    <li>1x Potenciômetro</li>
    <li>1x DHT11/22</li>
    <li>1x Buzzer</li>
    <li>1x Display LCD</li>
    <li>1x LDR</li>
    <li>2x Botões</li>
    <li>1x Sensor de proximidade (HC-SR04)</li>
</ul>
 
<br>
 
## Dependências 📦
<ul>
    <li>LiquidCrystal_I2C</li>
    <li>DHT Sensor library</li>
</ul>
 
<br>

## Explicando o <a href="https://github.com/Formula-E-Mahindra-Racing/Sprint1-Edge/blob/main/arduino-code.cc">Código</a> 🧑‍💻
 
Precisamos incluir as bibliotecas para podermos ter acesso a métodos dos quais vamos precisar.
 
Assim como também é preciso declarar, iniciando tais valores para podermos usá-los depois na aplicação.
 
```c
#define DHTPIN 2
#define DHTTYPE DHT22
#define LDRPIN A0
#define POTPIN A1
#define TRIGPIN 7
#define ECHOPIN 6
#define BTN_NEXT 8
#define BTN_PREV 9
```
<hr>

Estas linhas definem os pinos utilizados para conectar os diversos componentes ao microcontrolador. Os sensores e componentes incluem o sensor DHT, o sensor de luminosidade (LDR), um potenciômetro, um sensor de proximidade (usando o ultrassônico), e os botões de controle (próximo e anterior).

```c
DHT dht(DHTPIN, DHTTYPE);
LiquidCrystal_I2C lcd(0x27, 16, 2);
```
<hr>

Aqui são criadas instâncias dos objetos para interagir com os componentes. Um objeto dht é criado para interagir com o sensor DHT utilizando os pinos definidos anteriormente, e outro objeto lcd é criado para interagir com o display LCD utilizando a interface I2C.

```c
int currentScreen = 0;
int numScreens = 4;
```
<hr>

São definidas duas variáveis inteiras. currentScreen armazena o índice da tela atual que está sendo exibida no LCD, e numScreens define o número total de telas disponíveis.

 ## Funções 🛠️
```c
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
```
<hr>

No método setup(), a comunicação serial é iniciada a uma taxa de 9600 bauds. Os pinos são configurados conforme definido anteriormente: LDRPIN e POTPIN como entradas analógicas, TRIGPIN como saída digital, e ECHOPIN, BTN_NEXT e BTN_PREV como entradas digitais com resistores de pull-up internos. Em seguida, o sensor DHT é inicializado e o display LCD é inicializado e a luz de fundo é ligada.

```c
void loop() {
  if (digitalRead(BTN_NEXT) == LOW) {
    currentScreen = (currentScreen + 1) % numScreens;
    delay(200); // Debounce
  }
  if (digitalRead(BTN_PREV) == LOW) {
    currentScreen = (currentScreen - 1 + numScreens) % numScreens;
    delay(200); // Debounce
  }
```
<hr>

No loop principal (loop()), os botões são verificados. Se o botão "Próximo" for pressionado, currentScreen é incrementado para avançar para a próxima tela (e retorna para a primeira tela se estiver na última). O mesmo é feito para o botão "Anterior", exceto que currentScreen é decrementado.

```c
float temperature = dht.readTemperature();
float humidity = dht.readHumidity();
int ldrValue = analogRead(LDRPIN);
int potValue = map(analogRead(POTPIN), 0, 1023, 0, 320);
```
<hr>

Os valores dos sensores são lidos. Para o sensor DHT, são lidos os valores de temperatura e umidade. Para o LDR, é feita uma leitura analógica da luminosidade. Para o potenciômetro, é feita uma leitura analógica e mapeada para um intervalo de 0 a 320, representando uma faixa de velocidade em km/h.

```c
long duration, distance;
digitalWrite(TRIGPIN, LOW);
delayMicroseconds(2);
digitalWrite(TRIGPIN, HIGH);
delayMicroseconds(10);
digitalWrite(TRIGPIN, LOW);
duration = pulseIn(ECHOPIN, HIGH);
distance = (duration / 2) / 29.1;
```
<hr>

Para o sensor de proximidade, é enviado um pulso ultrassônico através do pino de gatilho (TRIGPIN), e a duração do pulso de retorno é medida pelo pino de eco (ECHOPIN). Essa duração é convertida em distância em centímetros e armazenada na variável distance.

```c
lcd.clear();

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
```
<hr>

O display LCD é limpo e, dependendo do valor de currentScreen, diferentes informações são exibidas. Cada case do switch corresponde a uma tela diferente, temperatura e umidade, luminosidade, velocidade e distância respectivamente.

```c
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

delay(1000);
```
<hr>

As informações lidas dos sensores são exibidas no Monitor Serial. Há um atraso de 1 segundo antes de iniciar a próxima iteração do loop. Isso controla a taxa de atualização das leituras dos sensores e a exibição nos displays.
<br>

A função `loop()` que retorna void, servirá como o ciclo de vida inteiro do projeto, é uma função que por padrão roda infinitamente até algo dentro ou fora do código pará-lo.
Aqui, vamos chamar nossas funções principais já declaradas para termos uma melhor leitura e manutenção do código.
<hr>

<center>Este projeto encontra sob a <a href="path">MIT License.</a></center>
