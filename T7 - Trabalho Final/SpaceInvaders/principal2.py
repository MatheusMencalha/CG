import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import png

vertices = (
    ( 0, 1, 0),  #0
    (-1,-1,-1),  #1
    ( 1,-1,-1),  #2
    ( 1,-1, 1),  #3
    (-1,-1, 1)   #4
    )
 
linhas = (
    (0,1),
    (0,2),
    (0,3),
    (0,4),
    (1,2),
    (2,3),
    (3,4),
    (4,1)
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
    glBegin(GL_TRIANGLES)
    i = 0
    for face in faces:
        for vertex in face:
            glVertex3fv(vertices[vertex])
        i = i+1
    glEnd()

def main():
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50)

    glTranslatef(0, 0, -8)

    clock = pygame.time.Clock()
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotatef(2,1,3,0)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        Nave()
        pygame.display.flip()

main()