def constants():
    INSS = 0.08
    IMPOSTO_RENDA = 0.11
    SINDICATO = 0.05
    
    return INSS, IMPOSTO_RENDA, SINDICATO

def calculos(salario, num_hrs):
    inss, imposto_renda, sindicato = constants()

    calculo_inss = salario * num_hrs * inss
    calculo_imposto_renda = salario * num_hrs * imposto_renda
    calculo_sindicato = salario * num_hrs * sindicato
    salario_bruto = salario * num_hrs

    salario_liquido = salario_bruto - (calculo_inss + calculo_imposto_renda + calculo_sindicato)

    return salario_bruto, calculo_inss, calculo_imposto_renda, calculo_sindicato, salario_liquido

def question_to_user():
    salario = float(input('Digite o seu salário por hora:\n'))
    num_hrs = int(input('\nDigite quantas horas você trabalha no mês:\n'))
    
    salario_bruto, calculo_inss, calculo_imposto_renda, calculo_sindicato, salario_liquido = calculos(salario, num_hrs)
    
    print(f"\nSalário Bruto: R${salario_bruto:.2f}")
    print(f"Desconto INSS: R${calculo_inss:.2f}")
    print(f"Desconto Imposto de Renda: R${calculo_imposto_renda:.2f}")
    print(f"Desconto Sindicato: R${calculo_sindicato:.2f}")
    print(f"Salário Líquido: R${salario_liquido:.2f}")
    

if __name__ == '__main__':
    question_to_user()