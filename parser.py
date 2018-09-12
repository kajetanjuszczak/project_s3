import pandas

def parser1(infile):
    with open(infile, "r") as f:
        count = 0
        for line in f:
            line = line.split()
            print("fielname:{} drug:{} time:{} species:{} from {} {} dose:{}-{} {}".format(line[34],line[30],line[40],line[42],line[2],line[3],line[13],line[14],line[15]))
            count += 1
            if count == 20:
                break

    #file 34; drug 30; time 40; tissue - 42; species 2,3; dose 13,14,15
if __name__ == "__main__":
    parser1("E-MTAB-799.sdrf.txt")