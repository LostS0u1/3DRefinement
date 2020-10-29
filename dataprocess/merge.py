import numpy as np
'''
filename=["Walking.54138969","Walking.55011271","Walking.58860488","Walking.60457274","Walking 1.54138969","Walking 1.55011271","Walking 1.58860488","Walking 1.60457274"]
subjectlist=["S1","S5","S6","S8","S9","S11"]
'''
filename=["Walking 1.54138969","Walking 1.55011271","Walking 1.58860488","Walking 1.60457274","Walking 2.54138969","Walking 2.55011271","Walking 2.58860488","Walking 2.60457274"]
subjectlist=["S7"]

cnt=0

for subject in subjectlist:
 for fle in filename:
  rgbpath = "/media/wanghao/TOSHIBA EXT/RGBdataset/rgbdata/"+subject+"/"+fle+".npy"
  x3d = "/media/wanghao/TOSHIBA EXT/RGBdataset/3Ddata/"+subject+"/"+fle+".npy"
  xx=np.load(x3d)
  if(subject=='S7'):
   if("Walking 1" in fle):
    xx=xx[:3636,:,:]
   elif("Walking 2" in fle):
    xx=xx[:3623,:,:]
  rgb=np.load(rgbpath)
  
  rst=np.concatenate((xx,rgb),axis=1)
  np.save(("/media/wanghao/TOSHIBA EXT/RGBdataset/mergeddata/"+subject+"/"+fle+".npy"),rst)
  
  cnt+=1
  print("save",subject,fle,rst.shape,"  ",cnt,"/",4*len(subjectlist))



