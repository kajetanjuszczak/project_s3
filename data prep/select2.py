import pandas as pd

def parser(infile):
    table = pd.read_csv(infile, sep="\t")
    pivot = pd.pivot_table(table, 
    index=["Parameter Value[Compound]"], values=["Parameter Value[TimeOfCollection]"], aggfunc='count')
    print(pivot)
    #p2 = pivot[pivot["Parameter Value[TimeOfCollection]"] == 16]
    #p2.to_csv("second_select.txt", sep="\t")
if __name__ == "__main__":
    parser("select_drugs.txt")