import sqlite3, string
conn = sqlite3.connect('population.db')

c = conn.cursor()
c.execute('''DROP TABLE IF EXISTS census''')
c.execute('''CREATE TABLE census (geography text, base int, estimate int, year0 int, year1 int, year2 int, year3 int, year4 int, year5 int, year6 int, year7 int)''')

pop = open('population.txt','r',encoding='ascii',errors='surrogateescape')
count = 0
for line in pop:
    count+=1
    print(line.strip())
    if count == 100:
        break

print(count)
    
pop.close()
conn.close()
