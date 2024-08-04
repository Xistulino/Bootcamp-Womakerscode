# Lendo dados de arquivos:

file = 'arquivo.txt'

#open somente para leitura


# abertura para escrita
arquivo_escrita = open(file, 'w')
arquivo_escrita.write('Texto a ser escrito')
arquivo_escrita.close()

# leitura
arquivo_leitura = open(file, 'r')
leitura = arquivo_leitura.read()
print(leitura)
arquivo_leitura.close()