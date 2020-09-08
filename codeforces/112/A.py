def fun(st, sr):
    if st.lower()>sr.lower():
        print(1)
    if st.lower()<sr.lower():
        print(-1)
    if st.lower()==sr.lower():
        print(0)
 
 

st = input()
sr=input()
fun(st , sr )
