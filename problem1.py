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

def mapper(record):
    # key: document identifier
    # value: document contents
    key = record[0]
    value = record[1]
    words = value.split()
    tracker = []
    for w in words:
      if w in tracker:
        continue
      else:
        mr.emit_intermediate(w, key)
        tracker.append(w)   

def reducer(word, list_of_docs):
    # key: word
    # value: list of occurrence counts
    all_docs = []
    for doc in list_of_docs:
      all_docs.append(doc)
    mr.emit((word, all_docs))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)