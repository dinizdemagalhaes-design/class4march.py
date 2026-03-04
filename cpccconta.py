valor = float(input("Digite o valor do pagamento:"))
conta = input("Digite o tipo de conta (corrente/poupanca):").lower()

if conta=="corrente":

    if valor <= 500:
         tarifa = valor * 0.30
    else:
        tarifa = valor * 0.20

elif conta == "poupanca":
    if valor <= 500:
        tarifa = valor * 0.10
    else:
        tarifa = valor * 0.05

else:
    print("Tipo de conta inválido")
    tarifa = 0

valor_final = valor - tarifa

print (f"Valor do pagamento: R$ {valor:}")
print (f"Tarifa cobrada: R$ {tarifa:}")
print (f"Valor final recebido: R$ {valor_final:}")
