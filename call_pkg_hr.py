import sys
import pkg_hr

if __name__ == "__main__":
    """
    if len(sys.argv) <> 2:
        print 'Usage: ' + sys.argv[0] + ' department_id'
        sys.exit(1)
    else:
        l_deptid = int(sys.argv[1])
    """

    hrq = pkg_hr.pkg_hr()

    """ add_department
    l_deptid = hrq.add_department('Cloud Heads', '200', '1700')
    print(l_deptid)
    """

    """ employee_count
    l_count = hrq.get_employee_count('30')
    print int(l_count)
    sql = "SELECT last_name FROM employees WHERE last_name ='King'"
    """

    """ find_employees """
    empArr = []
    empArr = hrq.find_employees('King')
    print empArr