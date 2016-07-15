"""
COMPUTACION GRAFICA
UNIVERSIDAD DEL VALLE

CASANOVA S. 1430032
GONZALEZ C. 1430031
JIMENEZ A. 1328837
PUNTO 1 FIGURAS

MAYO 2016
"""

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def main():

        global window        
        global r,e,ec,colr,colg,cola
        
        glutInit(sys.argv)
        glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
        glutInitWindowSize(500,500)
        glutInitWindowPosition(500,100)
        
        window=glutCreateWindow('Figuras')        
        r=0 
        e=1
        ec=1
        colr=0.4
        colg=0.2
        cola=0.4

        def InitGL(Width, Height):
        
            glClearColor(0,0,0,0)
            glMatrixMode(GL_PROJECTION)
               
        def mostrarEscena():         

            glClear(GL_COLOR_BUFFER_BIT)
                
            glPushMatrix()
            glColor3f(colr,colg,cola)                            
            glTranslatef(0.4,0.4,0.4)
            glScalef(e,e,e)
            glutSolidSphere(0.4,40,40) 
            glPopMatrix()  

            glPushMatrix()                         
            glTranslatef(-0.5,-0.5,-0.5)            
            glScalef(ec,ec,ec)
            glRotatef(r,1,1,0)
            glTranslatef(0.5,0.5,0.5)              
            glBegin(GL_QUADS)
            glColor3f(1,0,1)
            glVertex3f(-0.35, -0.35, -0.35)
            glVertex3f(-0.35, -0.65, -0.35)
            glVertex3f(-0.65, -0.65,-0.35)
            glVertex3f(-0.65, -0.35, -0.35) 
            glEnd() 
            #glScalef(ec,ec,ec) 
            
            #cara trasera
            glBegin(GL_QUADS)
            glColor3f(0.2,1,0.2)
            glVertex3f(-0.35,-0.35, -0.65)
            glVertex3f(-0.35, -0.65,  -0.65)
            glVertex3f(-0.65, -0.65,  -0.65)
            glVertex3f(-0.65, -0.35,  -0.65)
            glEnd() 

            #cara abajo
            glBegin(GL_QUADS)
            glColor3f(0.5,0,1.8)
            glVertex3f(-0.35,-0.65, -0.35)
            glVertex3f(-0.65, -0.65, -0.35)
            glVertex3f(-0.65, -0.65, -0.65)
            glVertex3f(-0.35, -0.65, -0.65)
            glEnd() 

            #cara arriba
            glBegin(GL_QUADS)
            glColor3f(1,0,0.7)
            glVertex3f(-0.35,-0.35, -0.35)
            glVertex3f(-0.65, -0.35, -0.35)
            glVertex3f(-0.65, -0.35, -0.65)
            glVertex3f(-0.35, -0.35, -0.65)
            glEnd() 

            #cara izquierda
            glBegin(GL_QUADS)
            glColor3f(0.5,0.5,1)
            glVertex3f(-0.65, -0.35, -0.35)
            glVertex3f(-0.65, -0.35, -0.65)
            glVertex3f(-0.65, -0.65, -0.65)
            glVertex3f(-0.65, -0.65, -0.35)
            glEnd() 

            #cara derecha
            glBegin(GL_QUADS)
            glColor3f(1,1,0.5)
            glVertex3f(-0.35, -0.35, -0.35)
            glVertex3f(-0.35, -0.35, -0.65)
            glVertex3f(-0.35, -0.65, -0.65)
            glVertex3f(-0.35, -0.65, -0.35)
            glEnd() 
            glPopMatrix()

            glutSwapBuffers();
               
        def keyPressed(*args):
                global r, e              
                key=args[0];                
                if(key=="r" or key=="R"):
                   r+=30
                   # glRotatef(30,0,0,1) 
                if(key=="s" or key=="S"):
                   e*=0.8
                if(key=="z" or key=="Z"):
                   e*=1.2

        def mouse(button,state,x,y):
                global ec,colr,colg,cola
                print "x" 
                print (x)
                print "y" 
                print (y)
                if (x>80 and x <165 and y<420 and y>330):                 
                 if (button == GLUT_LEFT_BUTTON and state==GLUT_DOWN):
                    ec*=1.3
                 if (button == GLUT_RIGHT_BUTTON and state==GLUT_DOWN):
                    ec*=0.7 
                if (x>250 and x <450 and y<250 and y>50):                 
                 if (button == GLUT_LEFT_BUTTON and state==GLUT_DOWN):
                    colr=0
                    colg=0
                    cola=1
                 if (button == GLUT_RIGHT_BUTTON and state==GLUT_DOWN):
                    colr=0.4
                    colg=0.2
                    cola=0.4  
                    

        glutDisplayFunc(mostrarEscena)
        glutIdleFunc(mostrarEscena)
        glutKeyboardFunc(keyPressed)   
        glutMouseFunc(mouse)
        InitGL(500,500)
        glutMainLoop()         

if __name__== "__main__":
        main() 