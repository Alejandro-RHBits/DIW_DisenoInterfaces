from fastapi import FastAPI

app = FastAPI()

@app.get('MiPrimerAPI')
def hola(name):
    return ("¡¡¡Hola mundo!!!", name)

print(hola("Alejo"))