import turtle


"""this is the DrawAngle""" 
"""def drawAngle(rad, angle, len, neckrad):
    for i in range(len):
                      turtle.fd(rad,0)
                      turtle.fd(rad,60)
"""                    
	  
	  
"""this is the mainwindow"""
def main():
	turtle.setup(1300,800,0,0)
	pythonsize = 30
	turtle.pensize(pythonsize)
	turtle.pencolor("black")
	turtle.seth(0)
	turtle.fd(360)
	turtle.seth(90)
	turtle.fd(360)
	turtle.seth(180)
	turtle.fd(360)
	turtle.seth(270)
	turtle.fd(360)
	turtle.done()
	
"""this is the mian"""
main()
