import os

filename=["Walking.54138969","Walking.55011271","Walking.58860488","Walking.60457274","Walking 1.54138969","Walking 1.55011271","Walking 1.58860488","Walking 1.60457274"]
subjectlist=["S1","S5","S6","S8","S9","S11"]


def getnum(x):
  if "54138969" in x: return "0"
  elif "55011271" in x: return "1"
  elif "58860488" in x: return "2"
  elif "60457274" in x: return "3"
  else: 
    return "xxxxx"

for subject in subjectlist:
  for fle in filename:
    string='python run.py -k cpn_ft_h36m_dbb -arc 3,3,3 -c checkpoint --evaluate epoch_200.bin --render --viz-subject '+ subject+' --viz-action Walking --viz-camera '+ getnum(fle) +'--viz-video "/media/wanghao/TOSHIBA/'+subject +'/Videos/'+fle+'.mp4" --viz-export "/media/wanghao/HD00/wanghao/3Ddata/'+subject+'/'+fle+'"'
    os.system(string)
