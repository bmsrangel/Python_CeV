'''for cont in range(1, 51):
    if cont % 2 == 0:
        print(cont,end=' ')'''

for cont in range(2, 51, 2): #reduz o número de iterações, ocupando o processador apenas metade do tempo
    print(cont, end=' ')