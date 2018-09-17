from PIL import Image

ascii_char=list("@B%8&WM#*oahkbdpqwmasdfghjklzzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,")
def get_char(r,g,b,alpha=256):
    if alpha==0:
        return ''
    gray=int(0.2123*r+0.7152*g+0.0722*b)
    unit=256/len(ascii_char)
    return ascii_char[int(gray//unit)]

def main():
    im=Image.open("E:\\TencentTIM\\文件\\MobileFile\\newP2.jpg")
    WIDTH,HEIGTH=108,144
    im=im.resize((WIDTH,HEIGTH))
    txt=""
    for i in range(HEIGTH):
        for j in range(WIDTH):
            txt+= get_char(*im.getpixel((j,i)))
        txt+= '\n'
    fo=open("E:\\TencentTIM\\文件\\MobileFile\\new_char.txt","w")
    fo.write(txt)
    fo.close()
main()
