import cv2
import os
import argparse

def change_res(path, width, height):
    fps = int(round((cv2.VideoCapture(path)).get(cv2.CAP_PROP_FPS)))
    os.rename(path, 'old_res_' + path)
    out = cv2.VideoWriter(path, cv2.VideoWriter_fourcc('M','J','P','G'), fps, (width, height))

    path = 'old_res_' + path
    cap = cv2.VideoCapture(path)

    while cap.isOpened():
        sucess, frame = cap.read()
        if sucess == False:
            break
     
        resize = cv2.resize(frame, (width, height))

        out.write(resize)

    cap.release()
    out.release()
    cv2.destroyAllWindows()

argp = argparse.ArgumentParser(description='Change video resolution')
argp.add_argument("-path", dest='path', type=str, nargs=1, required=True,
                 help='Usage: -path <path_to_video>')
argp.add_argument("-res", dest='res', type=int, nargs=2, required=True,
                 help='Usage: -res <x_res> <y_res>')

args = argp.parse_args()
change_res(args.path[0], args.res[0], args.res[1])
