def le_numero(mensagem):
    while True:
        try:
            n = int(input(mensagem))
            return n
        except ValueError:
            print("O valor digitado não é válido")

n = le_numero("Entre com n: ")
if n % 2 == 0:
    print(n, "é par")
else:
    print(n, "é impar")