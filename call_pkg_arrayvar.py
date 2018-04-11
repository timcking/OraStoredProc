import sys
import cx_Oracle

if __name__ == "__main__":
    """
    if len(sys.argv) <> 2:
        print 'Usage: ' + sys.argv[0] + ' department_id'
        sys.exit(1)
    else:
        l_deptid = int(sys.argv[1])
    """

    db = cx_Oracle.connect('hr', 'hr', 'orcl')
    cursor = db.cursor()
    L = cursor.arrayvar(cx_Oracle.NUMBER, [1, 2, 3])

    sum_result = cursor.callfunc("pkg_arrayvar.sum", cx_Oracle.NUMBER, [L])
    assert sum_result == 6
    print sum_result
