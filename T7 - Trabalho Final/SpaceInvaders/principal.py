import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


vertices = (
    ( 0, 1, 0),
    (-1,-1,-1),
    (-1,-1, 1),
    ( 1,-1, 1),
    ( 1,-1,-1)
    )
 
linhas = (
    (0,1),
    (0,2),
    (0,3),
    (0,4),
    (1,2),
    (1,4),
    (2,3),
    (3,4)
    )
 
faces = (
    (0,1,2),
    (0,2,3),
    (0,3,4),
    (0,4,1),
    (1,2,4),
    (2,3,4)
    )

def Nave():
    glLineWidth(5)
    glBegin(GL_LINES)
    for linha in linhas:
        for vertex in linha :
            glVertex3fv(vertices[vertex])
    glEnd()

def main():
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50)

    glTranslatef(0, 0, -5)

    clock = pygame.time.Clock()
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotatef(2, 1, 1, 3)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        Nave()
        pygame.display.flip()

main()