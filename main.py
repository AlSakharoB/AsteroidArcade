import sys
from sdl2.ext import SOFTWARE
import sdl2.ext
import ctypes
from random import randint
import DrawMenu as d
import DrawSkins as s
import DrawGame as g
import Prints as p

WHITE = sdl2.ext.Color(255, 255, 255)

YANTARNIJ = sdl2.ext.Color(245, 230, 191)
GOLD = sdl2.ext.Color(245, 218, 42)

ORANGE = sdl2.ext.Color(255, 153, 51)

RED = sdl2.ext.Color(244, 83, 41)

PINK = sdl2.ext.Color(255, 51, 255)

SALAT = sdl2.ext.Color(190, 245, 116)
SHARTREZ = sdl2.ext.Color(127, 255, 0)
EZ_GREEN = sdl2.ext.Color(154, 244, 102)
DARK_EMERALD = sdl2.ext.Color(38, 153, 128)

DARK_GREY = sdl2.ext.Color(80, 80, 80)
EX_GREY = sdl2.ext.Color(128, 128, 128)
EX_BLACK = sdl2.ext.Color(35, 35, 35)
BLACK = sdl2.ext.Color(0, 0, 0)
BROWN = sdl2.ext.Color(143, 71, 36)

AQUA = sdl2.ext.Color(0, 255, 255)

sdl2.ext.init()

skin = YANTARNIJ


class Velocity(object):
    def __init__(self):
        super(Velocity, self).__init__()
        self.vx = 0
        self.vy = 0


class MovementSystem(sdl2.ext.Applicator):
    def __init__(self, minx, miny, maxx, maxy):
        super(MovementSystem, self).__init__()
        self.componenttypes = (Velocity, sdl2.ext.Sprite)
        self.minx = minx
        self.miny = miny
        self.maxx = maxx
        self.maxy = maxy

    def process(self, world, componentsets):
        for velocity, sprite in componentsets:
            swidth, sheight = sprite.size
            sprite.x += velocity.vx
            sprite.y += velocity.vy

            sprite.x = max(self.minx, sprite.x)
            sprite.y = max(self.miny, sprite.y)

            pmaxx = sprite.x + swidth
            pmaxy = sprite.y + sheight
            if pmaxx > self.maxx:
                sprite.x = self.maxx - swidth
            if pmaxy > self.maxy:
                sprite.y = self.maxy - sheight


class TextureRenderSystem(sdl2.ext.TextureSpriteRenderSystem):
    def __init__(self, renderer):
        super(TextureRenderSystem, self).__init__(renderer)
        self.renderer = renderer

    def render(self, components):
        self.renderer.color = BLACK
        super(TextureRenderSystem, self).render(components)


class Player(sdl2.ext.Entity):
    def __init__(self, world, sprite, posx=0, posy=0):
        self.sprite = sprite
        self.sprite.position = posx, posy
        self.velocity = Velocity()


class Asteroids(sdl2.ext.Entity):
    def __init__(self, world, sprite):
        self.sprite = sprite
        x, y = randint(0, 560), 43
        self.sprite.position = x, y
        self.velocity = Velocity()


class CollisionSystem(sdl2.ext.Applicator):
    def __init__(self, player):
        super(CollisionSystem, self).__init__()
        self.componenttypes = Velocity, sdl2.ext.Sprite
        self.player = player
        self.cont = True

    def check(self, item):
        sprite = item[1]
        left, top, right, bottom = self.player.sprite.area
        bleft, btop, bright, bbottom = sprite.area
        return (left != bleft and right != bright and top != btop)

    def check_collision(self, sprite):
        left, top, right, bottom = self.player.sprite.area
        bleft, btop, bright, bbottom = sprite.area
        return (top <= bbottom and right >= bleft and bbottom <= bottom and left <= bright) or \
               (bottom >= btop and bottom <= bbottom and right >= bleft and left <= bright)

    def process(self, world, components):
        self.cont = True
        collitems = [comp for comp in components if self.check(comp)]
        if len(collitems) != 0:
            for velocity, sprite in collitems:
                if self.check_collision(sprite):
                    self.cont = False
                    break


class Ticks:
    def __init__(self):
        self.startticks = 0


class LifeBar:
    def __init__(self):
        self.hp = 100


class Score:
    def __init__(self):
        self.score = 0


def Deletion(list, score):
    for i in range(len(list)):
        x, y = list[i].sprite.position
        if y > 800:
            score.score += list[i].velocity.vy * 5
            list[i].delete()
            list.pop(i)
            break


def Asteroids_(time):
    if time <= 10:
        return 5
    elif time <= 50:
        return 4
    elif time <= 100:
        return 3
    elif time <= 160:
        return 2
    else:
        return 1


