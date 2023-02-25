from PIL import Image

img=Image.new('RGB',(250,250),'white')
pixels=img.load()
a=input('Give point A as x,y:')
b=input('Give point B as x,y:')
a=a.split(',')
b=b.split(',')
a=list(map(lambda x: int(x), a))
b=list(map(lambda x: int(x), b))

v1=(b[0]-a[0])
v2=(b[1]-a[1])
vector=[abs(v1),abs(v2)]
sv=sorted(vector)[0]

if sv != 0:
    k=[v1//sv,v2//sv]
else:
    k=[v1,v2]
    sv=1

counter=sum(vector)
while counter>0:
    for x in range(abs(k[0])):
        pixels[a[0],a[1]]=(255,0,0)
        a[0]+=v1//abs(v1)
        counter-=1
    for y in range(abs(k[1])):
        pixels[a[0],a[1]]=(255,0,0)
        a[1]+=v2//abs(v2)
        counter-=1

img.show()
