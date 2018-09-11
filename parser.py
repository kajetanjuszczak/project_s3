def parser1(infile):
    with open(infile, "r") as f:
        c = 0
        for line in f:
            line = line.split()
            count = 0
            for i in line:
                print(count, i)
                count += 1
            c += 1
            if c == 2:
                break

if __name__ == "__main__":
    parser1("E-MTAB-799.sdrf.txt")