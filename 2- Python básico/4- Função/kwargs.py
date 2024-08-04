def verificar_aluna(*args):
    if 'Aluna' in args and 'WomaKescode' in args:
        return 'Bem-Vinda Aluna'
    return 'Eu não sei quem você aluna'

print(verificar_aluna)
print(verificar_aluna(1, True, 'womakescode', 'Aluna'))