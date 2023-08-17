import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import pathlib

# Preparación de directorios y ficheros
# directorio_defecto = '/Users/jordi/Desktop/FORMACION/CODE/phdUVa/videoandimus/' # ruta absoluta al directorio de trabajo
directorio_defecto ='phdUVa/videoandimus/' # ruta relativa al directorio de trabajo
sujetos = os.listdir(directorio_defecto)
sujetoseleccionado = st.sidebar.selectbox('Selecciona el sujeto a analizar', sujetos)
actividades = []
directorio = pathlib.Path(directorio_defecto+"/"+sujetoseleccionado)
for fichero in directorio.iterdir():
    if fichero.is_file() and (fichero.name.startswith("ik") and fichero.name.endswith(".mot")):
        actividades.append(fichero.name)
actividadseleccionada = st.sidebar.selectbox('Selecciona la actividad a analizar', actividades)
fichero= (str(directorio) + '/'+ str(actividadseleccionada))

# Carga de datos 

file_oi= fichero

i=0
with open (file_oi, "r") as myfile:
    while i < 6:
        line = next(myfile)
        i += 1
    angles_col_names = next(myfile).split("\t")
    angles_values = [line.split('\t') for line in myfile.read().splitlines()]

# Creación de dataframe
df_angles = pd.DataFrame(angles_values, columns=angles_col_names)
df_angles = df_angles.astype('float32')

st.title('Análisis de datos de movimiento (VIDIMU)')
st.markdown('Visualiza de forma gráfica e interactiva la información de los movimientos de las articulaciones de los sujetos')

selected_joint = st.selectbox('Selecciona la articulación a analizar', df_angles.columns[1:])


fig, ax = plt.subplots()
ax=sns.lineplot(data=df_angles, x='time', y=selected_joint)
ax.set_title('Articulación: {}'.format(selected_joint))
plt.xlabel('Tiempo (s)')
plt.ylabel('Ángulo (º)')
st.pyplot(fig)