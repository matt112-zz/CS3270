# ########################### PART 1 #########################
# 
# def fcount(func):
#     def wrapper(*args, **kwargs):
#         wrapper.count += 1
#         return func(*args, **kwargs)
#     wrapper.count = 0
#     return wrapper
# 
# @fcount
# def f(n):
#     return n+2
#   
# for n in range(5):
#     print f(n)
#   
# print 'f count =', f.count
# 
# @fcount
# def g(n):
#     return n*n
# 
# print 'g count =', g.count
# print g(3)
# print 'g count=', g.count
# 
# 
# 
# #################### PART 2 ##############################

class fcount2(object):
    def __init__(self, func):
        #print('in the init of fcount2')
        self.func = func
        self.count = 0
        self.widthcount = None
    
    def __call__(self, *args, **kwargs):
        #print('function called')
        self.count += 1
        #print all_args
        if self.widthcount is not None:
            self.widthcount += 1
        return self.func(*args, **kwargs)
    
    def __enter__(self):
        #print('in enter of fcount2 function')
        #print 'self count ', self.count
        self.widthcount = 0
        return self
    
    def __exit__(self, exception_type, exception_value, traceback):
        print 'with block class =', self.widthcount


# @fcount2
# def f(n):
#     #print('calling f function')
#     return n+2
# 
# for n in range(5):
#     print f(n)
# print 'f count =',f.count
# 
# def foo(n):
#     return n*n
#     
# with fcount2(foo) as g:
#     print g(1)
#     print g(2)
# print 'g count =',g.count
# print 'f count =',f.count
# 
# with fcount2(f) as g:
#     print g(1)
#     print g(2)
# print 'g count =',g.count
# print 'f count =',f.count
# 
# with f:
#     print f(1)
#     print g(2)
# print 'g count =',g.count
# print 'f count =',f.count



############################# PART 3 #####################################3

"""
Write a generator named produce that takes a string as input 
and processes it a character at a time. If the character is a decimal digit, 
n, say, then (n+1) repetitions of the next character (digit or not) are returned as a 
string (so a digit of 0-9 means that 1-10 instances of the next character are desired; 
you may assume that the input does not end with a digit character). If the character 
is not a digit, it is returned as-is. The following code should work as indicated:
Output:
A BBB EEEEEE 4444 666 F G Z Y W 2222 00 P Q 999999999 R
"""

def produce(strs):
#     for x in range(len(strs)):
#         if strs[x].isdigit():
#             yell = int(strs[x]) + 1
#             x += 1
#             yield yell * strs[x]
#         else:    
#             yield strs[x]

    letters = list(strs)
    
    while(len(letters) is not 0):
        #print 'going again'
        if(letters[0].isdigit()):
            #print 'found digit'
            word = (int(letters[0])+1) * letters[1]
            letters.pop(0)
            letters.pop(0)
            yield word
        elif(letters[0].isalpha()):
            #print 'found letter'
            word = letters[0]
            letters.pop(0)
            #print letters
            yield word
        else:
            #print 'blah'
            break

p = produce('A2B5E3426FG0ZYW3210PQ89R')
for s in p: print s,
print














