## 🎮 Jogo da Forca Simples em Python 🐍

[![Python Version](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![Status](https://img.shields.io/badge/Status-Completo-brightgreen.svg)]()

Um projeto clássico de Jogo da Forca (Hangman) desenvolvido para praticar os fundamentos da linguagem Python. O objetivo é adivinhar a palavra secreta (relacionada à tecnologia!) em até **6 tentativas**. 🎯

---

### ✨ Destaques do Código

Este jogo demonstra conceitos fundamentais de Python como:

* **Seleção Aleatória:** Utiliza a biblioteca nativa `random` para escolher a palavra secreta dinamicamente.
* **Controle de Fluxo:** Implementação eficiente de *loops* (`while`) e condicionais (`if/else`) para gerenciar o jogo e as tentativas.
* **Manipulação de Listas:** Uso de listas (como `letras_descobertas`) para rastrear o progresso do jogador.
* **Lista de Palavras Temáticas:** O jogo utiliza uma lista inicial de palavras focadas em **tecnologia e programação** (ex: `python`, `programacao`, `dados`).

---

### ⚙️ Como Jogar (Instruções Rápidas)

#### Pré-requisitos

Certifique-se de que você tem o Python 3.x instalado em sua máquina.

#### 🚀 Rodando o Jogo

1.  **Clone o Repositório:** Baixe o código para sua máquina.
    ```bash
    git clone https://github.com/CarlosEduardo-J/jogo-da-forca
    cd [jogo-da-forca]
    ```
2.  **Execute o Script:** Use o comando `python` no terminal:
    ```bash
    python jogo_da_forca.py 
    ```

#### 🕹️ Regras

* O jogo começa com 6️⃣ tentativas.
* Você deve inserir apenas **uma letra** por vez.
* A cada erro, o número de tentativas diminui.
* O jogo termina quando você descobre a palavra ou esgota as tentativas.

---

### 🔮 Personalização (Para Desenvolvedores)

Quer deixar o jogo com a sua cara? É muito simples!

O coração do jogo está na lista `palavras`:

```python
# Lista de palavras
palavras = ["python", "programacao", "computador", "desenvolvedor", "dados"]

Basta editar esta lista para adicionar seus próprios temas, como: palavras = ["frutas", "animais", "filmes"] 🍎🦁🎬

🤝 Contribuições
Pull requests e sugestões são sempre bem-vindas! Se quiser melhorar este projeto:

Faça um Fork do projeto.

Crie sua Branch de recurso: git checkout -b minha-melhoria.

Faça o Commit das suas mudanças.

Faça o Push para a Branch.

Abra um Pull Request.
