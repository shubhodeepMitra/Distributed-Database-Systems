# Assignment 2: Parallel Spatial Join with PostGIS and MapReduce on Apache Spark

## Objective
This assignment is divided into two parts:
- **Part A:** Implement a parallel spatial join using PostgreSQL with the PostGIS extension.
- **Part B:** Implement a spatial join using MapReduce on Apache Spark with Apache Sedona.

## Setup Instructions

### Prerequisites
- **Part A:**
  - PostgreSQL 13 or higher with the PostGIS extension.
  - Python with `psycopg2` installed.
- **Part B:**
  - Apache Spark 2.4.7 or higher with Hadoop.
  - Apache Sedona and SedonaSQL libraries.
  - Scala with `sbt` for building and running the Spark application.

### Database Setup (Part A)
1. Create the database and enable the PostGIS extension.
2. Load the provided datasets (`points.csv` and `rectangles.csv`) into PostgreSQL.

### Environment Setup (Part B)
1. Install Apache Spark and Hadoop.
2. Configure Apache Sedona in your Spark environment.
3. Build the Spark project using `sbt`.

## Execution

### Part A: Parallel Spatial Join with PostGIS
- Execute the `Assignment2_Interface.py` script to perform the parallel spatial join.
- The results will be saved in `output_part_a.txt`.

### Part B: Spatial Join with MapReduce on Apache Spark
- Execute the built JAR using Spark submit:
  ```bash
  spark-submit --class Entrance target/scala-2.12/Map-Reduce-Apache-Sedona-assembly-0.1.jar mapreduce path/to/points.csv path/to/rectangles.csv
  ```

### Execution
- **Run the Spark Application:**
  ```bash
  spark-submit --class Entrance target/scala-2.12/Map-Reduce-Apache-Sedona-assembly-0.1.jar mapreduce path/to/points.csv path/to/rectangles.csv
  ```

### Output
The results will be saved in the specified output directory in CSV format.


## Skills Gained
- Spatial data processing with PostgreSQL and PostGIS.
- Parallel processing techniques in Python.
- Big data processing with Apache Spark and Sedona.
- Implementing MapReduce for spatial joins.