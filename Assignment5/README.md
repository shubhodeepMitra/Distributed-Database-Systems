# Assignment 5: Delta Lake and Apache Sedona for Spatial Data Processing

## Objective
This assignment involves using Apache Sedona and Delta Lake within a Spark environment to perform various operations on spatial data, such as reading, writing, and querying geospatial datasets.

## Setup Instructions

### Prerequisites
- Apache Spark 2.4.7 or higher with Delta Lake configured.
- Apache Sedona libraries integrated into the Spark environment.
- Scala with `sbt` for building and running the Spark application.

### Environment Setup
1. **Install Apache Spark:**
   - Follow the standard installation guide for [Apache Spark](https://spark.apache.org/downloads.html).

2. **Configure Delta Lake and Sedona in Spark:**
   - Include the necessary dependencies for Delta Lake and Sedona in your `build.sbt` file:
     ```sbt
     libraryDependencies += "io.delta" %% "delta-core" % "0.8.0"
     libraryDependencies += "org.apache.sedona" %% "sedona-sql" % "1.0.0-incubating"
     ```

3. **Build the Spark Project:**
   - Navigate to your project root and build the project using:
     ```bash
     sbt clean assembly
     ```

## Execution

1. **Run the Spark Application:**
   - Execute the built JAR using Spark submit:
     ```bash
     spark-submit --class assignment.five.AssignmentFive target/scala-2.12/your-jar-name.jar
     ```
   - The application will perform several spatial queries and print the results to the console.

## Skills Gained
- Working with Delta Lake for handling large-scale data.
- Using Apache Sedona for spatial data processing in a distributed environment.
- Implementing geospatial queries and spatial joins using Spark.

---

