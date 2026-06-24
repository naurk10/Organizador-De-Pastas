import os
import shutil
from pathlib import Path

# 1. Defina o caminho da pasta que será organizada (mude para o seu caminho)
PASTA_ORIGEM = Path("/Users/kauau/Downloads")

# 2. Defina o mapeamento de extensões para suas respectivas pastas
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

    # --- Novos (baseados no seu print) ---
    ".dmg": "Instaladores_Mac",       # Slack, VSCode, Claude, Brave, Docker...
    ".html": "Documentos/Web",         # altis.html, id917932200.html...
    ".pptx": "Documentos/Apresentacoes",# Voice-Pitch-AI.pptx
    ".csv": "Documentos/Planilhas",    # report.csv (vai junto com as planilhas)
    ".sql": "Desenvolvimento",         # SQL_Schema.sql
    ".pem": "Chaves_Seguranca",        # labsuser.pem (chaves da AWS/computação em nuvem)
    ".gif": "Imagens",                 # tenor.gif (imagens animadas)
}

def organizar_pasta():
    # Verifica se a pasta de origem realmente existe
    if not PASTA_ORIGEM.exists():
        print(f"A pasta {PASTA_ORIGEM} não foi encontrada.")
        return

    # Iterar por todos os arquivos da pasta de origem
    for arquivo in PASTA_ORIGEM.iterdir():
        # Ignorar se for uma pasta
        if arquivo.is_dir():
            continue
        
        # Pegar a extensão do arquivo em letras minúsculas
        extensao = arquivo.suffix.lower()

        # Verificar se a extensão está no nosso dicionário
        if extensao in DICIONARIO_EXTENSOES:
            nome_pasta_destino = DICIONARIO_EXTENSOES[extensao]
            pasta_destino = PASTA_ORIGEM / nome_pasta_destino

            # Criar a pasta de destino se ela não existir
            pasta_destino.mkdir(parents=True, exist_ok=True)

            # Mover o arquivo
            shutil.move(str(arquivo), str(pasta_destino / arquivo.name))
            print(f"Movido: {arquivo.name} -> Pasta {nome_pasta_destino}")

if __name__ == "__main__":
    print("Iniciando a organização...")
    organizar_pasta()
    print("Organização concluída!")