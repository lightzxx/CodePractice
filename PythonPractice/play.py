# def FancyDivide(list_of_numbers, index):
#     try:
#         try:
#             raise Exception("0")
#         finally:
#             denom = list_of_numbers[index]
#             for i in range(len(list_of_numbers)):
#                 list_of_numbers[i] /= denom
#     except Exception, e:
#         print e
        

# # FancyDivide([0,2,4], 0)
# # print

# try:
# 	x = 11/0
# except Exception, e:
# 	print str(e)+". Fucking Errors!"

class Networkerror(RuntimeError):
   def __init__(self, arg):
      self.args = arg

try:
   raise Networkerror("Bad hostname")
except Networkerror,e:
   print ''.join(e)
