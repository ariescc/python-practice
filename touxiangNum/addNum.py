from PIL import ImageDraw, ImageFont, ImageColor, Image


def add_num(img):
    # 创建一个draw对象
    draw = ImageDraw.Draw(img)

    # 创建一个font
    myfont = ImageFont.truetype('C:/windows/fonts/Arial.ttf', size=40)
    fillcolor = ImageColor.colormap.get('red')
    width, height = img.size
    draw.text((width-50, 0), '1', font=myfont, fill=fillcolor)
    img.save('result.jpg', 'jpeg')
    return 0

if __name__ == '__main__':
    image = Image.open('touxiang.jpg')
    add_num(image)
