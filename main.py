# "Faça um programa em python que leia em uma pasta arquivos pdfs diversos, procurando uma palavara especifica.
# No final, mostre em quais arquivos estão estas palavras e monte uma lista na tela."
# - Desafios - o número de arquivos pdf não importam.
# - Eu tenho que digitar a palavra que eu quero procurar.

# Desafios Bonus
# - Eu digito qual a pasta que eu quero procurar.
# - A lista pode ser gerada num arquivo TXT.

# Parte 1:
import os
from PyPDF2 import PdfReader

# Parte 2:
def main():
    path_da_pasta = input("Qual o caminho (path) da pasta"
                          " que você quer buscar?")
    palavra_desejada = input("Qual a palavra que você deseja procurar? ")

    # Parte 4:
    arquivos_encontrados = buscador_de_palavras(path_da_pasta,
                                                palavra_desejada)

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

# Parte 3:
def buscador_de_palavras(path_da_pasta, palavra_desejada):
    # arquivos_pdf = [file for file in os.listdir(path_da_pasta)
    # if file.endswith('.pdf')]
    arquivos_pdf = []
    for file in os.listdir(path_da_pasta):
        if file.endswith('.pdf'):
            arquivos_pdf.append(file)
    resultados = []

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

# Parte 5:
main()