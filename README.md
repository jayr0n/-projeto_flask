#  Projeto Flask

Esse projeto foi feito utilizando [Flask](https://flask.palletsprojects.com/). 🧐

## Pré-requisitos

Esse projeto requer [flask](https://flask.palletsprojects.com/)

```
pip install Flask
```

Esse projeto requer [jsonify](https://pypi.org/project/jsonify/)

```
pip install jsonify
```
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

