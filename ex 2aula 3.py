
HT = float(input("Informe a quantidade de horas trabalhadas no mês: "))
VH = float(input("Informe o valor da hora trabalhada: "))
PD = float(input("Informe o percentual de desconto: "))

SB = HT * VH

TD = (PD / 100) * SB

SL = SB - TD

50
print(f"Horas Trabalhadas: {HT:.2f}")
print(f"Salário Bruto: R${SB:.2f}")
print(f"Total de Desconto: R${TD:.2f}")
print(f"Salário Líquido: R${SL:.2f}")
