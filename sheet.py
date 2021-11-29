#Q3

s1="Nice to have it"
s2="here"
s3=" "
s1=s1+s2+s3
print(s1)



#Q4

a=[1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
print(a[3][1][2][0])




#Q5

a=[1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
s1="Nice to have it"
s2="here"
a.insert(0,s1)
a.append(s2)
print(a)




#Q6

numbers=[386,462,47,418,907,344,236,375,823,566,597,978,328,615,953,345,399,162,758,219,918,237,412,566,826,248,866,950,626,248,866,950,626,949,687,217,815,67,104,58,512,24,892,894,767,553,81,379,843,831,445,742,717,958,74,527]
for i in numbers:
    if(i%2==0 and i<=237):
        print(i)




#Q7

color_list_1={"White","Black","Red"}
color_list_2={"Red","Green"}
print(color_list_1.difference(color_list_2))




#Q8

str=input("enter a string")
s=[]
for i in str:
    s+=[i]
list=[]
for i in range(0,26):
    list+=[chr(i+97)]
c=0
for i in list:
    if i in s:
        c+=1
print(c)
if(c==26):
    print("pangram")
else:
    print("not")



#Q9

n=int(input("Enter a number"))
s=n+n*n+n*n*n
print(s)




#Q10

st=input("enter a hashtag string")  #23 54 12#98 3 17
st=st.split('#')
x=st[0].split(' ')
y=st[1].split(' ')
print(x)
print(y)



#Q11

sen=input("enter a comma seperated string")  #without,help,bag,world
sen=sen.split(',')
l=len(sen)
l=l-1
sen.sort()
print(sen)
for i in sen:
    if (i!=sen[l]):
        print(i,end=',')
    else:
        print(i)




#Q12

d={'Student':['Rahul','Kishore','Vidhya','Raakhi'],'Marks':[57,87,67,79]}
def higMarks(k):
    max=k['Marks'][0]
    for i in k['Marks']:
        if(i>max):
            max=i
    ind=d['Marks'].index(max)
    print(d['Student'][ind])
higMarks(d)



#Q13

str = input('enter a sentence')
l,d=0,0
for i in str:
    if(i.isalpha()):
        l+=1
    elif(i.isdigit()):
        d+=1
print("LETTERS",l)
print("DIGITS",d)

        

#Q14

d={'Name':['Akash','Soniya','Vishakha','Akshay','Rahul','Vikas'],'Subject':['Python','Java','Python','C','Python','Java'],'Ratings':[8,4,7.8,8,9,8.2,5.6]}
l=input("enter your preferred language")
newdata={}
j=d['Subject'].index(l)
newdata['Name']=[]
newdata['Subject']=[]
newdata['Ratings']=[]

for i in d['Subject']:
    if (i==l):
        newdata['Name'].append(d['Name'][j])
        newdata['Subject'].append(d['Subject'][j])
        newdata['Ratings'].append(d['Ratings'][j])
    j+=1
    
print(newdata)



#Q15

n=int(input("enter a number"))
div =[i for i in range(0,n) if i%7==0]
print(div)


#Q16

x=0;
y=0;
up=5;
down=3;
left=3;
right=2;
x1=up-down;
y1=left-right;
r=((x1-x)**2 + (y1-y)**2)**0.5
print(r)
            

    
    
    





