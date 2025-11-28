# calculadora.py

def adicionar(x, y):
    """Adiciona dois números."""
    return x + y


def subtrair(x, y):
    """Subtrai dois números."""
    return x - y


def multiplicar(x, y):
    """Multiplica dois números."""
    return x * y


def dividir(x, y):
    """Divide dois números."""
    if y == 0:
        return "Erro! Divisão por zero."
    return x / y


def calculadora():
    """Função principal da calculadora."""
    print("--- Calculadora Simples ---")
    print("Selecione a operação:")
    print("1. Adicionar")
    print("2. Subtrair")
    print("3. Multiplicar")
    print("4. Dividir")
    print("---------------------------")

    while True:
        # Pega a escolha do usuário
        escolha = input("Digite sua escolha (1/2/3/4): ")

        # Verifica se a escolha é válida
        if escolha in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
            except ValueError:
                print("Entrada inválida. Por favor, digite um número.")
                continue

            if escolha == '1':
                print(f"{num1} + {num2} = {adicionar(num1, num2)}")

            elif escolha == '2':
                print(f"{num1} - {num2} = {subtrair(num1, num2)}")

            elif escolha == '3':
                print(f"{num1} * {num2} = {multiplicar(num1, num2)}")

            elif escolha == '4':
                resultado = dividir(num1, num2)
                print(f"{num1} / {num2} = {resultado}")

            # Pergunta se o usuário quer continuar
            proximo_calculo = input("Fazer outro cálculo? (sim/não): ")
            if proximo_calculo.lower() != 'sim':
                print("Obrigado por usar a calculadora!")
                break
        else:
            print("Escolha inválida.")


if __name__ == "__main__":
    calculadora()