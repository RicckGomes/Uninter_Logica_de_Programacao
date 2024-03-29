"""
3 - Escreva um programa que calcule o preço a pagar pelo fornecimento de energia elétrica.
Pergunte a quantidade de kWh consumida e o tipo de instalação: R para residências, I para 
indústrias e C para comércios.

calcule o preço de acordo com os dados a seguir:
Residencial: 
até 500 kWh = R$0,40.
acima de 500 kWh = R$0,65.

Comercial:
até 1000 kWh = R$0,55.
acima de 1000 kWh = R$0,60.

Industrial:
até 5000 kWh = R$0,55.
acima de 5000 kWh = R$0,60.
"""

# Até 500 kWh
kResidenciaMin = 0.40;
# Acima de 500 kWh
kResidenciaMax = 0.65;
# Até 1000 kWh
kComercioMin   = 0.55;
# Acima de 1000 kWh
kComercioMax   = 0.60;
# Até 5000 kWh
kIndustriaMin  = 0.55;
# Acima de 5000 kWh
kIndustriaMax  = 0.60;
print("=" * 90);
tipoInstalacao = int(input("Informe o tipo de instalação: 1 - Residencial | 2 - Comercial | 3 - Industrial: "));
consumo = float(input("Informe o consumo de energia: "));

if (tipoInstalacao == 1) and (consumo <= 500):
    print("O tipo de instalação é residencial, o valor total é: R$", kResidenciaMin * consumo);
elif (tipoInstalacao == 1) and (consumo > 500):
    print("O tipo de instalação é residencial, o valor total é: R$", kResidenciaMax * consumo);
elif (tipoInstalacao == 2) and (consumo <= 1000):
    print("O tipo de instalação é comercial, o valor total é: R$", kComercioMin * consumo);
elif (tipoInstalacao == 2) and (consumo > 1000):
    print("O tipo de instalação é comercial, o valor total é: R$", kComercioMax * consumo);
elif (tipoInstalacao == 3) and (consumo <= 5000):
    print("O tipo de instalação é industrial, o valor total é: R$", kIndustriaMin * consumo);
else:
    print("O tipo de instalação é industrial, o valor total é: R$", kIndustriaMax * consumo);
print("=" * 90);
print();