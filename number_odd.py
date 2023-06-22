A=int(input()) #A four-digit integer is given. Find the number of odd digits in it.
a=A%10%2
b=A//10%10%2 #Create a variable "var_int" and assign it a four-digit integer value.
c=A//100%10%2
d=A//1000%2#Print the number of odd digits in the variable "var_int".
var_int=a+b+c+d
print(var_int)