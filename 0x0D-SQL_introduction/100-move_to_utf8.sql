-- convert to uft8
ALTER DATABASE hbtc_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

ALTER TABLE first_table MODIFY column name VARCHAR(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;