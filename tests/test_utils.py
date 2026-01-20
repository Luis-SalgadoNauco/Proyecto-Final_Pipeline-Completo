from src.utils import calcular_total_ventas


def test_calculo_totales():
    # Arrange (datos de prueba)
    ventas = [
        {"producto": "A", "cantidad": 2, "precio": 10},
        {"producto": "B", "cantidad": 1, "precio": 20},
        {"producto": "A", "cantidad": 3, "precio": 10},
    ]

    # Act (ejecutar función)
    resultado = calcular_total_ventas(ventas)

    # Assert (verificaciones)
    assert resultado["A"] == 50, f"Producto A: expected 50, got {resultado['A']}"
    assert resultado["B"] == 20, f"Producto B: expected 20, got {resultado['B']}"

print("✅ Test unitario de cálculo de ventas PASÓ")


if __name__ == "__main__":
    test_calculo_totales()
