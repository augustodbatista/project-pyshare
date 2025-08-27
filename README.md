# PyShare 🚀

A simple web service for temporary and secure file sharing. Upload a file and get a shareable link that expires in 24 hours. Built with a modern, cloud-native architecture.

---

### 🇧🇷 [Versão em Português](#pyshare-🇧🇷)

---

## 🇬🇧 English Version

### 🏛️ Architecture Overview

PyShare follows a decoupled, cloud-native architecture. The client-side application (frontend) is completely separate from the backend API, and all state (database and file storage) is handled by managed cloud services.

```
+----------------+      (1) Generate Upload URL      +------------------+
|                | --------------------------------> |                  |
|   Frontend     |      (3) Register File Info       |  Backend API     |
|   (Next.js)    | <-------------------------------- |  (FastAPI)       |
|                |      (2) Upload File Directly     |                  |
+----------------+ --------------------------------> +------------------+
      |                                                     |
      |                                                     |
      v                                                     v
+----------------+                                  +------------------+
|   AWS S3       |                                  |   Supabase       |
| (File Storage) |                                  | (PostgreSQL DB)  |
+----------------+                                  +------------------+
```

### 🛠️ Tech Stack

* **Frontend:** [Next.js](https://nextjs.org/) (React / TypeScript)
* **Backend:** [FastAPI](https://fastapi.tiangolo.com/) (Python)
* **Database:** [Supabase](https://supabase.com/) (Managed PostgreSQL)
* **File Storage:** [AWS S3](https://aws.amazon.com/s3/)
* **Deployment:** [Vercel](https://vercel.com/)

### ✨ Features

* [x] Secure generation of pre-signed URLs for direct-to-S3 uploads.
* [x] Temporary file sharing with links that expire after a set duration.
* [ ] Drag-and-drop file upload interface.
* [ ] Real-time upload progress bar.
* [ ] Clean and simple page for downloading files.
* [ ] Automated cleanup of expired files and database records.

### 🚀 Getting Started

To run this project locally, follow the steps below.

**1. Prerequisites:**

* Python 3.10+
* Node.js v18+ (we recommend using [nvm](https://github.com/nvm-sh/nvm))
* Git

**2. Clone the repository:**

```bash
git clone [https://github.com/seu-usuario/project-pyshare.git](https://github.com/seu-usuario/project-pyshare.git)
cd project-pyshare
```

**3. Setup Backend:**

* Navigate to the backend directory:
    ```bash
    cd backend
    ```
* Create and activate a virtual environment:
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```
* Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
* Create a `.env` file by copying the example and fill in your credentials:
    ```bash
    cp .env.example .env
    # Now, open the .env file and add your keys
    ```

**4. Setup Frontend:**

* Navigate to the frontend directory:
    ```bash
    cd ../frontend 
    # (from the backend folder)
    ```
* Install dependencies:
    ```bash
    npm install
    ```

**5. Run the application:**

* Run the backend server (from the `backend` directory):
    ```bash
    uvicorn app.main:app --reload
    ```
* In a new terminal, run the frontend server (from the `frontend` directory):
    ```bash
    npm run dev
    ```

---

## PyShare 🇧🇷

Um serviço web simples para o compartilhamento de arquivos de forma temporária e segura. Faça o upload de um arquivo e receba um link compartilhável que expira em 24 horas. Construído com uma arquitetura moderna e nativa da nuvem.

### 🏛️ Visão Geral da Arquitetura

O PyShare segue uma arquitetura desacoplada e nativa da nuvem. A aplicação do cliente (frontend) é completamente separada da API do backend, e todo o estado (banco de dados e armazenamento de arquivos) é gerenciado por serviços de nuvem.

*(Veja o diagrama na versão em inglês)*

### 🛠️ Stack Tecnológica

* **Frontend:** [Next.js](https://nextjs.org/) (React / TypeScript)
* **Backend:** [FastAPI](https://fastapi.tiangolo.com/) (Python)
* **Banco de Dados:** [Supabase](https://supabase.com/) (PostgreSQL Gerenciado)
* **Armazenamento de Arquivos:** [AWS S3](https://aws.amazon.com/s3/)
* **Deploy:** [Vercel](https://vercel.com/)

### ✨ Funcionalidades

* [x] Geração segura de URLs pré-assinadas para upload direto para o S3.
* [x] Compartilhamento de arquivos temporários com links que expiram.
* [ ] Interface de "arrastar e soltar" para upload de arquivos.
* [ ] Barra de progresso de upload em tempo real.
* [ ] Página limpa e simples para download de arquivos.
* [ ] Limpeza automatizada de arquivos e registros expirados no banco de dados.

### 🚀 Como Executar Localmente

Para rodar este projeto localmente, siga os passos abaixo.

**1. Pré-requisitos:**

* Python 3.10+
* Node.js v18+ (recomendamos o uso do [nvm](https://github.com/nvm-sh/nvm))
* Git

**2. Clone o repositório:**

```bash
git clone [https://github.com/seu-usuario/project-pyshare.git](https://github.com/seu-usuario/project-pyshare.git)
cd project-pyshare
```

**3. Configure o Backend:**

* Navegue até o diretório do backend:
    ```bash
    cd backend
    ```
* Crie e ative um ambiente virtual:
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```
* Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```
* Crie um arquivo `.env` copiando o exemplo e preencha suas credenciais:
    ```bash
    cp .env.example .env
    # Agora, abra o arquivo .env e adicione suas chaves
    ```

**4. Configure o Frontend:**

* Navegue até o diretório do frontend:
    ```bash
    cd ../frontend 
    # (a partir da pasta backend)
    ```
* Instale as dependências:
    ```bash
    npm install
    ```

**5. Execute a aplicação:**

* Execute o servidor do backend (a partir da pasta `backend`):
    ```bash
    uvicorn app.main:app --reload
    ```
* Em um novo terminal, execute o servidor do frontend (a partir da pasta `frontend`):
    ```bash
    npm run dev
    ```