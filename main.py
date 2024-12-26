import os

print("data ingestion started")
os.system("python src/data_ingestion.py")
print("data ingestion completed")

print("data preprocessing started")
os.system("python src/data_preprocessing.py")
print("data preprocessing completed")

print("feature engineering started")
os.system("python src/feature_engineering.py")
print("FE completed")

print("model building started")
os.system("python src/model_building.py")
print("model building completed")

print("model evaluation started")
os.system("python src/model_evaluation.py")
print("model evaluation completed")