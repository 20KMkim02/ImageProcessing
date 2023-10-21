import numpy as np
from PIL import Image
import matplotlib as plt
import copy

def MedianFilter(hight,width,imgArray):
    candidate=[]
    for i in range (hight-1,hight+2):
        for j in range(width-1,width+2):
            # print(imgArray[i][j])
            candidate.append(imgArray[i][j])
    candidate=sorted(candidate)
    # print(candidate)
    return candidate[0]//4+candidate[1]//4+candidate[2]//4+candidate[3]//4

imgpath="noisy_img2.jpg"
oriimg=Image.open(imgpath)
grayscaleimg=oriimg.convert('L')
GImgArray=np.array(grayscaleimg)
newImg=copy.deepcopy(GImgArray)
width,hight=oriimg.size
# print (width,hight)
# filtersize=3
for i in range(1,hight-1):
    for j in range(1,width-1):
        # print("rorb",i+j," ")
        newImg[i][j]= MedianFilter(i,j,GImgArray)


#rim filter
for i in range(0,hight+1):
    for j in range(0,width+1):
        if(i==0 and j<width-1):
            candidate=[]
            candidate.append(GImgArray[0][j])
            candidate.append(GImgArray[0][j+1])
            candidate.append(GImgArray[1][j])
            candidate.append(GImgArray[1][j+1])
            candidate=sorted(candidate)
            # print(candidate)
            newImg[i][j]=candidate[0]//4+candidate[1]//4+candidate[2]//4+candidate[3]//4
        if(i<hight-1 and j==0):
            candidate=[]
            candidate.append(GImgArray[i][0])
            candidate.append(GImgArray[i][1])
            candidate.append(GImgArray[i+1][0])
            candidate.append(GImgArray[i+1][1])
            candidate=sorted(candidate)
            # print(candidate)
            newImg[i][j]=candidate[0]//4+candidate[1]//4+candidate[2]//4+candidate[3]//4
        if(i==hight-1 and j<width-1):
            candidate=[]
            candidate.append(GImgArray[i][j])
            candidate.append(GImgArray[i][j+1])
            candidate.append(GImgArray[i-1][j])
            candidate.append(GImgArray[i-1][j+1])
            candidate=sorted(candidate)
            # print(candidate)
            newImg[i][j]=candidate[0]//4+candidate[1]//4+candidate[2]//4+candidate[3]//4
        if(i<hight-1 and j==width-1):
            candidate=[]
            candidate.append(GImgArray[i][j])
            candidate.append(GImgArray[i][j-1])
            candidate.append(GImgArray[i+1][j])
            candidate.append(GImgArray[i+1][j-1])
            candidate=sorted(candidate)
            # print(candidate)
            newImg[i][j]=candidate[0]//4+candidate[1]//4+candidate[2]//4+candidate[3]//4

FinalImg=Image.fromarray(newImg)
FinalImg.save("Averaging_filtered_Img2.jpg")        
FinalImg.show()