from black import main
import psycopg2
import sys


def all():
    conn = psycopg2.connect("dbname = devices user = postgres password = password1")
    cur = conn.cursor()
    try:
        code = sys.argv[2]
        cur.execute(
            "select * from employee left join usage on employee.id = employee_id where code = %(str)s;",
            {"str": code},
        )
        record = cur.fetchall()
        for row in record:
            print(("{} " * len(row)).format(*row))
    except IndexError:
        print("code cannot be empty")
        sys.exit(1)
    cur.close()
    conn.close()


def check_in():
    conn = psycopg2.connect("dbname = devices user = postgres password = password1")
    cur = conn.cursor()
    try:
        check_code = sys.argv[2]
        cur.execute(
            "select employee.id,employee.first_name, employee.last_name, employee.email, "
            "employee.code, usage.id, usage.device_id,  usage.date  "
            "from employee left join usage on employee.id = employee_id where type = 'CHECK_IN' and code = %(str)s ;",
            {"str": check_code},
            )
        record = cur.fetchall()
        for row in record:
            print(("{} " * len(row)).format(*row))
    except IndexError:
        print("Code cannot be empty")
        sys.exit(1)
    cur.close()
    conn.close()


def check_out():
    conn = psycopg2.connect("dbname = devices user = postgres password = password1")
    cur = conn.cursor()
    try:
        check_code = sys.argv[2]
        cur.execute(
            "select employee.id,employee.first_name, employee.last_name, employee.email, "
            "employee.code, usage.id, usage.device_id,  usage.date  "
            "from employee left join usage on employee.id = employee_id where type = 'CHECK_OUT' and code = %(str)s ;",
            {"str": check_code},
        )
        record = cur.fetchall()
        for row in record:
            print(("{} " * len(row)).format(*row))
    except IndexError:
        print("Code cannot be empty!")
        sys.exit(1)
    cur.close()
    conn.close()


if sys.argv[1] == "all":
    all()
elif sys.argv[1] == "check_in":
    check_in()
elif sys.argv[1] == "check_out":
    check_out()
