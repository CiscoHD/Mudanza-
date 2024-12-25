lost_memory = open('MemoriaDañada.txt', 'r').read()

prueba = str(lost_memory)

print(prueba[9])

for i in range(prueba.find('mul('), prueba.find('mul(') + 4):
    print(i)
