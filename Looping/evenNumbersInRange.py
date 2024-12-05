#print even numbers in a range: even numbers between 1 to 50

begin=int(input("enter starting point:"))

end=int(input("enter end point:"))

if begin>end:

    begin,end=end,begin

i=begin

while(i<=end):

    if i%2==0:

        print(i)

    i=i+1    
