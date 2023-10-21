from PIL import Image
import matplotlib as plt
import numpy as np

imgpath='img1.jpg'

def transformImage(imgpath):
    OriImg=Image.open(imgpath)
    OriImg=OriImg.convert("L")
    width,hight=OriImg.size
    OriImgArray=np.array(OriImg)
    latestImg=OriImgArray.copy()
    Dg=globalDeviat(OriImgArray,width,hight)
    Mg=0
    for i in range(hight):
        for j in range(width):
            Mg+=OriImgArray[i][j]/(hight*width)
    # print("Mean global= ",Mg)
    for i in range(1,hight-1):
        for j in range(1,width-1):
            latestImg[i][j]=Adjpixel(i,j,OriImgArray,Dg,Mg)
    newimg=Image.fromarray(latestImg)
    imgsavepath='newImgFromlocalHistrogram.jpg'
    newimg.show()
    newimg.save(imgsavepath)

def Adjpixel (y,x,OriImgArray,Dg,Mg):#return the new pixel 
    AdjArray=OriImgArray.copy()
    k0=0.35
    k1=0.1
    k2=0.8
    E=4
    sxy=0

    #create color dict: key is color0-255 value = count in filter
    color={}
    for i in range(256):
        color[i]=0
    # Create 3*3 filter
    tableFilter=[]
    tabletruthcolor=[]
    maxOri=0
    meanfilter=0
    # add original color to tableFilter and truthcolor and find max of all
    for i in range(y-1,y+2):
        for j in range(x-1,x+2):
            tableFilter.append(OriImgArray[i][j])
            tabletruthcolor.append(OriImgArray[i][j])
            if(OriImgArray[i][j]>maxOri):
                maxOri=OriImgArray[i][j]

    #put pixel from filter to nk/n
    for i in tableFilter:
        color[i]=color[i]+1/(len(tableFilter))   #not sure using 9/25/121 or x*y

    #Find mean of filter Ms(x,y)            
    for i in range(len(color)):
        meanfilter+=(i*color[i])
    # print(meanfilter)

    #Find sxy
    for i in range(len(color)):
        sxy+=((i-meanfilter)**2)*color[i]
    sxy=(sxy)**(1/2)
    # print("Meanfilter= ",meanfilter,"meanglobal= ",Mg,"Sxy= ",sxy," and Dg= ",Dg)
    
    if (meanfilter<=k0*Mg and(k1*Dg<=sxy) and (sxy<=k2*Dg)) :
        #Sk
        for i in range(1,256):
            color[i]+=color[i-1]
        maxx=color[255]

        #finalSk
        for i in range(0,255):
            color[i]=int((color[i]*maxOri)//maxx)

        #set new color back to filter
        for i in range(len(tableFilter)):
            tableFilter[i]=color[tableFilter[i]]
    else:
        return (tableFilter[4])
    #return Adj pixel
    return (E*tableFilter[4]) #4 #12 #60

def globalDeviat(inarray,x,y):
    allcolorfullimg=[]
    meanfullimg=0
    Dg=0
    countpixel={}
    for i in range(256):
        countpixel[i]=0

    for i in range(y):
        for j in range(x):
            allcolorfullimg.append(inarray[i][j])

    for i in allcolorfullimg:
        countpixel[i]=countpixel[i]+1/(x*y)

    for i in range(len(countpixel)):
        # print(i*countpixel[i])
        meanfullimg=meanfullimg+(i*countpixel[i])
        

    for i in range(len(countpixel)):
        Dg+=((i-meanfullimg)**2)*countpixel[i]
    Dg=Dg**(1/2)
    # print(countpixel)
    # print("meanfullimg= ",meanfullimg)
    # print("Dg =",Dg)
    return Dg


transformImage(imgpath)