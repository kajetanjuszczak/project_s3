import pandas as pd
import csv

def parser(infile):
    table = pd.read_csv(infile, sep="\t")
    list_comp = table[table.columns[0]].tolist()
    t = pd.read_csv("metadata.txt", sep="\t")
    restricted = t.loc[t["Parameter Value[Compound]"].isin(list_comp)]
    restricted1 = restricted.loc[restricted["Parameter Value[DoseLevel]"].isin(["Control", "High"])]
    restricted2 = restricted1.loc[restricted1["Parameter Value[TimeOfCollection]"].isin(["24"])]
    restricted2.to_csv("../selected_drugs.txt", sep="\t")

if __name__ == "__main__":
    parser("drugsin3.txt")