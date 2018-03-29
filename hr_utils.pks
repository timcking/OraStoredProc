CREATE OR REPLACE PACKAGE hr_utils AS
/******************************************************************************
   NAME:       hr_utils
   PURPOSE:

   REVISIONS:
   Ver        Date        Author           Description
   ---------  ----------  ---------------  ------------------------------------
   1.0        7/1/2012             1. Created this package.
   1.1        3/18/2018               Removed unused function
******************************************************************************/

  PROCEDURE get_emp_rs (
    p_deptid      IN       employees.department_id%TYPE,
    p_recordset   OUT      sys_refcursor
   );

END hr_utils;

/
