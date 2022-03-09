from pydoc import render_doc
from flask import Flask, render_template, redirect, request

app = Flask(__name__)


@app.route("/")
def la_funcion():
    return render_template("mipagina.html")


@app.route("/bye/<nombre>/<apellido>")
def otra_funcion(nombre, apellido):
    return render_template("paginadespedida.html", name=nombre, surname=apellido)
    return f"Hasta luego {nombre} {apellido}"

if __name__ == '__main__':
    app.run(debug=True)










# def index():
#     return '<h1>Hello World!</h1>'


