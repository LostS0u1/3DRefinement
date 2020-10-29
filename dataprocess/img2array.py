import skimage.io as io
import numpy as np
import cv2

def array_1(img_n):
  img_1=[]
  for i in img_n:
     for m in i:
        img_1.append(m)
     return img_1


def array_rgb_1(img):
   b=cv2.split(img)[0]
   g=cv2.split(img)[1]
   r=cv2.split(img)[2]

   b_1=array_1(b)
   g_1=array_1(g)
   r_1=array_1(r)

   return b_1,g_1,r_1

def folderimg(subject,camera):
  string="./Imgdata/S7/"+fle+'/*.jpg'
  coll = io.ImageCollection(string)
  lst=[]
  for count, i in enumerate(coll):
    b,g,r=array_rgb_1(i)
    lst.append([b,g,r])

  #lst [3134,3,1000]
  length=len(lst)
  
  dst=[]
  for j in range(length):
    
    tmpp=[]
    for i in range(1000):
     tmp=[]
     tmp.append(lst[j][0][i])
     tmp.append(lst[j][1][i])
     tmp.append(lst[j][2][i])
     tmpp.append(tmp)
    dst.append(tmpp)
  
  
  return dst
   
  

#filename=["Walking.54138969","Walking.55011271","Walking.58860488","Walking.60457274","Walking 1.54138969","Walking 1.55011271","Walking 1.58860488","Walking 1.60457274"]

filename=["Walking 1.54138969","Walking 1.55011271","Walking 1.58860488","Walking 1.60457274","Walking 2.54138969","Walking 2.55011271","Walking 2.58860488","Walking 2.60457274"]
#subjectlist=["S1","S5","S6","S8","S9","S11"]
subjectlist=["S7"]
cnt=0
for subject in subjectlist:
  for fle in filename:
   result=[]
   
   tmp=folderimg(subject,fle)
   
   result=np.array(tmp)
   result=np.squeeze(result)
   
   np.save(("/media/wanghao/TOSHIBA EXT/RGBdataset/rgbdata/"+subject+"/"+fle+".npy"),result)
   cnt+=1
   print("save",subject,fle,result.shape,"  ",cnt,"/48")

