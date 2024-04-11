# Notas: Division y Conquista Avanzada

Fecha: 15 de marzo de 2024 9:52
Materia: Teoria de Algoritmos

[2024-03-14 - TDA - División y Conquista Avanzada](https://www.youtube.com/watch?v=22h0kOTKZ0c&list=PLLfC2vEod54Iwg2t684y_fRoBVavY1HjR&index=3&t=8s&ab_channel=AlgoritmosFiubaCursoBuchwald)

Video de la clase

### COSAS

> Amigarme con los algoritmos recursivos
> 

Nunca un algoritmo de ordenamiento puede ser O(nlogn)

Haciendo particiones (recurrencia??) trabajando con indices/punteros/slices 

# Tecnicas de diseño

- Metodologia para resolver ejercicios
- Patrones de diseño para algoritmos

### Division y Conquista

1. Dividimos el problema en subproblemas
2. Resolvemos cada subproblema **recursivamente**
    
    *cada algoritmo se pueden escribir de forma iterativa y recursiva*
    
3. Combinamos las soluciones a cada subproblema

En general para analizar la complejidad debemos analizar la ecuacion de recurrencia que representa el algoritmo. 

```python
arr[:medio] // slice
```

- en Go es O(1) , usa la misma memoria
- en Python es O(n) , copia

### 💻 Ejemplo de Algoritmos

1. Busqueda Binaria
2. Mergesort y Quicksort
3. Otros algoritmos de dificultad similar
4. Arboles (incluyendo heaps)

### **⏱️ Ecuacion de recurrencia**

$T(n) = 2T(n/2) + O(n)$ , si n=2^k (matematica)

$T(n) = O(n log n)$

### ⚔️ Teorema Maestro

$AT(n/B) + O(n^c)$

- A: Cantidad de llamados recursivos
- B: Proporcion del tamaño origianl con el que llamaos recursivamenete
- O(n^c): costo de partir y juntar (todo lo que no son llamados recursivos

**Condiciones para aplicar el teorema**

1. A es natural
2. B es real mayor a 1, y es cte
3. El caso base es constante

si $log_b(A)$:

- $<$ C   ⇒   $T(n) = O(n^c)$
- $=$ C   ⇒   $T(n) = O(n^c log_b(n)) = O(n^clog(n))$
- $>$ C   ⇒   $T(n) = O(n$^$(log_b(A)) ) => Si A = B => T(n) = O(n)$

### Teorema Maestro general (poco probable)

$T(n) = AT(n/B) + f(n)$

- A y B lo mismo de antes
- f(n) siendo el costo de partir y juntar los resultados

**Casos de f(n)**

![Untitled](Clase%20Division%20y%20Conquista%20Avanzada%202a6cb7d29e76454dbe39b0dc515aee36/Untitled.png)

Ejemplo) $T(n) = 2T(n/2) + log n$

### Problema 1: Multiplicacion de numeros muy grandes

Cuando multplicamos dos enteros de largos **m** y **n**

- Como es el algoritmos? Se multiplican digito a digito y se suman
- Cuanto tiempo consume? $O(mn)$ → si m es el mas grande acoto como $O(m^2)$

Son necesarios todos los resultados parciales? **Si, si usamos este algoritmo si.**

### Problema 2: Buscar el vertice extremo en un grafo

### Problema 3: Dado n puntos, buscar los mas cercados en 2 dimensiones

Dado n puntos en un plano, buscar la pareja que se encuentre mas cerca

Algoritmo sencillo ⇒ ver todas las distancias

- Tiempo que consume → $O(n^2)$

Asumimos que ningun par de puntos tiene la misma coordenada xy

Si fuera de una sola dimension: 

> **Ordenar** me permite comparar el actual contra el siguiente → es lineal
En cambio si no esta ordenado → tengo que comparar todos con todos
> 

**Algoritmo**

p = (x,y)

- ordeno a todos los puntos con respecto al eje x → ***px***
- ordeno a todos los puntos con respecto al eje y → ***py***
- el elemento del medio de px es la ***coordenada de cort*e**, separo en dos partes, Q y R
- ***Qx*** y ***Rx*** son los puntos a Izq y derecha respectivamenete
- Ahora itero py, chequeo su coordenada x y me fijo si esta detras (≤) o delante (>) de la coordenada de corte, y lo asigno a ***Qy*** o ***Ry*** dependiendo la condicion
- Por ahora todo fue lineal 4 * $O(n)$ =  $O(n)$
- …

### Problema 4: Multiplicacion de matrices

Podemos dividir a cada matriz de nxn en 4 submatrices de n/2 x n/2 

(asumimos que n es potencia de 2 para simplificar)

**ALGORITMO STRASSEN**

Algo similar a karatsuba-offman para multiplicar numeros grandes

### Problema 5:

hay mas