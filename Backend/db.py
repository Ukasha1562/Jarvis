import sqlite3
import csv
con=sqlite3.connect("apps.db")
cur=con.cursor()

# for system apps

# table
# cur.execute("CREATE TABLE IF NOT EXISTS system_apps(id INTEGER PRIMARY KEY, name VARCHAR(100), path VARCHAR(1000))")
# apps
# cur.execute("INSERT INTO system_apps VALUES(null, 'word', 'C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\WINWORD.exe')")
# cur.execute("INSERT INTO system_apps VALUES(null, 'microsoft edge', 'C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe')")
# cur.execute("INSERT INTO system_apps VALUES(null, 'power point', 'C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\POWERPNT.exe')")
# con.commit()


# for websites

#table
#cur.execute("CREATE TABLE IF NOT EXISTS websites(id INTEGER PRIMARY KEY, name VARCHAR(100), url VARCHAR(1000))")

# websites
# cur.execute("INSERT INTO websites VALUES(null, 'chat gpt', 'https://chat.openai.com')")
# cur.execute("INSERT INTO websites VALUES(null, 'linkedin', 'https://linkedin.com')")
# cur.execute("INSERT INTO websites VALUES(null, 'gmail', 'https://mail.google.com')")
# cur.execute("INSERT INTO websites VALUES(null, 'lms', 'https://lms.superior.edu.pk')")
# cur.execute("INSERT INTO websites VALUES(null, 'erp', 'https://erp.superior.edu.pk')")
# cur.execute("INSERT INTO websites VALUES(null, 'youtube', 'https://www.youtube.com')")
# con.commit()


# for contacts

# table
#cur.execute("CREATE TABLE IF NOT EXISTS contacts(id INTEGER PRIMARY KEY, name VARCHAR(200), number VARCHAR(255))")

# insert contacts extracted from csv file
# desired_indexes=[0,30]
# with open('contacts.csv','r',encoding='utf-8') as csvfile:
#   csvreader=csv.reader(csvfile)
#   for row in csvreader:
#     data=[row[i] for i in desired_indexes]
#     cur.execute("INSERT INTO contacts VALUES(null,?,?);",tuple(data))

# con.commit()
# con.close()


