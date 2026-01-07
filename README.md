![Status](https://img.shields.io/badge/Status-Concluído-green?style=for-the-badge)
# 🚢 Batalha Naval com Comando de Voz

Um jogo clássico de Batalha Naval desenvolvido em Python, com um diferencial moderno: **você joga falando as coordenadas!**

O projeto utiliza a biblioteca **Flet** para a interface gráfica e **SpeechRecognition** para capturar e processar os comandos de voz do jogador.

**Projeto desenvolvido como Nota final da disciplina de algoritmos(2024.1)** 

## 📸 Screenshots
<br><br>
<code>Tela inicial</code>
<img width="1919" height="1019" alt="Captura de tela 2026-01-02 120141" src="https://github.com/user-attachments/assets/e5ee819a-74de-41c5-94e3-7cfd065dbbbf" />
<br><br>
<code>Escolha de dificuldade</code>
<img width="1918" height="1016" alt="Captura de tela 2026-01-02 120210" src="https://github.com/user-attachments/assets/1cfeb8aa-a277-44d6-bcfd-feed96dba6ad" />
<br><br>
<code>Visualização do seu tabuleiro</code>
<img width="1919" height="1022" alt="Captura de tela 2026-01-02 120300" src="https://github.com/user-attachments/assets/d973b2cb-cd7c-44e2-9526-e859fff27860" />
<br><br>
<code>Jogo em andamento</code>
<img width="1919" height="1029" alt="Captura de tela 2026-01-02 120401" src="https://github.com/user-attachments/assets/af30bdd2-c12b-4d8e-add8-d1f67bcdf810" />

## ✨ Funcionalidades

-   **Comando de Voz:** Dite as coordenadas (ex: "zero zero", "dois cinco") para realizar seus ataques.
-   **Interface Gráfica:** Visualização clara dos tabuleiros (Jogador vs Computador) usando Flet.
-   **Níveis de Dificuldade:**
    -   🟢 Fácil
    -   🟡 Médio
    -   🔴 Difícil
    -   ☠️ Modo Kézia (Desafio personalizado com tabuleiro pre-programado para fins de apresentação)
-   **Feedback Visual:** Cores diferentes para água, navios, acertos e erros.
-   **Lógica de Jogo:** O computador joga contra você, evitando repetir jogadas e caçando seus navios.

## 🛠️ Tecnologias Utilizadas

* [Python 3](https://www.python.org/)
* [Flet](https://flet.dev/) (Interface Gráfica)
* [SpeechRecognition](https://pypi.org/project/SpeechRecognition/) (Reconhecimento de Voz)

## 🚀 Como executar o projeto

### Pré-requisitos

Você precisa ter o Python instalado em sua máquina. Além disso, é necessário instalar as bibliotecas utilizadas.

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/SEU-USUARIO/SEU-REPOSITORIO.git](https://github.com/SEU-USUARIO/SEU-REPOSITORIO.git)
    cd SEU-REPOSITORIO
    ```

2.  **Crie um ambiente virtual (Opcional, mas recomendado):**
    ```bash
    python -m venv venv
    # No Windows:
    venv\Scripts\activate
    # No Linux/Mac:
    source venv/bin/activate
    ```

3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```
    *Nota: A biblioteca `pyaudio` é necessária para usar o microfone. Se tiver problemas na instalação dela, consulte a documentação oficial para o seu sistema operacional.*

4.  **Execute o jogo:**
    ```bash
    python main.py
    ```

## 🎮 Como Jogar

1.  Ao abrir o jogo, clique em **"Jogar"**.
2.  Escolha a **Dificuldade** desejada.
3.  Visualize o posicionamento dos seus navios e clique em **"Começar jogo"**.
4.  Quando for sua vez ("Turno do Jogador"):
    * Clique no botão **"Atacar"**.
    * O sistema dirá "Escutando...".
    * Fale dois números correspondentes à Linha e Coluna que deseja atacar (ex: "três quatro" para atacar a linha 3, coluna 4).
    * **Dica:** Fale pausadamente para garantir que o reconhecimento entenda os números.

## 🧩 Estrutura do Projeto

* `main.py`: Arquivo principal que gerencia a interface (GUI) e o fluxo do jogo.
* `logica.py`: Contém as regras do jogo, geração de tabuleiros, lógica do computador e verificação de vitória.
* `reconhecimento_de_voz.py`: Módulo responsável por capturar o áudio do microfone e transformar em texto/coordenadas.

## ⚠️ Limitações Conhecidas
- O reconhecimento de voz pode falhar em ambientes muito ruidosos.
- A biblioteca `pyaudio` pode apresentar dificuldades de instalação em alguns sistemas.

## 🤝 Contribuidores
<table>
  <tr>
    <td align="center">
      <a href="https://github.com/julioP-dev">
        <img src="https://github.com/julioP-dev.png" width="100px;" alt="Foto de Júlio"/><br>
        <sub>
          <b>Júlio Pedro</b>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/LittleNeto">
        <img src="https://github.com/LittleNeto.png" width="100px;" alt="Foto de josé Neto"/><br>
        <sub>
          <b>josé Neto</b>
        </sub>
      </a>
    </td>
     <td align="center">
      <a href="https://github.com/mateuserikNA">
        <img src="https://github.com/mateuserikNA.png" width="100px;" alt="Foto de Mateus"/><br>
        <sub>
          <b>Mateus Erik</b>
        </sub>
      </a>
    </td>
  </tr>
</table>


## 📝 Licença

Este projeto está sob a licença MIT.
