#  Projeto Flask

Esse projeto foi feito utilizando [Flask](https://flask.palletsprojects.com/). 🧐

---

## Pré-requisitos

Esse projeto requer [flask](https://flask.palletsprojects.com/)
```
pip install Flask
```
Esse projeto requer [jsonify](https://pypi.org/project/jsonify/)
```
pip install jsonify
```
---
## Como usar?

Depois de ter instalado os requisitos, você deve usar o comando abaixo para inciar o **Flask**:
```
flask run
```
---
## Visão Geral

### A API apresenta dois recursos: 
- **Endpoint 1:** /repositories?q={repo}{&page,per_page,sort,order} 
  - **q**(sua pesquisa)
  - **page**(páginação)
  - **per_page**(quantidade de repositórios por página)
  - **sort**(forma como estão ordenados)
  - **order**(ordem dos itens)
- **Exemplo de uso:**
  ```
  /repositories?q=crypto&page=1&per_page=10&sort=updated&order=desc
  ```
  ---
- **Endpoint 2:** /repositorieuser/{user}
  - **user**(usuário que você quer pesquisar)
- **Exemplo de uso:**
  ```
  /repositorieuser/jayr0n
  ```
  ---
- **Endpoint 3:** /repository/{user}/{repo}
  - **user**(usuário que você quer pesquisar)
  - **repo**(repositório que você quer pesquisar)
- **Exemplo de uso:**
  ```
  /repository/jayr0n/UnfollowbyVisualRecognition
  ```

