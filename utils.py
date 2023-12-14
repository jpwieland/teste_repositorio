def get_int(texto): 
    while True:
        try:
            numero = int(input(texto))
            return numero
        except ValueError: 
            print("Você precisa digitar um número!")

def get_float(texto): 
    while True:
        try:
            numero = float(input(texto))
            return numero
        except ValueError: 
            print("Você precisa digitar um número!")


def lerArquivo(nomeArquivo):
    try: 
        with open(nomeArquivo, 'r') as arquivo: 
            valorDoConteudo = arquivo.read() 
            if (valorDoConteudo ==""): 
                return "0"

    except FileNotFoundError: 
        print("Arquivo não localizado")
        print("criando arquivo...")
        escreverArquivo(nomeArquivo,"")
        return "0"
    return valorDoConteudo

def escreverArquivo(nomeArquivo,textoASalvar):
    try:
        with open(nomeArquivo, 'w') as arquivo: 
            arquivo.write(str(textoASalvar))
    except Exception as e: 
        print(f'ERRO AO SALVAR: {e}')
