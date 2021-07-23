from fastapi import FastAPI
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
