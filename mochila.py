class Caja:
    def __init__(self, _monto = 0, _peso = 0):
        self.peso = _peso
        self.monto = _monto
        self.ratio = _monto / _peso if _peso > 0 else 0
        
cajas = [Caja(3,3), Caja(1.8,2), Caja(3,4), Caja(2,3), Caja(3,7), Caja(4,10), Caja(2,5), Caja(1,3)]

mochila = int(input("Ingrese capacidad de mochila:\n"))
total = 0
for paq in cajas:
    if mochila == 0:
        break
    elif paq.peso > mochila:
        #parcial
        partePeso = mochila
        parteMonto = paq.monto*partePeso/paq.peso
        print(f"Kg{partePeso}, S/{parteMonto}")
        total += parteMonto
        mochila = 0
    else:
        #total
        print(f"Kg{paq.peso}, S/{paq.monto}")
        total += paq.monto
        mochila -= paq.peso

print(f"Total ganado S/{total}")