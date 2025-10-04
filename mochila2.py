#falta ajustar
def kg_utilidad(p_max, precios, pesos):
    rel = []
    res_peso = 0
    uti = 0
    for a in precios:
        for b in pesos:
            if (a == b):
                rel.append(a*b)

        for i in rel:
            if i >= 1 | i >= 0.9:
                while res_peso < p_max:
                    res_peso += pesos(rel.index(i))
                uti = res_peso * precios(rel.index(i))    

    return uti


p_max = float(input("Ingrese el peso maximo de la caja Rappi:\n"))
packs = ["H", "G", "B", "F", "C", "A", "D", "E"]
precios = [3, 1.8, 3, 2, 3, 4, 2, 1]
pesos = [3, 2, 4, 3, 7, 10, 5, 3]
utilidad = kg_utilidad(p_max, precios, pesos)

print (f"Utilidad obtenida por relacion de pesos y precios: {utilidad}")