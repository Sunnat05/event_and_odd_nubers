var_int=int(input())#A four-digit integer is given. Find the sum of even digits in it.
sum_even=0
sum_even+=(var_int%10)*(1-var_int%2)#Create a variable "var_int" and assign it a four-digit integer value.
var_int=var_int//10
sum_even+=(var_int%10)*(1-var_int%2)#Create a variable "sum_even" and assign it 0.
var_int//=10
sum_even+=(var_int%10)*(1-var_int%2)#Find the sum of the even digits in the variable "var_int".
var_int//=10
sum_even+=(var_int%10)*(1-var_int%2)
print(sum_even)