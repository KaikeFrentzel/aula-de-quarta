ano_atual = int(input("Digite o ano atual: "))
ano_nascimento = int(input("Digite o seu ano de nascimento: "))


idade = ano_atual - ano_nascimento


if idade >= 18:
    print("Você pode tirar a CNH!")
