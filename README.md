# IA Project

###### [EN] This project was developed for college subject Artificial Intelligence to the course Systems Analysis and Development at Fatec de Cruzeiro-SP.
###### [PT-BR] Este projeto foi desenvolvido para a disciplina de Inteligência Artificial do curso Análise e Desenvolvimento de Sistemas da Fatec de Cruzeiro-SP.


## [EN] Libraries and Tools
## [PT-BR] Bibliotecas e ferramentas

### Backend

* 🐍 [Python](https://www.python.org/)
* 🧪 [Flask](https://flask.palletsprojects.com/en/2.3.x/)


### Frontend
* 🖥️ [HTML5](https://developer.mozilla.org/en-US/docs/Glossary/HTML5)
* ⚡️ [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
* ✨ [Javascript](https://developer.mozilla.org/en-US/docs/Web/javascript)


## Project Setup

[EN] First, create a virtual env to host the project dependencies.
Install the necessary dependencies with the following commands:

[PT-BR]Primeiro, crie um ambiente virtual para hospedar as dependências do projeto.
Instale as dependências necessárias com os seguintes comandos:

Linux:

```bash
cd Backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Windows:

```bash
cd Backend
python3 -m venv .venv
env\Scripts\activate.bat
pip install -r requirements.txt
```

[EN] Then, initialize the API server:
[PT] Em seguida, inicialize o servidor API:

```bash
python3 main.py
```