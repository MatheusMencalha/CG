from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from math import *
from random import *
from numpy import *
p1x = 0;
p1y = 1;
p2x = -4;
p2y = 0;
p3x = 0;
p3y = -1;
dteta = math.pi/16

def Px(teta):
    return r*cos(teta)

def Py(teta):
    return r*sin(teta)

def Qx(r2, phi):
    return r2*cos(phi)

def Qz(r2, phi):
    return r2*sin(phi)


def Prisma():
    glBegin(GL_LINE_STRIP)
    
    glColor3fv((1,1,1))
    
    auxI = 0;
    auxF = 2*math.pi
    ang=0;
    while auxI < auxF:
        ang += dteta    
        t = 0;
        glColor3fv((1,1,1))
        glVertex3fv((p1x*cos(ang),p1y,p1x*sin(ang)))
        while t<=1:

            ax = p1x +  t*(p2x-p1x);
            bx = p2x +  t*(p3x-p2x);
            cx = ax  +  t*(bx-ax);
            ay = p1y +  t*(p2y-p1y);
            by = p2y +  t*(p3y-p2y);
            cy = ay  +  t*(by-ay);
            glColor3fv((1,1,1))
            
            glVertex3fv((cx*cos(ang),cy,cx*sin(ang)))
            
            t+=0.1;
    
        glColor3fv((1,1,1))
        glVertex3fv((p3x*cos(ang),p3x,p3x*sin(ang)))
        auxI+=dteta

    glEnd()

    
def abacaxi():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glRotatef(1,1,1,1)
    Prisma()
    glutSwapBuffers()
 
def timer(i):
    glutPostRedisplay()
    glutTimerFunc(5,timer,1)

# PROGRAMA PRINCIPAL
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800,600)
glutCreateWindow("BEZIE DA HORA")
glutDisplayFunc(abacaxi)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,1.)
gluPerspective(25,800.0/600.0,0.1,50.0)
glTranslatef(0.0,0.0,-8)
glRotatef(45,0,0,0)
glutTimerFunc(50,timer,1)
glutMainLoop()