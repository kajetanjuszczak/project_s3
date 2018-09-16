import pandas as pd
import csv

def parser(infile):
    table = pd.read_csv(infile, sep="\t")
    t = table.drop_duplicates(
    subset=["Parameter Value[Compound]","Characteristics[CellType]", "Characteristics[Organism]","Parameter Value[DoseLevel]"])
    pivot = pd.pivot_table(t, 
    index=["Parameter Value[Compound]"], values=["Parameter Value[TimeOfCollection]"], aggfunc='count')
    p2 = pivot[pivot["Parameter Value[TimeOfCollection]"] == 16]
    p2.to_csv("second_select.txt", sep="\t")

if __name__ == "__main__":
    parser("metadata.txt") 