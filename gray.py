import cv2

def  grayScale(src) :
    
    dst = cv2.cvtColar(src, cv2.COLOR_RGB2GRAY)

    return dst
