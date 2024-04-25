times = ('Flamengo', 'Internacional', 'Atlético-MG', 'São Paulo', 'Fluminense', 'Grêmio', 'Palmeiras', 'Santos', 'Athletico-PR', 'Bragantino', 'Ceará', 'Corinthians', 'Atlético-GO', 'Bahia', 'Sport', 'Fortaleza', 'Vasco', 'Goiás', 'Chapecoense', 'Coritiba', 'Botafogo')

print(f'Os 5 primeiros colocados são: {times[:5]}')
print(f'Os 4 últimos colocados são: {times[-4:]}')
print(f'Os times em ordem alfabética são: {sorted(times)}')
print(f'O time da Chapecoense está na {times.index("Chapecoense")}ª posição')