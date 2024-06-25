pessoa = {
    "Nome":"Aparicio",
    "email":"aparicio@cesul.com.br",
    "idade": 30
}

print("Chaves em pessoa:")
for chave in pessoa:
    print(chave)

print("-" * 10)

print("Valores em pessoa:")
for valor in pessoa.values():
    print(valor)

print("-" * 10)

print("Itens em pessoa:")
for chave, valor in pessoa.items():
    print(f"Chaves:{chave} | Valor: {valor}")