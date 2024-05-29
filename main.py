pessoa = {
    'Nome': 'Michael Oliveira',
    'Idade': 30,
    'Profissão': 'Programador',
    'Empresa': 'SENAI',
    'Gênero': 'Masculino',
    'Cidade': 'Taguatinga',
    'Nome': 'Michael Oliveira'
}

#REMOVER CHAVE
del pessoa [input('Informe o nome da chave a ser deletada: ')]

#Exibindo Dados
for delete in pessoa:
    print(f'{delete}: {pessoa.get(delete)}')