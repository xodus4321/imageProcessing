import cv2

##함수 선언부


##전역 변수부
src = None  #원본 이미지
dst1, dst2, dst3 = None, None, None  #영상처리한 결과


##메인 코드부
src = cv2.imread('c:/images/picture45.jpg')

dst1 = grayScale(src)
dst2 = cannyEdge(src)



cv2.imshow('Src', src) #화면출력
cv2.imshow('Dst1', dst1)
cv2.imshow('Dst2'', dst2)
##마무리
cv2.waitKey(0)
cv2.destoryAllWindows()
