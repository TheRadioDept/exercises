import psycopg2
import sys

conn = psycopg2.connect("dbname=devices user = postgres password=password1")

cur = conn.cursor()


def add_employee():
    """
    Function to add an employee into a table.
    """

    print("Enter the values for the Employee")
    fname = input("Enter the first name ")
    lname = input("Enter the last name ")
    emp_email = input("Enter the email ")
    emp_code = input("Enter unique code")
    cur.execute(
        "INSERT INTO employee (first_name, last_name, email, code) VALUES (%s, %s, %s, %s);",
        (fname, lname, emp_email, emp_code),
    )
    conn.commit()
    print("done")
    cur.close()
    conn.close()


def list_employee():
    """
    Function to list all employees.
    """

    cur.execute("SELECT * FROM employee;")
    record = cur.fetchall()
    for row in record:
        print("Id = ", row[0])
        print("First name = ", row[1])
        print("Last name = ", row[2])
        print("Email = ", row[3])
        print("Unique code  = ", row[4], "\n")


def update_employee():
    """
    Function to update employees information.
    """

    print("Enter the updated employee information")
    new_name = input("Enter the first name ")
    new_lname = input("Enter the last name ")
    new_email = input("Enter new email ")
    code = input("Enter code of the employee ")
    if code == "":
        print("Code cannot be empty")
    else:
        cur.execute(
            "UPDATE employee SET first_name = %s, last_name = %s, email = %s WHERE code = %s;",
            (new_name, new_lname, new_email, code),
        )
        conn.commit()
        print("done")
        cur.close()
        conn.close()


def delete_employee():
    """
    Function to delete employee based on his unique code.
    """

    print("Enter the code of employee to delete: ")
    code = input()
    cur.execute("DELETE FROM employee WHERE CODE = %(str)s;", {"str": code})
    conn.commit()
    print("done")
    cur.close()
    conn.close()


if __name__ == "__main__":
    globals()[sys.argv[1]]()
