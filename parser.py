import pandas as pd

def parser(infile):
    table = pd.read_csv(infile, sep="\t")
    t = table.drop_duplicates(
    subset=["Parameter Value[Compound]","Characteristics[CellType]", "Characteristics[Organism]"])
    pivot = pd.pivot_table(t, 
    index=["Parameter Value[Compound]"], aggfunc='count')
    print(pivot)

if __name__ == "__main__":
    parser("metadata.txt")