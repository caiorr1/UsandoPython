import requests
import json

response_baralho = requests.get('https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1')
baralho = response_baralho.json()
print(baralho)

deck_id = baralho['deck_id']
response_carta = requests.get(f'https://deckofcardsapi.com/api/deck/3xmbqqvbst4n/draw/?count=2')

carta = response_carta.json()['cards'][0]
print(response_carta)

valor = input('informe o valor da carta: ')
naipe = input('informe o naipe: ').upper()
dicionario_naipes = {
    'COPAS' : 'HEARTS',
    'PAUS' : 'CLUBS',
    'ESPADAS' : 'SPADES',
    'OUROS' : 'DIAMONDS'    
}
if carta['value'] == valor:
    print('LEGAL')
else:
    print('CHATO')