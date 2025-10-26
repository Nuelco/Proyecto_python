import pandas as pd

# Ruta correcta al dataset
csv_path = r"C:\Users\mzbs\Documents\Curso Python\datasets\all_musk_posts.csv"
csv_path_date = r"C:\Users\mzbs\Documents\Curso Python\datasets\musk_tweets_cleaned.csv"
# Leer el CSV
df = pd.read_csv(csv_path_date, low_memory=False)
print(df)
#df['createdAt'] = pd.to_datetime(df['createdAt'],errors='coerce')
#df=df.dropna(subset=['fullText'])

#df.to_csv(r"C:\Users\mzbs\Documents\Curso Python\datasets\musk_tweets_cleaned.csv", index=False)
#print("Dataset guardado correctamente.")