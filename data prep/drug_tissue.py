import pandas as pd

def parser(infile):
    table = pd.read_csv(infile, sep="\t")
    t = table.drop_duplicates(subset=["Parameter Value[Compound]", "Characteristics[CellType]","Characteristics[Organism]"])
    t2 = t.groupby(["Characteristics[CellType]","Characteristics[Organism]"]).agg(['count'])
    print(t2)

if __name__ == "__main__":
    parser("../selected_drugs.txt")