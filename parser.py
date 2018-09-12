import pandas

def parserhuman(infile):
    with open(infile, "r") as f:
        dictionary = {}
        c = 0
        for line in f:
            count = 0
            line = line.split()
            ## add to pandas dataframe one collumn consisting of all info
            c += 1
            if c == 2:
                break
        
    # hepatocytes human:: 2 - tissue 3,4 organism; 22 - dru; 26 - file, time - 32 , 33, dose - 11,12,13
if __name__ == "__main__":
    parser1("E-MTAB-798.sdrf.txt")