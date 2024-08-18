# Assignment 1: Data Fragmentation in PostgreSQL

## Objective
This assignment focuses on understanding and implementing data fragmentation techniques using PostgreSQL. The goal is to create and manipulate data fragments while ensuring properties like completeness, reconstruction, and disjointness.

## Input Data
- **Dataset:** Movie ratings from the MovieLens dataset.
- **Format:** The dataset contains ratings provided by users for different movies, with fields for `userid`, `movieid`, `rating`, and `timestamp`.

## Tasks Overview
1. **Part A - Basic SQL Queries:**
   - Write basic SQL queries to extract and manipulate data from the `ratings` table.
   
2. **Part B - Fragmentation:**
   - Implement various fragmentation strategies:
     - **B1:** Fragmentation that satisfies completeness and reconstruction but not disjointness.
     - **B2:** Fragmentation that satisfies completeness and disjointness but not reconstruction.
     - **B3:** Fragmentation that satisfies completeness, reconstruction, and disjointness.
   - Demonstrate the properties of each fragmentation strategy with SQL queries.

3. **Part C - Queries on Fragments:**
   - Re-write SQL queries from Part A to operate on the fragmented tables created in Part B.

## Setup Instructions

### Prerequisites
- PostgreSQL 13 or higher should be installed on your machine.
- The MovieLens dataset (`test_data.txt`) should be available in the directory where you will execute the SQL scripts.

### Step-by-Step Guide

1. **Set Up the Database:**
   - Start by creating a table and loading the dataset into PostgreSQL.
   - Use the provided SQL script to create the `ratings` table and load data from `test_data.txt`:
     ```sql
     DROP TABLE IF EXISTS ratings;
     CREATE TABLE ratings (
         userid INT, 
         temp1 VARCHAR(10),  
         movieid INT , 
         temp3 VARCHAR(10),  
         rating REAL, 
         temp5 VARCHAR(10), 
         timestamp INT
     );
     COPY ratings FROM 'path/to/your/test_data.txt' DELIMITER ':';
     ALTER TABLE ratings DROP COLUMN temp1, DROP COLUMN temp3, DROP COLUMN temp5, DROP COLUMN timestamp;
     ```
   - **Note:** Replace `'path/to/your/test_data.txt'` with the actual path to your dataset file.

2. **Run Part A - Basic SQL Queries:**
   - Execute the SQL queries provided for Part A to explore and manipulate the data:
     ```sql
     SELECT * FROM ratings;
     SELECT userid, rating FROM ratings;
     SELECT userid, movieid FROM ratings WHERE rating > 4.0;
     SELECT userid, movieid FROM ratings WHERE rating > 4.0 AND rating < 2.0;
     CREATE VIEW best AS
         SELECT userid, movieid
         FROM ratings
         WHERE rating > 4.5;
     ```

3. **Implement Part B - Fragmentations:**
   - Implement the fragmentations as described in the provided code, and run the associated queries to demonstrate the properties of each fragmentation:
     ```sql
     -- Example for Part B1 Fragmentation
     DROP TABLE IF EXISTS bad_movies;
     CREATE TABLE bad_movies AS
         SELECT * FROM ratings
         WHERE rating < 2.0;
     ```

4. **Run Part C - Queries on Fragments:**
   - Re-write and execute the queries from Part A on the fragmented tables created in Part B:
     ```sql
     SELECT * FROM f1;
     SELECT userid, rating FROM f1;
     ```

5. **Verify the Fragmentation Properties:**
   - Use intersection queries to verify disjointness and reconstruction properties:
     ```sql
     SELECT * FROM ratings
     INTERSECT
     SELECT * FROM ratings_disjoint_reconstructed;
     ```

## Execution
1. **Ensure PostgreSQL is running** and the required extensions (if any) are installed.
2. **Copy the SQL script** into your PostgreSQL command-line interface or a SQL editor.
3. **Replace file paths** where necessary, and execute the script to perform the tasks outlined.
4. **Review the output** to verify that the fragmentations and queries have been executed correctly.

## Skills Gained
- Advanced SQL query writing.
- Understanding and implementation of database fragmentation techniques.
- Proficiency in PostgreSQL operations.

---
