import cx_Oracle
import sys

class pkg_hr:
  '''
  From http://www.oracle.com/technetwork/articles/prez-stored-proc-084100.html
  TK: changed __enter__ method to __init__
  '''
  # def __enter__(self):
  def __init__(self):
    self.__db = cx_Oracle.Connection('hr', 'maxcat', 'xe')
    self.__cursor = self.__db.cursor()
    # return self
    return None

  def __exit__(self, type, value, traceback):
    self.__cursor.close()
    self.__db.close()

  def add_department(self, p_department_name, p_manager_id, p_location_id):
    l_department_id = self.__cursor.var(cx_Oracle.NUMBER)
    self.__cursor.callproc("PKG_HR.ADD_DEPARTMENT",
      [l_department_id, p_department_name, p_manager_id, p_location_id])

    # there are no OUT parameters in Python, regular return here
    return l_department_id

  def get_employee_count(self, p_department_id):
    l_count = self.__cursor.callfunc("PKG_HR.GET_EMPLOYEE_COUNT", cx_Oracle.NUMBER, [p_department_id])
    return l_count

  def find_employees(self, p_query):
    # as it comes to all complex types we need to tell Oracle Client
    # what type to expect from an OUT parameter
    l_cur = self.__cursor.var(cx_Oracle.CURSOR)
    l_query, l_emp = self.__cursor.callproc("PKG_HR.FIND_EMPLOYEES", [p_query, l_cur])
    return list(l_emp)
