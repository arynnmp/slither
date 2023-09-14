#nested loops example

#raises a number in the bases list to every number in the powers list
#outputs a new list.

def exponents(bases, powers):
  output = []
  for b in bases:
    for p in powers:
      output.append(b ** p)
  return output


#enter your two lists here
print(exponents([2, 3, 4], [1, 2, 3]))