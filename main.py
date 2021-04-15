linhas = materia = str(
    input('Professor Andre Godoi digite a sua disciplina: '))
dia = str(input('Qual a linguagem e o dia da semana que temos a sua aula: '))

# Arquivos dentro da variavel ou objeto

arquivo = open('bancoDeDados2_write.txt', 'w')
arquivo.writelines(materia + '\n' + dia)
arquivo.close()

# Representação da linha utilizando strip

with open('bancoDeDados2_write.txt', 'r') as arquivo:
    for dados in arquivo:
        conteudo = dados.strip()
        print(repr(conteudo))

# Função Seek
    arquivo.seek(26)
    linhas = arquivo.readline()
    item = linhas.strip()
    print(repr(item))


# Incluir a informação do ponteiro no bancoDeDados

arquivo = open('bancoDeDados2_write.txt', 'a')
arquivo.writelines('\n' + item)
arquivo.close()

# Quantidade da palavra python descrito na função count

with open('bancoDeDados2_write.txt', 'r') as arquivo:
    contador = 0
    for python in arquivo:
        if python.strip():
            contador += 1
    print('Total =', contador)


arquivo = [materia,dia]
dados1 = ' '.join(arquivo)
with open ('bancoDeDados2_write.txt', 'r') as arquivo:
  print(repr(dados1))



