# student.py
import pandas as pd

def analiza_ocen(dane):
    df = pd.DataFrame(dane)
    df["srednia"] = df.mean(axis=1)
    df["status"] = df["srednia"].apply(lambda x: "Zaliczony" if x >= 3 else "Nie zaliczony")
    return df

if __name__ == "__main__":
    dane = {"matematyka": [5, 2], "fizyka": [4, 2], "chemia": [3, 3]}
    print(analiza_ocen(dane))
