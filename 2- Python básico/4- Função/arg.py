#kwargs

def mini_bio(**dados_pessoais):
    for key, value in dados_pessoais.items():
        print(f'{key} - {value}')
        print('Mini Biografia')
mini_bio(nome='Rosicleide', especializacao='Back=end', linguagem='Python', senioridade='Junior')