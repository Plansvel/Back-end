<h1>Plansvel Backend</h1>
<h2>Instalação e Execução:</h2>



> Clone o repositório:
```bash 
git clone https://github.com/Plansvel/Back-end
``````
> Crie uma branch para a feature que você vai adicionar:
```bash
git checkout -b minha-feature
```
<h3>Dependências:</h3>

> Instale o virtualenv:
   
   ```bash
   pip install virtualenv
   ```

> Crie um ambiente virtual: 

```bash
python -m venv env
```
<br>

> Execute o ambiente virtual:

*Windows:*
```bash
.\env\Scripts\activate.ps1
```

<br>

*Linux:*

```bash
source env/bin/activate
```
<br>
<br>

> Entre no diretório e Instale as dependências do projeto 

*Windows:*
```bash
cd Back-end ; pip install -r requirements.txt 

```
*Linux:*
```bash
cd Backend && pip install -r requirements.txt
```

<h3>Executando</h3>

> Entre no diretório

```bash
cd app 
```
> Execute
```bash
uvicorn main:app
```

> Execute Modo de Depuração
```bash
uvicorn main:app --reload
```
