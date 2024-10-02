# CODESYS - Configuração do Servidor OPC UA

Este README descreve os passos necessários para configurar um projeto no **CODESYS** com suporte ao protocolo **OPC UA**, utilizado para a comunicação entre um CLP virtual e outros componentes do sistema no contexto de automação industrial.

## Requisitos

- **CODESYS versão 3.5.11 ou superior**
- **CODESYS Control Win V3** (CLP virtual)
- **OPC UA Server** configurado no CODESYS
- Certificado digital para comunicação segura via OPC UA

## Instruções de Configuração

### 1. Criação do Projeto no CODESYS

1. Abra o **CODESYS** e crie um novo projeto:
   - Tipo de projeto: **Standard Project**
   - Dispositivo: **CODESYS Control Win V3**
   - Linguagem de programação: **Ladder Diagram (LD)**

2. Adicione um programa chamado **PLC_PRG**. Este programa será responsável pela lógica de controle das esteiras, contagem de peças e outras funções relacionadas à operação simulada.

### 2. Programação Ladder no PLC_PRG

Implemente a lógica básica de controle no **PLC_PRG** utilizando blocos de funções para as seguintes operações:

- **Controle e movimentação das esteiras**:
  - Monitore os motores das esteiras em tempo real.
  - Gere feedbacks operacionais para verificar o funcionamento correto dos motores e detectar falhas.

- **Monitoramento e contagem de peças**:
  - Use sensores de proximidade para incrementar contadores.
  - Adicione lógica para resetar contadores, permitindo novas execuções do sistema.

- **Controle de segurança e parada de emergência**:
  - Implemente lógica de parada de emergência que desative as esteiras ao detectar um sinal de parada, garantindo a segurança dos operadores e equipamentos.

- **Monitoramento de parâmetros operacionais**:
  - Monitore variáveis como corrente e rotação.
  - Configure alertas automáticos para desvio desses parâmetros, para uso em manutenção preditiva e tomada de decisão em tempo real.

- **Horímetro e registro de tempo de operação**:
  - Implemente um horímetro para acumular o tempo de operação dos motores e esteiras, com contagem de segundos, minutos e horas.

### 3. Configuração do Servidor OPC UA

Para habilitar a comunicação via **OPC UA** entre o CLP virtual e outros sistemas:

1. Adicione o objeto **Symbol Configuration**:
   - Este objeto permite que as variáveis do programa **PLC_PRG** sejam acessíveis externamente via **OPC UA**.
   - Selecione as variáveis que deseja expor e configure os direitos de acesso (**Access Rights**) para garantir o nível apropriado de segurança.

2. Configure a comunicação segura com **OPC UA**:
   - Utilize o **CODESYS Security Agent** para adicionar um certificado digital.
   - Este certificado permite que a comunicação entre o servidor **OPC UA** e seus clientes seja criptografada e autenticada, garantindo a integridade dos dados.

### 4. Teste e Deploy

1. Conclua a implementação do programa **PLC_PRG** e a configuração do servidor **OPC UA**.
2. Realize o deploy do projeto no **CODESYS Control Win V3** (CLP virtual).
3. Use um cliente **OPC UA** compatível para testar a comunicação com o servidor e acessar as variáveis expostas.

## Notas Finais

O projeto foi desenvolvido para facilitar a comunicação entre o CLP virtual e sistemas externos via **OPC UA**, com foco em segurança, controle de movimentação e monitoramento de parâmetros operacionais. A configuração pode ser adaptada para atender a diferentes cenários de automação industrial.
