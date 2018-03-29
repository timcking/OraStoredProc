import cx_Oracle
import sys

def connect_ora():
    error_msg = ""
    try:
        # Just a demo db, don't worry about the password
        connection = cx_Oracle.connect('hr', 'maxcat', 'xe')
        # we need first cursor for callproc
        cursor = connection.cursor()
        # and second one for refcursor OUT parameter from PL/SQL proc
        ref_cursor = connection.cursor()    
        return cursor, ref_cursor
    except cx_Oracle.DatabaseError, exc:
        error, = exc.args
        error_msg = error.message    
        print error_msg
        return None, None
    
def find_employees(p_deptid, cursor, ref_cursor):
    l_deptid = cursor.var(cx_Oracle.NUMBER)
    l_deptid.setvalue(0, p_deptid)
    
    cursor.callproc('HR_UTILS.GET_EMP_RS', [p_deptid, ref_cursor]) 
    return ref_cursor

if __name__ == "__main__":
    if len(sys.argv) <> 2:
        print 'Usage: ' + sys.argv[0] + ' department_id'
        sys.exit(1)
    else:
        l_deptid = int(sys.argv[1])
        
    cursor, ref_cursor = connect_ora()
    if cursor == None:
        sys.exit(1)
    
    emp_list = find_employees(l_deptid, cursor, ref_cursor)
    
    for row in emp_list:
        print ("%s,%s,%s" % (row[1], row[0], row[2]))
        # print row
    
    ref_cursor.close()
    cursor.close()    
    
