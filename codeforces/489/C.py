def fun(ls):
    n,num=ls
    max_number=''
    min_number=''
    if(num>9*n ):
        print(-1,-1)
        return
    if(num==0):
        if(n!=1):
            print(-1,-1)
            return
        else:
            print(0,0)
            return
    last_number=-1
    for i in range(n):
        if(num>9):
            max_number+=str(9)
            num-=9
            min_number=max_number
        else:
            # last number to be filled in max sequence
            if(num==9):
                max_number+=str(9)
                last_number=9
                num-=9
            else:
                if(num==0):
                    max_number+='0'
                else:
                    max_number+=str(num)
                    last_number=num
                    num-=num
    if(len(min_number)+1!=n):
        min_number+=str(last_number-1)
        zero='0'*(n-len(min_number)-1)
        min_number+=zero
        min_number+=str(1)
        min_number=min_number[::-1]
    else:
        min_number+=str(last_number)
        min_number=min_number[::-1]
    print(min_number,max_number)


T = 1
for _ in range(T):
    ls= list(map(int, input().split()))
    fun(ls)