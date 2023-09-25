#calculate farenheit
#enter temp to convert here
farenheit = 85

def f_to_c(f_temp):
  c_temp = (f_temp - 32) * 5/9
  return c_temp
celcius = round(f_to_c(farenheit), 1)
print(str(farenheit) + " degrees farenheit is " + str(celcius) + " degrees celcius")

print("--------------------------------------")
#calculate celcius
#enter temp to convert here
celcius = 10

def c_to_f(c_temp):
  f_temp = c_temp * (9/5) + 32
  return f_temp
farenheit = round(c_to_f(celcius), 1)
print(str(celcius) + " degrees celcius is " + str(farenheit) + " degrees farenheit")
