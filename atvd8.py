import math

def calcular_custo_tinta(altura, raio):
    litro_por_lata = 5
    cobertura_por_litro = 3
    preco_por_lata_1 = 50.00
    preco_por_lata_2 = 48.00
    preco_por_lata_3 = 46.00
    preco_por_lata_mais_3 = 45.00
    
    pi = 3.1415
    area_base = pi * raio ** 2
    perimetro = 2 * pi * raio
    area_lateral = altura * perimetro
    
    area_total = 2 * area_base + area_lateral
    litros_necessarios = area_total / cobertura_por_litro
    latas_necessarias = math.ceil(litros_necessarios / litro_por_lata)
    
    if latas_necessarias == 1:
        preco_total = latas_necessarias * preco_por_lata_1
    elif latas_necessarias == 2:
        preco_total = latas_necessarias * preco_por_lata_2
    elif latas_necessarias == 3:
        preco_total = latas_necessarias * preco_por_lata_3
    else:
        preco_total = latas_necessarias * preco_por_lata_mais_3
    
    return latas_necessarias, preco_total

altura = float(input("Informe a altura do cilindro (em metros): "))
raio = float(input("Informe o raio do cilindro (em metros): "))

latas, preco = calcular_custo_tinta(altura, raio)

print(f"Quantidade de latas necessárias: {latas}")
print(f"Custo total: R${preco:.2f}")
