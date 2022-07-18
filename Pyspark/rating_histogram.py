from pyspark import SparkConf, SparkContext
import collections

conf = SparkConf().setMaster("local").setAppName("ratinghistogram")
sc = SparkContext(conf=conf)

lines = sc.textFile(r"C:\Users\sid\Downloads\diggibyte\Pyspark\ml-100k/u.data")
ratings = lines.map(lambda x:x.spark()[2])
result = ratings.countByValue()

sortedResults = collections.OrderedDict(sorted(result.items()))
for key, value in sortedResults.iteritems():
    print("%s %i"%(key, value))