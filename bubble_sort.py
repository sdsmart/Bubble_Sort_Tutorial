# UNIVERSITY OF OKLAHOMA -- SCHOOL OF COMPUTER SCIENCE
# BUBBLE SORT TUTORIAL

# This function executes one iteration of the bubble sort algorithm
def bubble_sort(my_list):
	
	number_of_elements = len(my_list)
	
	# Simple bubble sort algorithm.
	for i in range(number_of_elements - 1):
	
		if my_list[i] > my_list[i+1]:
	
			# Explicit 3 line swapping is used to illustrate this method to
			# new coders.
			temp = my_list[i]
			my_list[i] = my_list[i+1]
			my_list[i+1] = temp
