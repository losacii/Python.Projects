# coding:utf-8
''' 测试微信模块 '''
# from a_pack import pyWechat
# pyWechat.sendMsg("hi, this is a testing message 2!", u'losacii')


import cv2

def ajustImage():

    def func(x):
        print ("nothing...")


    cv2.namedWindow('result')

    cv2.createTrackbar('X', 'result', 0, 255, func)
    cv2.createTrackbar('Y', 'result', 0, 255, func)

    img = cv2.imread("img/tmp.jpg")
    x = 127
    y = 255
    _ret, thresh = cv2.threshold(img, x, y, cv2.THRESH_TRUNC)

    while True:
        cv2.imshow("result", thresh)

        if cv2.waitKey(33) & 0xff == 27:
            break

        x = cv2.getTrackbarPos('X', 'result')
        y = cv2.getTrackbarPos('Y', 'result')
        _ret, thresh = cv2.threshold(img, x, y, cv2.THRESH_BINARY)

def processImages():
    import cv2
    import os
    '''
    img = cv2.imread("img/tmp.jpg")
    _ret, thresh = cv2.threshold(img, 198, 255, cv2.THRESH_TRUNC)

    cv2.imwrite("")
    '''
    imgDir = "./"
    imgs = os.listdir(imgDir)

    for i in imgs:

        if i.endswith(".jpg") or i.endswith(".png"):

            fp = os.path.join(imgDir, i)

            img = cv2.imread(fp, cv2.IMREAD_GRAYSCALE)

            _ret, thresh = cv2.threshold(img, 200, 255, cv2.THRESH_BINARY)


            sp = os.path.join(imgDir, 'xrz_' + i)
            cv2.imwrite(sp, thresh)
            print(sp, "saved")
            cv2.waitKey(400)

    cv2.destroyAllWindows()
    print ("Done")
    cv2.waitKey(2500)
            



if __name__ == '__main__':
    processImages()





