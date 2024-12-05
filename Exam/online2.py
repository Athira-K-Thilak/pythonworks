def next_fibonacci_number(number:int):
    prev=0
    current=1
    i=0
    while(i<number):
        
        next=prev+current
        prev,current=current,next
        if prev==number:
            return print(next)
    
next_fibonacci_number(13)    