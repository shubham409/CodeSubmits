st=input()
ls=st.replace('><' ,' ')[1:-1].split()
stack=[]
tag=0
for i in ls:
    if i[0]!='/':
        # opening tag
        stack.append([i,tag])
        ans= '  '*tag + '<'+i+'>'
        print(ans)
        tag+=1

    else:
        char,tage_value=stack.pop()
        ans= '  '* tage_value+ '</'+i[1]+'>'
        print(ans)
        tag-=1