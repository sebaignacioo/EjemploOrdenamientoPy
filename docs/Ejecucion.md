# Ejemplo de ejecución

## Salida por consola
```
Lista: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] -> [10, 3, 5, 8, 4, 2, 9, 6, 1, 7]

Ordenamiento de [10, 3, 5, 8, 4, 2, 9, 6, 1, 7] de mayor a menor
  => i está entre 0 y 8
    => i = 0 -> j está entre 0 y 8 
      - j = 0
        => Se revisa si lista[0] = 10 es menor a lista[1] = 3: False
      - j = 1
        => Se revisa si lista[1] = 3 es menor a lista[2] = 5: True
          -- ** SE INTERCAMBIAN **
             ** [10, 3, 5, 8, 4, 2, 9, 6, 1, 7] -> [10, 5, 3, 8, 4, 2, 9, 6, 1, 7]
      - j = 2
        => Se revisa si lista[2] = 3 es menor a lista[3] = 8: True
          -- ** SE INTERCAMBIAN **
             ** [10, 5, 3, 8, 4, 2, 9, 6, 1, 7] -> [10, 5, 8, 3, 4, 2, 9, 6, 1, 7]
      - j = 3
        => Se revisa si lista[3] = 3 es menor a lista[4] = 4: True
          -- ** SE INTERCAMBIAN **
             ** [10, 5, 8, 3, 4, 2, 9, 6, 1, 7] -> [10, 5, 8, 4, 3, 2, 9, 6, 1, 7]
      - j = 4
        => Se revisa si lista[4] = 3 es menor a lista[5] = 2: False
      - j = 5
        => Se revisa si lista[5] = 2 es menor a lista[6] = 9: True
          -- ** SE INTERCAMBIAN **
             ** [10, 5, 8, 4, 3, 2, 9, 6, 1, 7] -> [10, 5, 8, 4, 3, 9, 2, 6, 1, 7]
      - j = 6
        => Se revisa si lista[6] = 2 es menor a lista[7] = 6: True
          -- ** SE INTERCAMBIAN **
             ** [10, 5, 8, 4, 3, 9, 2, 6, 1, 7] -> [10, 5, 8, 4, 3, 9, 6, 2, 1, 7]
      - j = 7
        => Se revisa si lista[7] = 2 es menor a lista[8] = 1: False
      - j = 8
        => Se revisa si lista[8] = 1 es menor a lista[9] = 7: True
          -- ** SE INTERCAMBIAN **
             ** [10, 5, 8, 4, 3, 9, 6, 2, 1, 7] -> [10, 5, 8, 4, 3, 9, 6, 2, 7, 1]
    OBS: El último dato de la lista ya está ordenado. [10, 5, 8, 4, 3, 9, 6, 2, 7, 1]

    => i = 1 -> j está entre 0 y 7 
      - j = 0
        => Se revisa si lista[0] = 10 es menor a lista[1] = 5: False
      - j = 1
        => Se revisa si lista[1] = 5 es menor a lista[2] = 8: True
          -- ** SE INTERCAMBIAN **
             ** [10, 5, 8, 4, 3, 9, 6, 2, 7, 1] -> [10, 8, 5, 4, 3, 9, 6, 2, 7, 1]
      - j = 2
        => Se revisa si lista[2] = 5 es menor a lista[3] = 4: False
      - j = 3
        => Se revisa si lista[3] = 4 es menor a lista[4] = 3: False
      - j = 4
        => Se revisa si lista[4] = 3 es menor a lista[5] = 9: True
          -- ** SE INTERCAMBIAN **
             ** [10, 8, 5, 4, 3, 9, 6, 2, 7, 1] -> [10, 8, 5, 4, 9, 3, 6, 2, 7, 1]
      - j = 5
        => Se revisa si lista[5] = 3 es menor a lista[6] = 6: True
          -- ** SE INTERCAMBIAN **
             ** [10, 8, 5, 4, 9, 3, 6, 2, 7, 1] -> [10, 8, 5, 4, 9, 6, 3, 2, 7, 1]
      - j = 6
        => Se revisa si lista[6] = 3 es menor a lista[7] = 2: False
      - j = 7
        => Se revisa si lista[7] = 2 es menor a lista[8] = 7: True
          -- ** SE INTERCAMBIAN **
             ** [10, 8, 5, 4, 9, 6, 3, 2, 7, 1] -> [10, 8, 5, 4, 9, 6, 3, 7, 2, 1]
    OBS: Los 2 últimos datos de la lista ya están ordenados. [10, 8, 5, 4, 9, 6, 3, 7, 2, 1]

    => i = 2 -> j está entre 0 y 6 
      - j = 0
        => Se revisa si lista[0] = 10 es menor a lista[1] = 8: False
      - j = 1
        => Se revisa si lista[1] = 8 es menor a lista[2] = 5: False
      - j = 2
        => Se revisa si lista[2] = 5 es menor a lista[3] = 4: False
      - j = 3
        => Se revisa si lista[3] = 4 es menor a lista[4] = 9: True
          -- ** SE INTERCAMBIAN **
             ** [10, 8, 5, 4, 9, 6, 3, 7, 2, 1] -> [10, 8, 5, 9, 4, 6, 3, 7, 2, 1]
      - j = 4
        => Se revisa si lista[4] = 4 es menor a lista[5] = 6: True
          -- ** SE INTERCAMBIAN **
             ** [10, 8, 5, 9, 4, 6, 3, 7, 2, 1] -> [10, 8, 5, 9, 6, 4, 3, 7, 2, 1]
      - j = 5
        => Se revisa si lista[5] = 4 es menor a lista[6] = 3: False
      - j = 6
        => Se revisa si lista[6] = 3 es menor a lista[7] = 7: True
          -- ** SE INTERCAMBIAN **
             ** [10, 8, 5, 9, 6, 4, 3, 7, 2, 1] -> [10, 8, 5, 9, 6, 4, 7, 3, 2, 1]
    OBS: Los 3 últimos datos de la lista ya están ordenados. [10, 8, 5, 9, 6, 4, 7, 3, 2, 1]

    => i = 3 -> j está entre 0 y 5 
      - j = 0
        => Se revisa si lista[0] = 10 es menor a lista[1] = 8: False
      - j = 1
        => Se revisa si lista[1] = 8 es menor a lista[2] = 5: False
      - j = 2
        => Se revisa si lista[2] = 5 es menor a lista[3] = 9: True
          -- ** SE INTERCAMBIAN **
             ** [10, 8, 5, 9, 6, 4, 7, 3, 2, 1] -> [10, 8, 9, 5, 6, 4, 7, 3, 2, 1]
      - j = 3
        => Se revisa si lista[3] = 5 es menor a lista[4] = 6: True
          -- ** SE INTERCAMBIAN **
             ** [10, 8, 9, 5, 6, 4, 7, 3, 2, 1] -> [10, 8, 9, 6, 5, 4, 7, 3, 2, 1]
      - j = 4
        => Se revisa si lista[4] = 5 es menor a lista[5] = 4: False
      - j = 5
        => Se revisa si lista[5] = 4 es menor a lista[6] = 7: True
          -- ** SE INTERCAMBIAN **
             ** [10, 8, 9, 6, 5, 4, 7, 3, 2, 1] -> [10, 8, 9, 6, 5, 7, 4, 3, 2, 1]
    OBS: Los 4 últimos datos de la lista ya están ordenados. [10, 8, 9, 6, 5, 7, 4, 3, 2, 1]

    => i = 4 -> j está entre 0 y 4 
      - j = 0
        => Se revisa si lista[0] = 10 es menor a lista[1] = 8: False
      - j = 1
        => Se revisa si lista[1] = 8 es menor a lista[2] = 9: True
          -- ** SE INTERCAMBIAN **
             ** [10, 8, 9, 6, 5, 7, 4, 3, 2, 1] -> [10, 9, 8, 6, 5, 7, 4, 3, 2, 1]
      - j = 2
        => Se revisa si lista[2] = 8 es menor a lista[3] = 6: False
      - j = 3
        => Se revisa si lista[3] = 6 es menor a lista[4] = 5: False
      - j = 4
        => Se revisa si lista[4] = 5 es menor a lista[5] = 7: True
          -- ** SE INTERCAMBIAN **
             ** [10, 9, 8, 6, 5, 7, 4, 3, 2, 1] -> [10, 9, 8, 6, 7, 5, 4, 3, 2, 1]
    OBS: Los 5 últimos datos de la lista ya están ordenados. [10, 9, 8, 6, 7, 5, 4, 3, 2, 1]

    => i = 5 -> j está entre 0 y 3 
      - j = 0
        => Se revisa si lista[0] = 10 es menor a lista[1] = 9: False
      - j = 1
        => Se revisa si lista[1] = 9 es menor a lista[2] = 8: False
      - j = 2
        => Se revisa si lista[2] = 8 es menor a lista[3] = 6: False
      - j = 3
        => Se revisa si lista[3] = 6 es menor a lista[4] = 7: True
          -- ** SE INTERCAMBIAN **
             ** [10, 9, 8, 6, 7, 5, 4, 3, 2, 1] -> [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    OBS: Los 6 últimos datos de la lista ya están ordenados. [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

    => i = 6 -> j está entre 0 y 2 
      - j = 0
        => Se revisa si lista[0] = 10 es menor a lista[1] = 9: False
      - j = 1
        => Se revisa si lista[1] = 9 es menor a lista[2] = 8: False
      - j = 2
        => Se revisa si lista[2] = 8 es menor a lista[3] = 7: False
    OBS: Los 7 últimos datos de la lista ya están ordenados. [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

    => i = 7 -> j está entre 0 y 1 
      - j = 0
        => Se revisa si lista[0] = 10 es menor a lista[1] = 9: False
      - j = 1
        => Se revisa si lista[1] = 9 es menor a lista[2] = 8: False
    OBS: Los 8 últimos datos de la lista ya están ordenados. [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

    => i = 8 -> j está entre 0 y 0 
      - j = 0
        => Se revisa si lista[0] = 10 es menor a lista[1] = 9: False
    OBS: Los 9 últimos datos de la lista ya están ordenados. [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]


### LISTA FINAL: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1] ###
```