CREATE OR REPLACE PACKAGE BODY pkg_hr AS

  PROCEDURE add_department(
    p_department_id OUT NUMBER,
    p_department_name IN VARCHAR2,
    p_manager_id IN NUMBER,
    p_location_id IN NUMBER
  ) AS
  BEGIN
    INSERT INTO departments(department_id, department_name, manager_id, location_id)
    VALUES (departments_seq.nextval, p_department_name, p_manager_id, p_location_id)
    RETURNING department_id
    INTO p_department_id;

    COMMIT;
  END add_department;

  FUNCTION get_employee_count(
    p_department_id IN NUMBER
  ) RETURN NUMBER AS
    l_count NUMBER;
  BEGIN
    SELECT COUNT(*)
    INTO l_count
    FROM employees
    WHERE department_id= p_department_id;

    RETURN l_count;
  END get_employee_count;

 PROCEDURE find_employees(
    p_query IN VARCHAR2,
    p_results OUT SYS_REFCURSOR
  ) AS
  BEGIN
    OPEN p_results FOR
      SELECT *
      FROM employees
      WHERE UPPER(last_name) LIKE '%'||UPPER(p_query)||'%';

  END find_employees;

END pkg_hr;
/
