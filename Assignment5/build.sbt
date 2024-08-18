ThisBuild / version := "0.1.0-SNAPSHOT"

ThisBuild / scalaVersion := "2.12.12"

lazy val root = (project in file("."))
  .settings(
    name := "AssignmentFive"
  )
val SparkVersion = "3.2.0"

val SparkCompatibleVersion = "3.0"

val HadoopVersion = "2.7.2"

val SedonaVersion = "1.1.1-incubating"

val ScalaCompatibleVersion = "2.12"

// Change the dependency scope to "provided" when you run "sbt assembly"
val dependencyScope = "compile"

val geotoolsVersion = "1.1.0-25.2"

logLevel := Level.Warn

libraryDependencies ++= Seq(
  "org.apache.spark" %% "spark-core" % SparkVersion % dependencyScope exclude("org.apache.hadoop", "*"),
  "org.apache.spark" %% "spark-sql" % SparkVersion % dependencyScope exclude("org.apache.hadoop", "*"),
  "org.apache.hadoop" % "hadoop-mapreduce-client-core" % HadoopVersion % dependencyScope,
  "org.apache.hadoop" % "hadoop-common" % HadoopVersion % dependencyScope,
  "org.apache.hadoop" % "hadoop-hdfs" % HadoopVersion % dependencyScope,
  "org.apache.sedona" % "sedona-core-".concat(SparkCompatibleVersion).concat("_").concat(ScalaCompatibleVersion) % SedonaVersion,
  "org.apache.sedona" % "sedona-sql-".concat(SparkCompatibleVersion).concat("_").concat(ScalaCompatibleVersion) % SedonaVersion ,
  "org.apache.sedona" % "sedona-viz-".concat(SparkCompatibleVersion).concat("_").concat(ScalaCompatibleVersion) % SedonaVersion,
  "io.delta" %% "delta-core" % "1.1.0",
  "org.wololo" % "jts2geojson" % "0.14.3" % "compile",
  "io.delta" %% "delta-sharing-spark" % "0.4.0",
  "org.datasyslab" % "geotools-wrapper" % "geotools-24.1",
  "org.locationtech.jts" % "jts-core" % "1.17.0"
)

