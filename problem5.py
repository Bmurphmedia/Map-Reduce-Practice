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
    dna = record[1]
    dna_trimmed = dna[0:-10]

    mr.emit_intermediate(dna_trimmed, record[1])
 

       

# reducer invocations run on each unique key and a list of values
def reducer(key, values):
	mr.emit(key)
   

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)