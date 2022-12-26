import pytest

from calcula_notas import calcula_nota_alumno, calcula_notas_curso

testdata_calcula_notas_alumno = [
    (
        {
            "nombre": "Luisa López",
            "exercises": [4, 6.5, 10, 8],
            "practise_passed": True,
            "partial_exam": 7.5,
            "final_exam": 8
        },
        7.8375
    ),
    (
        {
            "nombre": "Pedro García",
            "exercises": [2, 0, 5, 6],
            "practise_passed": True,
            "partial_exam": 3.3,
            "final_exam": 5.5
        },
        4.945
    ),
    (
        {
            "nombre": "Fermín Gutiérrez",
            "exercises": [8, 8, 10, 9.5],
            "practise_passed": False,
            "partial_exam": 8.2,
            "final_exam": 9
        },
        0
    )
]


@pytest.mark.parametrize("datos_alumno, nota_esperada", testdata_calcula_notas_alumno)
def test_calcula_nota_alumno(datos_alumno: {}, nota_esperada: float):
    assert calcula_nota_alumno(datos_alumno) == nota_esperada


testdata_calcula_notas_curso = [
    (
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
        ],
        [("Luisa López", 7.8375), ("Pedro García", 4.945), ("Fermín Gutiérrez", 0)]
    ),
    ([], [])
]


@pytest.mark.parametrize("datos_curso, notas_esperadas", testdata_calcula_notas_curso)
def test_calcula_notas_curso(datos_curso: {}, notas_esperadas: [(str, float)]):
    notas_calculadas = calcula_notas_curso(datos_curso)
    assert len(notas_calculadas) == len(notas_esperadas)
    for nota_esperada in notas_esperadas:
        nota_encontrada = None
        for nota_calculada in notas_calculadas:
            if nota_esperada[0] == nota_calculada[0]:
                nota_encontrada = nota_calculada
                assert nota_esperada[1] == nota_calculada[1]
        notas_calculadas.remove(nota_encontrada)
    assert len(notas_calculadas) == 0
