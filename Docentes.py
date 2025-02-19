import pandas as pd
import os

# Verificar o diretório atual
print("Diretório atual:", os.getcwd())
# Alterar para o diretório correto (onde está o arquivo TXT)
os.chdir(r"SEU DIRETÓRIO")

#Função para ler e processar o arquivo TXT
def processar_txt_para_excel(arquivo_txt):
    #Abrir o arquivo com a codificação UTF-8
    with open(arquivo_txt, 'r', encoding='utf-8') as f:
        linhas = f.readlines()

    codigo_registro = None
    codigo_IES = None
    docente_dados = None

    dados_combinados = []

    for linha in linhas:
        campos = linha.strip().split('|')

        if campos[0] == '50':
           codigo_registro = campos[0]
           codigo_IES = campos[1]

        elif campos[0] == '51': #dados do docente
            docente_dados = campos

        elif campos[0] == '52': #dados do curso
            curso_dados = campos

            if docente_dados:
                dados_combinados.append([codigo_registro,codigo_IES] + docente_dados + curso_dados)

    #DataFrame dos dados combinados
    df_resultados = pd.DataFrame(dados_combinados)            

    #Salvar em Excel
    df_resultados.to_excel("Resultado_Exportado_Docentes.xlsx", index=False, header=False)

    print("Arquivo Excel gerado com sucesso!")

    #Chamada para processar o arquivo
processar_txt_para_excel('Censo_Docente.txt')

