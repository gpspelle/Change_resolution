import cv2
import os
import argparse
import sys

def change_res(path, width, height):
    fps = int(round((cv2.VideoCapture(path)).get(cv2.CAP_PROP_FPS)))
    os.rename(path, path[:-4] + '_old_' + '.avi')
    out = cv2.VideoWriter(path, cv2.VideoWriter_fourcc('X','V','I','D'), fps, (width, height))

    path = path[:-4] + '_old_' + '.avi'

    cap = cv2.VideoCapture(path)

    while cap.isOpened():
        sucess, frame = cap.read()
        if sucess == False:
            break
     
        resize = cv2.resize(frame, (width, height), cv2.INTER_CUBIC)
        out.write(resize)

    cap.release()
    out.release()
    os.rename(path, 'trash.avi')
    cv2.destroyAllWindows()

argp = argparse.ArgumentParser(description='Change video resolution')
argp.add_argument("-path", dest='path', type=str, nargs=1, required=True,
                 help='Usage: -path <path_to_video>')
argp.add_argument("-res", dest='res', type=int, nargs=2, required=True,
                 help='Usage: -res <x_res> <y_res>')

try:
    args = argp.parse_args()
except:
    argp.print_help(sys.stderr)
    exit(1)
change_res(args.path[0], args.res[0], args.res[1])
