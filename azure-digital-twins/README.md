# Azure Digital Twins - Atualização via Azure IoT Hub

Este módulo as configurações utilizadas na **Azure Function** para atualizar gêmeos digitais no **Azure Digital Twins**, recebendo dados de dispositivos conectados através do **Azure IoT Hub**. Além disso, fornece também as configurações da ontologia de manufatura utilizada.

## Cenário Geral de Uso

Neste cenário, dispositivos IoT enviam dados para o **Azure IoT Hub**. A **Azure Function** é responsável por processar esses dados e atualizar os gêmeos digitais no **Azure Digital Twins** com base nos dados recebidos.

### Fluxo Geral:

- **Ingestão de Dados**: Dispositivos IoT publicam dados no **Azure IoT Hub**.
- **Processamento dos Dados**: A **Azure Function** consome esses dados do IoT Hub e os processa.
- **Atualização de Gêmeos Digitais**: A **Azure Function** atualiza o estado dos gêmeos digitais no **Azure Digital Twins** com base nas informações recebidas.

## Configuração e Deploy

Para entender os passos detalhados de como configurar a ingestão de dados de dispositivos e o deploy da **Azure Function** para atualizar os gêmeos digitais, siga as instruções fornecidas no link de apoio da Microsoft:

- [Sincronizando Azure Digital Twins com Dados de Dispositivos IoT](https://learn.microsoft.com/en-us/training/modules/synchronize-azure-digital-twins-with-iot-device-data/3-ingest-device-data)

## Configuração da Ontologia dos Gêmeos Digitais

A ontologia dos gêmeos digitais usada neste projeto é baseada no padrão **ISA-95**. Carregue o arquivo de ontologia apropriado no seu ambiente do **Azure Digital Twins**.

1. Navegue até a sua instância do **Azure Digital Twins**.
2. Importe o modelo de ontologia para definir os gêmeos digitais.

## Links de Apoio

- [Manufacturing Ontologies - GitHub](https://github.com/AlberiSantos/ManufacturingOntologies/tree/d998ad09ec10a1b81a6a5dd099c0f3a56f3b658e)
- [Sincronizando Azure Digital Twins com Dados de Dispositivos IoT](https://learn.microsoft.com/en-us/training/modules/synchronize-azure-digital-twins-with-iot-device-data/3-ingest-device-data)

## Notas Finais

Este módulo foi desenvolvido para integrar o **Azure IoT Hub** com o **Azure Digital Twins**, permitindo a atualização dinâmica de gêmeos digitais a partir de dados de dispositivos IoT. A ontologia utilizada foi baseada no padrão **ISA-95**, que é amplamente utilizado em cenários industriais.
