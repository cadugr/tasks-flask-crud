# Tasks API com Flask

Este é um projeto de uma simples API RESTful para gerenciamento de tarefas, desenvolvido em Python com o framework Flask. O projeto foi criado como um estudo inicial sobre o desenvolvimento de APIs com Flask.

## Funcionalidades

- Criar uma nova tarefa
- Listar todas as tarefas
- Obter uma tarefa específica por ID
- Atualizar uma tarefa existente
- Deletar uma tarefa

## Pré-requisitos

Antes de começar, você vai precisar ter instalado em sua máquina as seguintes ferramentas:
- [Python 3.10+](https://www.python.org/downloads/)
- [Pip](https://pip.pypa.io/en/stable/installation/) (geralmente já vem com o Python)
- [Git](https://git-scm.com/downloads)

## Como Rodar o Projeto

Siga os passos abaixo para executar o projeto em seu ambiente local:

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/cadugr/tasks-flask-crud.git
    cd tasks-flask-crud
    ```

2.  **Crie e ative um ambiente virtual:**
    ```bash
    # Para macOS/Linux
    python3 -m venv .venv
    source .venv/bin/activate

    # Para Windows
    python3 -m venv .venv
    .venv\Scripts\activate
    ```

3.  **Instale as dependências:**
    ```bash
    pip3 install -r requirements.txt
    ```

4.  **Execute a aplicação:**
    ```bash
    python3 app.py
    ```
    O servidor estará rodando em `http://127.0.0.1:5000`.

## Endpoints da API

Você pode testar os endpoints da API usando uma ferramenta como o [Postman](https://www.postman.com/) ou `curl`.

#### Criar uma nova tarefa

- **Método:** `POST`
- **URL:** `/tasks`
- **Corpo da Requisição (JSON):**
  ```json
  {
    "title": "Minha primeira tarefa",
    "description": "Esta é a descrição da minha tarefa."
  }
  ```
- **Exemplo com `curl`:**
  ```bash
  curl -X POST -H "Content-Type: application/json" -d '''{"title": "Minha primeira tarefa", "description": "Descrição da tarefa"}''' http://127.0.0.1:5000/tasks
  ```

#### Listar todas as tarefas

- **Método:** `GET`
- **URL:** `/tasks`
- **Exemplo com `curl`:**
  ```bash
  curl http://127.0.0.1:5000/tasks
  ```

#### Obter uma tarefa por ID

- **Método:** `GET`
- **URL:** `/tasks/<id>`
- **Exemplo com `curl` (substitua `1` pelo ID da tarefa):**
  ```bash
  curl http://127.0.0.1:5000/tasks/1
  ```

#### Atualizar uma tarefa

- **Método:** `PUT`
- **URL:** `/tasks/<id>`
- **Corpo da Requisição (JSON):**
  ```json
  {
    "title": "Título Atualizado",
    "description": "Descrição Atualizada",
    "completed": true
  }
  ```
- **Exemplo com `curl` (substitua `1` pelo ID da tarefa):**
  ```bash
  curl -X PUT -H "Content-Type: application/json" -d '''{"title": "Título Atualizado", "description": "Descrição Atualizada", "completed": true}''' http://127.0.0.1:5000/tasks/1
  ```

#### Deletar uma tarefa

- **Método:** `DELETE`
- **URL:** `/tasks/<id>`
- **Exemplo com `curl` (substitua `1` pelo ID da tarefa):**
  ```bash
  curl -X DELETE http://127.0.0.1:5000/tasks/1
  ```

## Executando os Testes

O projeto possui um conjunto de testes automatizados para garantir a qualidade do código. Para executá-los, utilize o `pytest`:

```bash
pytest tests.py -v
```
