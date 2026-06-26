# 🤖 Organizador de Pastas Inteligente

Um aplicativo em Python com interface gráfica (GUI) que monitora uma pasta específica em tempo real e organiza automaticamente os novos arquivos em subpastas com base em suas extensões (Documentos, Imagens, Vídeos, Compactados, etc.).

---

## ✨ Funcionalidades

- **Monitoramento em Tempo Real:** Utiliza a biblioteca `watchdog` para detectar instantaneamente quando um novo arquivo é adicionado à pasta escolhida.
- **Evita Conflito de Duplicados:** Se um arquivo com o mesmo nome já existir na pasta de destino, o sistema gera automaticamente um nome único (ex: `foto (1).jpg`).
- **Interface Gráfica Nativa:** Interface simples desenvolvida em `Tkinter`, otimizada para funcionar perfeitamente tanto no modo claro quanto no modo escuro (Dark Mode) do macOS.
- **Execução Assíncrona (Multi-threading):** O monitoramento roda em uma thread separada para garantir que a interface visual nunca trave ou congele durante a execução.

---

## 🛠️ Tecnologias Utilizadas

- **[Python](https://www.python.org/)** (Linguagem base)
- **[Watchdog](https://pypi.org/project/watchdog/)** (Monitoramento do sistema de arquivos)
- **[Tkinter](https://docs.python.org/3/library/tkinter.html)** (Interface gráfica nativa)
- **Multi-threading** (Processamento em segundo plano)

---

## 🚀 Como Executar o Projeto

### Pré-requisitos
Certifique-se de ter o Python 3 instalado no seu computador. Além disso, é necessário instalar a biblioteca `watchdog`.

### Passos
1. Clone este repositório:
```bash
git clone [https://github.com/naurk10/Organizador-De-Pastas.git](https://github.com/naurk10/Organizador-De-Pastas.git)
```

2. Instalar as dependências
Instale o pacote watchdog via terminal:
   ```bash
   pip3 install watchdog
   
3. Rodar o aplicativo
Execute o arquivo principal:
   ```bash
   python3 app.py

---

## 📖 Como Usar

0.  **Abra o aplicativo.**
1.  **Clique no botão** 📁 **Escolher Pasta** para selecionar o diretório que você deseja que seja organizado (ex: a pasta *Downloads*).
2.  **O botão exibirá o marcador** 📍 **Pasta: [Nome]** confirmando sua seleção.
3.  **Clique em Iniciar Monitoramento.**
4.  **Pronto!** Qualquer novo arquivo jogado ou baixado nessa pasta será movido para a subpasta correta instantaneamente.


https://github.com/user-attachments/assets/01a9cb02-f676-43b9-af40-ffc45002e367


---

# 📂 Organização das Pastas (Regras)
O script categoriza os arquivos seguindo as regras abaixo:
- .pdf, .docx, .txt ➡️ Documentos
- .xlsx ➡️ Documentos/Planilhas
- .jpg, .jpeg, .png ➡️ Imagens
- .mp4 ➡️ Vídeos
- .zip, .rar ➡️ Compactados ||
Desenvolvido com 💙 por Naurk10

   ![Mon Laferte GIF](https://media1.tenor.com/m/sUQgrMDcwvkAAAAC/mon-laferte-viña-del-mar.gif)
