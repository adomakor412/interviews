import sqlite3, string

conn1 = sqlite3.connect('unemployment.db')
c = conn1.cursor()

conn2 = sqlite3.connect('workforce.db')
d = conn2.cursor()

c.execute('DROP TABLE IF EXISTS proletariat')
d.execute('''DROP TABLE IF EXISTS stat''')

c.execute('CREATE TABLE proletariat (county text, year17 int, year16 int, year15 int, year14 int, year13 int)')

d.execute('CREATE TABLE stat (county int, rate17 int, rate16 int, rate15 int, rate14 int, rate13 int)')

    
pop = open('unemployment.txt','r',encoding='ascii',errors='ignore')

def numConverter(str2num):
    try:
        num = int(str2num)
        return num
    except:
        pass

for line in pop:
    myLine = line.strip().split(',')
    county = myLine[2] + myLine[3]#string

    year17 = numConverter(myLine[4])
    year16 = numConverter(myLine[5])
    year15 = numConverter(myLine[7])
    year14 = numConverter(myLine[9])
    year13 = numConverter(myLine[11])
    
    rate17 = myLine[13]
    rate16 = myLine[14]
    rate15 = myLine[16]
    rate14 = myLine[18]
    rate13 = myLine[20]
    
    db = [(county, year17, year16, year15, year14, year13)]
    c.executemany("INSERT INTO proletariat VALUES (?,?,?,?,?,?)",db)
       
    db = [(county, rate17, rate16, rate15, rate14, rate13)]
    d.executemany("INSERT INTO stat VALUES (?,?,?,?,?,?)",db)
    
conn1.commit()
conn2.commit()
    
pop.close()
#conn1.close()
#conn2.close()

print('''Your query for the county and it's labor force population is of the form: ''',
      'TABLE proletariat (county text, year17 int, year16 int, year15 int, year14 int, year13 int)')

print('''Your query for the rate of the workforce active is of the form: ''',
      'TABLE stat (county int, rate17 int, rate16 int, rate15 int, rate14 int, rate13 int)')
