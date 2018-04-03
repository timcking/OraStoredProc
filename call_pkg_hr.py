import sys
import pkg_hr

if __name__ == "__main__":
    if len(sys.argv) <> 2:
        print 'Usage: ' + sys.argv[0] + ' department_id'
        sys.exit(1)
    else:
        l_deptid = int(sys.argv[1])

    hrq = pkg_hr.pkg_hr()

    # l_count = hrq.get_employee_count(l_deptid)
    # print int(l_count)
    # sql = "SELECT last_name FROM employees WHERE last_name ='King'"

    empArr = []

    empArr = hrq.find_employees('King')
    print empArr