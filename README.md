# 📦 Desafio Técnico Cotefácil

Crawler desenvolvido com **Scrapy** para realizar login no portal **Servimed**, coletar informações de produtos e gerar dinamicamente um arquivo `products.json` contendo a base completa de produtos.

---

## 🔍 Observações

* As requisições são enviadas **uma a uma** até que seja encontrada uma resposta com lista vazia.
* A API da Servimed limita a quantidade de registros retornados para **25 itens por requisição**.
* O processo é interrompido automaticamente quando não há mais produtos disponíveis para consulta.

---

## ⚙️ Configuração

Antes de executar o projeto, configure as seguintes variáveis de ambiente:

```env
USER=pharmagold@gmail.com
PASSWORD=a007299A
```

---

## 🚀 Instalação

### 1. Clone o repositório

```bash
git clone https://github.com/VictorLourenco-ctf/Desafio_Tecnico_Cotefacil.git
```

### 2. Acesse o diretório do projeto

```bash
cd Desafio_Tecnico_Cotefacil
```

### 3. Ative o ambiente virtual

#### Windows (PowerShell)

```powershell
.venv\Scripts\Activate.ps1
```

#### Linux / macOS (Bash ou Zsh)

```bash
source .venv/bin/activate
```

### 4. Instale as dependências

```bash
uv sync
```

---

## ▶️ Executando o Crawler

Para iniciar o processo de coleta dos produtos, execute:

```bash
python run_spider.py --usuario "meu@email.com" --senha "minha_senha"
```

---

## 📄 Resultado

Ao final da execução será gerado um arquivo:

```text
products.json
```

na raiz do projeto, contendo todos os produtos coletados durante o processamento.

---

## 🛠️ Tecnologias Utilizadas

* Python 3.13+
* Scrapy
* UV
* Requests
* JWT

---

## 📂 Arquivos Gerados

| Arquivo         | Descrição                                       |
| --------------- | ----------------------------------------------- |
| `products.json` | Base de produtos retornada pela API da Servimed |

---

## 📌 Fluxo de Execução

1. Realiza autenticação no portal Servimed utilizando as credenciais informadas.
2. Obtém o token de acesso necessário para as requisições.
3. Consulta os produtos de forma paginada.
4. Continua realizando requisições até encontrar uma página sem registros.
5. Consolida os resultados em um único arquivo `products.json`.
