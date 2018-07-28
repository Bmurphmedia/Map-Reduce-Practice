import MapReduce
import sys

# Create an inverted index, dictionary where each word is associated with a list of document identifiers 
# inwhich the word appears.
# Output should be a (word, document ID list) tuple where word is String,
# and documen Id list is a list of Strings

"""
Word Count Example in the Simple Python MapReduce Framework
"""
# apple, orange - apple, banana - orange, apple 
# = apple, orage 

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

# mapper invocations result in key value pairs
def mapper(record):
    # send a key value for the relation and it's inverse
    mr.emit_intermediate(record[0], record[1])
    mr.emit_intermediate(record[1], record[0])

       

# reducer invocations run on each unique key and a list of values
def reducer(key, values):
    score = {}
    for value in values:
      try:
        score[value] += 1
      except KeyError:
        score[value] = 1
    for x, y in score.iteritems():
      if y > 0:
        mr.emit((key, x))
   

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)