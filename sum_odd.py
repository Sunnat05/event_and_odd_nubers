var_int=int(input())
sum_odd=0
sum_odd+=(var_int%10)*(var_int%2)#Create a variable "var_int" and assign it a four-digit integer value.
var_int//=10

sum_odd+=(var_int%10)*(var_int%2)#Create a variable "sum_even" and assign it 0.
var_int//=10#Create a variable "sum_even" and assign it 0.

sum_odd+=(var_int%10)*(var_int%2)#Find the sum of the odd digits in the variable "var_int".
var_int//=10

sum_odd+=(var_int%10)*(var_int%2)
print(sum_odd)