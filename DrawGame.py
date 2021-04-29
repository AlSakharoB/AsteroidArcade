from PIL import Image
import sdl2.ext

lifebar = Image.open("images\\LifeBar.png")

WHITE = sdl2.ext.Color(255, 255, 255)
BLACK = sdl2.ext.Color(0, 0, 0)
EX_GREY = sdl2.ext.Color(128, 128, 128)


def DrawLifeBar(renderer):
    for x in range(260):
        for y in range(37):
            color, hz = lifebar.getpixel((x, y))
            if hz != 0:
                if color == 158:
                    renderer.draw_point([7 + x, 8 + y], EX_GREY)
                elif color == 255:
                    renderer.draw_point([7 + x, 8 + y], WHITE)
                else:
                    renderer.draw_point([7 + x, 8 + y], BLACK)
