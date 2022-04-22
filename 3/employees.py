import psycopg2
import sys


if len(sys.argv) == 1:
    print("Parameter cannot be empty!")
    sys.exit()
elif len(sys.argv) > 2:
    print("Too many parameters!")
    sys.exit()
else:
    arg = sys.argv[1]


def add_employee():
    """
    Function to add an employee into a table.
    """
    conn = psycopg2.connect("dbname = devices user = postgres password = password1")
    cur = conn.cursor()
    emp_code = input("Enter the code of the employee:")
    cur.execute(f"SELECT * from EMPLOYEE WHERE code='{emp_code}'")
    if cur.fetchall():
        print("Code is already taken!")
    elif emp_code == "":
        print("Code cannot be empty")
    else:
        fname = input("Enter the first name ")
        lname = input("Enter the last name ")
        emp_email = input("Enter the email: ")
        if (
            fname != ""
            and lname != ""
            and emp_email != ""
            and emp_email.find("@") != -1
        ):
            cur.execute(
                "INSERT INTO employee (first_name, last_name, email, code) VALUES (%s, %s, %s, %s);",
                (fname, lname, emp_email, emp_code),
            )
            print("Added employee")
        else:
            print("Invalid parameters")
    conn.commit()


def list_employee():
    """
    Function to list all employees.
    """
    try:
        conn = psycopg2.connect("dbname=devices user = postgres password=password1")
        cur = conn.cursor()
        cur.execute(f"SELECT code from EMPLOYEE;")
        if not cur.fetchall():
            print("Table is empty")
        else:
            cur.execute("SELECT id, first_name, last_name, email, code FROM employee;")
            record = cur.fetchall()
            for row in record:
                print(("{:<14}" * len(row)).format(*row))
    except NameError:
        print("An error occured")


def update_employee():
    """
    Function to update employees information.
    """

    conn = psycopg2.connect("dbname=devices user = postgres password=password1")
    cur = conn.cursor()
    # print("Enter the updated employee information")
    code = input("Enter code of the employee ")
    if code == "":
        print("Code cannot be empty")
    else:
        new_name = input("Enter the first name ")
        new_lname = input("Enter the last name ")
        new_email = input("Enter new email ")
        if (
            new_email != ""
            and new_name != ""
            and new_lname != ""
            and new_email.find("@") != -1
        ):
            cur.execute(
                "UPDATE employee SET first_name = %s, last_name = %s, email = %s WHERE code = %s;",
                (new_name, new_lname, new_email, code),
            )
        else:
            print("Invalid parameters")
        conn.commit()


def delete_employee():
    """
    Function to delete employee based on his unique code.
    """

    conn = psycopg2.connect("dbname=devices user = postgres password=password1")
    cur = conn.cursor()
    print("Enter the code of employee to delete: ")
    code = input()
    if code == "":
        print("Code cannot be empty")
        sys.exit(1)
    cur.execute(f"SELECT * from EMPLOYEE WHERE code='{code}'")
    if not cur.fetchall():
        print("No such code!")
    else:
        confirm_delete = input(
            "Are you sure you want to delete the user with code : {}? ".format(code)
        )
        if confirm_delete.lower() == "yes":
            cur.execute("DELETE FROM employee WHERE CODE = %(str)s;", {"str": code})
            print("User deleted.")
        else:
            print("Deleting canceled")
    conn.commit()


try:
    if sys.argv[1] == "add_employee":
        add_employee()
    elif sys.argv[1] == "list_employee":
        list_employee()
    elif sys.argv[1] == "update_employee":
        update_employee()
    elif sys.argv[1] == "delete_employee":
        delete_employee()
    else:
        print("No such function")
except:
    print("Error occured")
