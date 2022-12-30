import mysql.connector
con = mysql.connector.connect(host="localhost", password = "admin@123", user="root",database="employee_management" )

def Emp_Menu():
    print("Welcome to Employee Management")
    print("select : ")
    print("1.Add Employee")
    print("2.Remove Employee")
    print("3.Promote Employee")
    print("4.Display Employee")
    print("5.Exit")
    ch = int(input("Enter your Choice : "))
    if ch == 1:
        Add_Employee()
    elif ch == 2:
        Remove_Employee()
    elif ch == 3:
        Promote_Employee()
    elif ch == 4:
        Display_Employee()
    elif ch == 5:
        exit(0)
    else:
        print("Invalid Choice")

def Add_Employee():

    emp_id = int(input("Enter Employee id : "))

    if((Check_Employee(emp_id) == True)):
        print("Employee Already Exist")
        Emp_Menu()
    else:
        emp_name = input("Enter Employee Name : ")
        emp_post = input("Enter Employee Post : ")
        salary = input("Enter Employee Salary : ")
        data = (emp_id,emp_name,emp_post,salary)
        sql = 'insert into employee_details values(%s,%s,%s,%s)'
        c = con.cursor()
        c.execute(sql,data)
        con.commit()
        print("Employee Details Added Successfully")
        Emp_Menu()

def Remove_Employee():

    emp_id = int(input("Enter Employee id : "))
    if(Check_Employee(emp_id) == False):
        print("Entered Employee Id not Exist")
        Emp_Menu()
    else:
        sql = 'delete from employee_details where emp_id=%s'
        data = (emp_id,)
        c = con.cursor()
        c.execute(sql,data)
        con.commit()
        print("Employee Removed Successfully")
        Emp_Menu()
    
def Check_Employee(employee_id):

    sql = 'select * from employee_details where emp_id=%s'
    c = con.cursor(buffered=True)
    data = (employee_id,)
    c.execute(sql,data)
    r = c.rowcount
    if r == 1:
        return True
    else:
        return False

def Promote_Employee():
    emp_id = int(input("Enter Employee id : "))
    if (Check_Employee(emp_id) == False):
        print("Entered Employee Id not Exist")
        Emp_Menu()
    else:
        amount = int(input("Enter increase in Salary : "))
        sql = 'select salary from employee_details where emp_id=%s'
        c = con.cursor()
        data = (emp_id,)
        c.execute(sql,data)
        r = c.fetchone()
        t = r[0]+amount
        sql = 'update employee_details set salary=%s where emp_id=%s'
        d = (t,emp_id)
        c.execute(sql,d)
        con.commit()
        print("Employee Promoted")
        Emp_Menu()
    
def Display_Employee():
    sql = 'select * from employee_details'
    c = con.cursor()
    c.execute(sql,)
    r = c.fetchall()
    for i in r:
        print("Employee Id : ", i[0])
        print("Employee Name : ", i[1])
        print("Employee Post : ", i[2])
        print("Employee Salary : ", i[3])
        print("---------------------\
              -----------------------------\
              ---------------------")

    Emp_Menu()
Emp_Menu()
