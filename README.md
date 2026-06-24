# 📂 Organizador Automático de Arquivos (macOS & Windows)

Um script em Python automatizado que monitora e organiza sua pasta de Downloads (ou qualquer outra pasta bagunçada) movendo os arquivos para diretórios específicos com base em suas extensões.

---

## ✨ Funcionalidades
* **Organização por Categoria:** Separa automaticamente Documentos, Imagens, Vídeos e Compactados.
* **Multiplataforma:** Adaptado para rodar perfeitamente tanto em **macOS** quanto em **Windows** (usando caminhos dinâmicos com `pathlib`).
* **Feedback Visual:** Mostra no terminal em tempo real quais arquivos foram movidos e para onde.

## 🛠️ Tecnologias Utilizadas
* **Python 3.x**
* **Pathlib:** Para manipulação inteligente e segura de caminhos de arquivos.
* **Shutil & OS:** Para operações de sistema e movimentação de arquivos.

## 🚀 Como Rodar o Projeto

### Pré-requisitos
Você vai precisar do Python instalado na sua máquina.

### Passos
1. Clone este repositório:
   ```bash
   git clone [https://github.com/SEU-USUARIO/NOME-DO-REPOSITORIO.git](https://github.com/SEU-USUARIO/NOME-DO-REPOSITORIO.git)

2. Instalar as dependências
Instale o pacote watchdog via terminal:
   ```bash
   pip3 install watchdog
   
3. Rodar o aplicativo
Execute o arquivo principal:
   ```bash
   python3 app.py

# 📖 Como Usar
0 - Abra o aplicativo.
1 - Clique no botão 📁 Escolher Pasta para selecionar o diretório que você deseja que seja organizado (ex: a pasta Downloads).
2 - O botão exibirá o marcador 📍 Pasta: [Nome] confirmando sua seleção.
3 - Clique em Iniciar Monitoramento.
4 - Pronto! Qualquer novo arquivo jogado ou baixado nessa pasta será movido para a subpasta correta instantaneamente.

# 📂 Organização das Pastas (Regras)
O script categoriza os arquivos seguindo as regras abaixo:
- .pdf, .docx, .txt ➡️ Documentos
- .xlsx ➡️ Documentos/Planilhas
- .jpg, .jpeg, .png ➡️ Imagens
- .mp4 ➡️ Vídeos
- .zip, .rar ➡️ Compactados
Desenvolvido com 💙 por Naurk10
   

