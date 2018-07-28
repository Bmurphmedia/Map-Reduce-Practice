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
#initialize matrixes for list of lists
a_matrix_data = []
b_matrix_data = []

#First we need to scan the data and find dimensions of each matrix 
# then with the dimensions we can build matrix with available values and fill in 0s as placeholder where it is sparse 
# then send each matrix and needed dimensions to mapper which will emit according 

def matrix(record):
	if record[0] == "a":
		a_matrix_data.append(record[1:4])
	else:
		b_matrix_data.append(record[1:4])


def mapper(record):
    # send a key value for the relation and it's inverse
    matrix = record[0]
    row = record[1]
    column = record[2] 
    value = record[3]


    if matrix == "a":
    	for place in outline:
    		mr.emit_intermediate((row, place), value)
    
    if matrix == "b":
    	for place in outline:
    		mr.emit_intermediate((place,column),value)

  
 

       

# reducer invocations run on each unique key and a list of values
def reducer(key, values):
	return
	# initialize a list to hold list of multiplication problems
	
	# print key, values

	# mr.emit(answer)
   

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, matrix, reducer)

print b_matrix_data
