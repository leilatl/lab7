#warmup-1
def not_string(str):
  if len(str) >= 3 and str[:3] == "not":
    return str
  return "not " + str

#warmup-2
def last2(str):
  if len(str) < 2:
    return 0
  
  last2 = str[len(str)-2:]
  count = 0
  
  for i in range(len(str)-2):
    sub = str[i:i+2]
    if sub == last2:
      count = count + 1

  return count

#String-1
def hello_name(name):
  return("Hello "+name+"!")

#List-1
def first_last6(nums):
  if(nums[0]==6 or nums[len(nums)-1]==6): return True
  else: return False

#Logic-1
def cigar_party(cigars, is_weekend):
  if(60>=cigars>=40 or(is_weekend and cigars>=40)): return True
  else: return False

#Logic-2
def make_bricks(small, big, goal):
  return (goal%5)<=small and (goal-(big*5))<=small

