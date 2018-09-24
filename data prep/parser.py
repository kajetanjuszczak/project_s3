import pandas as pd
import csv

def parser(infile):
    table = pd.read_csv(infile, sep="\t")
    restricted = table.loc[table["Parameter Value[DoseLevel]"].isin(["Control", "High"])]
    restrictedt = restricted.loc[restricted["Parameter Value[TimeOfCollection]"].isin(["24"])]
    droped = restrictedt.drop_duplicates(subset=["Parameter Value[Compound]", "Parameter Value[DoseLevel]","Characteristics[CellType]","Characteristics[Organism]"])
    df = droped.groupby(["Parameter Value[Compound]", "Parameter Value[DoseLevel]"]).agg(['count'])
    df1 = df[df.gt(2).any(axis=1)]
    #df1.to_csv("drugsin3.txt", sep="\t", header=False)
    print(df1)

if __name__ == "__main__":
    parser("metadata.txt")