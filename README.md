# Geo-Explorer 🚀

O Geo-Explorer reúne duas experiências: uma interface web para descobrir trilhas ao ar livre e uma ferramenta Python para explorar trilhas de aprendizagem em tecnologia. O projeto também disponibiliza as funções de aprendizagem como ferramentas de um servidor MCP (Model Context Protocol).

## 🥾 Interface web

A página apresenta trilhas com região, dificuldade, distância, duração, tipo e coordenadas. É possível filtrar as trilhas por dificuldade.

Para iniciar o servidor web local na raiz do projeto:

```bash
python3 -m http.server 8000
```

Depois, acesse [http://localhost:8000](http://localhost:8000).

## 🧑‍💻 Trilhas de aprendizagem via terminal

### Instalação

Requer Python 3. Instale as dependências com:

```bash
python -m pip install -r requirements.txt
```

### Comandos

```bash
python main.py trilha python
python main.py desafio python iniciante
python main.py certificado "Seu Nome" python
```

As tecnologias disponíveis são `python`, `java` e `cybersecurity`. Os níveis de desafio são `iniciante`, `intermediario` e `avancado`. Os certificados são fictícios.

## 🔌 Servidor MCP

Inicie o servidor MCP com:

```bash
python src/mcp_server.py
```

O servidor expõe as ferramentas `trilha`, `desafio` e `certificado`.

## 🧪 Testes

Execute os testes com:

```bash
python -m pytest
```

## 📁 Estrutura do projeto

- `data/trilhas.json` — dados das trilhas ao ar livre exibidas na página.
- `data/trilhas-aprendizado.json` — trilhas de tecnologia e desafios usados pela CLI e pelo servidor MCP.
- `index.html` — página principal da interface web.
- `src/main.js` e `src/styles.css` — lógica e estilos da interface web.
- `main.py` — interface de linha de comando para trilhas de aprendizagem.
- `src/` — módulos Python para trilhas, desafios, certificados e servidor MCP.
- `tests/` — testes automatizados da aplicação Python.
