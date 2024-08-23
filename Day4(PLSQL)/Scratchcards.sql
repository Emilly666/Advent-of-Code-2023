--set serveroutput on;

CREATE DIRECTORY DIR__DAY4 AS 'C:\Repos\Advent-of-Code-2023\Day4(PLSQL)';
--DROP DIRECTORY DIR__DAY4;

CREATE TABLE CARDS 
(
    CARD_NUMBER NUMBER NOT NULL PRIMARY KEY,
    WINNING_NUMBERS VARCHAR2(150) NOT NULL,
    CARD_NUMBERS VARCHAR2(150) NOT NULL,
    WINNING_COUNT NUMBER
);
--DROP TABLE CARDS;
--TRUNCATE TABLE CARDS;
--SELECT * FROM CARDS;

-------------------------execute function----------------------------------------------------------
BEGIN
    EXECUTE IMMEDIATE ('TRUNCATE TABLE TEST.CARDS');
    dbms_output.PUT_LINE(SCRATCHCARDS.COUNT_WINNINGS('input.txt'));
END;

/
-------------------------package definition--------------------------------------------------------
CREATE OR REPLACE PACKAGE SCRATCHCARDS AS
    FUNCTION COUNT_WINNINGS(file_name VARCHAR2) RETURN NUMBER;
END SCRATCHCARDS;
/
-------------------------package body definition---------------------------------------------------
CREATE OR REPLACE PACKAGE BODY SCRATCHCARDS AS
-------------------------reading file into table---------------------------------------------------
    PROCEDURE READ_FILE(file_name VARCHAR2) AS
        v_file UTL_FILE.FILE_TYPE;
        v_line VARCHAR2(117);
        v_card CARDS%ROWTYPE;

    BEGIN
        v_file := UTL_FILE.FOPEN( 'DIR__DAY4', file_name, 'R', 150 );
    
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
    END READ_FILE;
-------------------------main function-------------------------------------------------------------
    FUNCTION COUNT_WINNINGS(file_name VARCHAR2) RETURN NUMBER AS
    BEGIN
        SCRATCHCARDS.READ_FILE(file_name);
        RETURN(1);
    END COUNT_WINNINGS;
END SCRATCHCARDS;