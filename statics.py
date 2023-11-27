import random
import pandas as pd

def read_csv(filename):
    data = pd.read_csv(filename, delimiter=';')
    return data

if __name__ == "__main__":
    symptoms = read_csv("/Applications/Учебное/Машинка/symptom.csv")
    diseases = read_csv("/Applications/Учебное/Машинка/disease.csv")

    patient_sympt = []
    for i in range(23):
        patient_sympt.append(random.randint(0,1))