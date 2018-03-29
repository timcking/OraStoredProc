CREATE OR REPLACE PACKAGE BODY hr_utils AS
/******************************************************************************
   NAME:       hr_utils
   PURPOSE:

   REVISIONS:
   Ver        Date        Author           Description
   ---------  ----------  ---------------  ------------------------------------
   1.0        7/1/2012             1. Created this package body.
   1.1        3/18/2018               Removed unused function
******************************************************************************/

  PROCEDURE get_emp_rs (
   p_deptid      IN       employees.department_id%TYPE,
   p_recordset   OUT      sys_refcursor
   ) IS
    BEGIN
       OPEN p_recordset FOR
            SELECT first_name, last_name, job_id
              FROM employees
             WHERE department_id = p_deptid
          ORDER BY last_name;
    END get_emp_rs;

END hr_utils;
/
