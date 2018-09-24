import pandas as pd

def file_names(organ, species, db_file):
    df = pd.read_csv(db_file, sep="\t")
    df1 = df.loc[df["Characteristics[CellType]"].isin([organ])]
    df2 = df1.loc[df1["Characteristics[Organism]"].isin([species])]
    list_cel = df2[df2.columns[9]].tolist()
    print(list_cel)
if __name__ == "__main__":
    file_names("hepatocyte", "Rattus norvegicus", "../selected_drugs.txt")
