def calcula_nota_alumno(datos_alumno: {}) -> float:
    # si el alumno no ha aprobado la práctica, devuelvo un 0
    if datos_alumno["practise_passed"] is False:
        return 0

    # calculo la media de los ejericios de clase
    acumulado_ejercicios_clase = 0
    for nota_ejercicio_clase in datos_alumno["exercises"]:
        acumulado_ejercicios_clase += nota_ejercicio_clase
    media_ejercicios_clase = acumulado_ejercicios_clase / len(datos_alumno["exercises"])

    # pondero cada nota y devuelvo la suma
    valor_ejercicios_clase = media_ejercicios_clase * 0.1
    valor_examen_parcial = datos_alumno["partial_exam"] * 0.15
    valor_examen_final = datos_alumno["final_exam"] * 0.75
    return valor_ejercicios_clase + valor_examen_parcial + valor_examen_final


def calcula_notas_curso(datos_alumnos: []) -> [(str, float)]:
    notas_alumnos = []
    for datos_alumno in datos_alumnos:
        nota_alumno = calcula_nota_alumno(datos_alumno)
        entrada_alumno = (datos_alumno["nombre"], nota_alumno)
        notas_alumnos.append(entrada_alumno)
    return notas_alumnos
