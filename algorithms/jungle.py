__author__ = 'ggdhines'
import aggregation_api
import cv2
import numpy as np
import matplotlib.pyplot as plt


# project = aggregation_api.AggregationAPI(153,"development")
# f_name = project.__image_setup__(1125393)
f_name = "/home/ggdhines/Databases/images/e1d11279-e515-42f4-a4d9-8e8a40a28425.jpeg"
def analyze(f_name,display=False):
    image = cv2.imread(f_name)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # image2 = cv2.threshold(image,127,255,cv2.THRESH_BINARY)

    # cv2.imwrite("/home/ggdhines/jungle.jpeg",gray_image)

    # print gray_image.ravel()
    ix = np.in1d(gray_image.ravel(),range(175)).reshape(gray_image.shape)
    x,y = np.where(ix)

    if display:
        plt.plot(y,x,".")
        plt.ylim((gray_image.shape[0],0))
        plt.show()

    n, bins, patches = plt.hist(y,range(min(y),max(y)+1))
    med = np.median(n)


    peaks = [i for i,count in enumerate(n) if count > 2*med]
    buckets = [[peaks[0]]]




    for j,p in list(enumerate(peaks))[1:]:
        if (p-1) != (peaks[j-1]):
            buckets.append([p])
        else:
            buckets[-1].append(p)

    bucket_items = list(enumerate(buckets))
    bucket_items.sort(key = lambda x:len(x[1]),reverse=True)

    a = bucket_items[0][0]
    b = bucket_items[1][0]


    vert = []
    for x,p in bucket_items:
        if (a <= x <= b) or (b <= x <= a):
            vert.extend(p)

    print vert
    print min(vert)
    print max(vert)

    if display:
        plt.plot((min(y),max(y)+1),(2*med,2*med))
        plt.show()

        n, bins, patches = plt.hist(x,range(min(x),max(x)+1))
        med = np.median(n)

        plt.plot((min(x),max(x)+1),(2*med,2*med))
        plt.plot((min(x),max(x)+1),(1*med,1*med),color="red")
        plt.xlim((0,max(x)+1))
        plt.show()
