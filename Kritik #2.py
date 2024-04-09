def function(x):
  import math
  if (x>0):
    value = (math.e**x)+(math.log(x))
    return value

def roots (a,b):
  if (function(a)<0 and function(b)>0):
      j=0
      x=0
      while (j<10):
          x=(a+b)/2
          j+=1
          if (function(x)<0):
            b=x
          elif (function(x)>0):
            a=x
          else:
               return x
      return x
  elif (function(b)<=0 and function(a)>=0):
      j=0
      x=0
      while (j<10):
          x=(a+b)/2
          j+=1
          if (function(x)<0):
            a=x
          elif (function(x)>0):
            b=x
          else:
            return x
      return x
  else:
    print ("Error!")

a=0
b=1
root = roots(a,b)
print (root)