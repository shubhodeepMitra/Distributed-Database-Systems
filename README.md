# Distributed Database Systems and Spatial Data Processing - CSE 512

## Objective
This repository contains the completed assignments for the CSE 512 course. Each assignment covers various topics related to database management systems, spatial data processing, and big data frameworks.

## Table of Contents
- [Assignment 1: Data Fragmentation in PostgreSQL](#assignment-1-data-fragmentation-in-postgresql)
- [Assignment 2: Parallel Spatial Join with PostGIS and MapReduce on Apache Spark](#assignment-2-parallel-spatial-join-with-postgis-and-mapreduce-on-apache-spark)
- [Assignment 4: Textual and Spatial Searching in MongoDB](#assignment-4-textual-and-spatial-searching-in-mongodb)
- [Assignment 5: Delta Lake and Apache Sedona](#assignment-5-delta-lake-and-apache-sedona)
- [General Setup Overview](#general-setup-overview)
- [Overall Skills Gained](#overall-skills-gained)

## Assignments Overview

### Assignment 1: Data Fragmentation in PostgreSQL
- **Objective:** Implement and verify different data fragmentation techniques in PostgreSQL.
- **Key Tasks:**
  - Write SQL queries to retrieve and manipulate data.
  - Implement various fragmentation strategies and demonstrate their properties.
- **Setup:** PostgreSQL 13 with data loaded from `test_data.txt`.
- **Execution:** Execute SQL scripts in PostgreSQL to perform the tasks.
- **Skills Gained:** SQL query writing, database fragmentation, PostgreSQL operations.

### Assignment 2: Parallel Spatial Join with PostGIS and MapReduce on Apache Spark
- **Objective:** Perform spatial joins using PostgreSQL with PostGIS and Apache Spark with Apache Sedona.
- **Key Tasks:**
  - Part A: Implement a parallel spatial join in PostgreSQL.
  - Part B: Perform a spatial join using MapReduce in Apache Spark.
- **Setup:** PostgreSQL with PostGIS, Apache Spark with Sedona.
- **Execution:**
  - Part A: Run `Assignment2_Interface.py`.
  - Part B: Submit the built JAR using Spark submit.
- **Skills Gained:** Spatial data processing, parallel processing, big data frameworks.

### Assignment 4: Textual and Spatial Searching in MongoDB
- **Objective:** Conduct textual and spatial searches on business data in MongoDB.
- **Key Tasks:**
  - Search businesses by city and review count.
  - Search businesses by location and categories.
- **Setup:** MongoDB with data loaded from `testData.json`.
- **Execution:** Run `Assignment4_Tester.py`.
- **Skills Gained:** MongoDB querying, geospatial calculations, Python integration with MongoDB.

### Assignment 5: Delta Lake and Apache Sedona for Spatial Data Processing
- **Objective:** Use Delta Lake and Apache Sedona in Spark for handling and querying spatial data.
- **Key Tasks:**
  - Perform spatial queries, filtering, and joins using Delta Lake and Sedona.
- **Setup:** Apache Spark with Delta Lake and Sedona.
- **Execution:** Run the Spark application using the built JAR.
- **Skills Gained:** Delta Lake for large-scale data handling, Apache Sedona for spatial data processing, geospatial queries in Spark.

## General Setup Overview

To successfully run the assignments in this repository, you will need to install the following tools and dependencies:

- **PostgreSQL 13** (with PostGIS extension for spatial data processing)
- **MongoDB** (for handling NoSQL data and geospatial queries)
- **Apache Spark 2.4.7 or higher** (for big data processing, with Delta Lake and Apache Sedona configured)
- **Python** (with libraries such as `psycopg2` for PostgreSQL and `pymongo` for MongoDB integration)
- **Scala with sbt** (for building and running Spark applications)

Each assignment directory contains more detailed setup and execution instructions tailored to the specific tasks. Please refer to the respective README files within each directory for step-by-step guides.

## Overall Skills Gained
- **Database Management:** SQL, PostgreSQL, and MongoDB operations.
- **Big Data Processing:** Apache Spark, Delta Lake, and MapReduce.
- **Spatial Data Analysis:** PostGIS, Apache Sedona, geospatial queries.
- **Programming Languages & Tools:** Python, Scala, Spark, SQL.

---
