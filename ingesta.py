import pandas as pd
import pymysql
import boto3

# Conexión a la base de datos en tu EC2
conn = pymysql.connect(
    host='54.172.56.232',  # 👈 Cambia esto por la IP pública de tu instancia EC2
    port=3307,             # 👈 O 3306 si usaste el puerto original
    user='root',
    password='1234',
    database='empresa'
)

# Leer los datos de la tabla 'personas'
df = pd.read_sql("SELECT * FROM personas", conn)
conn.close()

# Guardar como CSV
csv_file = "personas.csv"
df.to_csv(csv_file, index=False)

# Subir a S3
s3 = boto3.client('s3')

# 👇 Cambia 'tu-bucket' al nombre de tu bucket real de S3
bucket_name = "mbcoutput02"
s3.upload_file(csv_file, bucket_name, csv_file)

print("Ingesta completada desde MySQL y archivo subido a S3")
