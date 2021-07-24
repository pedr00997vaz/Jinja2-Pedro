from typing import Optional
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

lista_integrantes = [{'item_id': 1, 'matricula': 918104111, 'nombre': 'Pedro', 'edad': 22, 'APaterno': 'Vázquez','AMaterno': 'Sánchez', 'correo': 'Pedro@laselva.edu.mx', 'telefono': 9191401432, 'carrera': 'Redes Inteligentes'},
                     {'item_id': 2, 'matricula': 918105122, 'nombre': 'Rocio', 'edad': 19, 'APaterno': 'Vázquez','AMaterno': 'Martínez', 'correo': 'Roci@laselva.edu.mx', 'telefono': 9611778457, 'carrera': 'Redes Inteligentes'},
                     {'item_id': 3, 'matricula': 918106133, 'nombre': 'Rafael', 'edad': 20, 'APaterno': 'Luna','AMaterno': 'Gómez', 'correo': 'Rafa@laselva.edu.mx', 'telefono': 9191541408, 'carrera': 'Contaduria'},
                     {'item_id': 4, 'matricula': 918107144, 'nombre': 'Lorenzo', 'edad': 20, 'APaterno': 'Guzmán','AMaterno': 'Gómez', 'correo': 'lencho@laselva.edu.mx', 'telefono': 9672771457, 'carrera': 'Mecatronica'},
                     {'item_id': 5, 'matricula': 918108155, 'nombre': 'Carolina', 'edad': 21, 'APaterno': 'Sántiz','AMaterno': 'López', 'correo': 'karo@laselva.edu.mx', 'telefono': 9191735389, 'carrera': 'Turismo'},
                     {'item_id': 6, 'matricula': 918109156, 'nombre': 'Orlando', 'edad': 22, 'APaterno': 'Girón','AMaterno': 'Luna', 'correo': 'Orly@laselva.edu.mx', 'telefono': 9191771245, 'carrera': 'Ciberseguridad'},
                     {'item_id': 7, 'matricula': 918110157, 'nombre': 'Manuel', 'edad': 21, 'APaterno': 'Gutierres','AMaterno': 'García', 'correo': 'Man@laselva.edu.mx', 'telefono': 961177546, 'carrera': 'Redes Inteligentes'},
                     {'item_id': 8, 'matricula': 918111158, 'nombre': 'Angelica', 'edad': 20, 'APaterno': 'Pérez','AMaterno': 'Gómez', 'correo': 'Anyi@laselva.edu.mx', 'telefono': 9671773457, 'carrera': 'Agroalimetaria'},
                     {'item_id': 9, 'matricula': 918112159, 'nombre': 'Rosa', 'edad': 21, 'APaterno': 'González','AMaterno': 'Gómez', 'correo': 'Rosy@laselva.edu.mx', 'telefono': 9671774554, 'carrera': 'Desarrolo de Sofware'},
                     {'item_id': 10, 'matricula': 918113160, 'nombre': 'Uriel', 'edad': 19, 'APaterno': 'Moreno','AMaterno': 'Vázquez', 'correo': 'Uriel@laselva.edu.mx', 'telefono': 9191764733, 'carrera': 'Mecatronica'}]

@app.get('/integrantes')
async def leer_integrantes(item_id: int):
    for diccionario in lista_integrantes:
        if diccionario.get('item_id') == item_id:
            respuesta = f"""
            <html>
            <head>
                <title>{diccionario.get('nombre')}</title>
            </head>
            <body>
            <h3>Sitio personal {diccionario.get('nombre')}</h3>
            <ul>
                <li>Matricula: {diccionario.get('matricula')}</li>
                <li strong>APaterno: {diccionario.get('APaterno')}
                <li>AMaterno: {diccionario.get('AMaterno')}</li>
                <li>Nombre: {diccionario.get('nombre')}</li>
                <li>Edad: {diccionario.get('edad')} </li>
                <li>Correo: {diccionario.get('correo')}</li>
                <li>Telefono: {diccionario.get('telefono')}</li>
                <li>Carrera: {diccionario.get('carrera')}</li>
            </ul>
            </body>
            </html>
            """
            return HTMLResponse(content=respuesta, status_code=200)
    return "No se encontro el registro"