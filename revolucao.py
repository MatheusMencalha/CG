from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from math import *
import random
 
a = 4
b = 4
x0 = -2
y0 = -2
xf = 2
yf = 2
px = 100
py = 10


def desenho():
    dx = (xf - x0)/ px
    dy = (yf - y0)/ py 

    y = y0

    while(y < yf):
        x = x0
        glBegin(GL_QUAD_STRIP)
        glColor3fv((1,0.5, 0))
        while(x < xf):
            glVertex3f(x, y, f(x, y))
            glVertex3f(x , y + dy, f(x , y + dy))
            x += dx
        glEnd()
        y += dy

def desenho2():
    dx = (xf - x0)/ px
    dy = (yf - y0)/ py 

    y = y0

    while(y < yf):
        x = x0
        glBegin(GL_QUAD_STRIP)
        glColor3fv((0, 1,0.5))
        while(x < xf):
            glVertex3f(x, y, f2(x, y))
            glVertex3f(x , y + dy, f2(x , y + dy))
            x += dx
        glEnd()
        y += dy

def desenho3():
    dx = (xf - x0)/ px
    dy = (yf - y0)/ py 

    y = y0

    while(y < yf):
        x = x0
        glBegin(GL_QUAD_STRIP)
        glColor3fv((0.5, 0.5, 0.5))
        while(x < xf):
            glVertex3f(f3(x, y), y , x)
            glVertex3f(f3(x , y + dy) , y + dy , x)
            x += dx
        glEnd()
        y += dy

def desenho4():
    dx = (xf - x0)/ px
    dy = (yf - y0)/ py 

    y = y0

    while(y < yf):
        x = x0
        glBegin(GL_QUAD_STRIP)
        glColor3fv((random.uniform(0,1), random.uniform(0,1), random.uniform(0,1)))
        while(x < xf):
            glVertex3f(f4(x, y), y, x)
            glVertex3f( f4(x , y + dy) , y + dy, x)
            x += dx
        glEnd()
        y += dy

def f(x,y):
    return (x**2)/a - (y**2)/b

def f2(x,y):
    return -((x**2)/a - (y**2)/b)

def f3(x,y):
    return -((x**2)/a - (y**2)/b)

def f4(x,y):
    return ((x**2)/a - (y**2)/b)

def abacaxi():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glRotatef(100,0,1,0)
    desenho()
    desenho2()
    desenho3()
    desenho4()  
    glutSwapBuffers()

def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50,timer,1)

# PROGRAMA PRINCIPAL
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800,600)
glutCreateWindow("REVOLUCAO")
glutDisplayFunc(abacaxi)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,1.)
gluPerspective(45,800.0/600.0,0.1,50.0)
glTranslatef(0.0,0.0,-8)
#glRotatef(45,1,1,1)
glutTimerFunc(50,timer,1)
glutMainLoop()  

