# 📂 Simple File Server

Servidor simples de arquivos feito com **Flask + Tailwind CSS**, permitindo:

* ✅ Listar arquivos
* ✅ Download
* ✅ Upload
* ✅ Exclusão
* ✅ Interface moderna com Tailwind CDN
* ✅ Execução isolada via `venv`


## 📁 Estrutura do Projeto

```
/root/
 ├── file_server.py
 ├── init.sh
 ├── venv/
 └── downloads/
```

* `file_server.py` → servidor Flask
* `init.sh` → script de inicialização
* `venv/` → ambiente virtual Python
* `downloads/` → pasta onde os arquivos ficam disponíveis


# 🚀 Instalação

## 1️⃣ Criar diretório do projeto

```bash
cd /root
mkdir downloads
```


## 2️⃣ Criar ambiente virtual

```bash
python3 -m venv venv
```


## 3️⃣ Instalar dependências

```bash
source venv/bin/activate
pip install flask
deactivate
```


# ▶️ Execução

## Opção recomendada (via script)

Edite o arquivo `init.sh`:

```bash
#!/bin/bash

cd /root
./venv/bin/python file_server.py
```

Dar permissão:

```bash
chmod +x init.sh
```

Executar:

```bash
./init.sh
```


## Acessar no navegador

Se estiver rodando na porta 80:

```
http://IP_DO_SERVIDOR
```

Se estiver usando porta 8080:

```
http://IP_DO_SERVIDOR:8080
```


# 🛑 Porta 80 exige root

Se rodar na porta 80, será necessário executar como root.

Para rodar como usuário comum, altere no `file_server.py`:

```python
app.run(host="0.0.0.0", port=8080)
```


# 📦 Dependências

* Python 3.8+
* Flask


