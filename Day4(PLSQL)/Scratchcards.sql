--set serveroutput on;

CREATE DIRECTORY DIR__DAY4 AS 'C:/Repos/Advent-of-Code-2023/Day4(PLSQL)';
/
DECLARE
    file UTL_FILE.FILE_TYPE;
    str VARCHAR2(150);

BEGIN
    file := UTL_FILE.FOPEN( 'DIR__DAY4', 'input.txt', 'R', 150 );
    UTL_FILE.GET_LINE( file, str );
    UTL_FILE.FCLOSE( file );
    DBMS_OUTPUT.PUT_LINE( str );
END;