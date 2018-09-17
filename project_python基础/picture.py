from PIL import Image
from PIL import ImageFilter
im=Image.open("E:\\TencentTIM\\文件\\MobileFile\\-30094ff1b416ad8d.jpg")
"""r,g,b=im.split()
newg=g.point(lambda i:i*0.9)
newb=b.point(lambda i:i<100)
om=Image.merge(im.mode,(r,newg,newb))
om.save("E:\\TencentTIM\\文件\\MobileFile\\newP1.jpg")"""
# 此过程为去掉图片光线

"""
om=im.filter(ImageFilter.CONTOUR)
om.save("E:\\TencentTIM\\文件\\MobileFile\\newP4.jpg")
"""
#此过程为获取图片轮廓