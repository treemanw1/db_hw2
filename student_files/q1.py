import sys
from pyspark.sql import SparkSession
# you may add more import if you need to
from pyspark.sql.functions import col


# don't change this line
hdfs_nn = sys.argv[1]

spark = SparkSession.builder.appName("Assigment 2 Question 1").getOrCreate()
# YOUR CODE GOES BELOW

# Reading the CSV file into a DataFrame
df = (spark.read.option("header", True).option("inferSchema", True).option("delimiter", ",").option("quotes", '"').csv(f"hdfs://{hdfs_nn}:9000/assignment2/part1/input/"))

# Cleaning up the DataFrame by removing rows with no reviews or rating < 1.0 or no rating
cleaned_df = df.filter(
    (col("Rating") >= 1.0) & (col("Rating").isNotNull()) & (col("Reviews").isNotNull())
)

# Writing the cleaned DataFrame as CSV into an HDFS path
df.coalesce(1).write.mode('overwrite').csv(f"hdfs://{hdfs_nn}:9000/assignment2/output/question1/", header=True)


# Stopping the SparkSession
spark.stop()
