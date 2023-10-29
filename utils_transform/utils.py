# Definindo os valores que serão retornados na pesquisa por repositório
def repo_transform(item):
    data = {
            "id" : item['id'], 
            "user_repo" : item['full_name'], 
            "user" : { 
                "login" : item['owner']['login'],
                "url_user" : item['owner']['url'],
            }, 
            "description" : item['description'], 
            "clone_url" : item['clone_url'], 
            "programming_language" : item['language'] , 
            "visibility" : item['visibility'],
            "forks" : item['forks'], 
            "watchers" : item['watchers'],
            }
    return data

# Definindo os valores que serão retornados na pesquisa por usuário
def user_transform(item):
    data = {
            "user" : item['owner']['login'], 
            "repository_name" : item['name'],
            "url_repository" : item['html_url'],
            "visibility" : item['visibility'],
            "programming_language" : item['language'], 
            "watchers_count" : item['watchers_count'],
            }
    
    return data