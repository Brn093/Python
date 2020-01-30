

def dados_pessoais(nome, sobrenome, idade, casado):
    print("Nome: {}\n SobreNome: {}\n Idade: {}\n Casado: {}\n" .format(nome, sobrenome, idade, casado))

# argumentos nomeados
dados_pessoais(idade=40, sobrenome="lopes", nome="norberto", casado=True)

# argumentos posicionais
dados_pessoais(
        idade=30,
        sobrenome="Miranda",
        nome="montenegro",
        casado=True
        )
