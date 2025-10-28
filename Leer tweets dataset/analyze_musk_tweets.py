import nltk 
#Solo se ejecuta una vez para descargar los recursos necesarios
#nltk.download('stopwords')
#nltk.download('vader_lexicon')
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
import re
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import numpy as np

df= pd.read_csv(r"C:\Users\mzbs\Documents\Curso Python\datasets\musk_tweets_cleaned.csv", low_memory=False)
df['createdAt'] = pd.to_datetime(df['createdAt'],errors='coerce')

# 1- HORAS DE PUBLICACIÓN
df['hour'] = df['createdAt'].dt.hour
tweets_por_hora=df['hour'].value_counts().sort_index()

# Usar las horas reales como posiciones en x para etiquetas legibles
x = tweets_por_hora.index

# Crear figura/axes explícitos y mapeo de colores
fig, ax = plt.subplots(figsize=(10, 5))
norm = plt.Normalize(tweets_por_hora.min(), tweets_por_hora.max())
colors = plt.cm.plasma(norm(tweets_por_hora.values))
ax.bar(x, tweets_por_hora.values, color=colors)

# Asociar un ScalarMappable al Axes para que colorbar funcione correctamente
mappable = plt.cm.ScalarMappable(norm=norm, cmap='plasma')
mappable.set_array(tweets_por_hora.values)
fig.colorbar(mappable, ax=ax, label='Número de tweets de Elon Musk')

ax.set_title("Número de tweets por hora del día")
ax.set_xlabel("Hora del día")
ax.set_ylabel("Número de tweets")
ax.set_xticks(x)
ax.set_xticklabels(x, rotation=45)
plt.tight_layout()
plt.grid(True, linestyle='-', alpha=0.36)
#plt.show()


# Visualización de tweets por hora ejercicio
#plt.figure(figsize=(10,6))
#sns.barplot(x=tweets_por_hora.index, y=tweets_por_hora.values, palette="plasma")
#plt.title("Número de tweets por hora del día")
#plt.xlabel("Hora del día")
#plt.ylabel("Número de tweets")
#plt.xticks(rotation=45)
#plt.savefig(r"C:\Users\mzbs\Documents\Curso Python\Graficos\hora_tweets.png")
#plt.show()


# 2- PALABRAS MAS REPETIDAS ULTIMOS 1000 TWEETS
df_last_1000= df.sort_values('createdAt', ascending=False)

def limpiar_texto(texto):
    texto = texto.lower()  # Convertir a minúsculas
    texto = re.sub(r'http\S+', '', texto)  # Eliminar URLs
    texto = re.sub(r'[@#]\w+', '', texto)  # Eliminar menciones y hastags
    texto = re.sub(r'[^a-z\s]', '', texto)  # Eliminar puntuación y caracteres especiales
    return texto.strip()

df_last_1000['texto_limpio'] = df_last_1000['fullText'].apply(limpiar_texto)# convertir la columna en una lista de strings y unirlas en un solo string
texto_completo = " ".join(df_last_1000['texto_limpio'].tolist())# convertir la columna en una lista de strings y unirlas en un solo string
palabras= texto_completo.split()# dividir el texto en palabras individuales
stop_words = set(stopwords.words('english'))# conjunto de palabras comunes en inglés
palabras_filtradas = [palabra for palabra in palabras if palabra not in stop_words and len(palabra) > 2]# filtrar palabras comunes y de una sola letra
contador_palabras = Counter(palabras_filtradas)# contar la frecuencia de cada palabra

palabras_filtradas2 = [palabra for palabra in palabras if palabra not in stop_words and len(palabra) > 1 and palabra == "wow"]# filtrar palabras comunes y de una sola letra
contador_palabras2 = Counter(palabras_filtradas2)# contar la frecuencia de cada palabra

print("Las 10 palabras más comunes en los últimos 1000 tweets son:")
print(contador_palabras.most_common(10))
print(contador_palabras2.most_common(10))


# 3- ANALISIS DE SENTIMIENTO
top5 = df.sort_values('createdAt', ascending=False).head(5).copy()
sia = SentimentIntensityAnalyzer()



def classificar_sentimiento(texto):
    score = sia.polarity_scores(texto)['compound'] # -1 (negativo) a 1 (positivo)
    if score >= 0.05:
        return "Positivo"
    elif score <= -0.05:
        return "Negativo"
    else:
        return "Neutral"

top5['sentimiento'] = top5['fullText'].apply(lambda x: sia.polarity_scores(x)['compound'])# calcular el puntaje de sentimiento compuesto
top5['clasificacion'] = top5['fullText'].apply(classificar_sentimiento)# clasificar el sentimiento

print("Análisis de sentimiento de los últimos 5 tweets:")
top5[['fullText','likeCount','sentimiento', 'clasificacion']].to_csv(r"C:\Users\mzbs\Documents\Curso Python\datasets\analisis_sentimiento_top5.csv", index=False)
print(top5[['fullText','likeCount','sentimiento', 'clasificacion']])    