-- a script that updates the score of Bob to 10 in the table 
-- not allowed to use Bob’s id value, only the name field
UPDATE TABLE second_table
SET score = 10
WHERE name = "Bob";
