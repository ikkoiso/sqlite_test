import csv
import sqlite3
with open('./wk_m_employee.csv','r',encoding='utf-8-sig') as csv_file:
    read = csv.DictReader(csv_file,fieldnames = ['EMPLOYEE_NO','EMP_NAME','DEPARTMENT_KBN','MAIL_ADDRESS'])
    conn = sqlite3.connect('testdb')
    curs = conn.cursor()
#curs.execute("CREATE TABLE Employee2( EMPLOYEE_NO int PRIMARY KEY,EMP_NAME string,DEPARTMENT_KBN string,MAIL_ADDLESS string)")


#l=[]
    for row in read:
        print(row["EMPLOYEE_NO"],row["EMP_NAME"],row["DEPARTMENT_KBN"],row["MAIL_ADDRESS"])
        #l.append({"EMPLOYEE_NO":row["EMPLOYEE_NO"],"EMP_NAME":row["EMP_NAME"],"DEPARTMENT_KBN":row["DEPARTMENT_KBN"],"MAIL_ADDRESS":row["MAIL_ADDRESS"]})
        curs.execute('INSERT INTO Employee2(EMPLOYEE_NO,EMP_NAME,DEPARTMENT_KBN,MAIL_ADDLESS) values(?,?,?,?)',[row["EMPLOYEE_NO"],row["EMP_NAME"],row["DEPARTMENT_KBN"],row["MAIL_ADDRESS"]])
    conn.commit()
    conn.close()
