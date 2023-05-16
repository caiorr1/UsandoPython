import requests

# Requisição do Site
response = requests.get('https://www.youtube.com')

# Código de Status do Site
print('Status code: ', response.status_code)

# Cabeçalho do site
print('Header')
print(response.headers)

# Conteúdo HTML do Site
print('\n Content')
print(response.content)