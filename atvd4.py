salario = float(input("Digite o salário do funcionário: R$ "))

if salario > 1250.00:
    aumento = salario * 0.10
    novo_salario = salario + aumento
    print(f"Salário: R$ {salario:.2f}")
    print(f"Aumento de 10%. Novo salário: R$ {novo_salario:.2f}")
elif salario <= 1250.00:
    aumento = salario * 0.15
    novo_salario = salario + aumento
    print(f"Salário: R$ {salario:.2f}")
    print(f"Aumento de 15%. Novo salário: R$ {novo_salario:.2f}")
