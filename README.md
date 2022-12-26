# Proyecto 2

Tenemos una estructura de datos que contiene todas las notas del curso de todos los alumnos. La estructura tiene la siguiente forma:

```python

[
    {
        "nombre": "Luisa López",
        "exercises": [4, 6.5, 10, 8],
        "practise_passed": True,
        "partial_exam": 7.5,
        "final_exam": 8
    },
    {
        "nombre": "Pedro García",
        "exercises": [2, 0, 5, 6],
        "practise_passed": True,
        "partial_exam": 3.3,
        "final_exam": 5.5
    },
    {
        "nombre": "Fermín Gutiérrez",
        "exercises": [8, 8, 10, 9.5],
        "practise_passed": False,
        "partial_exam": 8.2,
        "final_exam": 9
    }
]
```

Es decir, disponemos de una lista donde cada elemento es un diccionario que contiene los datos de un alumno. Dichos datos son:

* nombre
* notas de ejercicios durante el curso
* si ha pasado o no la práctica
* nota del examen parcial
* nota del examen final

## Parte 1

Nos piden hacer una función que devuelva la nota obtenida por el alumno durante el curso, sabiendo que los pesos para calcular la nota son:

* ejercicios durante el curso representa el 10% de la nota
* examen parcial representa el 15% de la nota
* examen final representa el 75% de la nota

Además, solamente se podrá aprobar el curso si se tiene la práctica aprobada. Si el alumno no tiene aprobada la práctica la nota que deberá devolver esta función será un 0.

La función a implementar tiene la siguiente interfaz:

```python
def calcula_nota_alumno(datos_alumno: {}) -> float:
```

Siendo **datos_alumno** un diccionario con los datos de un alumno, como se ha descrito anteriormente. Por ejemplo:

```python
    {
        "nombre": "Luisa López",
        "exercises": [4, 6.5, 10, 8],
        "practise_passed": True,
        "partial_exam": 7.5,
        "final_exam": 8
    }
```

### SOLUCIÓN

Ya que conocemos las claves del diccionario (nombre, exercises, etc.) accederemos a los valores haciendo uso de las mismas. Además, cada valor tiene que ser tratado de distinta forma, ya que los tipos de datos son diferentes y el cálculo del peso de cada elemento es distinto.

Por ejemplo, los ejercicios son una lista de ejercicios, así que deberemos calcular la nota media de los ejercicios.

```python

acumulado_ejercicios_clase = 0
for nota_ejercicio_clase in datos_alumno["exercises"]:
    acumulado_ejercicios_clase += nota_ejercicio_clase

media_ejercicios_clase = acumulado_ejercicios_clase / len(datos_alumno["exercises"])
```

Es un problema típico de cálculo de media. Lo he resuelto usando un acumulador de nota y finalmente dividiendo por el número de ejercicios del curso, obtenido usando la función *len* sobre la lista de ejercicios. Otra opción habría sido declarar una variable que fuera incrementando en 1 por cada nota de ejercicio de clase recorrida.

En relación a los ejercicios de clase, todavía tenemos que calcular su valor según el peso que tienen los ejercicios de clase, que es un 10%.

```python
valor_ejercicios_clase = media_ejercicios_clase * 0.1
```

Haríamos lo mismo con el resto de notas:

```python
valor_examen_parcial = datos_alumno["partial_exam"] * 0.15
valor_examen_final = datos_alumno["final_exam"] * 0.75
```

Y la suma de todos estos valores sería la nota del alumno:

```python
return valor_ejercicios_clase + valor_examen_parcial + valor_examen_final
```

Todavía nos faltaría considerar un detalle, y es que el alumno tendría un 0 si no ha aprobado la práctica. Por ello, lo primero de todo, comprobaríamos si el alumno **NO** ha aprobado la práctica para devolver un 0 si fuera el caso:

```python
if datos_alumno["practise_passed"] is False:
    return 0
```

## Parte 2

Una vez implementada la función **calcula_nota_alumno** y haciendo uso de ella, nos piden procesar todos los datos del curso para obtener una lista con los resultados de todos los alumnos.

El resultado será una lista de tuplas donde el primer término será el nombre del alumno y el segundo la nota obtenida mediante **calcula_nota_alumno**

La función a implemente tiene la siguiente interfaz:

```python
def calcula_notas_curso(datos_alumnos: []) -> [(str, float)]:
```

### SOLUCIÓN

Tendremos que recorrer la lista de todos los alumnos e invocando la función *calcula_nota_alumno* con cada uno de los elementos de la lista.

Esta vez la estructura es una lista, así que la recorro de la siguiente forma:

```python
for datos_alumno in datos_alumnos:
```

Además, como resultado nos piden una lista de tuplas con el nombre del alumno y la nota que tiene, así que por un lado tenemos que obtener el nombre del alumno y por otro calcular su nota:

```python
for datos_alumno in datos_alumnos:
    nombre_alumno = datos_alumno["nombre"]
    nota_alumno = calcula_nota_alumno(datos_alumno)
```

Estos datos obtenidos tenemos que ir almacenándolos en una lista:

```python
notas_alumnos = []
for datos_alumno in datos_alumnos:
    nombre_alumno = datos_alumno["nombre"]
    nota_alumno = calcula_nota_alumno(datos_alumno)
    entrada_alumno = (nombre_alumno, nota_alumno)
    notas_alumnos.append(entrada_alumno)
```

Mención especial a que en las notas alumnos almacenamos una tupla con los dos elementos descritos. Para facilitarnos las lectura he decidido crear una variable con la tupla y luego añadirla al resultado.