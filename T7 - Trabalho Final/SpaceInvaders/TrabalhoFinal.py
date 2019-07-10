from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import png
from math import *
from random import *
from numpy import *

idtiro = 0
translate = 0
bolotas = []
descerCubo = 7
destruir1 = 0
destruir2 = 0
destruir3 = 0
destruir4 = 0
destruirTodos = 0

vertices = (
    ( 0, 1, 0),  #0
    (-1,-1,-1),  #1
    ( 1,-1,-1),  #2
    ( 1,-1, 1),  #3
    (-1,-1, 1)   #4
    )
 
verticesCubo = (
    ( 1,-1,-1),
    ( 1, 1,-1),
    (-1, 1,-1),
    (-1,-1,-1),
    ( 1,-1, 1),
    ( 1, 1, 1),
    (-1,-1, 1),
    (-1, 1, 1),
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

linhasCubo = (
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,7),
    (6,3),
    (6,4),
    (6,7),
    (5,1),
    (5,4),
    (5,7),
    )

faces = (
    (0,1,2),
    (0,2,3),
    (0,3,4),
    (0,4,1),
    (1,2,4),
    (2,3,4)
    )

facesCubo = (
    (0,1,2,3),
    (3,2,7,6),
    (6,7,5,4),
    (4,5,1,0),
    (1,5,7,2),
    (4,0,3,6)
    )

cor = ((1,0,0),(0.5,0.5,0),(0.1,0.1,0.1),(0.5,0.5,0),(1,0,1))
coresCubo = ( (1,0,0),(1,1,0),(0,1,0),(0,1,1),(0,0,1),(1,0,1),(0.5,1,1),(1,0,0.5) )

teta0 = (-math.pi)/2
tetaF = (math.pi)/2
phi0 = 0
phiF = 2*math.pi
r = 0.3
dphi = math.pi/3
dteta = math.pi/3

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

def Cubo():
    glBegin(GL_QUADS)
    i = 0
    for face in facesCubo:
        glColor3fv(coresCubo[i])
        for vertex in face:
            #glColor3fv(cores[vertex])
            glVertex3fv(verticesCubo[vertex])
        i = i+1
    glEnd()
 
    glColor3fv((0,0.5,0))
    glBegin(GL_LINES)
    for linha in linhasCubo:
        for vertice in linha:
            glVertex3fv(verticesCubo[vertice])
    glEnd()

def desenha():
    global dy
    global estado
    global bolotas
    global descerCubo
    global miraTiro
    global destruir1
    global destruir2
    global destruir3
    global destruir4
    global destruirTodos
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glPushMatrix()
    glTranslatef(translate, -7.0, -8)
    Nave()
    glPopMatrix()
    glPushMatrix()
    glTranslatef(-12, descerCubo, -8)
    if(destruir1 == 0):
         Cubo()
    glPopMatrix()
    glPushMatrix()
    glTranslatef(-4, descerCubo, -8)
    if(destruir2 == 0):
         Cubo()
    glPopMatrix()
    glPushMatrix()
    glTranslatef(4, descerCubo, -8)
    if(destruir3 == 0):
         Cubo()
    glPopMatrix()
    glPushMatrix()
    glTranslatef(12, descerCubo, -8)
    if(destruir4 == 0):
         Cubo()
    glPopMatrix()
    copiaBolotas = []
    for bolota in bolotas:
        glPushMatrix()
        glTranslatef(bolota[0], -5.5 + bolota[1], -8)
        if((bolota[0] == -12) and (bolota[1] - 5.5 > descerCubo)):
            destruir1 += 1
        if((bolota[0] == -4) and (bolota[1] - 5.5 > descerCubo)):
            destruir2 += 1
        if((bolota[0] == 4) and (bolota[1] - 5.5 > descerCubo)):
            destruir3 += 1
        if((bolota[0] == 12) and (bolota[1] - 5.5 > descerCubo)):
            destruir4 += 1
        Tiro()
        glPopMatrix()
        if(bolota[1] < 13):
            copiaBolotas.append((bolota[0],bolota[1]+0.5))
        if(bolota[1] == descerCubo):
            copiaBolotas.append((bolota[0],bolota[1]+0.5))
    bolotas = copiaBolotas
    if(destruir1 == 1):
        destruirTodos += 1
    if(destruir2 == 1):
        destruirTodos += 1
    if(destruir3 == 1):
        destruirTodos += 1
    if(destruir4 == 1):
        destruirTodos += 1
    if(destruirTodos == 4):
            print("Você Venceu!")
            sys.exit()
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
            glColor3fv((0.8,0.6,0.5))
            glVertex3fv(P)
            glVertex3fv(Q)
            glVertex3fv(R)
            glColor3fv((1,0.5,0.2))
            glVertex3fv(S)
            glVertex3fv(R)
            glVertex3fv(Q)


            phi += dphi
        teta += dteta
    glEnd()

def timer(i):
    global descerCubo
    glutPostRedisplay()
    glutTimerFunc(50,timer,1)
    descerCubo -= 0.05
    if(descerCubo < -7):
        print("Você Perdeu!")
        sys.exit()

def keyPressed(tecla, x, y):
    global bolotas, translate
    if tecla == b' ':
        print("Tiro")
        bolotas.append((translate, 0))

def teclaEspecialPressionada(tecla, x, y):
    global translate
    if tecla == GLUT_KEY_LEFT:
        print("ESQUERDA")
        translate -= 0.5

    elif tecla == GLUT_KEY_RIGHT:
        print("DIREITA")
        translate += 0.5

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