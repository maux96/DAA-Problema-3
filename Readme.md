# III Tarea Evaluativa de DAA

#### Integrantes

- Mauricio Mahmud Sánchez C412 
- Raúl Beltrán Gómez C412 

---

# Problema 

Kevin ha sido puesto al frente de la comisión de la facultad que elegirá las fechas de las pruebas de los k cursos que se dan en la facultad.

Cada curso tiene una cantidad de pruebas determinadas que quiere poner, y propone para esto, por ejemplo, los días { 17, 34, 65 y 87 } del curso escolar, si vemos a este como una sucesión de días en los que se imparten clases. Para mostrarse flexibles, los cursos a veces elaboran más de una propuesta incluso.

Por un problema de desorganización las propuestas se regaron y ahora no se sabe que curso propuso que propuesta, pero ya Kevin esta cansado de tanta gestión. Kevin quiere elegir k propuestas que ninguna quiera poner pruebas el mismo día que las otras, así supone que todo el mundo estará contento, ayude a Kevin.


## Set Packing Problem

El problema de Set Packing (Empaquetamiento de conjuntos) es un problema NP-Completo y se puede describir formalmente de la siguiente manera:

Dado un conjunto universal $U$, una colección $S$ de subconjuntos de $U$ y un entero positivo $k$, se busca determinar si existen $K$ subconjuntos de $S$ que sean disjuntos entre sí (es decir, que no compartan elementos) tal que $K >= k$.


## Demostración

Reduzcamos el problema set packing al nuestro. 

1. Se toma el conjunto universal $U$ como el conjunto de días del curso, osea se remplaza cada elemento del conjunto $U$ por un día del curso donde no existen dos elementos de $U$ asignados al mismo día.
2. Cada uno de los subconjuntos se toman como una propuesta existente.
3. Se toma $k$ como las propuestas a elegir.

Esta reducción se puede hacer de manera lineal, ya que solo habría que sustituir por numeros los elementos.

Una vez resuelto el problema dado, se tiene (si existen),  el conjunto de tamaño $k$ de propuestas. Luego se tendria la solución del problema Set Packing ya que existiría un conjunto con cardinalidad mayor o igual que $k$ de subconjuntos disjuntos si existe este conjunto, de lo contrario la respuesta es negativa en Set Packing. 

Por lo anterior expuesto si el problema dado tiene una complejidad polinomial podríamos resolver el problema Set Packing en tiempo polinomial, lo cual conocemos que no es posible ya que este es NP-Completo. Luego el problema dado, si existe una solucion determinista a este, tiene que ser no polinomial. 


## Solución

Por cada uno de los subconjuntos dados se va a comprobar que la interseccion sea nula con un conjunto acumulado (inicialmente en el conjunto vacío), cada vez que se evalue si un subconjunto tiene intersección nula con el conjunto acumulado se va a unir a este formando parte de el de ser cierto, esto se va hacer recursivamente hasta que se llegue a que se han unido k subconjuntos al conjunto acumulado, de no lograrse llegar a los k subconjuntos unidos, el problema no tiene solución.

#### Complejidad
La complejidad de recorrer los n subconjuntos por cada entrada recursiva seria en total $O(n^n)$ esto no es necesario, pues la operación que se va a llevar a cabo es la intersección o unión la cuál es simétrica por lo que no es necesario comprobar si un conjunto anteriormente comprobado tiene intersección nula con el actual (pues ya vamos a haberlo comprobado) por lo que sería $O(n!)$, también hay que hacer la unión de dos conjuntos en cada entrada recursiva, esto tiene complejidad $O(m)$ siendo $m$ la máxima cantidad de elementos(días), luego la complejidad final sería $O(m·n!)$ siendo $m$ la cantidad de días máxima que tiene una propuesta y $n$ la cantidad de propuestas. 
