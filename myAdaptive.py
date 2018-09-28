import sqlite3, string
conn = sqlite3.connect('population.db')

c = conn.cursor()
c.execute('''DROP TABLE IF EXISTS census''')
c.execute('''CREATE TABLE census (geography text, base int, estimate int,
                year0 int, year1 int, year2 int, year3 int, year4 int,
                year5 int, year6 int, year7 int)''')

pop = open('population.txt','r',encoding='ascii',errors='ignore')
count = 0
for line in pop:
    count+=1
    myLine = line.strip().split(',')

    zipCode = myLine[1] #effective unique identifier
    geography = myLine[2] + ', ' + myLine[3]
    base = int(myLine[4])
    estimate = int(myLine[5])
    year0 = int(myLine[6])
    year1 = int(myLine[7])
    year2 = int(myLine[8])
    year3 = int(myLine[9])
    year4 = int(myLine[10])
    year5 = int(myLine[11])
    year6 = int(myLine[12])
    year7 = int(myLine[13])
    
    census = [(geography, base, estimate, year0, year1, year2, year3, year4, year5, year6, year7)]

    c.executemany("INSERT INTO census VALUES (?,?,?,?,?,?,?,?,?,?,?)", census)
conn.commit()


pop.close()
conn.close()
