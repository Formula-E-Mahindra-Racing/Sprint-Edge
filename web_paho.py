from flask import Flask, render_template_string
from flask_socketio import SocketIO
import paho.mqtt.client as mqtt
import json

# Constantes para MQTT
MQTT_BROKER = "34.171.152.225"  # Substitua pelo endereço do seu broker
MQTT_TOPIC_POT = "/TEF/device010/attrs/p"  # Tópico do valor do potenciômetro
MQTT_TOPIC_DHT = "/TEF/device010/attrs/dht"  # Tópico do sensor DHT

# Inicializa o aplicativo Flask e o SocketIO
app = Flask(__name__)
socketio = SocketIO(app)

# Variáveis globais para armazenar os últimos valores
ultimo_valor_pot = None
ultima_temperatura = None
ultima_umidade = None

# Funções de callback do MQTT
def on_connect(client, userdata, flags, rc):
    print("Conectado com código de resultado " + str(rc))
    client.subscribe(MQTT_TOPIC_POT)
    client.subscribe(MQTT_TOPIC_DHT)

def on_message(client, userdata, msg):
    global ultimo_valor_pot, ultima_temperatura, ultima_umidade
    try:
        payload = msg.payload.decode('utf-8')
        
        # Verifica qual tópico recebeu a mensagem
        if msg.topic == MQTT_TOPIC_POT:
            ultimo_valor_pot = int(payload)
            socketio.emit('novo_dado_pot', {'valor': ultimo_valor_pot})
            print(f"Mensagem de potenciômetro recebida: {ultimo_valor_pot}")
        
        elif msg.topic == MQTT_TOPIC_DHT:
            data = payload.split('|')
            temp = data[0].split(':')[1]
            hum = data[1].split(':')[1]
            
            ultima_temperatura = float(temp)
            ultima_umidade = float(hum)
            
            socketio.emit('novo_dado_dht', {
                'temperatura': ultima_temperatura,
                'umidade': ultima_umidade
            })
            print(f"Mensagem de DHT recebida - Temperatura: {ultima_temperatura}, Umidade: {ultima_umidade}")
    
    except json.JSONDecodeError:
        print("Falha ao decodificar JSON")

# Configura o cliente MQTT e conecta
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(MQTT_BROKER, 1883, 60)
client.loop_start()  # Inicia o loop MQTT em uma thread separada

@app.route('/')
def index():
    return render_template_string('''
        <!DOCTYPE html>
        <html lang="pt-BR">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Visualizador de Dados do Sensor</title>
            <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
            <script src="https://code.jquery.com/jquery-3.5.1.min.js"></script>
            <script src="https://cdn.socket.io/4.0.0/socket.io.min.js"></script>
            <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
            <style>
                .chart-container {
                    display: flex;
                    justify-content: space-around;
                    align-items: center;
                    flex-wrap: wrap;
                }
                canvas {
                    max-width: 300px;
                    margin: 20px;
                }
                #valor-potenciometro, #valor-temperatura, #valor-umidade {
                    font-size: 18px;
                    font-weight: bold;
                    text-align: center;
                    margin-top: 10px;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h1 class="mt-5 text-center">Sensores</h1>
                <div class="chart-container">
                    <div class="text-center">
                        <h3>Velocidade</h3>
                        <canvas id="gaugePot" width="300" height="300"></canvas>
                        <div id="valor-potenciometro">Aguardando dados...</div>
                    </div>
                    <div class="text-center">
                        <h3>Temperatura</h3>
                        <canvas id="gaugeTemp" width="300" height="300"></canvas>
                        <div id="valor-temperatura">Aguardando dados...</div>
                    </div>
                    <div class="text-center">
                        <h3>Umidade</h3>
                        <canvas id="gaugeHum" width="300" height="300"></canvas>
                        <div id="valor-umidade">Aguardando dados...</div>
                    </div>
                </div>
            </div>

            <script>
                var ctxPot = document.getElementById('gaugePot').getContext('2d');
                var gaugeChartPot = new Chart(ctxPot, {
                    type: 'doughnut',
                    data: {
                        labels: ['Valor', 'Restante'],
                        datasets: [{
                            label: 'Valor do Potenciômetro',
                            data: [0, 400],
                            backgroundColor: ['#36A2EB', '#E0E0E0'],
                            borderWidth: 1,
                        }]
                    },
                    options: {
                        responsive: true,
                        cutoutPercentage: 70,
                        animation: {
                            animateRotate: true,
                        }
                    }
                });

                var ctxTemp = document.getElementById('gaugeTemp').getContext('2d');
                var gaugeChartTemp = new Chart(ctxTemp, {
                    type: 'doughnut',
                    data: {
                        labels: ['Temperatura', 'Restante'],
                        datasets: [{
                            label: 'Temperatura',
                            data: [-40, 80],
                            backgroundColor: ['#FF6384', '#E0E0E0'],
                            borderWidth: 1,
                        }]
                    },
                    options: {
                        responsive: true,
                        cutoutPercentage: 70,
                        animation: {
                            animateRotate: true,
                        }
                    }
                });

                var ctxHum = document.getElementById('gaugeHum').getContext('2d');
                var gaugeChartHum = new Chart(ctxHum, {
                    type: 'doughnut',
                    data: {
                        labels: ['Umidade', 'Restante'],
                        datasets: [{
                            label: 'Umidade',
                            data: [0, 100],
                            backgroundColor: ['#4BC0C0', '#E0E0E0'],
                            borderWidth: 1,
                        }]
                    },
                    options: {
                        responsive: true,
                        cutoutPercentage: 70,
                        animation: {
                            animateRotate: true,
                        }
                    }
                });

                $(document).ready(function() {
                    var socket = io.connect('http://' + document.domain + ':' + location.port);
                    
                    socket.on('novo_dado_pot', function(data) {
                        $('#valor-potenciometro').text('Velocidade: ' + data.valor + ' Km/h');
                        gaugeChartPot.data.datasets[0].data[0] = data.valor;
                        gaugeChartPot.data.datasets[0].data[1] = 400 - data.valor;
                        gaugeChartPot.update();
                    });
                    
                    socket.on('novo_dado_dht', function(data) {
                        $('#valor-temperatura').text('Temperatura: ' + data.temperatura + ' °C');
                        $('#valor-umidade').text('Umidade: ' + data.umidade + ' %');

                        gaugeChartTemp.data.datasets[0].data[0] = data.temperatura;
                        gaugeChartTemp.data.datasets[0].data[1] = 80 - data.temperatura;
                        gaugeChartTemp.update();

                        gaugeChartHum.data.datasets[0].data[0] = data.umidade;
                        gaugeChartHum.data.datasets[0].data[1] = 100 - data.umidade;
                        gaugeChartHum.update();
                    });
                });
            </script>
        </body>
        </html>
    ''')

if __name__ == '__main__':
    socketio.run(app, debug=True)
