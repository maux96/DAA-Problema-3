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

