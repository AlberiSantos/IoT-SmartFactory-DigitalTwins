# Configurações do Factory I/O

Este documento descreve as configurações realizadas no **Factory I/O** para permitir a simulação e integração com o sistema de controle utilizando o **Node-RED** e o **CODESYS**. 

## Passos para Configurar o Factory I/O

### 1. Selecionar o Sistema de Automação

Para conectar o **Factory I/O** ao sistema de controle baseado em **CODESYS**, siga os passos abaixo:

1. Abra o **Factory I/O**.
2. No menu superior, vá em **File** > **Drivers**.
3. Escolha **CODESYS Control Win V3** como o driver de automação. Certifique-se de que o **CODESYS** já está instalado e funcionando no seu computador.
4. Clique em **Connect**.

### 2. Configuração do CODESYS com Factory I/O

- No **CODESYS**, crie um projeto que utilize o driver **CODESYS Control Win V3** para se comunicar com o **Factory I/O**.
- Certifique-se de que as variáveis do **PLC_PRG** no **CODESYS** estejam configuradas corretamente para se comunicar com os sensores e atuadores do **Factory I/O**.
- Adicione o servidor **OPC UA** no **CODESYS** para permitir a leitura e escrita de dados a partir do **Node-RED** e outros sistemas.

### 3. Configuração dos Sensores e Atuadores no Factory I/O

No **Factory I/O**, siga os seguintes passos para configurar os sensores e atuadores:

1. No ambiente do **Factory I/O**, posicione os dispositivos necessários (sensores de proximidade, esteiras, atuadores, etc.). Neste cenário foi utilizada a cena "Buffer Station".
2. Para cada dispositivo, abra as propriedades e configure a interface de comunicação com o **CODESYS** (mapeamento de endereços).
3. Certifique-se de que cada dispositivo está associado a uma variável no **CODESYS** que será utilizada para leitura e escrita de dados.

### 4. Testar a Integração

1. Inicie a simulação no **Factory I/O**.
2. Inicie o programa **CODESYS** e certifique-se de que o PLC está rodando.
3. No **Node-RED**, verifique se os dados do **Factory I/O** estão sendo recebidos corretamente via **OPC UA**.
4. Teste os botões de controle (Iniciar e Parar) no painel do **Node-RED** e verifique se o sistema responde corretamente no **Factory I/O**.

### 5. Ajustar Parâmetros de Simulação

Você pode ajustar a velocidade das esteiras, o tempo de resposta dos sensores e outros parâmetros diretamente no **Factory I/O** para adequar a simulação às suas necessidades de controle.

### 6.  Finalizar e Salvar o Projeto

1. Quando tudo estiver configurado corretamente, salve seu projeto no **Factory I/O**.
2. No **CODESYS**, salve o projeto com as variáveis mapeadas para o **Factory I/O**.
3. No **Node-RED**, certifique-se de que os fluxos estão funcionando corretamente para leitura e controle.

## Dicas Adicionais

- Certifique-se de que todas as variáveis e endereços OPC UA estão corretamente mapeados entre o **Factory I/O** e o **CODESYS** para evitar falhas de comunicação.
