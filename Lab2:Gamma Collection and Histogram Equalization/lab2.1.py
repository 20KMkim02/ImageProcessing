from PIL import Image
# import numpy as np

imgpath='img1.jpg'
img=Image.open(imgpath)
img=img.convert("L")
# img1=np.asarray(img)
# print(type(img1))
x,y=img.size
e=6
gamma=0.6
tot=[]
for i in range(x):
    for j in range(y):
        r=img.getpixel((i,j))
        s=e*(r**gamma)
        tot.append(s)
        # print(indexcolor)
mx=max(tot)
k=0
for i in range(x):
    for j in range(y):
        indexcolor=int((tot[k]/mx)*255)
        img.putpixel((i,j),indexcolor)
        k+=1
# print(max(tot))
img.show()
newimgpath='new_img.jpg'
img.save(newimgpath)

        