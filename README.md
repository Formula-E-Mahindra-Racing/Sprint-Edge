# Sprint 2 - Edge Computing

## Integrantes 👋
<ul>
    <li>Gabriel Barros (RM556309)</li>  
    <li>João Marcelo Furtado Romero (RM555199)</li>
    <li>Kayky Silva Stiliano (RM555148)</li>
    <li>Pedro Henrique Bizzo de Santana (RM557263)</li>
    <li>Pedro Henrique Mendes (RM555332)</li>
</ul>
 
<img src="path" alt="print do circuito Arduino/printscreen Arduino circuit"/>

Link da simulação no <a href="path">Wokwi</a>

## Instruções
O Wokwi está com um bug onde se você da uma certa quantidade de zoom algumas funcionalidades não irão aparecer no display.

## Explicação do Projeto 📖
Este projeto consiste em dois componentes principais:
<ul>
    <li>`fiware_IOT.cc`: Código para um dispositivo IoT baseado em ESP32 que lê dados de sensores (como DHT e luminosidade), conecta-se a uma rede Wi-Fi e publica/recebe informações de um Broker MQTT.</li>
    <li>`web_paho.py`: Um servidor web em Flask que exibe os dados do dispositivo IoT em gráficos em tempo real, utilizando WebSockets para comunicação em tempo real e Paho MQTT para receber dados do dispositivo.</li>
</ul>
 
## Componentes 🛠️
<ul>
    <li>ESP32</li>
    <li>DHT11/22</li>
    <li>LDR</li>
    <li>Potenciomêtros</li>
</ul>
 
<br>
 
## Dependências 📦
<ul>
    <li>WiFi.h</li>
    <li>PubSubClient.h</li>
    <li>DHT.h</li>
</ul>
 
<br>

## Explicando o <a href="path">Código</a> 🧑‍💻
 
`fiware_IOT.cc`
Este código é responsável por conectar o dispositivo IoT à rede Wi-Fi e ao Broker MQTT para enviar e receber dados dos sensores e controlar o estado de saída do dispositivo (como o LED onboard).

<br>

Principais Funcionalidades:
<ul>
    <li>Wi-Fi: Conexão com a rede Wi-Fi utilizando o nome e senha configurados.</li>
    <li>MQTT: Publicação e assinatura em tópicos MQTT para enviar dados de sensores e receber comandos do broker.</li>
    <li>Tópicos utilizados:</li>
        <ul>
            <li>/TEF/device010/attrs: Publica o estado do dispositivo.</li>
            <li>/TEF/device010/attrs/p: Publica o valor da luminosidade (potenciômetro).</li>
            <li>/TEF/device010/attrs/dht: Publica dados do sensor DHT (temperatura e umidade).</li>
            <li>/TEF/device010/cmd: Recebe comandos para controlar o dispositivo (ex: ligar/desligar LED).</li>
        </ul>
    <li>DHT22: Leitura de temperatura e umidade usando o sensor DHT22.</li>
    <li>Luminosidade: Lê valores de luminosidade simulados e os publica no Broker MQTT.</li>
    <li>Callback MQTT: Executa ações com base em mensagens recebidas, como ligar/desligar o LED onboard.</li>
    <li>Gerenciamento de Conexões: Reconecta automaticamente ao Wi-Fi e ao Broker MQTT em caso de desconexão.</li>
</ul>












<center>Este projeto encontra sob a <a href="https://github.com/Formula-E-Mahindra-Racing/Sprint1-Edge/blob/main/LICENSE">MIT License.</a></center>
