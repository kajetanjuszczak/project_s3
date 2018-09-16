import pandas as pd

def parser(infile):
    table = pd.read_csv(infile, sep="\t")
    pivot = pd.pivot_table(table, 
    index=["Parameter Value[Compound]"], values=["Parameter Value[TimeOfCollection]"], aggfunc='count')
    print(pivot)
    #p2 = pivot[pivot["Parameter Value[TimeOfCollection]"] == 16]
    #p2.to_csv("second_select.txt", sep="\t")
    #SELECT 2 CONFIRMED, DATA I HAVE NOW IS SAME FOR ALL DRUGS
    #2 REPEATS FOR HEPATOCYTES FOR 2,8,24H AND 3,6,9,24 FOR LIVER AND KIDNEYS
if __name__ == "__main__":
    parser("select2.txt")