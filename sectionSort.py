import csv


def importJude():
    with open('./Jude.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        array_boii=[]
        for row in csv_reader:
            array_boii.append(row)
    return array_boii

def sectionSort(cleaned):
    C2=[]
    C4=[]
    D1=[]
    D2=[]

    for x in cleaned:
        print(x[4])
        if x[4]=="C2":
            C2.append(x)
        elif x[4]=="C4":
            C4.append(x)
        elif x[4]=="D1":
            D1.append(x)
        elif x[4]=="D2":
            D2.append(x)
    listOf=[]
    listOf.append(C2)
    listOf.append(C4)
    listOf.append(D1)
    listOf.append(D2)
    return listOf

def printer(i,name):
    with open(name, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(i)

def main():
    list=importJude()
    sections=sectionSort(list)
    printer(sections[0],"C2.csv")
    printer(sections[1],"C4.csv")
    printer(sections[2],"D1.csv")
    printer(sections[3],"D2.csv")

if __name__ == "__main__":
    main()
