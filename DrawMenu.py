from PIL import Image
import sdl2.ext

WHITE = sdl2.ext.Color(255, 255, 255)
EX_GREY = sdl2.ext.Color(165, 165, 165)
BLACK = sdl2.ext.Color(0, 0, 0)

img1 = Image.open("images\\StartButton.png")
img2 = Image.open("images\\Start.png")
img3 = Image.open("images\\copyrights.png")
img4 = Image.open("images\\SkinButton.png")
img5 = Image.open("images\\RuleButton.png")


def DrawCopyrights(renderer):
    for x in range(400):
        for y in range(26):
            tr_, hz = img3.getpixel((x, y))
            if hz == 255:
                renderer.draw_point([100 + x, 720 + y], EX_GREY)


def DrawPlayButton(renderer):
    for x in range(360):
        for y in range(220):
            red, green, blue, hz = img1.getpixel((x, y))
            if hz == 255:
                renderer.draw_point([110 + x, 280 + y], WHITE)


def StartGamePic(renderer):
    for x in range(545):
        for y in range(83):
            hz = img2.getpixel((x, y))
            if hz == 0:
                renderer.draw_point([30 + x, 183 + y], BLACK)
            else:
                renderer.draw_point([30 + x, 183 + y], WHITE)


def DrawSkinButton(renderer):
    for x in range(191):
        for y in range(94):
            tr_, hz = img4.getpixel((x, y))
            if hz == 255:
                renderer.draw_point([105 + x, 500 + y], WHITE)


def DrawRuleButton(renderer):
    for x in range(191):
        for y in range(94):
            red, green, blue, hz = img5.getpixel((x, y))
            if hz == 255:
                renderer.draw_point([305 + x, 500 + y], WHITE)
