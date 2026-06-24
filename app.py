import os
import shutil
import time
import tkinter as tk
from tkinter import filedialog, messagebox
from pathlib import Path
import threading
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# --- CONFIGURAÇÃO DE EXTENSÕES ---
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

# --- CLASSE DO WATCHDOG (MONITOR) ---
class GerenciadorDeArquivosHandler(FileSystemEventHandler):
    def __init__(self, pasta_origem):
        super().__init__()
        self.pasta_origem = pasta_origem

    def on_created(self, event):
        if event.is_directory:
            return

        arquivo = Path(event.src_path)
        if arquivo.suffix in ['.crdownload', '.download', '.tmp']:
            return

        tamanho_antigo = -1
        while True:
            try:
                if not arquivo.exists():
                    return
                tamanho_atual = arquivo.stat().st_size
                if tamanho_atual == tamanho_antigo:
                    break
                tamanho_antigo = tamanho_atual
                time.sleep(1)
            except FileNotFoundError:
                return

        self.organizar_arquivo(arquivo)

    def generar_nome_unico(self, pasta_destino, nome_arquivo):
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
            pasta_destino = self.pasta_origem / nome_pasta_destino

            pasta_destino.mkdir(parents=True, exist_ok=True)
            destino_final = self.generar_nome_unico(pasta_destino, arquivo.name)

            try:
                shutil.move(str(arquivo), str(destino_final))
                print(f"⚡ Automatizado: {arquivo.name} -> {nome_pasta_destino}")
            except Exception as e:
                print(f"Erro ao mover arquivo: {e}")

# --- CLASSE DA INTERFACE GRÁFICA (GUI FOCADA EM BOTÕES) ---
class AppAutomacao:
    def __init__(self, root):
        self.root = root
        self.root.title("🤖 Organizador")
        self.root.geometry("400x250")
        
        self.observer = None
        self.monitorando = False
        self.pasta_selecionada = None

        # --- COMPONENTES DA TELA ---
        self.titulo = tk.Label(root, text="Automação de Arquivos", font=("Helvetica", 16, "bold"))
        self.titulo.pack(pady=(30, 20))

        # Botão Principal - Ele mesmo vai mostrar o nome da pasta selecionada
        self.btn_selecionar = tk.Button(root, text="📁 Escolher Pasta", font=("Helvetica", 12), width=25, command=self.selecionar_pasta)
        self.btn_selecionar.pack(pady=10)

        # Botão Iniciar/Parar
        self.btn_status = tk.Button(root, text="Iniciar Monitoramento", font=("Helvetica", 12), width=25, state="disabled", command=self.alternar_monitoramento)
        self.btn_status.pack(pady=10)

        # Barra de status do rodapé (simples e direta)
        self.lbl_status = tk.Label(root, text="Status: 🛑 Parado", font=("Helvetica", 10, "italic"))
        self.lbl_status.pack(pady=(20, 0))

    def selecionar_pasta(self):
        pasta = filedialog.askdirectory(initialdir=Path.home())
        if pasta:
            self.pasta_selecionada = Path(pasta)
            
            # ATUALIZAÇÃO SINALIZADORA: Muda o texto do próprio botão!
            # O Mac é obrigado a renderizar isso com alto contraste por padrão
            self.btn_selecionar.config(text=f"📍 Pasta: {self.pasta_selecionada.name}")
            self.btn_status.config(state="normal")
            
            # Força o redesenho dos elementos na interface
            self.root.update()

    def alternar_monitoramento(self):
        if not self.monitorando:
            self.iniciar_monitoramento()
        else:
            self.parar_monitoramento()

    def iniciar_monitoramento(self):
        if not self.pasta_selecionada:
            return

        self.monitorando = True
        self.btn_status.config(text="🛑 Parar Monitoramento")
        self.lbl_status.config(text=f"🤖 Monitorando: {self.pasta_selecionada.name}...")
        self.btn_selecionar.config(state="disabled")

        event_handler = GerenciadorDeArquivosHandler(self.pasta_selecionada)
        self.observer = Observer()
        self.observer.schedule(event_handler, path=str(self.pasta_selecionada), recursive=False)
        
        self.observer_thread = threading.Thread(target=self.observer.start, daemon=True)
        self.observer_thread.start()

    def parar_monitoramento(self):
        self.monitorando = False
        self.btn_status.config(text="Iniciar Monitoramento")
        self.lbl_status.config(text="Status: 🛑 Parado")
        self.btn_selecionar.config(state="normal")
        
        if self.observer:
            self.observer.stop()
            self.observer.join()

if __name__ == "__main__":
    root = tk.Tk()
    app = AppAutomacao(root)
    root.mainloop()