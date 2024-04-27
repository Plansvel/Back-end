<h1>Plansvel Backend</h1>
<p>Aqui resida o backend de nosso Projeto.</p>
<h2>Instalação e Building</h2>
<h3>Git</h3>
<ul>
    <li>Clone o repositório. <code>git clone https://github.com/Plansvel/Back-end</code></li>
    <li>Crie uma branch para a feature que você vai adicionar. <code>git checkout -b minha-feature</code></li>
</ul>
<h3>Dependências</h3>
<ul>
    <li>Instale o virtualenv <code>pip install virtualenv</code></li>
    <li>Crie um ambiente virtual <code>python -m venv env</code></li>
    <li>(Windows) Rode esse ambiente virtual <code>env\Scripts\activate.bat</code> ou <code>env\Scripts\activate.ps1</code></li>
    <li>(Linux) Rode esse ambiente virtual <code>env\Scripts\activate</code>></li>
    <li>Instale as dependências do projeto <code>pip install -r requirements.txt</code></li>
</ul>
<h3>Rodando</h3>
<ul>
    <li>Entre na pasta app. <code>cd app</code></li>
    <li>Rode a aplicação. <code>uvicorn main:app</code> ou <code>uvicorn main:app --reload</code></li>
</ul>