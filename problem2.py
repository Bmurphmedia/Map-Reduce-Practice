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

def mapper(record):
    # tuple of order record, list of line item records
    key = record[1]
    mr.emit_intermediate(key, record)
       

# reducer invocations run on each unique key and a list of values
def reducer(key, list_of_records):
    amount = len(list_of_records)
    order = list_of_records[0]
    line_items = list_of_records[1:amount]
    for item in line_items:
      mr.emit(order + item)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)