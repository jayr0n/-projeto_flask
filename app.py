import requests
from flask import Flask, jsonify, request
from utils_transform.utils import repo_transform, user_transform


app = Flask(__name__)

# Variáveis globais para alterar o display do JSON
false = False
true = True 
null = None

# Pesquisa o repositório pelo nome
# https://api.github.com/search/repositories?q=script&page=1&per_page=30&sort=updated-desc&order=desc
@app.route('/repositories', methods=['GET'])
def get_github_repositories():
    repo = request.args.get('q', default='script lol', type=str)
    page = request.args.get('page', default=1, type=int)
    order = request.args.get('order', default='desc', type=str)
    sort = request.args.get('sort', default='updated-desc', type=str)
    per_page = request.args.get('per_page', default=30, type=int)

    url = f'https://api.github.com/search/repositories?q={repo}&page={page}&per_page={per_page}&sort={sort}&order={order}'

    response = requests.get(url)

    if response.status_code == 200:
        resultados = [repo_transform(i) for i in dict(response.json())["items"]]
        return jsonify(resultados)
    else:
        return jsonify({'error': 'Repositório não encontrado ou falha na solicitação de API'}), 404

# Pesquisa os repositórios relacionados ao nome do usuário
# https://api.github.com/users/{user}/repos
@app.route('/repositorieuser/<user>', methods=['GET'])
def get_github_repositories_by_user(user):
    url = f'https://api.github.com/users/{user}/repos'
    
    response = requests.get(url)

    if response.status_code == 200:
        resultados_user = [user_transform(dict(i)) for i in response.json()]

        return jsonify(resultados_user)
    else:
        return jsonify({'error': 'Usuário não encontrado ou falha na solicitação de API'}), 404

# Pesquisa o repositório de acordo com o usuário
# https://api.github.com/repos/jayr0n/UnfollowbyVisualRecognition
@app.route('/repository/<user>/<repo>')
def get_github_repository(user, repo):
    url = f'https://api.github.com/repos/{user}/{repo}'

    response = requests.get(url)

    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({'error': 'Usuário/Repositório não encontrado ou falha na solicitação de API'}), 404

if __name__ == "__main__":
    app.run(debug=True)
