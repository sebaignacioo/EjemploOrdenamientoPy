from random import shuffle as desordenar

def generarLista():
    lista = list(range(1, 11))
    print(f'Generando lista: {lista}', end=' -> ')
    desordenar(lista)
    print(lista, end = '\n\n')
    return lista

def ejecutarOrdenamiento(lista):
    print(f'Ordenamiento de {lista} de mayor a menor')
    print(f'  => i está entre 0 y {len(lista) - 2}')
    for i in range(len(lista) - 1):
        print(f'    => i = {i} -> j está entre 0 y {len(lista) - i - 2} ')
        for j in range(len(lista) - i - 1):
            print(f'      - j = {j}')
            print(f'        => Se revisa si lista[{j}] = {lista[j]} es menor a lista[{j + 1}] = {lista[j + 1]}: '
                  f'{lista[j] < lista[j + 1]}', end = '')
            if lista[j] < lista[j + 1]:
                print('\n          -- ** SE INTERCAMBIAN **')
                print(f'             ** {lista}', end = ' ')
                aux = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = aux
                print(f'-> {lista}')
            else: print()
        if i == 0:
            print(f'    OBS: El último dato de la lista ya está ordenado. {lista}\n')
        else:
            print(f'    OBS: Los {i + 1} últimos datos de la lista ya están ordenados. {lista}\n')
    print(f'\n### LISTA FINAL: {lista} ###')

if __name__ == '__main__':
    lista = generarLista()
    ejecutarOrdenamiento(lista)
