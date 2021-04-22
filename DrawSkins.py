from PIL import Image
import sdl2.ext

tick = Image.open("images\\Tick.png")
chosetxt = Image.open("images\\Chosetxt.png")

WHITE = sdl2.ext.Color(255, 255, 255)
BLACK = sdl2.ext.Color(0, 0, 0)

YANTARNIJ = sdl2.ext.Color(245, 230, 191)
SALAT = sdl2.ext.Color(190, 245, 116)
AQUA = sdl2.ext.Color(0, 255, 255)
DARK_EMERALD = sdl2.ext.Color(38, 153, 128)
RED = sdl2.ext.Color(244, 83, 41)
GOLD = sdl2.ext.Color(245, 218, 42)
PINK = sdl2.ext.Color(255, 51, 255)
ORANGE = sdl2.ext.Color(255, 153, 51)


def DrawChoseText(renderer):
    for x in range(550):
        for y in range(64):
            red, green, blue, hz = chosetxt.getpixel((x, y))
            if red == 0 and green == 0 and blue == 0 and hz == 255:
                renderer.draw_point([25 + x, 20 + y], WHITE)


def DrawColorsSkins(renderer, skin):
    renderer.fill([50, 140, 88, 88], RED)
    renderer.fill([188, 140, 88, 88], ORANGE)
    renderer.fill([326, 140, 88, 88], GOLD)
    renderer.fill([464, 140, 88, 88], YANTARNIJ)
    renderer.fill([50, 278, 88, 88], DARK_EMERALD)
    renderer.fill([188, 278, 88, 88], SALAT)
    renderer.fill([326, 278, 88, 88], AQUA)
    renderer.fill([464, 278, 88, 88], PINK)
    CheckTick(skin, renderer)


def CheckTick(skin, renderer):
    if skin == RED:
        DrawTick(renderer, 50, 140)
    elif skin == ORANGE:
        DrawTick(renderer, 188, 140)
    elif skin == GOLD:
        DrawTick(renderer, 326, 140)
    elif skin == YANTARNIJ:
        DrawTick(renderer, 464, 140)
    elif skin == DARK_EMERALD:
        DrawTick(renderer, 50, 278)
    elif skin == SALAT:
        DrawTick(renderer, 188, 278)
    elif skin == AQUA:
        DrawTick(renderer, 326, 278)
    elif skin == PINK:
        DrawTick(renderer, 464, 278)


def DrawTick(renderer, x1, y1):
    for x in range(32):
        for y in range(32):
            red, green, blue, hz = tick.getpixel((x, y))
            if hz == 255:
                renderer.draw_point([28 + x1 + x, 28 + y1 + y], BLACK)
