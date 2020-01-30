# -*- coding: utf-8 -*-
def calcula_preco(value, **kwargs):
	taxa_percentual = kwargs.get('taxa_percentual')
	desconto = kwargs.get('desconto')

	if taxa_percentual:
		valor += valor*(taxa_percentual/100)
	
	if desconto:
		valor -= desconto

	return valor

print("Calculando o preço final sem desconto")
preco_final = calcula_preco(100.0)
print(preco_final)

print("Calculando o preço final com desconto")
preco_final = calcula_preco(100.0, desconto=5.0)
print(preco_final)

print("Calculando o preço com uma taxa percentual")
preco_final = calcula_preco(100.0, taxa_percentual=5.0)
print(preco_final)
