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
<br>
- O código no Arduino é responsável por inicializar os componentes, ler os valores dos sensores em intervalos regulares e exibir esses valores no display LCD.
- O usuário pode navegar entre diferentes telas de informações usando os botões de controle, permitindo a visualização dos dados de temperatura/umidade, luminosidade, velocidade simulada e distância medida.
- Além da exibição no display LCD, os valores lidos pelos sensores também são enviados para o Monitor Serial do computador, proporcionando uma forma alternativa de visualização e monitoramento.
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
    <li>LiquidCrystal</li>
    <li>DHT Sensor library</li>
</ul>
 
<br>

## Explicando o <a href="path">Código</a> 🧑‍💻
 
Precisamos incluir as bibliotecas para podermos ter acesso a métodos dos quais vamos precisar.
 
Assim como também é preciso declarar, iniciando tais valores para podermos usá-los depois na aplicação.
 
```c

```
<hr>

 ## Funções 🛠️


<hr>

A função `loop()` que retorna void, servirá como o ciclo de vida inteiro do projeto, é uma função que por padrão roda infinitamente até algo dentro ou fora do código pará-lo.
Aqui, vamos chamar nossas funções principais já declaradas para termos uma melhor leitura e manutenção do código.

<hr>
 
<center>Este projeto encontra sob a <a href="path">MIT License.</a></center>
