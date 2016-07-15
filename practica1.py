from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def main():

        global window              
        
        glutInit(sys.argv)
        glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
        glutInitWindowSize(500,500)
        glutInitWindowPosition(500,100)
        
        window=glutCreateWindow('Practica')        


        def InitGL(Width, Height):
        
            glClearColor(0,0,0,0)
            glMatrixMode(GL_PROJECTION)
               
        def mostrarEscena():         

            glClear(GL_COLOR_BUFFER_BIT)                       
            glMatrixMode(GL_PROJECTION);  
            glLoadIdentity();  
            #glOrtho(-1,1, -1,1, -1, 1); 
            #glFrustum(-2,2,-2,2,0.2,1)
            x,y,width,height = glGetDoublev(GL_VIEWPORT)
#            gluPerspective(
#		-100, # field of view in degrees
#		1,#width/float(height or 1), # aspect ratio
#		0.1, # 0near clipping plane
#		10, # far clipping plane
#	)       
            gluPerspective(-100,1,0.25,20);
            glMatrixMode(GL_MODELVIEW)
	    glLoadIdentity()
            gluLookAt(
		0,0,0, # eyepoint
		0,-0.5,-0.5, # center-of-view
		1,1,0, # up-vector
	)
                 
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
           

            glutSwapBuffers();               
                   

        glutDisplayFunc(mostrarEscena)
        glutIdleFunc(mostrarEscena)
        InitGL(500,500)
        glutMainLoop()         

if __name__== "__main__":
        main() 
