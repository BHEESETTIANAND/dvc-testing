import os

print("data ingestion started")
os.system("python src/data_ingestion.py")
print("data ingestion completed")
print("data preprocessing started")
os.system("python src/data_preprocessing.py")
print("data preprocessing completed")