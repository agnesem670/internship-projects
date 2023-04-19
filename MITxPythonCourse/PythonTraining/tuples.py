# t = ()
# tu = (2, "one", 3)
# tu[1]
# (2, "one", 3) + (5, 6)
# print ( tu[1:2] )
# ("one",) 
# =============================================

# # can be used to swap variable values
# (x,y) = (y,x) 
# ==============================================

# # can be used to return more than one value from function
# def quotient_and_remainder (x, y):
#     q = x/y
#     r = x%y
#     return (q, r)
# (quot, rem) = quotient_and_remainder (4, 5)
# print (quot)
# print (rem)

# ===============================================
# # can iterate over tuples
# def get_data (aTuple):
#     nums = ()
#     words = ()
#     for t in aTuple:
#         nums = nums + (t[0], )
#         if t[1] not in words:
#             words = words + (t[1],)
#     min_nums = min(nums)
#     max_nums = max(nums)
#     unique_words = len(words)
#     return (min_nums, max_nums, unique_words)

# (small, large, words) = get_data(((1, 'mine'), 
#                                   (3, 'yours'),
#                                   (5, 'ours'),
#                                   (7, 'mine')))
# print (small)
# print (large)
# print (words)
# ===============================================

def oddTuples(aTup):
    """
    aTup: a tuple
    return: a tuple, every other element of the tuble

    """
    rTup = ()
    index = 0

    while index < len (aTup):
        rTup += (aTup[index],)
        index += 2
    return rTup

print (oddTuples (('I', 'am', 'a', 'test', 'tuple')))