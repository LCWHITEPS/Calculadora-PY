import os
from flask import Flask, render_template, request, redirect, url_for, session
from descuento import descuento

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "calculadora-py-dev-key-cambia-en-produccion")


def numero(valor, etiqueta):
    try:
        return float(valor)
    except (TypeError, ValueError):
        raise ValueError(f"Escribe un número válido en «{etiqueta}».")


@app.route("/", methods=["GET"])
def inicio():
    historial = session.get("historial", [])
    return render_template("index.html", historial=historial, resultado=None,
                           valores={"num1": "", "num2": "", "porcentaje": "", "operacion": "suma"})


@app.route("/calcular", methods=["POST"])
def calcular():
    historial = session.get("historial", [])
    valores = {
        "num1": request.form.get("num1", "").strip(),
        "num2": request.form.get("num2", "").strip(),
        "porcentaje": request.form.get("porcentaje", "").strip(),
        "operacion": request.form.get("operacion", "suma").strip()
    }
    resultado = None
    error = None
    expresion = ""

    try:
        op = valores["operacion"]
        if op == "descuento":
            precio = numero(valores["num1"], "precio")
            porcentaje = numero(valores["porcentaje"], "porcentaje de descuento")
            final = descuento(precio, porcentaje)
            resultado = final
            expresion = f"Descuento de {porcentaje:g}% sobre ${precio:,.2f}"
        else:
            a = numero(valores["num1"], "primer número")
            b = numero(valores["num2"], "segundo número")
            if op == "suma":
                resultado, simbolo = a + b, "+"
            elif op == "resta":
                resultado, simbolo = a - b, "−"
            elif op == "multiplicacion":
                resultado, simbolo = a * b, "×"
            elif op == "division":
                if b == 0:
                    raise ValueError("No se puede dividir entre cero.")
                resultado, simbolo = a / b, "÷"
            elif op == "potencia":
                resultado, simbolo = a ** b, "^"
            else:
                raise ValueError("Selecciona una operación válida.")
            if isinstance(resultado, complex) or not isinstance(resultado, (int, float)) or abs(resultado) == float("inf"):
                raise ValueError("El resultado no es un número real válido.")
            expresion = f"{a:g} {simbolo} {b:g}"

        resultado = round(resultado, 8)
        item = {"expresion": expresion, "resultado": f"{resultado:,.8f}".rstrip("0").rstrip(".")}
        historial.insert(0, item)
        session["historial"] = historial[:8]
    except (ValueError, OverflowError, TypeError) as exc:
        error = str(exc) or "No se pudo realizar el cálculo."

    return render_template("index.html", historial=session.get("historial", []),
                           resultado=resultado, error=error, expresion=expresion, valores=valores)


@app.route("/limpiar", methods=["POST"])
def limpiar_historial():
    session["historial"] = []
    return redirect(url_for("inicio"))


@app.route("/health")
def health():
    return {"status": "ok"}, 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=False)
