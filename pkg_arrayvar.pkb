CREATE OR REPLACE PACKAGE BODY pkg_arrayvar AS

FUNCTION sum(p_list IN NUM_ARRAY) RETURN NUMBER AS
    l_sum NUMBER := 0;
  BEGIN
    FOR i IN 1..p_list.COUNT LOOP
      l_sum := l_sum+p_list(i);
    END LOOP i;

    RETURN l_sum;
  END sum;

END pkg_arrayvar;
/