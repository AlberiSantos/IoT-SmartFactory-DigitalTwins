# Análise de Dados do Wireshark

Este guia explica como usar o script de análise de dados coletados pelo Wireshark em um arquivo CSV, executando diretamente no Google Colab.

## Passo a Passo

### 1. **Abrir o Google Colab**
   - Acesse o [Google Colab](https://colab.research.google.com) e crie um novo notebook.

### 2. **Carregar Bibliotecas Necessárias**
   - Certifique-se de que o notebook possui as bibliotecas `pandas` e `matplotlib` instaladas. Execute o seguinte código na primeira célula:

   ```python
   pip install pandas matplotlib
   ```

### 3. **Carregar o Script de Análise**
   - Copie e cole o script `utility.py` em `./scripts` em uma nova célula no Colab.

### 4. **Upload do Arquivo CSV**
   - No menu lateral do Colab (ícone de pasta), clique no botão **Upload** para enviar seu arquivo CSV (por exemplo, `tcp.port502_ensaio0.csv`).

### 5. **Executar a Função**
   - Com o arquivo CSV carregado, execute o script passando o caminho do arquivo e o número da porta TCP. Por exemplo:

   ```python
   results = analyze_wireshark_data('/content/tcp.port502_ensaio0.csv', 502)
   ```

   - Isso gerará a saída com as métricas e o gráfico conforme mostrado na imagem.

### 6. **Resultados**
   - O script imprimirá os seguintes resultados no console:
     - Latência Média Geral
     - Throughput Médio Geral
     - Número de Pacotes Pequenos, Médios e Grandes
     - Número Total de Retransmissões
   - Um histograma da latência também será exibido.
