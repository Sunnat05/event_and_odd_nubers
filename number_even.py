A=int(input()) #A four-digit integer is given. Find the number of even digits in it.
a=A%10
b=A//10%10 #Create a variable "var_int" and assign it a four-digit integer value.
c=A//100%10
d=A//1000 #Print the number of even digits in the variable "var_int".
x1=abs(a%2-1)
x2=abs(b%2-1)
x3=abs(c%2-1)
x4=abs(d%2-1)
sum=x1+x2+x3+x4
print(sum)