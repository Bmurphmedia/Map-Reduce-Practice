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
# for a matrix multiple for each row of matrix a sum the cross product of all values which match rows in b 



outline = [0 , 1, 2, 3, 4]
def mapper(record):
    # send a key value for the relation and it's inverse
    matrix = record[0]
    row = record[1]
    column = record[2] 
    value = record[3]


    if matrix == "a":
    	for place in outline:
    		mr.emit_intermediate((row, place), {"a": [column, value]})
    
    if matrix == "b":
    	for place in outline:
    		mr.emit_intermediate((place,column),{"b": [row, value]})

  
 

       

# reducer invocations run on each unique key and a list of values
def reducer(key, values):
	# initialize a list to hold list of multiplication problems
	a_items = {}
	b_items = {}
	matrix = ""
	total = 0 
	answer = ()

	for value in values:
		try:
			a_items[value["a"][0]]= value["a"][1]
		except KeyError:
			b_items[value["b"][0]] = value["b"][1]

	for place in outline:
		a = 0 
		b = 0 
		try: 
			a = a_items[place]
		except KeyError:
			continue
		try:
			b = b_items[place]
		except KeyError:
			continue
		total += a * b 

	answer = (key[0], key[1], total)
	mr.emit(answer)
   

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)