import numpy as np



#filename=["Walking.54138969","Walking.55011271","Walking.58860488","Walking.60457274","Walking 1.54138969","Walking 1.55011271","Walking 1.58860488","Walking 1.60457274"]
#subjectlist=["S1","S5","S6","S8","S9","S11"]

filename=["Walking 1.54138969","Walking 1.55011271","Walking 1.58860488","Walking 1.60457274","Walking 2.54138969","Walking 2.55011271","Walking 2.58860488","Walking 2.60457274"]
subjectlist=["S7"]

'''
tmp=[]
cnt=0
for subject in subjectlist:
  for i,fle in enumerate(filename):
   
   pth="/media/wanghao/TOSHIBA EXT/RGBdataset/mergeddata/"+subject+"/"+fle+".npy"
   tmp.append(list(np.load(pth)))
   if i==3:
    np.save(("/media/wanghao/TOSHIBA EXT/RGBdataset/mydataset/"+subject+"/Walking 1.npy"),tmp)
    tmp=[]
   if i==7:
    np.save(("/media/wanghao/TOSHIBA EXT/RGBdataset/mydataset/"+subject+"/Walking 2.npy"),tmp)
    tmp=[]
   cnt+=1
   print(cnt)
'''

positions_3d={'S1':{'Walking':np.load("/media/wanghao/TOSHIBA EXT/RGBdataset/mydataset/S1/Walking.npy"),'Walking 1':np.load("/media/wanghao/TOSHIBA EXT/RGBdataset/mydataset/S1/Walking 1.npy")},'S5':{'Walking':np.load("/media/wanghao/TOSHIBA EXT/RGBdataset/mydataset/S5/Walking.npy"),'Walking 1':np.load("/media/wanghao/TOSHIBA EXT/RGBdataset/mydataset/S5/Walking 1.npy")},'S6':{'Walking':np.load("/media/wanghao/TOSHIBA EXT/RGBdataset/mydataset/S6/Walking.npy"),'Walking 1':np.load("/media/wanghao/TOSHIBA EXT/RGBdataset/mydataset/S6/Walking 1.npy")},'S7':{'Walking 1':np.load("/media/wanghao/TOSHIBA EXT/RGBdataset/mydataset/S7/Walking 1.npy"),'Walking 2':np.load("/media/wanghao/TOSHIBA EXT/RGBdataset/mydataset/S7/Walking 2.npy")},'S8':{'Walking':np.load("/media/wanghao/TOSHIBA EXT/RGBdataset/mydataset/S8/Walking.npy"),'Walking 1':np.load("/media/wanghao/TOSHIBA EXT/RGBdataset/mydataset/S8/Walking 1.npy")},'S9':{'Walking':np.load("/media/wanghao/TOSHIBA EXT/RGBdataset/mydataset/S9/Walking.npy"),'Walking 1':np.load("/media/wanghao/TOSHIBA EXT/RGBdataset/mydataset/S9/Walking 1.npy")},'S11':{'Walking':np.load("/media/wanghao/TOSHIBA EXT/RGBdataset/mydataset/S11/Walking.npy"),'Walking 1':np.load("/media/wanghao/TOSHIBA EXT/RGBdataset/mydataset/S11/Walking 1.npy")}}

np.save('positions_3d.npy',positions_3d)

