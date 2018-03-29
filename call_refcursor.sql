DECLARE
   v_cursor   sys_refcursor;
   v_fname    employees.first_name%TYPE;
   v_lname    employees.last_name%TYPE;
   v_jobid    employees.job_id%TYPE;
   
BEGIN
   DBMS_OUTPUT.ENABLE;
   hr_utils.get_emp_rs (p_deptid => 80, p_recordset => v_cursor);

   LOOP
      FETCH v_cursor
       INTO v_fname, v_lname, v_jobid;

      EXIT WHEN v_cursor%NOTFOUND;
      DBMS_OUTPUT.put_line (v_lname || ', ' || v_fname || '  ' || v_jobid);
   END LOOP;

   CLOSE v_cursor;
END;
/