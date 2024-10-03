# Node-RED - Monitoramento e Controle via OPC UA, MQTT e Azure IoT Hub

Este módulo do projeto utiliza o **Node-RED** para monitorar e controlar dispositivos em um ambiente industrial. O fluxo conecta-se a um servidor **OPC UA** para leitura de dados em tempo real e publica alertas e relatórios para o **AWS IoT** via **MQTT**. Além disso, os dados de produção são enviados para o **Azure IoT Hub**. O fluxo também inclui um painel de monitoramento com indicadores de desempenho e controle.

## Estrutura do Fluxo

O fluxo do **Node-RED** é dividido em várias funções principais para leitura, controle e publicação de dados.

### 1. **Leitura de Dados via OPC UA**

Os nós **OpcUa-Client** e **OpcUa-Item** conectam-se ao servidor **OPC UA** (como o configurado no **CODESYS**) para ler dados em tempo real. As variáveis monitoradas incluem:

- **Corrente M1 e M2**: Medidas da corrente elétrica dos motores.
- **Rotação M1 e M2 (RPM)**: Medidas das rotações por minuto dos motores.
- **Tempo de Operação**: Medidas em segundos, minutos e horas de operação do sistema.
- **Quantidade de Produtos (Caixas)**: Quantidade de caixas ou produtos que passaram pelo sistema.
- **Estado dos Motores (Alerta M1)**: Indica o status do motor, gerando alertas em caso de falha.

Esses dados são enviados para o painel de controle em tempo real e exibidos em gráficos, medidores e logs.

### 2. **Controle de Operação (Iniciar/Parar)**

O fluxo também inclui botões de controle no painel que permitem a interação com o sistema:

- **Botão Iniciar**: Envia um comando via OPC UA para iniciar o funcionamento das esteiras e dos motores.
- **Botão Parar**: Envia um comando para parar o sistema.

Esses comandos são tratados pelos nós **OpcUa-Client** e **OpcUa-Item** e enviados para o servidor OPC UA, que atua no controle das operações.

### 3. **Monitoramento de Tempo de Operação (Horímetro)**

O fluxo possui nós específicos para monitorar o tempo de operação do sistema, dividindo-o em:

- **Segundos**
- **Minutos**
- **Horas**

Esses dados são exibidos no painel para que os operadores possam acompanhar quanto tempo o sistema está em operação contínua.

### 4. **Gerenciamento de Alertas e Logs**

O fluxo verifica continuamente o estado dos motores. Quando uma anomalia ou falha é detectada (como uma corrente anormal ou parada do motor), o sistema gera um alerta:

- O alerta é mostrado no painel de controle.
- O alerta é publicado via MQTT para o **AWS IoT**, para que possa ser registrado e processado remotamente.
- Logs são salvos em arquivos CSV, permitindo a geração de relatórios históricos.

### 5. **Indicadores de Desempenho (OEE)**

A eficiência do sistema é monitorada com base em cálculos de **OEE** (Overall Equipment Effectiveness), divididos em três principais indicadores:

- **Disponibilidade**: Tempo que o sistema esteve disponível comparado ao tempo planejado.
- **Desempenho**: Eficiência do processo de produção.
- **Qualidade**: Percentual de produtos bons comparado ao total de produtos produzidos.

Esses valores são atualizados continuamente no painel de controle e também enviados via MQTT para o **AWS IoT**.

### 6. **Publicação via MQTT (AWS IoT)**

Dados operacionais, alertas e indicadores de desempenho são publicados no **AWS IoT** via MQTT. O nó **MQTT** conecta-se ao broker configurado no **AWS IoT** e publica:

- **Alertas de falha**
- **Logs de operação**
- **Indicadores de desempenho (OEE)**

Isso permite o monitoramento remoto e a análise dos dados enviados pela planta industrial.

### 7. **Envio de Dados para o Azure IoT Hub**

Além de enviar dados para o **AWS IoT**, o fluxo também publica relatórios de desempenho para o **Azure IoT Hub**. O nó **Azure IoT Hub** é configurado para enviar dados de operação, incluindo o **OEE** e status dos dispositivos, permitindo o acompanhamento e análise na plataforma do **Azure Digital Twins**.

### 8. **Visualização e Painel de Controle**

O painel de controle, construído com **Node-RED Dashboard**, oferece uma interface visual amigável e clara para monitorar o estado do sistema em tempo real. O painel inclui:

- **Gráficos de Corrente**: Gráficos de linha que mostram as correntes elétricas dos motores ao longo do tempo.
- **Medidores de RPM**: Medidores que exibem as rotações por minuto dos motores.
- **Indicadores de Tempo de Operação**: Mostra o tempo total de operação em segundos, minutos e horas.
- **Indicadores de Produção**: Exibe a quantidade de produtos (caixas) processados.
- **Logs e Alertas**: Logs em tempo real exibidos no painel para acompanhar alertas e eventos críticos.

## Como Acessar o Dashboard

Para acessar o painel de controle do **Node-RED**:

1. **Inicie o Node-RED** no ambiente de execução:
   ```bash
   node-red
   ```

2. **Acesse o Dashboard** pelo navegador usando o seguinte URL:
   ```
   http://localhost:1880/ui
   ```