# Incremental strategy:   increase size of array by a
#                         constant number of cells at a time
#
# doubling strategy:      double the size each time more space is needed
#
#
# 1)  Write aditional method append_1 that
#     uses incremental instead of doubling strategy.
#     It should take an aditional integer parameter that specifies
#     how many cells should be added each time.
#
# 2)  rewrite method compute_average and call it in main() the function
#     must use the dynamic array object instead of list because
#     list relies on doubling method
#
# 3)  compute_average should compare time for n inserts using append and then using append_1
#
# 4)    in main call append once and then call append_1 with the value of 1 and then with the value of 5
#
#Submision should be modified code for:  compute_average,
#                                         modified code for dynamic array,
#                                         print out of results
