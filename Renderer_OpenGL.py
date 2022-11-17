from math import cos, radians, sin
from pickle import TRUE
import pygame
from pygame.locals import *
from gl import Model, Renderer
from shaders import *

width = 1060
height = 740

deltaTime = 0.0

pygame.init()

screen = pygame.display.set_mode((width, height), pygame.OPENGL | pygame.DOUBLEBUF)
clock = pygame.time.Clock()

rend = Renderer(screen)

# Pato
# bgPato = pygame.image.load('./Models/Background/lago.jpg').convert()
pato = Model("./Models/pato2.obj", "./Models/Skin/patoSkin.bmp")
pato.position.z -= 17
pato.scale.x = 0.5
pato.scale.y = 0.5
pato.scale.z = 0.5

# Beagel
beagel = Model("./Models/beagle1.obj", "./Models/Skin/beagleSkin.bmp")
beagel.position.z -= 17
beagel.scale.x = 0.5
beagel.scale.y = 0.5
beagel.scale.z = 0.5

# Delfin
delfin = Model("./Models/delfin.obj", "./Models/Skin/delfinSkin.bmp")
delfin.position.z -= 17
delfin.scale.x = 0.5
delfin.scale.y = 0.5
delfin.scale.z = 0.5

# Pajaro
pajaro = Model("./Models/pajaro.obj", "./Models/Skin/pajaroSkin.bmp")
pajaro.position.z -= 17
pajaro.scale.x = 0.5
pajaro.scale.y = 0.5
pajaro.scale.z = 0.5

# Tortuga
turtle = Model("./Models/turtle.obj", "./Models/Skin/turtleSkin.bmp")
turtle.position.z -= 17
turtle.scale.x = 0.5
turtle.scale.y = 0.5
turtle.scale.z = 0.5

# Default
rend.target.z = -17
rend.scene.append( turtle )
rend.setShaders(vertex_shader, fragment_shader)
model = 1

isRunning = True

while isRunning:

    keys = pygame.key.get_pressed()
    mouse = pygame.mouse.get_pressed()
    pointer = pygame.mouse.get_rel()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                isRunning = False

            elif event.key == pygame.K_z:
                rend.filledMode()
            elif event.key == pygame.K_x:
                rend.wireframeMode()
            elif event.key == pygame.K_1:
                rend.setShaders(still_shader, toon_shader)
            elif event.key == pygame.K_2:
                rend.setShaders(still_shader, funBlue_shader)
            elif event.key == pygame.K_3:
                rend.setShaders(vertex_shader, colorExplotion_shader)
            elif event.key == pygame.K_4:
                rend.setShaders(explote_shader, funBluee_shader)
            elif event.key == pygame.K_m:
                if model<=4:
                    model = model + 1
                elif model == 5:
                    model = 1

                if model == 1:
                    if pajaro in rend.scene:
                        rend.scene.remove(pajaro)
                    rend.scene.append( turtle )
                elif model == 2:
                    rend.scene.remove(turtle)
                    rend.scene.append( pato )
                elif model == 3:
                    rend.scene.remove(pato)
                    rend.scene.append( beagel )
                elif model == 4:
                    rend.scene.remove(beagel)
                    rend.scene.append( delfin )
                elif model == 5:
                    rend.scene.remove(delfin)
                    rend.scene.append( pajaro )

    # CAMARA
    # Zoom in
    if event.type == pygame.MOUSEWHEEL:
        # Limite de zoom
        if rend.camDistance >= 4.5 and rend.camDistance <= 10:
            rend.camDistance -= 2 * event.y * deltaTime
        elif rend.camDistance < 4.5:
            rend.camDistance = 4.5
        elif rend.camDistance > 10:
            rend.camDistance = 10

    # Izq
    rend.angle -= pointer[0] * deltaTime * 15

    # Arriba
    if rend.camPosition.y <= 2 and rend.camPosition.y >= -2:
        rend.camPosition.y += pointer[1] * deltaTime 
    elif rend.camPosition.y > 2:
        rend.camPosition.y = 2
    elif rend.camPosition.y < -2:
        rend.camPosition.y = 2

    rend.target.y = rend.camPosition.y

    rend.camPosition.x = rend.target.x + sin(radians(rend.angle)) * rend.camDistance
    rend.camPosition.z = rend.target.z + cos(radians(rend.angle)) * rend.camDistance
    
    if keys[K_LEFT]:
        rend.pointLight.x -= 10 * deltaTime
    elif keys[K_RIGHT]:
        rend.pointLight.x += 10 * deltaTime
    elif keys[K_UP]:
        rend.pointLight.y += 10 * deltaTime
    elif keys[K_DOWN]:
        rend.pointLight.y -= 10 * deltaTime


    deltaTime = clock.tick(60) / 1000
    rend.time += deltaTime

    rend.update()
    rend.render()
    pygame.display.flip()

pygame.quit()
