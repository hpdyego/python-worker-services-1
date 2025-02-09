import time
import logging
import threading

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def executar_tarefa(nome, tempo):
    """Função que simula uma tarefa demorada."""
    logging.info(f"Tarefa {nome} iniciada...")
    time.sleep(tempo)
    logging.info(f"Tarefa {nome} concluída!")

def iniciar_worker():
    """Cria e gerencia múltiplas threads."""
    tarefas = [
        ("A", 3),  # Nome da tarefa, tempo de execução
        ("B", 5),
        ("C", 2)
    ]

    threads = []

    for nome, tempo in tarefas:
        thread = threading.Thread(target=executar_tarefa, args=(nome, tempo))
        thread.start()
        threads.append(thread)

    # Aguarda todas as threads terminarem antes de continuar
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    logging.info("Iniciando Worker Service com múltiplas threads...")
    
    while True:
        iniciar_worker()
        logging.info("Todas as tarefas concluídas. Reiniciando em 10 segundos...")
        time.sleep(3)  # Pausa antes de reiniciar o loop