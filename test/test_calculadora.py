
import subprocess
import sys
import unittest
from pathlib import Path

# Ruta del archivo principal
CALCULADORA = Path(__file__).resolve().parent.parent / "calculator.py"



def ejecutar_calculadora(entrada):
    proceso = subprocess.run(
        [sys.executable, str(CALCULADORA)],
        input=entrada,
        capture_output=True,
        text=True,
        encoding="cp1252",
        errors="replace",
        timeout=10
    )

    return (proceso.stdout or "") + (proceso.stderr or "")


class TestCalculadora(unittest.TestCase):

    def test_suma(self):
        salida = ejecutar_calculadora("1\n8\n2\n6\n")
        self.assertIn("Resultado: 10.0", salida)

    def test_resta(self):
        salida = ejecutar_calculadora("2\n8\n3\n6\n")
        self.assertIn("Resultado: 5.0", salida)

    def test_multiplicacion(self):
        salida = ejecutar_calculadora("3\n4\n5\n6\n")
        self.assertIn("Resultado: 20.0", salida)

    def test_division(self):
        salida = ejecutar_calculadora("4\n10\n2\n6\n")
        self.assertIn("Resultado: 5.0", salida)

    def test_potencia(self):
        salida = ejecutar_calculadora("5\n2\n3\n6\n")
        self.assertIn("Resultado: 8.0", salida)

    def test_division_entre_cero(self):
        salida = ejecutar_calculadora("4\n10\n0\n6\n")
        self.assertIn(
            "no se puede dividir entre cero",
            salida
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)