class GameProcess:
    def __init__(self, window, renderer, factory, ticks_, score):
        global skin

        renderer.clear()

        world = sdl2.ext.World()
        movement = MovementSystem(0, 0, 600, 1000)

        player_sprite = factory.from_color(skin, size=(25, 25))
        player = Player(world, player_sprite, 288, 600)

        collision = CollisionSystem(player)
        spriterenderer = TextureRenderSystem(renderer)

        world.add_system(movement)
        world.add_system(spriterenderer)
        world.add_system(collision)

        running = True
        minspeed, maxspeed = 3, 5

        asteroids_ = []

        life = LifeBar()
        renderer.fill([14, 14, 25, 20], skin)
        g.DrawLifeBar(renderer)

        while running:
            renderer.fill([0, 43, 800, 757], BLACK)
            renderer.fill([59, 20, 200, 15], BLACK)
            renderer.fill([59, 20, life.hp * 2, 15], skin)
            renderer.fill([59, 20, 5, 5], EX_GREY)

            Deletion(asteroids_, score)

            if not collision.cont and life.hp > 0:
                life.hp -= 1
                if life.hp <= 0:
                    running = False

            game_ticks = sdl2.timer.SDL_GetTicks() - ticks_.startticks
            score.score += game_ticks // 5000
            gap = Asteroids_(round(game_ticks / 1000, 1))
            time = round(game_ticks / 1000, 1)

            if time >= 200:
                minspeed, maxspeed = 6, 9
            elif gap <= 3:
                minspeed, maxspeed = 4, 7
            if time != 0.0 and (time % gap == 0.0) or (time % gap == 0.5):
                size = randint(10, 40)
                aster = factory.from_color(WHITE, size=(size, size))
                asteroid = Asteroids(world, aster)
                asteroids_.append(asteroid)
                asteroid.velocity.vy = randint(minspeed, maxspeed)
            for event in sdl2.ext.get_events():
                if event.type == sdl2.SDL_QUIT:
                    running = False
                    break
                if event.type == sdl2.SDL_KEYDOWN:
                    if event.key.keysym.sym == sdl2.SDLK_a:
                        player.velocity.vx = -4
                    elif event.key.keysym.sym == sdl2.SDLK_d:
                        player.velocity.vx = 4
                elif event.type == sdl2.SDL_KEYUP:
                    if event.key.keysym.sym in (sdl2.SDLK_a, sdl2.SDLK_d):
                        player.velocity.vx = 0
            window.refresh()
            sdl2.SDL_Delay(10)
            world.process()
        renderer.clear()


class Skins:
    def __init__(self, window, renderer):
        global skin

        renderer.clear()
        skin_ = sdl2.ext.World()

        running = True
        s.DrawChoseText(renderer)
        s.DrawButtonMainMenu(renderer)

        while running:
            s.DrawColorsSkins(renderer, skin)
            for event in sdl2.ext.get_events():
                x, y = ctypes.c_int(0), ctypes.c_int(0)
                if event.type == sdl2.SDL_QUIT:
                    running = False
                    break
                if event.type == sdl2.SDL_MOUSEBUTTONUP:
                    state = sdl2.mouse.SDL_GetMouseState(ctypes.byref(x), ctypes.byref(y))
                    if 28 <= x.value <= 203 and 728 <= y.value <= 784:
                        running = False
                        break
                    elif 50 <= x.value <= 138 and 140 <= y.value <= 228:
                        skin = RED
                    elif 188 <= x.value <= 276 and 140 <= y.value <= 228:
                        skin = ORANGE
                    elif 326 <= x.value <= 414 and 140 <= y.value <= 228:
                        skin = GOLD
                    elif 464 <= x.value <= 552 and 140 <= y.value <= 228:
                        skin = YANTARNIJ
                    elif 50 <= x.value <= 138 and 278 <= y.value <= 366:
                        skin = DARK_EMERALD
                    elif 188 <= x.value <= 276 and 278 <= y.value <= 366:
                        skin = SALAT
                    elif 326 <= x.value <= 414 and 278 <= y.value <= 366:
                        skin = AQUA
                    elif 464 <= x.value <= 552 and 278 <= y.value <= 366:
                        skin = PINK
            window.refresh()
            skin_.process()
            renderer.present()
        renderer.clear()


def run():
    window = sdl2.ext.Window("Asteroid Crash", size=(600, 800))
    window.show()

    menu = sdl2.ext.World()

    renderer = sdl2.ext.Renderer(window)
    factory = sdl2.ext.SpriteFactory(sdl2.ext.TEXTURE, renderer=renderer)

    ticks_ = Ticks()

    d.Manu(renderer)

    running = True
    while running:
        for event in sdl2.ext.get_events():
            x, y = ctypes.c_int(0), ctypes.c_int(0)
            if event.type == sdl2.SDL_QUIT:
                running = False
                break
            if event.type == sdl2.SDL_MOUSEBUTTONUP:
                state = sdl2.mouse.SDL_GetMouseState(ctypes.byref(x), ctypes.byref(y))
                if 155 <= x.value <= 440 and 325 <= y.value <= 460:
                    score = Score()
                    ticks_.startticks = sdl2.timer.SDL_GetTicks()
                    GameProcess(window, renderer, factory, ticks_, score)
                    p.PrintScore(score.score)
                    d.Manu(renderer)
                elif 115 <= x.value <= 295 and 510 <= y.value <= 590:
                    Skins(window, renderer)
                    d.Manu(renderer)
                elif 305 <= x.value <= 485 and 510 <= y.value <= 590:
                    p.PrintRules()
        renderer.present()
        window.refresh()
        menu.process()


if __name__ == "__main__":
    sys.exit(run())
