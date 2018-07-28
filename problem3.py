import MapReduce
import sys

# Create an inverted index, dictionary where each word is associated with a list of document identifiers 
# inwhich the word appears.
# Output should be a (word, document ID list) tuple where word is String,
# and documen Id list is a list of Strings

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

# mapper invocations result in key value pairs
# for this the record is 2 element list of person and person b
def mapper(record):
    # tuple of order record, list of line item records
    mr.emit_intermediate(record[0], record[1])
       

# reducer invocations run on each unique key and a list of values
def reducer(key, list_of_records):
    amount = len(list_of_records)
    mr.emit((key, amount))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)