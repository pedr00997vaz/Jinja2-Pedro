from fastapi import FastAPI
from typing import Optional
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def inicio():
    contenido_html = """
    <html>
    <head>
        <title>PedroVS</title>
    </head>
    <body>
        <h3>BIENVENIDOS</h3>
        <p>Este sitio pertenece a PedroVazquez y mostrará sus datos</p>
        <a href="Pedro.html">Pedro </a>
    </body>
    </html>
    """
    return HTMLResponse(content= contenido_html, status_code=200)

@app.get("/integrantes/item_id")
def integrantes(item_id: int, matricula: int, nombre: str, edad: Optional[int]=None):
    respuesta = f"""
    <html>
    <head>
    <title>{nombre}</title>
    </head>
    <body>
        <h3>sitio personal de {nombre}</h3>
        <ul>
            <li>Matricula: {matricula}</li>
            <li>Nombre: {nombre}</li>
            <li>Edad: {edad}</li>
        </ul>
    </body>
    </html>
    """
    return HTMLResponse(content=respuesta, status_code=200)
