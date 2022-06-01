
"""myArray=[1,3,4,2,7,0]

flag=0

for  x in myArray:
  if flag==0:
      for y in myArray:
          if x != y and x + y==10:
              flag=1
              print(x,y)
"""



myArray = [ 1,3,2,0,0,7,8,1,3,0,6,7,1 ]
new_array=[]
listmp=[]
listafinal=[]
resultado=""
for i in myArray:
    if i != 0:
        listmp.append(i)

    elif i==0:
        if len(listmp)!=0:

            listmp.sort()
            listafinal =listafinal+listmp
            resultado=resultado+"".join(map(str,listmp))
            listmp=[]
    else:
        if not listmp:
            listmp.sort()
            resultado=resultado+"".join(map(str,listmp))
        
    if i==0:
        resultado=resultado+" "


print(resultado)

              