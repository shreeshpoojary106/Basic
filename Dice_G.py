import pandas as pd
import numpy as np
import os

FILE_NAME = "dice_history.csv"

if not os.path.exists(FILE_NAME):
    df = pd.DataFrame(columns=["Die1", "Die2", "Die3"])
    df.to_csv(FILE_NAME, index=False)

df = pd.read_csv(FILE_NAME)

def predict_next(df):
    if len(df) == 0:
        return np.random.randint(1, 7, 3)

    prediction = []

    for col in ["Die1", "Die2", "Die3"]:
        prediction.append(int(df[col].mode()[0]))

    return prediction

prediction = predict_next(df)

print("\nPredicted Next Roll")
print("-------------------")
print(f"Die 1: {prediction[0]}")
print(f"Die 2: {prediction[1]}")
print(f"Die 3: {prediction[2]}")

print("\nEnter Actual Roll")

d1 = int(input("Die 1: "))
d2 = int(input("Die 2: "))
d3 = int(input("Die 3: "))

new_row = pd.DataFrame([[d1, d2, d3]], columns=["Die1", "Die2", "Die3"])
df = pd.concat([df, new_row], ignore_index=True)

df.to_csv(FILE_NAME, index=False)

print("\nData saved successfully!")
print(df.tail())