import pandas as pd
from fastapi import FastAPI

df=pd.read_csv("datos_alumnos.csv")
df.columns = df.columns.str.strip()

app = FastAPI(title="iesazarquiel", description="API para gestión de alumnos del IES Azarquiel")

#Sacar listado de alumnos por id
@app.get("/info-alumnos", summary="Obtener ID de alumnos")
def info_alumnos():
    ids = df['ID'].tolist()
    return{"ID": ids}


#Asistencia de alumnos
@app.get("/asistencia", summary="Consultar asistencia de un alumno")
def asistencia(idalumno: int = None):

    if idalumno is None:
        return{
            "mensaje": "Debes indicar un ID en el cuadro",
            "ejemploUso": "/asistencia?idalumno=1",
            "idValidos": df['ID'].tolist()
        }
    
    filaAlumno = df[df['ID'] == idalumno]

    if filaAlumno.empty:
        return {"error": f"El alumno con id {idalumno} no existe"}
    
    nombre = filaAlumno.iloc[0]['Nombre']
    apellidos = filaAlumno.iloc[0]['Apellidos']
    asistencia_valor = filaAlumno.iloc[0]['Asistencia']

    return {
        "alumno": f"{nombre} {apellidos}",
        "asistencia": f"{int(asistencia_valor*100)}%"
    }


#Consultar notas de alumno
@app.get("/notas", summary="Consultar notas")
def notas(idalumno: int = None, notaConsultada: str = None):
    
    if idalumno is None or notaConsultada is None:
        cols_notas = [c for c in df.columns if c not in ['ID', 'Nombre', 'Apellidos', 'Asistencia']]
        return {
            "mensaje": "Debes completar los parametros 'id' y 'nota'",
            "ejemplo": "/notas?idalumno=1001&notaConsultada=Parcial1",
            "notas_posibles": cols_notas
        }

    filaAlumno = df[df['ID'] == idalumno]
    if filaAlumno.empty:
        return {"error": f"El alumno con id {idalumno} no existe"}

    columna_real = None
    for col in df.columns:
        if col.lower() == notaConsultada.lower():
            columna_real = col
            break
    
    if not columna_real:
        return {"error": f"La nota '{notaConsultada}' no existe en el registro."}

    valor_nota = filaAlumno.iloc[0][columna_real].item()
    
    return {
        "alumno": f"{filaAlumno.iloc[0]['Nombre']} {filaAlumno.iloc[0]['Apellidos']}",
        "asignatura": columna_real,
        "calificacion": valor_nota
    }