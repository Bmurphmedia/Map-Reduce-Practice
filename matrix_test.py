test = (63 * 63) + (63 * 59) + (63 * 30) + (63 * 77) 
test = 63 * (63 + 59 + 30 + 77) 

test = 63 * (63 + 18 + 89 + 28 + 39) 

# this what each reducer needs for 0, 0 
test = (63 * 63) + (45 * 59) + (93 * 30) + (32 * 77) 

# this is what it needs for 0.1 
test2 = (63 * 18) + (45 * 76) + (93 * 52) + (32 * 75) + (49 * 46)

# 1, 0 
test3 = (33 * 63) + (0 * 59) + (0 * 30) + (26 * 77) + (95 * 0)

print test 
print test2
print test3

# 63, 45, 93, 32, 49
# 33, __, __, 26, 95
# 25, 11, __, 26, 89



#63, 18, 89, 28, 39
#59, 76, 34
#30, 52, 49
#77, 75, 85
#__, 46, 33
