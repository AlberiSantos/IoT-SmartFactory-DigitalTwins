#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt

def analyze_wireshark_data(file_path, port):
    """
    Analisa os dados coletados do Wireshark para uma porta TCP específica.
    
    Args:
        file_path (str): Caminho para o arquivo CSV contendo os dados capturados pelo Wireshark.
        port (int): Porta TCP para a qual os dados foram coletados (ex: 502, 4840, 8883).
    
    Returns:
        dict: Dicionário contendo a latência média, throughput médio e outras métricas calculadas.
    """
    # Carregar o arquivo CSV em um DataFrame
    df = pd.read_csv(file_path)

    # Converter as colunas relevantes para o tipo numérico e datetime
    df['TCP Delta'] = pd.to_numeric(df['TCP Delta'], errors='coerce')
    df['Length'] = pd.to_numeric(df['Length'], errors='coerce')
    df['Time since first frame in this TCP stream'] = pd.to_numeric(df['Time since first frame in this TCP stream'], errors='coerce')
    df['Time'] = pd.to_datetime(df['Time'], format='%H:%M:%S', errors='coerce')

    # Calcular a Latência Média Geral
    latency_mean = df['TCP Delta'].mean()

    # Calcular o Throughput Médio Geral
    total_data_transferred = df['Length'].sum()  # Total de dados transferidos
    total_time = df['Time since first frame in this TCP stream'].max()  # Duração total da captura
    throughput_mean = total_data_transferred / total_time

    # Análise da Distribuição de Tamanhos de Pacotes
    small_packets = df[df['Length'] <= 100].shape[0]
    medium_packets = df[(df['Length'] > 100) & (df['Length'] <= 1000)].shape[0]
    large_packets = df[df['Length'] > 1000].shape[0]

    # Contar o número total de retransmissões
    retransmissions = df['Info'].str.contains('retransmission', case=False, na=False).sum()

    # Exibir os resultados agregados
    results = {
        "latency_mean": latency_mean,
        "throughput_mean_kb_s": throughput_mean / 1024,
        "small_packets": small_packets,
        "medium_packets": medium_packets,
        "large_packets": large_packets,
        "retransmissions": retransmissions
    }

    print(f"Latência Média Geral: {latency_mean:.3f} segundos")
    print(f"Throughput Médio Geral: {throughput_mean / 1024:.2f} KB/s")
    print(f"Número de Pacotes Pequenos (<= 100 bytes): {small_packets}")
    print(f"Número de Pacotes Médios (101 - 1000 bytes): {medium_packets}")
    print(f"Número de Pacotes Grandes (> 1000 bytes): {large_packets}")
    print(f"Número Total de Retransmissões: {retransmissions}")

    # Histograma da Latência
    plt.figure(figsize=(10, 6))
    plt.hist(df['TCP Delta'].dropna() * 1000, bins=50, color='blue', edgecolor='black')
    plt.title(f'Histograma da Latência (ms) - Porta TCP {port}')
    plt.xlabel('Latência (ms)')
    plt.ylabel('Frequência')
    plt.grid(True)
    plt.show()

    # Gráfico de Barras da Distribuição de Tamanho de Pacotes
    plt.figure(figsize=(8, 5))
    plt.bar(['Pequenos (<= 100B)', 'Médios (101-1000B)', 'Grandes (> 1000B)'],
            [small_packets, medium_packets, large_packets], color=['green', 'orange', 'red'])
    plt.title(f'Distribuição de Tamanho de Pacotes - Porta TCP {port}')
    plt.ylabel('Número de Pacotes')
    plt.grid(True)
    plt.show()

    # Gráfico de Linhas do Throughput ao Longo do Tempo
    df = df.sort_values(by='Time')
    df['Cumulative Data'] = df['Length'].cumsum()
    df['Throughput'] = df['Cumulative Data'] / (df['Time'].astype('int64') // 1e9 - df['Time'].astype('int64').iloc[0] // 1e9)

    plt.figure(figsize=(10, 6))
    plt.plot(df['Time'], df['Throughput'] / 1024, color='purple')
    plt.title(f'Throughput ao Longo do Tempo - Porta TCP {port}')
    plt.xlabel('Tempo')
    plt.ylabel('Throughput (KB/s)')
    plt.grid(True)
    plt.show()

    # Gráfico I/O - Número de Pacotes por Intervalo de Tempo
    df.set_index('Time', inplace=True)
    packet_count_per_second = df.resample('1s').size()

    plt.figure(figsize=(10, 6))
    plt.plot(packet_count_per_second.index, packet_count_per_second.values, marker='o', linestyle='-', color='blue')
    plt.title(f'Número de Pacotes por Segundo - Porta TCP {port}')
    plt.xlabel('Tempo')
    plt.ylabel('Número de Pacotes')
    plt.grid(True)
    plt.show()

    # Gráfico I/O - Taxa de Bytes por Intervalo de Tempo
    byte_count_per_second = df['Length'].resample('1s').sum()

    plt.figure(figsize=(10, 6))
    plt.plot(byte_count_per_second.index, byte_count_per_second.values, marker='o', linestyle='-', color='orange')
    plt.title(f'Taxa de Bytes por Segundo - Porta TCP {port}')
    plt.xlabel('Tempo')
    plt.ylabel('Bytes por Segundo')
    plt.grid(True)
    plt.show()

    return results
