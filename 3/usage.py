import psycopg2
import sys


if len(sys.argv) == 1:
    print("Please call a function ")
    sys.exit()
elif len(sys.argv) > 3:
    print("Too many parameters! ")
    sys.exit()
else:
    arg = sys.argv[1]


def all(conn, cur):
    """
    Function to list all usage for employee code
    """

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
        print("code cannot be empty ")
        sys.exit(1)
    cur.close()
    conn.close()


def check_in(conn, cur):
    """
    Function to list all check-in for employee code
    """

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
        print("Code cannot be empty ")
        sys.exit(1)
    cur.close()
    conn.close()


def check_out(conn, cur):
    """
    Function to list all check-out for employee code
    """

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
        print("Code cannot be empty! ")
        sys.exit(1)
    cur.close()
    conn.close()


def check_in_set(conn, cur):
    """
    Function to change type to CHECK_IN
    Note that you cannot change type to CHECK_IN if it's already set
    """

    employee_id = input("Enter the employee id : ")
    device_id = input("Enter the device id : ")
    if employee_id == "" or device_id == "":
        print("Empty parameter(s)")
        sys.exit(1)
    else:
        cur.execute(
            f"SELECT employee_id from USAGE where employee_id = '{employee_id}'"
        )
        if not cur.fetchall():
            print("Employee does not exist ")
            sys.exit(1)
        cur.execute(f"SELECT device_id from USAGE where device_id = '{device_id}'")
        if not cur.fetchone():
            print("Device does not exist ")
            sys.exit(1)
        cur.execute(
            f"SELECT type from USAGE WHERE type = 'CHECK_IN' and device_id = '{device_id}'"
        )
        if cur.fetchall():
            print("Device already checked in. ")
            sys.exit(1)
        else:
            cur.execute(
                f"UPDATE USAGE SET type = 'CHECK_IN' WHERE usage.employee_id = '{employee_id}' AND usage.device_id = '{device_id}'"
            )
    conn.close()
    cur.close()


def check_out_set(conn, cur):
    """
    Function to change type to CHECK_OUT
    Note that you cannot change type to CHECK_OUT if it's already set
    """

    employee_id = input("Enter the employee id : ")
    device_id = input("Enter the device id : ")
    if employee_id == "" or device_id == "":
        print("Empty parameter(s)")
        sys.exit(1)
    else:
        cur.execute(
            f"SELECT employee_id from USAGE where employee_id = '{employee_id}'"
        )
        if not cur.fetchall():
            print("Employee does not exist ")
            sys.exit(1)
        cur.execute(f"SELECT device_id from USAGE where device_id = '{device_id}'")
        if not cur.fetchone():
            print("Device does not exist ")
            sys.exit(1)
        cur.execute(
            f"SELECT type from USAGE WHERE type = 'CHECK_OUT' and device_id = '{device_id}'"
        )
        if cur.fetchall():
            print("Device already checked out. ")
            sys.exit(1)
        else:
            cur.execute(
                f"UPDATE USAGE SET type = 'CHECK_OUT' WHERE usage.employee_id = '{employee_id}' AND usage.device_id = '{device_id}'"
            )
            conn.commit()
            print("Entry updated.")
    conn.close()
    cur.close()


def main():
    conn = psycopg2.connect("dbname = devices user = postgres password = password1")
    cur = conn.cursor()
    if sys.argv[1] == "all":
        all(conn, cur)
    elif sys.argv[1] == "check_in":
        check_in(conn, cur)
    elif sys.argv[1] == "check_out":
        check_out(conn, cur)
    elif sys.argv[1] == "check_in_set":
        check_in_set(conn, cur)
    elif sys.argv[1] == "check_out_set":
        check_out_set(conn, cur)


if __name__ == "__main__":
    main()
