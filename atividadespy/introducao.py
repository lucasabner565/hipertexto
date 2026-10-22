#atividade1

nome_moto = input("Digite o nome do motorista: ")
distancia = int(input("Digite a distância percorrida em km: "))
litros = float(input("Digite a quantidade de litros consumidos: "))
preco_litro = float(input("Digite o preço do litro de combustível: "))
consumo_medio = distancia / litros
print ("O consumo médio do veículo é de: ", consumo_medio, "km/l")
valor_gasto = litros * preco_litro
print ("O valor gasto com combustível é de: R$ ", valor_gasto)

#atividade2

segundos = int(input("Digite o tempo em segundos: "))
horas = segundos / 3600
print ("O tempo em horas é de: ", horas, "h")
minutos = (segundos % 3600) / 60
print ("O tempo em minutos é de: ", minutos, "min")
segundos_restantes = segundos % 60
print ("O tempo em segundos é de: ", segundos_restantes, "s")

#atividade3

nome_funcionario = input("Digite o nome do funcionário:" )
salario_bruto = float(input("Digite o salário bruto do funcionário: "))
percentual_inss = float(input("Digite o percentual de desconto do INSS: "))
percentual_plano_saude = float(input("Digite o percentual de desconto do plano de saúde: "))
valor_inss = salario_bruto * (percentual_inss / 100)
print ("O valor do desconto do INSS é de: R$ ", valor_inss)
valor_plano_saude = salario_bruto * (percentual_plano_saude / 100)
print ("O valor do desconto do plano de saúde é de: R$ ", valor_plano_saude)
total_descontos = valor_inss + valor_plano_saude
print ("O total de descontos é de: R$ ", total_descontos)
salario_liquido = salario_bruto - total_descontos
print ("O salário líquido do funcionário é de: R$ ", salario_liquido)

#atividade4

nome_produto = input("Digite o nome do produto: ")
preco_produto = float(input("Digite o preço do produto: "))
quantidade_comprada = int(input("Digite a quantidade comprada: "))
percentual_desconto = float(input("Digite o percentual de desconto: "))
numero_parcelas = int(input("Digite o número de parcelas: "))
valor_bruto = preco_produto * quantidade_comprada
print ("O valor bruto da compra é de: R$ ", valor_bruto)
valor_desconto = valor_bruto * (percentual_desconto / 100)
print ("O valor do desconto é de: R$ ", valor_desconto)
valor_final = valor_bruto - valor_desconto
print ("O valor final da compra é de: R$ ", valor_final)
valor_parcela = valor_final / numero_parcelas
print ("O valor de cada parcela é de: R$ ", valor_parcela)

#atividade5

prova1 = float(input("Digite a nota da primeira prova: "))
peso1 = 2
prova2 = float(input("Digite a nota da segunda prova: "))
peso2 = 3
projeto = float(input("Digite a nota do projeto: "))
peso_projeto = 5
media_ponderada = (prova1 * peso1 + prova2 * peso2 + projeto * peso_projeto) / (peso1 + peso2 + peso_projeto)
print ("A média ponderada do aluno é de: ", media_ponderada)

#fim.atividades
