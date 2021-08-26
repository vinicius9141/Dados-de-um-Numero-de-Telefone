import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier


telefone = "+5512997357850"
telefoneAjustado = phonenumbers.parse(telefone)
print('Telefone formatado:> ', telefoneAjustado)

local = geocoder.description_for_number(telefoneAjustado, 'pt-br')
print('Localização do telefone (estado):> ', local)

operadora = carrier.name_for_number(telefoneAjustado, 'pt-br')
print('Operadora do telefone:> ', operadora)

