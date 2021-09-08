import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv("source data/births.csv")


print("A. Geef het aantal rijen en kolommen van de dataset terug")
print(df.info(), "\n")


print("B. Geef alle rijen van het jaar 2001")
result_B = df.loc[df["year"] == 2001]
print(result_B, "\n")


print("C. Geef het aantal rijen uit de vorige query")
result_C = len(result_B.index)
print(result_C, "\n")


print("D. Geef het aantal geboorten per jaar")
result_D = df.groupby(["year"]).agg({"births": [np.sum]})
print(result_D, "\n")


print("E. Geef het aantal geboorten per jaar per maand waar deze onder de 325000 is")
result_E = df.groupby(["year", "month"]).agg({"births": [np.sum]})
result_E = result_E[result_E["births"]["sum"] < 325000]
print(result_E, "\n")


print("F. Visualiseer het totaal aantal geboorten per jaar")
result_F = df.groupby(["year"]).agg({"births": [np.sum]})
result_F.reset_index(level=[0], inplace=True)
result_F.columns = result_F.columns.droplevel()
result_F.columns.values[0] = "year"
result_F.plot(x="year", y="sum", kind="bar")
plt.show()
print()


print("G. Stel dat je meer dan 1 csv file had waarbij de gegevens gecombineerd zouden moeten worden, wat zou anders in de code gedaan moeten worden?")
multiple_birth_files = []
source_birth_files = []

for file_number in range(1, 4):
    temp_df = pd.read_csv(f"separated data/{file_number}_births.csv")
    source_birth_files.append(f"{file_number}_births.csv")
    multiple_birth_files.append(temp_df)

result_G = pd.concat(multiple_birth_files, keys=source_birth_files)
result_G.to_csv("extracted data/concatenated_births.csv")
print()


print("H. Bedenk zelf 1 query per groepslid op basis van de 3 datasets uit vraag G \n")

print("H - Akash. Wat is het totaal aantal geboortes op november 1999")
result_H_Akash = df.loc[(df["year"] == 1999) & (df["month"] == 11)]
total = result_G["births"].sum()
print(total, "\n")

print("H - Richal. Wat is het gemiddeld aantal geboorters per jaar na 1999")
temp = df.loc[df["year"] > 1999]
result_H_Richal = temp.groupby(["year"]).agg({"births": [np.average]})
print(result_H_Richal)
print()

print("H - Jimmy. Vraag")
print("\n")

print("H - Roderick. Vraag")
print("\n")
