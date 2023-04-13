import sys
from pyspark.sql import SparkSession
# you may add more import if you need to
from pyspark.sql.functions import col


# don't change this line
hdfs_nn = sys.argv[1]

spark = SparkSession.builder.appName("Assigment 2 Question 1").getOrCreate()
# YOUR CODE GOES BELOW
df = (
    spark.read.option("header", True)
    .option("inferSchema", True)
    .option("delimiter", ",")
    .option("quotes", '"')
    .csv("hdfs://%s:9000/assignment2/part1/input/" % (hdfs_nn))
)

df = df.filter(
    (col("Rating") >= 1.0) & (col("Rating").isNotNull())
)

df.coalesce(1).write.mode('overwrite').csv("hdfs://%s:9000/assignment2/output/question1/" % (hdfs_nn), header=True)
