import os
import shutil
import time
from pathlib import Path
# Importando os módulos do watchdog
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# 1. Configuração dos caminhos (Ajustado para o seu macOS)
PASTA_ORIGEM = Path.home() / "Downloads"

DICIONARIO_EXTENSOES = {
    ".pdf": "Documentos",
    ".docx": "Documentos",
    ".txt": "Documentos",
    ".xlsx": "Documentos/Planilhas",
    ".jpg": "Imagens",
    ".jpeg": "Imagens",
    ".png": "Imagens",
    ".mp4": "Videos",
    ".zip": "Compactados",
    ".rar": "Compactados",
}

# 2. Criar a classe que vai "escutar" os eventos da pasta
import time

class GerenciadorDeArquivosHandler(FileSystemEventHandler):
    def __init__(self, pasta_origem):
        super().__init__()
        self.pasta_origem = pasta_origem  # Guarda a pasta selecionada na interface

    def gerar_nome_unico(self, pasta_destino, nome_arquivo):
        # ... (pode manter o seu código idêntico ao do print a partir daqui)
        arquivo_path = pasta_destino / nome_arquivo
        if not arquivo_path.exists():
            return arquivo_path
        nome_sem_extensao = arquivo_path.stem
        extensao = arquivo_path.suffix
        contador = 1
        while True:
            novo_nome = f"{nome_sem_extensao} ({contador}){extensao}"
            novo_caminho = pasta_destino / novo_nome
            if not novo_caminho.exists():
                return novo_caminho
            contador += 1

    def organizar_arquivo(self, arquivo):
        extensao = arquivo.suffix.lower()

        if extensao in DICIONARIO_EXTENSOES:
            nome_pasta_destino = DICIONARIO_EXTENSOES[extensao]
            # CORREÇÃO CRÍTICA: Usa a pasta do construtor, não a variável estática global
            pasta_destino = self.pasta_origem / nome_pasta_destino

            pasta_destino.mkdir(parents=True, exist_ok=True)

            destino_final = self.gerar_nome_unico(pasta_destino, arquivo.name)

            shutil.move(str(arquivo), str(destino_final))
            print(f"⚡ Automatizado: {arquivo.name} -> {nome_pasta_destino} (Salvo como: {destino_final.name})")

# 3. Inicializar o monitoramento
if __name__ == "__main__":
    print(f"🤖 Monitorando a pasta: {PASTA_ORIGEM}")
    print("Pressione Ctrl+C para parar.")

    event_handler = GerenciadorDeArquivosHandler()
    observer = Observer()
    observer.schedule(event_handler, path=str(PASTA_ORIGEM), recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        print("\n🤖 Monitoramento encerrado.")
    observer.join()