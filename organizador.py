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
    # Esse método é disparado automaticamente quando um arquivo ou pasta é criado
    def on_created(self, event):
        if event.is_directory:
            return

        arquivo = Path(event.src_path)
        
        # Ignora arquivos temporários de download comuns
        if arquivo.suffix in ['.crdownload', '.download', '.tmp']:
            return

        # Espera o arquivo terminar de ser gravado no disco
        tamanho_antigo = -1
        while True:
            try:
                # Se o arquivo sumir no meio do processo (ex: mudou de nome pelo navegador)
                if not arquivo.exists():
                    return
                
                tamanho_atual = arquivo.stat().st_size
                if tamanho_atual == tamanho_antigo:
                    # O tamanho parou de mudar, o download provavelmente terminou
                    break
                tamanho_antigo = tamanho_atual
                time.sleep(1) # Aguarda mais um segundo para checar de novo
            except FileNotFoundError:
                return

        self.organizar_arquivo(arquivo)

    def organizar_arquivo(self, arquivo):
        extensao = arquivo.suffix.lower()

        if extensao in DICIONARIO_EXTENSOES:
            nome_pasta_destino = DICIONARIO_EXTENSOES[extensao]
            pasta_destino = PASTA_ORIGEM / nome_pasta_destino

            pasta_destino.mkdir(parents=True, exist_ok=True)

            # Lógica simples para evitar substituir arquivos com o mesmo nome
            destino_final = pasta_destino / arquivo.name
            if destino_final.exists():
                # Se já existe, adiciona o timestamp atual ao nome do arquivo
                timestamp = int(time.time())
                novo_nome = f"{arquivo.stem}_{timestamp}{arquivo.suffix}"
                destino_final = pasta_destino / novo_nome

            shutil.move(str(arquivo), str(destino_final))
            print(f"⚡ Automatizado: {arquivo.name} -> {nome_pasta_destino}")

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