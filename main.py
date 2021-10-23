import csv 
import plotly.express as ps
import os
with open("data.csv") as f:
    reader=csv.reader(f)
    data=list(reader)
    data.pop(0)
val=[]    
leng=0
sum=0
for i in range(len(data)):
    val.append(float(data[i][2]))
    sum=float(data[i][2])+sum
    leng+=1
val.sort()
print(sum/leng)
ba=ps.bar(val,x=val,y=val)
ba.write_html("index.html")
with open("index.html") as f
html=os.write("")
#html = '


