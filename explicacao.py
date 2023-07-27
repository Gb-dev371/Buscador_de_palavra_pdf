import os
from PyPDF2 import PdfReader


def main():  # Aqui estamos definindo a função main
    path_da_pasta = input("Qual o caminho (path) da pasta"
                          "que você quer buscar?")  # Essa variável recebe o caminho da pasta
    palavra_desejada = input("Qual a palavra que você deseja procurar?")  # Essa variável recebe a palavra que queremos encontrar

    arquivos_encontrados = buscador_de_palavras(path_da_pasta,
                                                palavra_desejada)  # A variável recebe o retorno da nossa função buscador_de_palavras usando os parâmetros path_da_pasta e palavra_desejada

    if arquivos_encontrados:
        print("A palavra foi encontrada nos seguintes arquivos:")
        for file in arquivos_encontrados:
            print(file)
        # Salvar a lista em um arquivo TXT (desafio bônus)
        with open("arquivos_encontrados.txt", "w") as txt_file:
            txt_file.write("\n".join(arquivos_encontrados))
        print("A lista foi salva em 'arquivos_encontrados.txt'.")
    else:
        print("A palavra não foi encontrada em nenhum arquivo PDF na pasta.")

    # Caso a variável arquivos_encontrados esteja com algum valor, aparece um
    # print na tela dizendo que a palavra foi encontrada. Para cada pdf
    # contido na lista de pdfs que tem a palavra, o nome do pdf
    # é printado na tela.


def buscador_de_palavras(path_da_pasta, palavra_desejada):  # Aqui estamos criando nossa função buscador_de_palavras
    arquivos_pdf = []
    for file in os.listdir(path_da_pasta):
        if file.endswith('.pdf'):
            arquivos_pdf.append(file)
    resultados = []
    # A variável arquivos_pdf recebe o nome de todos os pdfs que estão dentro
    # da pasta informada. A lógica funciona assim:
    # Para cada arquivo que está na pasta, a variável receberá somente os
    # arquivos que tenham ".pdf".

    for pdf in arquivos_pdf:
        pdf_path = os.path.join(path_da_pasta, pdf)
        with open(pdf_path, 'rb') as file:
            pdf_reader = PdfReader(file)
            for pagina in pdf_reader.pages:
                texto = pagina.extract_text()
                if palavra_desejada.lower() in texto.lower():
                    resultados.append(pdf)
                    break
    return resultados
    # Para cada pdf que esteja na lista arquivos_pdf, o python irá ler o
    # arquivo e para cada página do pdf, o texto será extraído e estará na
    # variável texto. Se a palavra desejada estiver contida no texto, nós
    # adicionamos esse pdf na lista resultados.


main()
