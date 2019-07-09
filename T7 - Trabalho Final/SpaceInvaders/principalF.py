from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import png
from math import *
from random import *
from numpy import *

translate = 0
estado = 0
dy = 0 

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

cor = ((1,0,0),(0,1,0),(0,1,1),(0,0,1),(1,0,1))

teta0 = (-math.pi)/2
tetaF = (math.pi)/2
phi0 = 0
phiF = 2*math.pi
r = 1
dphi = math.pi/10
dteta = math.pi/10

def Px(teta):
    return r*cos(teta)

def Py(teta):
    return r*sin(teta)

def Qx(r2, phi):
    return r2*cos(phi)

def Qz(r2, phi):
    return r2*sin(phi)

def Nave():
    glBegin(GL_TRIANGLES)
    i = 0
    for face in faces:
        glColor3fv(cor[i%5])
        for vertex in face:
            glVertex3fv(vertices[vertex])
        i = i+1
    glEnd()

def desenha():
    global dy
    global estado
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glPushMatrix()
    glTranslatef(translate, -7.0, -8)
    Nave()
    glPopMatrix()
    if(estado == 1):
        glPushMatrix()
        glTranslatef(translate, -5.0 + dy, -8)
        dy += 0.5
        if(dy >= 12):
            dy = 0
            estado = 0

        Tiro()
        glPopMatrix()
    glutSwapBuffers()

def Tiro():
    teta = teta0
    phi = phi0
    glBegin(GL_TRIANGLES)
    while(tetaF > teta):
        #glVertex3f(Px(teta), Py(teta), 0)
        phi = phi0
        while(phiF > phi):
            
            P = (Qx(Px(teta), phi), Py(teta), Qz(Px(teta), phi))
            Q = (Qx(Px(teta), phi + dphi), Py(teta), Qz(Px(teta), phi + dphi))
            R = (Qx(Px(teta + dteta), phi), Py(teta + dteta), Qz(Px(teta + dteta), phi))
            S = (Qx(Px(teta + dteta), phi + dphi), Py(teta + dteta), Qz(Px(teta + dteta), phi + dphi))
            glColor3fv((1,1,1))
            glVertex3fv(P)
            glVertex3fv(Q)
            glVertex3fv(R)
            glColor3fv((1,0,0))
            glVertex3fv(S)
            glVertex3fv(R)
            glVertex3fv(Q)


            phi += dphi
        teta += dteta
    glEnd()

def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50,timer,1)

def keyPressed(tecla, x, y):
    global estado
    if tecla == b' ':
        print("Tiro")
        estado = 1

def teclaEspecialPressionada(tecla, x, y):
    global translate
    if tecla == GLUT_KEY_LEFT:
        print("ESQUERDA")
        translate -= 0.2

    elif tecla == GLUT_KEY_RIGHT:
        print("DIREITA")
        translate += 0.2

def main():

    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
    glutInitWindowSize(1000,600)
    glutCreateWindow("Space Invaders")
    glutDisplayFunc(desenha)
    glEnable(GL_MULTISAMPLE)
    glEnable(GL_DEPTH_TEST)
    glClearColor(0.,0.,0.,1.)
    gluPerspective(100, 1000.0/600.0, 0.1, 50.0)
    glutTimerFunc(50,timer,1)
    glutSpecialFunc(teclaEspecialPressionada)
    glutKeyboardFunc(keyPressed)
    glutMainLoop()

main()