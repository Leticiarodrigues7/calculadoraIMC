peso = float (input ("Digite o seu peso: "))
altura = float (input("Digite a sua altura: "))

imc = peso / (altura * altura)


if imc < 16.00:
    print(f'Seu IMC é: {imc:.2f} - Baixo peso grau III')

elif imc >= 16.00 and imc <= 16.99:
    print(f' Seu IMC é: {imc:.2f} - Baixo peso grau II')
        
elif imc >= 17.00 and imc <= 18.49:
    print(f'Seu IMC é: {imc:.2f} - Baixo peso grau I')

elif imc >= 18.50 and imc <= 24.99:
    print(f' Seu IMC é: {imc:.2f} - Peso ideal')

elif imc >= 25.00 and imc <= 29.99:
    print(f'Seu IMC é: {imc:.2f} - Soprepeso')

elif imc >= 30.00 and imc <= 34.99:
    print(f'Seu IMC é: {imc:.2f} - Obesidade Grau I')

elif imc >= 35.00 and imc <= 39.99:
    print(f' Seu IMC é: {imc:.2f} - Obesidade Grau II')

else:
    print(f'Seu IMC é: {imc:.2f} - Obesidade Grau III')




