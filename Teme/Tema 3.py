import random

lista_piese = ['turbo', 'ulei', 'filtru', 'cheie', 'roata', 'bucsa', 'brat', 'bujie', 'piston', 'fulie']

nr_vieti = 3

cuvant = random.choice(lista_piese)
# print(cuvant)

# cuvant cu asterix
cuvant_ghicit = cuvant
for i in range(len(cuvant)):
    cuvant_ghicit = cuvant_ghicit[:i] + '*' + cuvant_ghicit[i+1:]

print(cuvant_ghicit)

# incepe jocul prin introducerea literelor

while nr_vieti > 0 and cuvant_ghicit != cuvant:
    litera = input('Introduceti cate o litera  ').lower()
    if cuvant.find(litera) == -1 :
        nr_vieti = nr_vieti -1
        print('Mai aveti '+ str(nr_vieti) + ' vieti')
    else:
        for i in range(len(cuvant)):
            if cuvant[i] == litera:
                cuvant_ghicit = cuvant_ghicit[:i] + litera + cuvant_ghicit[i+1:]
    print(cuvant_ghicit)

if nr_vieti == 0:
    print('Ai pierdut! Cuvantul a fost ' + cuvant)

else:
    print('Ai castigat! Cuvantul a fost ' + cuvant)

