#hw grader for EAS 230

#README
# -download the week's grades from the google sheet as a .csv csv_file
# -rename the file to 'hw.csv'
# -place this file into the same folder with 'hwgrader.py'
# -make sure '____.csv'
# -make sure python3 is installed
# -cd to the directory containing the files from your terminal
# -run the program with 'python3 hwGrader.py'

#I can just run it lol.

import csv

def import1():
    with open('./____.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        array_boii=[]
        for row in csv_reader:
            array_boii.append(row)
    return array_boii

def import2():
    with open('./____.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        array_boii=[]
        for row in csv_reader:
            array_boii.append(row)
    return array_boii

def importhw():
    with open('./hw.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        array_boii=[]
        for row in csv_reader:
            array_boii.append(row)
    return array_boii

def cleaner(roster1):
    cleaned=[]
    for line in roster1:
        cleaned.append(line[3])
    return cleaned

def gradeSum(grades):
    students=[]
    ungraded = []
    returner=[]
    counter=0
    for x in grades:

        if counter == 0:
            counter+=1
        else:

            #try:
            intA=float(x[5])
            intB=float(x[6])
            intC=float(x[7])
            intD=float(x[8])
        #    except ValueError:
        #        intA=-1
        #        intB=-1
        #        intC=-1
        #        intD=-1
            if intA<0:
                stringy=[x[1],x[0],x[3],"Q1 Incomplete"]
                ungraded.append(stringy)
            elif intB<0:
                stringy=[x[1],x[0],x[3],"Q2 Incomplete"]
                ungraded.append(stringy)
            elif intC<0:
                stringy=[x[1],x[0],x[3],"Q3 Incomplete"]
                ungraded.append(stringy)
            elif intD<0:
                stringy=[x[1],x[0],x[3],"Q4 Incomplete"]
                ungraded.append(stringy)
            else:
                x.append(intA+intB+intC+intD)
                students.append(x)

            counter+=1
    returner.append(students)
    returner.append(ungraded)
    return returner

def whichSection(students,judeStudents,alaaStudents):
    1Class=[]
    2Class=[]
    snmackayClass=[]
    mostafaClass=[]

    for a in students:
        for b in 1Students:
            if b==a[3]:
                1Class.append(a)
    for a in students:
        for b in 2Students:
            if b==a[3]:
                2Class.append(a)

    with open("grades1.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Last Name","First Name","ubit name","person #", " ","Q1","Q2","Q3","Q4"," ","Total"])
        writer.writerows(1Class)

    with open("grades2.csv", "w", newline="") as g:
        writer = csv.writer(g)
        writer.writerow(["Last Name","First Name","ubit name","person #", " ","Q1","Q2","Q3","Q4"," ","Total"])
        writer.writerows(2Class)

def ungraded(ungradedKids):

    with open("ungradedStudents.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(ungradedKids)

def main ():
    roster1=import1()
    roster2=import2()
    grades=importhw()
    1Students =cleaner(roster1)
    2Students =cleaner(roster2)
    listy=gradeSum(grades)
    whichSection(listy[0],1Students,2Students)
    ungraded(listy[1])

if __name__ == "__main__":
    main()
