package assignment.five

import org.apache.log4j.{Level, Logger}
import org.apache.sedona.viz.core.Serde.SedonaVizKryoRegistrator
import org.apache.sedona.sql.utils.{Adapter, SedonaSQLRegistrator}
import org.apache.sedona.viz.sql.utils.SedonaVizRegistrator
import org.apache.spark.serializer.KryoSerializer
import org.apache.spark.sql.SparkSession

object AssignmentFive extends App {

  Logger.getLogger("org").setLevel(Level.WARN)
  Logger.getLogger("akka").setLevel(Level.WARN)

  var sparkSession:SparkSession = SparkSession.builder().
    config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension")
    .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog")
    .config("spark.serializer",classOf[KryoSerializer].getName).
    config("spark.kryo.registrator", classOf[SedonaVizKryoRegistrator].getName).
    master("local[*]")
    .appName("lastassignment").getOrCreate()

  SedonaSQLRegistrator.registerAll(sparkSession)
  SedonaVizRegistrator.registerAll(sparkSession)

  val resourseFolder = System.getProperty("user.dir")+"/src/test/resources/"
  val csvPolygonInputLocation = resourseFolder + "testenvelope.csv"
  val csvPointInputLocation = resourseFolder + "testpoint.csv"
  val firstpointdata = resourseFolder + "outputdata/firstpointdata"
  val firstpolydata = resourseFolder + "outputdata/firstpolygondata"

  println("Q2.1")
  firstPointQuery()
  println("Q2.2")
  secondPointQuery()
  println("Q2.3")
  firstPloygonQuery()
  println("Q2.4")
  secondPolygonQuery()
  println("Q2.5")
  JoinQuery()

  println("Assignment Five Done!!!")

  def firstPointQuery(): Unit = {
    //Read the given testpoint.csv file in csv format and write in delta format and save named firstpointdata
    var inp_buf = sparkSession.read.csv(csvPointInputLocation)
    var read_pointsDf = inp_buf.toDF()
    read_pointsDf.createOrReplaceTempView("points")
    // create two columns from the DF, the x1/y1 will be present in points._c0 and x2/y2 will be present in points._c1 and points._c1
    read_pointsDf = sparkSession.sql("select ST_Point(CAST(points._c0 as Decimal(24,20)), CAST(points._c1 as Decimal(24,20))) as point from points where CAST(points._c0 as Decimal(24,20)) >500 and CAST(points._c1 as Decimal(24,20)) >500")
    // overwrite the queries result to the output file
    read_pointsDf.write.format("delta").mode("overwrite").option("mergeSchema", "true").save(firstpointdata)
  }

  def secondPointQuery(): Unit = {
    //Read the firstpointdata in delta format. Print the total count of the points.
    var read_parquet = sparkSession.read.format("delta").load(firstpointdata)
    read_parquet.count()
    println(read_parquet.count())
  }

  def firstPloygonQuery(): Unit = {
    //Read the given testenvelope.csv in csv format and write in delta format and save it named firstpolydata
    var inp_buf = sparkSession.read.csv(csvPolygonInputLocation)
    var read_points = inp_buf.toDF()
    read_points.createOrReplaceTempView("polygon")
    // create two columns from the DF, the x1/y1 will be present in points._c0,  x2/y2 will be present in points._c1 and points._c1 and xn/yn will be present in points._cn
    read_points = sparkSession.sql("select ST_PolygonFromEnvelope(CAST(polygon._c0 as Decimal(24,20)), CAST(polygon._c1 as Decimal(24,20)), CAST(polygon._c2 as Decimal(24,20)), CAST(polygon._c3 as Decimal(24,20))) as poly from polygon where CAST(polygon._c0 as Decimal(24,20)) >900 and CAST(polygon._c1 as Decimal(24,20)) >900 and CAST(polygon._c2 as Decimal(24,20)) >900 and CAST(polygon._c3 as Decimal(24,20)) >900")
    // overwrite the query result to the output file
    read_points.write.format("delta").mode("overwrite").option("mergeSchema", "true").save(firstpolydata)
  }

  def secondPolygonQuery(): Unit = {
    //Read the firstpolydata in delta format. Print the total count of the polygon
    var read_parquet = sparkSession.read.format("delta").load(firstpolydata)
    read_parquet.count()
    println(read_parquet.count())
  }

  def JoinQuery(): Unit = {
    //Read the firstpointdata in delta format and find the total count for point pairs where distance between the points within a pair is less than 2.
    var read_points = sparkSession.read.format("delta").load(firstpointdata)
    var read_poly_points = sparkSession.read.format("delta").load(firstpolydata)
    read_points = read_points.toDF()
    read_points.createOrReplaceTempView("points")

    read_poly_points = read_poly_points.toDF()
    read_poly_points.createOrReplaceTempView("polygon")

    var read_join = sparkSession.sql("select points.point as point from polygon, points where ST_Contains(polygon.poly, points.point)")
    read_join.createOrReplaceTempView("joinDF")

    var joinPoints = sparkSession.sql("select * from joinDF p1 join joinDF p2 where p1.point != p2.point and ST_Distance(p1.point, p2.point) < 2")
    println(joinPoints.count()/2)
  }
}