import cv2
import os
filename=["Walking 1.54138969","Walking 1.55011271","Walking 1.58860488","Walking 1.60457274","Walking 2.54138969","Walking 2.55011271","Walking 2.58860488","Walking 2.60457274"]

def video2img(video_path, frame_save_dir):
    cap = cv2.VideoCapture(video_path)
    suc = cap.isOpened()
    frame_count = 0
    while suc:
        suc, frame = cap.read()  # suc是bool变量，用于判断视频帧是否存在
        frame_count += 1
        if suc:
            save_path = os.path.join(frame_save_dir, "{:04d}.jpg".format(frame_count))  # 格式化命名，不足补零
            cv2.imwrite(save_path, frame)
            print(frame_count, suc)
    cap.release()


if __name__ == "__main__":
 for fle in filename:
    video_path = "./H36m_video/Walking/S7/Videos/"+fle+".mp4"
    frame_save_dir = "./Imgdata/S7/"+fle+"/"  # 需要预先创立该文件夹
    video2img(video_path, frame_save_dir)
