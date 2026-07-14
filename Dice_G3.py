import pandas as pd
import numpy as np
import os

FILE_NAME = "dice_Gambel_history.csv"

if not os.path.exists(FILE_NAME):
    df = pd.DataFrame(columns=["Die"])
    df.to_csv(FILE_NAME, index=False)

df = pd.read_csv(FILE_NAME)

def predict_next(df):
    if len(df) == 0:
        return np.random.randint(1, 19)

    prediction = []

    for col in ["Die"]:
        prediction.append(int(df[col].mode()[0]))

    return prediction

prediction = predict_next(df)

print("\nPredicted Next Roll")
print("-------------------")
print(f"Die : {prediction}")


print("\nEnter Actual Roll")

d = int(input("Die : "))

new_row = pd.DataFrame([[d]], columns=["Die"])
df = pd.concat([df, new_row], ignore_index=True)

df.to_csv(FILE_NAME, index=False)

print("\nData saved successfully!")
print(df.tail())