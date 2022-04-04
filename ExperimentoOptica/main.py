from scipy.io import wavfile
import matplotlib.pyplot as plt


def indices(lista, buscar):
    list_indices = []
    for i in range(len(lista)):
        if buscar == lista[i]:
            list_indices.append(i)

    return list_indices


######PARA EL AUDIO 1#######
amplitudes1 = []

numeros_de_archivo1 = [x for x in range(1, 22)]

frecuencias_en_cada_audio = []

for n in numeros_de_archivo1:
    samplerate, data = wavfile.read(f"recs1/rec_{n}.wav")
    tiempo = len(data)/samplerate
    ymax = max(data)
    ymin = min(data)
    media = (ymax + ymin)/2
    amplitudes1.append(ymax - media)

    lista_indices = indices(data, media)
    frecuencias = []

    for i in range(len(lista_indices) - 1):
        periodo = ((lista_indices[i + 1] - lista_indices[i]) / (samplerate-1))*2
        frecuencias.append(1/periodo)
    try:
        frecuencias_en_cada_audio.append(sum(frecuencias)/len(frecuencias))
    except:
        continue

frecuencia1 = sum(frecuencias_en_cada_audio)/len(frecuencias_en_cada_audio)
frecuencia1 = int(round(frecuencia1, 0))
print(f"Frecuencia de los audios de la carpeta 1: {frecuencia1}")

coef1 = max(amplitudes1)/min(amplitudes1)
R = (coef1 - 1)/(coef1 + 1)
R = round(R, 1)
print(f"Indice de reflexion para la frecuencia {frecuencia1}Hz: {R}")

######PARA EL AUDIO 2#######

amplitudes2 = []

numeros_de_archivo2 = [x for x in range(1, 52)]

frecuencias_en_cada_audio2 = []

for n in numeros_de_archivo1:
    samplerate, data = wavfile.read(f"recs2/rec_{n}.wav")
    tiempo = len(data)/samplerate
    ymax = max(data)
    ymin = min(data)
    media = (ymax + ymin)/2
    amplitudes2.append(ymax - media)

    lista_indices = indices(data, media)
    frecuencias = []

    for i in range(len(lista_indices) - 1):
        periodo = ((lista_indices[i + 1] - lista_indices[i]) / (samplerate - 1))*2
        frecuencias.append(1/periodo)
    try:
        frecuencias_en_cada_audio2.append(sum(frecuencias)/len(frecuencias))
    except:
        continue

frecuencia2 = sum(frecuencias_en_cada_audio2)/len(frecuencias_en_cada_audio2)
frecuencia2 = int(round(frecuencia2, 0))
print(f"Frecuencia de los audios de la carpeta 2: {frecuencia2}")

coef2 = max(amplitudes2)/min(amplitudes2)
R2 = (coef2 - 1)/(coef2 + 1)
R2 = round(R2, 1)
print(f"Indice de reflexion para la frecuencia {frecuencia2}Hz: {R2}")

##### GRAFICAS #####

eje_x = [frecuencia1, frecuencia2]
eje_y = [R, R2]

###### GRAFICA OCUPANDO TODA LA IMAGEN ######
plt.plot(eje_x, eje_y)
plt.xscale("log")

plt.xlabel("Escala Logarítmica de la frecuencia")
plt.ylabel("Indice de reflexión")

plt.savefig("Grafica_en_zoom.png")
plt.show()

##### GRAFICA CON LOS LIMITES CORRECTOS #####
plt.plot(eje_x, eje_y)
plt.xscale("log")

plt.xlabel("Escala Logarítmica de la frecuencia")
plt.ylabel("Indice de reflexión")

plt.xlim(250, 8000)
plt.ylim(0, 1)

plt.savefig("Grafica_final.png")
plt.show()
