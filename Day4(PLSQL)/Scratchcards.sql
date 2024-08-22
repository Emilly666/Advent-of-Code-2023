--set serveroutput on;

CREATE DIRECTORY DIR__DAY4 AS '/media/sf_Advent-of-Code-2023/Day4(PLSQL)';

CREATE TABLE CARDS 
(
    CARD_NUMBER NUMBER NOT NULL PRIMARY KEY,
    WINNING_NUMBERS VARCHAR2(150) NOT NULL,
    CARD_NUMBERS VARCHAR2(150) NOT NULL,
    WINNING_COUNT NUMBER
);
DROP TABLE CARDS;
TRUNCATE TABLE CARDS;
SELECT * FROM CARDS;

-- rading input file and inserting into table
DECLARE
    v_file UTL_FILE.FILE_TYPE;
    v_line VARCHAR2(117);
    v_card CARDS%ROWTYPE;

BEGIN
    v_file := UTL_FILE.FOPEN( 'DIR__DAY4', 'input.txt', 'R', 150 );
    
    LOOP
        UTL_FILE.GET_LINE(v_file, v_line);
        SELECT 
            TO_NUMBER(REGEXP_SUBSTR (v_line, '(\S+):', 1, 1, NULL, 1)),
            TRIM(REGEXP_SUBSTR (v_line, ':(.+)\|', 1, 1, NULL, 1)),
            TRIM(REGEXP_SUBSTR (v_line, '\|(.+)', 1, 1, NULL, 1)),
            NULL
        INTO v_card
        FROM dual;
        
        dbms_output.put_line(TO_CHAR(v_card.CARD_NUMBER) || ', ' || v_card.WINNING_NUMBERS || ' --- ' || v_card.CARD_NUMBERS);
        
        INSERT INTO CARDS VALUES v_card;
        dbms_output.put_line('row inserted');
        
    END LOOP;
    
    EXCEPTION
        WHEN no_data_found THEN
            dbms_output.put_line('The whole file was read!');
            UTL_FILE.FCLOSE(v_file);
END;

-- 