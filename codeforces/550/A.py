def fun(st:str):
    a=st.find('AB')
    b=st.find('BA',a+2)
    x=st.find('BA')
    y=st.find('AB',x+2)
    if ((a!=-1 and b!=-1) or (x!=-1 and y!=-1)):
        print('yes')
        return
    print('no')
st= input()
fun(st)   