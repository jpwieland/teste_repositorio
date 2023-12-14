from utils import get_float, get_int,lerArquivo,escreverArquivo 

def aberturaCaixa(): 
    notas=[200,100,50,20,10,5,2]
    quantidade=[]
    for valor in notas: 
        valorDigitado = get_int(f'Quantas notas de R${valor},00? ')
        quantidade.append(valorDigitado)
    soma = 0 
    for i in range(len(notas)):
        soma = soma + (notas[i] * quantidade[i])
    print(f'você abriu o caixa com R${soma}')
    return soma

def aberturaCaixaDicionario(): 
    notas = {200:0,100:0,50:0,20:0,10:0,5:0,2:0}
    for valor in notas: 
        quantidade= get_int(f'Quantas notas de R$ {valor},00?')
        notas[valor]=quantidade
    soma = sum(valor* quantidade for valor,quantidade in notas.items())
    print(f'você abriu o caixa com R${soma}')
    return soma

def realizaCompra(): 
    print("Nova compra iniciada. Para finalizar a compra, digite 0")
    soma = 0 
    valorDigitado = get_float("Digite valor do produto: ")
    while (valorDigitado!=0): 
        soma= valorDigitado+ soma 
        valorDigitado = get_float("Digite valor do produto: ")
    return soma

def fazCompras(nomeArquivo,valorInicial):
    controle = 1
    while(controle == 1):
        totalDacompra = realizaCompra()
        valorCaixa = totalDacompra + valorInicial
        escreverArquivo(nomeArquivo,valorCaixa)
        print(f"Compra finalizada! valor em caixa : {valorCaixa} ")
        controle = get_int("Digite 1 para nova compra")

def main():
    print("======Mercado do João=======")

    nomeArquivo ="mercado.txt" 
    valorInicial = float(lerArquivo(nomeArquivo)) 

    resposta = "S"
    if(valorInicial!=0): 
        print("Estou vendo que você tem dados salvos!")
        resposta = input("Caso queira informar novamente os valores, digite S, senão, digite N: ")

    if(resposta=="S"):
        print("Para abertura do caixa é preciso que você digite o valor da quantidade de cada nota para totalização final.")
        valorInicial = aberturaCaixaDicionario()
        escreverArquivo(nomeArquivo ,valorInicial)

    print(f"O seu caixa foi aberto com R${valorInicial}")

    fazCompras(nomeArquivo,valorInicial)



if __name__ == "__main__": 
    main()