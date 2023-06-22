A=int(input()) #A four-digit integer is given. Find the number of even digits in it.
a=abs(A%10%2-1)
b=abs(A//10%10%2-1) #Create a variable "var_int" and assign it a four-digit integer value.
c=abs(A//100%10%2-1)
d=abs(A//1000%2-1) #Print the number of even digits in the variable "var_int".
var_int=a+b+c+d
print(var_int)