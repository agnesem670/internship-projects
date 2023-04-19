# simple example
# try:
#     a = int (input('Number one:'))
#     b = int (input('Number two:'))
#     print (a/b)
#     print ('ok')
# except:
#     print ("Bug in user input")
# print ("outside")
# -------------------------------------

# else
# finally
# raise
# assertion

# --------------------------------------
# # diffrent excepts
# try:
#     a = int (input('Number one:'))
#     b = int (input('Number two:'))
#     print (a/b)
#     print ('ok')
# except ValueError:
#     print ("Could not convert to a number")
# except ZeroDivisionError:
#     print ("Can't divide by zero")
# except:
#     print ("Something went wrong")

# ----------------------------------
# loop
# while True:
#     try:
#         n = input ("Enter number:")
#         n = int (n)
#         break
#     except ValueError:
#         print (input ("Imput is not an intiger. Try again."))
# print ("Correct input")

# ------------------------------------

# def fancy_divide(numbers,index):
#     try:
#         denom = numbers[index]
#         for i in range(len(numbers)):
#             numbers[i] /= denom
#     except IndexError:
#         print("-1")
#     else:
#         print("1")
#     finally:
#         print("0")
# fancy_divide ([0, 2, 4], 4)

# ---------------------------------------------- v1 division by zero
# def fancy_divide(list_of_numbers, index):
#     try:
#         try:
#             raise Exception("0")
#         finally:
#             denom = list_of_numbers[index]
#             for i in range(len(list_of_numbers)):
#                 list_of_numbers[i] /= denom
#     except Exception as ex:
#         print(ex)

# v2
def fancy_divide(list_of_numbers, index):
    try:
        try:
            denom = list_of_numbers[index]
            for i in range(len(list_of_numbers)):
                list_of_numbers[i] /= denom
        finally:
            raise Exception("0")
    except Exception as ex:
        print(ex)

fancy_divide([0, 2, 4], 0)