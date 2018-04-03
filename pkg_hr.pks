 CREATE OR REPLACE PACKAGE pkg_hr AS 
  
  PROCEDURE add_department(
    p_department_id OUT NUMBER,
    p_department_name IN VARCHAR2,
    p_manager_id IN NUMBER,
    p_location_id IN NUMBER
  ); 

  FUNCTION get_employee_count(
    p_department_id IN NUMBER
  ) RETURN NUMBER;
 
  PROCEDURE find_employees(
    p_query IN VARCHAR2,
    p_results OUT SYS_REFCURSOR
  ); 

END pkg_hr;
/ 