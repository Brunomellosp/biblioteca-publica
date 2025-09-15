
# Sistema de Gestão da Biblioteca Pública — MVP (Semana 2)

Este repositório atende **aos entregáveis da Semana 2**:

- ✅ **Quadro Kanban (Trello)** — já criado pelo grupo (anexado pelo aluno).
- ✅ **Repositório Git com estrutura inicial** (front, back, configs).
- ✅ **Primeiro fluxo funcional implementado**: **Cadastro de Usuário → Upload de documentos → Persistência no banco**.

## Arquitetura (alto nível)

- **Front-end (estático)**: formulário HTML simples (`frontend/index.html`) que envia `multipart/form-data` para a API.
- **Back-end (FastAPI + SQLAlchemy)**: endpoints REST, validação, salvamento de arquivos e persistência em **SQLite**.
- **Uploads**: armazenados em `uploads/` (serviço estático em `/uploads` apenas para testes).
- **Banco**: SQLite padrão (`app.db`). Pode usar Postgres mudando `DATABASE_URL` no `.env`.

## Estrutura de pastas

```
biblioteca-publica-semana2/
├── backend/
│   ├── main.py              # App FastAPI + montagem de rotas/arquivos estáticos
│   ├── database.py          # Engine/Session do SQLAlchemy + Base
│   ├── models.py            # Tabela Usuario
│   ├── schemas.py           # Pydantic (entrada/saída)
│   └── routers/
│       └── usuarios.py      # POST /usuarios (fluxo MVP)
├── frontend/
│   └── index.html           # Formulário de cadastro
├── uploads/                 # Destino de documentos (git-ignored)
├── .env.example             # Exemplo de variáveis
├── requirements.txt
├── .gitignore
└── README.md
```

## Como rodar (Windows, macOS ou Linux)

> Recomendado: **Python 3.11+**

1) **Clone** este projeto e entre na pasta:
```bash
git clone <seu-fork-ou-repo>.git
cd biblioteca-publica-semana2
```

2) **Crie e ative o ambiente virtual**:
```bash
# Windows (PowerShell)
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# macOS/Linux
python3 -m venv .venv
source .venv/bin/activate
```

> Se aparecer erro de *Execution Policy* no Windows, abra o PowerShell **como administrador** e rode:
> ```powershell
> Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
> ```

3) **Instale as dependências**:
```bash
pip install -r requirements.txt
```

4) **Configure variáveis de ambiente**:
```bash
copy .env.example .env   # Windows
# ou
cp .env.example .env     # macOS/Linux
```
- (opcional) Edite `.env` e troque `DATABASE_URL` para Postgres, por exemplo:
  `DATABASE_URL=postgresql+psycopg2://user:pass@localhost:5432/biblioteca`

5) **Suba a API** (na raiz do projeto):
```bash
uvicorn backend.main:app --reload
```
Acesse **http://127.0.0.1:8000/docs** (Swagger) para testar o endpoint.

6) **Abra o formulário**:
- Clique em `frontend/index.html` e use o formulário **Cadastro de Usuário**.
- Ao salvar, os arquivos são guardados em `uploads/` e o registro é persistido em `app.db`.

## Endpoint implementado (MVP)

### `POST /usuarios` — *multipart/form-data*

Campos:
- `nome` (obrigatório)
- `email` (obrigatório, validado)
- `telefone` (opcional)
- `endereco` (opcional)
- `documento` (upload opcional: PNG/JPG/PDF)
- `comprovante` (upload opcional: PNG/JPG/PDF)

Retorna `201 Created` com o objeto cadastrado.

### Teste por `curl`
```bash
curl -X POST "http://127.0.0.1:8000/usuarios" ^
  -F "nome=Maria da Silva" ^
  -F "email=maria@example.com" ^
  -F "telefone=11999999999" ^
  -F "endereco=Rua A, 123" ^
  -F "documento=@/caminho/rg.pdf" ^
  -F "comprovante=@/caminho/conta_luz.jpg"
```

## Próximos passos sugeridos (Semana 3+)

- Autenticação (JWT) e perfis (bibliotecário x leitor).
- CRUD de **Livro** e **Exemplar** com leitura de **código de barras**.
- Fluxo **Empréstimo/Devolução** (com regras e multas).
- Notificações por e-mail (atrasos).
- Relatórios (CSV/PDF).

---

> Qualquer dúvida, abra uma *issue* no repositório ou me chame. Boa entrega! 🚀
