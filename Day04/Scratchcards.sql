--set serveroutput on;
-------------------------create schema level objects-----------------------------------------------
CREATE OR REPLACE DIRECTORY DIR__DAY4 AS 'C:\Repos\Advent-of-Code-2023\Day4(PLSQL)';

CREATE OR REPLACE TYPE T_CARD_NUMBERS AS TABLE OF NUMBER(2);

CREATE TABLE CARDS 
(
    CARD_NUMBER NUMBER NOT NULL PRIMARY KEY,
    WINNING_NUMBERS T_CARD_NUMBERS,
    CARD_NUMBERS T_CARD_NUMBERS,
    WINNING_COUNT NUMBER,
    POINTS NUMBER,
    APPEARANCES NUMBER DEFAULT 1
)
    NESTED TABLE WINNING_NUMBERS STORE AS WINNING_NUMBERS_TABLE,
    NESTED TABLE CARD_NUMBERS STORE AS CARD_NUMBERS_TABLE;
-------------------------execute function----------------------------------------------------------
BEGIN
    EXECUTE IMMEDIATE ('TRUNCATE TABLE TEST.CARDS');
    --dbms_output.PUT_LINE(SCRATCHCARDS.COUNT_WINNINGS('input.txt'));
    dbms_output.PUT_LINE(SCRATCHCARDS.COUNT_WINNINGS_WITH_APPERANCES('input.txt'));
END;
/ 
-------------------------package definition--------------------------------------------------------
CREATE OR REPLACE PACKAGE SCRATCHCARDS AS
    FUNCTION COUNT_WINNINGS(file_name VARCHAR2) RETURN NUMBER;
    FUNCTION COUNT_WINNINGS_WITH_APPERANCES(file_name VARCHAR2) RETURN NUMBER;
END SCRATCHCARDS;
/
-------------------------package body definition---------------------------------------------------
CREATE OR REPLACE PACKAGE BODY SCRATCHCARDS AS
-------------------------converting string to table of numbers-------------------------------------
    FUNCTION TO_CARD_NUMBERS(text VARCHAR2) RETURN T_CARD_NUMBERS AS
        v_return T_CARD_NUMBERS := T_CARD_NUMBERS();
    BEGIN
        FOR i IN 1..REGEXP_COUNT(text, '[^ ]+') LOOP
            v_return.EXTEND;
            v_return(i) := TO_NUMBER(REGEXP_SUBSTR(text, '[^ ]+', 1, i));

        END LOOP;
        RETURN(v_return);

    END TO_CARD_NUMBERS;
-------------------------reading file into table---------------------------------------------------
    PROCEDURE READ_FILE(file_name VARCHAR2) AS
        v_file UTL_FILE.FILE_TYPE;
        v_line VARCHAR2(117);
        v_card CARDS%ROWTYPE;
        v_temp VARCHAR2(100);
    BEGIN
        v_file := UTL_FILE.FOPEN( 'DIR__DAY4', file_name, 'R', 150 );
    
        LOOP
            UTL_FILE.GET_LINE(v_file, v_line);
            -- get card number
            SELECT REGEXP_SUBSTR(v_line, '(\S+):', 1, 1, NULL, 1)
            INTO v_card.CARD_NUMBER
            FROM dual;

            -- get winning numbers
            SELECT TRIM(REGEXP_SUBSTR(v_line, ':(.+)\|', 1, 1, NULL, 1))
            INTO v_temp
            FROM dual;
            v_card.WINNING_NUMBERS := TO_CARD_NUMBERS(v_temp);

            --get card numbers
            SELECT TRIM(REGEXP_SUBSTR (v_line, '\|(.+)', 1, 1, NULL, 1))
            INTO v_temp
            FROM dual;
            v_card.CARD_NUMBERS := TO_CARD_NUMBERS(v_temp);    

            INSERT INTO CARDS (CARD_NUMBER, WINNING_NUMBERS, CARD_NUMBERS, WINNING_COUNT)
            VALUES (v_card.CARD_NUMBER, v_card.WINNING_NUMBERS, v_card.CARD_NUMBERS, 0);

        END LOOP;
        
        EXCEPTION
            WHEN no_data_found THEN
                dbms_output.put_line('The whole file was read!');
                UTL_FILE.FCLOSE(v_file);

    END READ_FILE;
-------------------------calculate winnings for each row-------------------------------------------
    PROCEDURE CALCULATE_WINNINGS AS
        CURSOR c_cards IS SELECT * FROM CARDS FOR UPDATE;
        v_row_win_count NUMBER;
    BEGIN
        FOR row in c_cards LOOP
            v_row_win_count := 0;
            FOR x in 1..row.CARD_NUMBERS.COUNT() LOOP
                IF row.CARD_NUMBERS(x) MEMBER OF row.WINNING_NUMBERS THEN
                    v_row_win_count := v_row_win_count + 1;
                END IF;
            END LOOP;

            UPDATE CARDS SET WINNING_COUNT = v_row_win_count
            WHERE CURRENT OF c_cards;

            IF v_row_win_count > 0 THEN
                UPDATE CARDS SET POINTS = POWER(2, v_row_win_count - 1)
                WHERE CURRENT OF c_cards;
            ELSE
                UPDATE CARDS SET POINTS = 0
                WHERE CURRENT OF c_cards;
            END IF;

        END LOOP;
    END CALCULATE_WINNINGS;
-------------------------calculate appearances-----------------------------------------------------
    PROCEDURE CALCULATE_APPERANCEES AS
         v_row_count NUMBER;
         v_card_row CARDS%ROWTYPE;
    BEGIN
        SELECT COUNT(*) INTO v_row_count FROM CARDS;

        FOR i in 1..v_row_count LOOP
            SELECT * INTO v_card_row FROM CARDS WHERE CARD_NUMBER = i;

            UPDATE CARDS
            SET APPEARANCES = APPEARANCES + v_card_row.APPEARANCES 
            WHERE CARD_NUMBER BETWEEN v_card_row.CARD_NUMBER + 1 AND v_card_row.CARD_NUMBER + v_card_row.WINNING_COUNT;

        END LOOP;
    END CALCULATE_APPERANCEES;
-------------------------main function for part 1--------------------------------------------------
    FUNCTION COUNT_WINNINGS(file_name VARCHAR2) RETURN NUMBER AS
        v_sum NUMBER := 0;
    BEGIN
        SCRATCHCARDS.READ_FILE(file_name);
        SCRATCHCARDS.CALCULATE_WINNINGS;

        SELECT SUM(POINTS) INTO v_sum FROM CARDS;

        RETURN(v_sum);
    END COUNT_WINNINGS;
-------------------------main function for part 2--------------------------------------------------
    FUNCTION COUNT_WINNINGS_WITH_APPERANCES(file_name VARCHAR2) RETURN NUMBER AS
        v_sum NUMBER := 0;
    BEGIN
        SCRATCHCARDS.READ_FILE(file_name);
        SCRATCHCARDS.CALCULATE_WINNINGS;
        SCRATCHCARDS.CALCULATE_APPERANCEES;

        SELECT SUM(APPEARANCES) INTO v_sum FROM CARDS;

        RETURN(v_sum);
    END COUNT_WINNINGS_WITH_APPERANCES;
END SCRATCHCARDS;