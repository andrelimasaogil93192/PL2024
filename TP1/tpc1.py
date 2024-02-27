def tpc1(nome_arquivo):
    with open(nome_arquivo,'r') as arquivo:
        lines = arquivo.readlines()


    cabecalho = lines.pop(0)

    modalidades = set()
    aptos = 0
    inaptos = 0
    dist_etaria = {'[20-24]': 0,'[25-29]':0,'[30-34]':0,'[35-39]':0,'[40-44]':0, '[45-49]':0,'[50-54]':0, '[55-59]':0,'[60-64]':0, '[65-69]':0,'[70-74]':0, '[75-79]':0,'[80-84]':0, '[85-89]':0}


    for line in lines:
        data = line.strip().split(',')
        modalidades.add(data[8])
 

        if data[12] == 'true' :
            aptos += 1
        else :
            inaptos += 1

 
        idade = int(data[5])

        grupo_etario = f"[{idade // 5 * 5}-{(idade // 5 * 5) + 4}]"
        dist_etaria[grupo_etario] += 1

    modalidades_sort = sorted(modalidades)

    return modalidades_sort, aptos, inaptos, dist_etaria

nome_arquivo = '/home/mesutogil/uni/PL/TPC1/emd.csv'

modalidades, aptos, inaptos, dist_etaria = tpc1(nome_arquivo)
total_atletas = aptos + inaptos
p_aptos = (aptos/total_atletas) * 100
p_inaptos = (inaptos/total_atletas) * 100

print("Lista ordenada das modelidades: ")

for modalidade in modalidades: 
    print(modalidade)


print("Percentagem de atletas aptos: ")
print(p_aptos)

print("Percentagem de atletas inaptos: ")
print(p_inaptos)

print("Total de atletas: ")
print(total_atletas)







