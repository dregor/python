from test import *

def kub(a,b):
	for x in xrange(a,b):
		print '%2d %3d %4d' % (x,x*x,x*x*x)
def TStr():
	x=10*3.14
	print str(x)
	print repr(x)
	print str('test \n string \n')
	print `'test \n string \n'`
	print max([34,556,234,22]),'\n'
	kub(1,13)
	
TStr()
