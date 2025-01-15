import psutil
from flask import Flask, request
import time

app = Flask(__name__)

@app.before_request
def monitor_resources():
    # Captura o estado inicial de CPU e memória
    request.start_time = time.perf_counter()  # Usa perf_counter para maior precisão
    request.cpu_start = psutil.cpu_percent(interval=0)  # Garante uma medição inicial
    request.memory_start = psutil.virtual_memory().used

@app.after_request
def log_resources(response):
    # Calcula a diferença de recursos
    duration = time.perf_counter() - request.start_time
    cpu_end = psutil.cpu_percent(interval=0)  # Medição final da CPU
    memory_end = psutil.virtual_memory().used

    # Evita valores negativos para memória
    memory_diff = (memory_end - request.memory_start) / 1024**2
    memory_diff = max(memory_diff, 0)  # Corrige para evitar negativos

    # Exibe os dados no terminal
    print(f"CPU usado: {cpu_end - request.cpu_start:.2f}%")
    print(f"Memória usada: {memory_diff:.2f} MB")
    print(f"Tempo de resposta: {duration:.4f}s")

    return response

@app.route('/')
def home():
    return "Monitoramento de recursos ativo!"

if __name__ == '__main__':
    app.run(debug=True)
