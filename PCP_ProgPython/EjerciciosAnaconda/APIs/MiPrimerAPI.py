from fastapi import FastAPI

app = FastAPI()

@app.get('MiPrimerAPI')
def hola():
    return ("¡¡¡Hola mundo!!!")

print(hola())