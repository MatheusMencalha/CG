from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from math import *
 
print("Quantos vertices na base voce quer?")
a = int(input())
ang = 2*pi/a
r = 1

vertices = []
linhas = []
faces = []
facesBase = []
facesTopo = []

for i in range (0,a):
    x = r*cos(ang*i)
    y = -1
    z = r*sin(ang*i)

    vertices += [(x,y,z)]

for i in range (0,a):
    x = r*cos(ang*i)
    y = 1
    z = r*sin(ang*i)

    vertices += [(x,y,z)]

for i in range (0,a):
    if i != a-1:
        linhas += [(i,i+1)]
    else:
        linhas += [(i,0)]
    linhas += [(i+a, i+a+1)]
    linhas += [(i, i+a)]  

for i in range(0, a):
    if i == a-1:
        faces += [(i, i+1-a, i+1, i+a)]
        facesBase += [(i, i)]
        facesTopo += [(i, i+a)]
        break
    facesBase += [(i, i)]
    faces += [(i, i+1, i+a+1, i+a)]
    facesTopo += [(i, i+a)]

cores = ( (1,0,0),(1,1,0),(0,1,0),(0,1,1),(0,0,1) )
corBase = (1,1,1)
corTopo = (0.5,0.5,0.5)
 
def RetanguloPara():
    glBegin(GL_QUADS)
    i = 0
    for face in faces:
        glColor3fv(cores[i%len(cores)])
        for vertex in face:
            #glColor3fv(cores[vertex])
            glVertex3fv(vertices[vertex])
        i = i+1
    glEnd()

    glBegin(GL_POLYGON)
    for face in facesBase:
        for vertex in face:
            glColor3fv(corBase)
            glVertex3fv(vertices[vertex])
    glEnd()

    glBegin(GL_POLYGON)
    for face in facesTopo:
        for vertex in face:
            glColor3fv(corTopo)
            glVertex3fv(vertices[vertex])
    glEnd()
 
    glColor3fv((0,0.5,0))
    glBegin(GL_LINES)
    for linha in linhas:
        for vertice in linha:
            glVertex3fv(vertices[vertice%len(vertices)])
    glEnd()
 
def abacaxi():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glRotatef(2,1,3,0)
    RetanguloPara()
    glutSwapBuffers()
  
def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50,timer,1)
 
# PROGRAMA PRINCIPAL
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800,600)
glutCreateWindow("Retangulo Parametrizado")
glutDisplayFunc(abacaxi)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,1.)
gluPerspective(45,800.0/600.0,0.1,50.0)
glTranslatef(0.0,0.0,-8)
glRotatef(45,1,1,1)
glutTimerFunc(50,timer,1)
glutMainLoop()