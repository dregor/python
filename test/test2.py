from test import *

def TEST():
	x=10*3.14
	print str(x)
	print repr(x)
	print str('test\nstring\n')
	print `'test \nstring \n'`,'\n'
	print max([34,556,234,22]),'\n'
	kub(1,13),'\n'
	form(),'\n'

def kub(a,b):
	for x in xrange(a,b):
		print '%2d %3d %4d' % (x,x*x,x*x*x)

def form():
	table={'Joe':2122,
	       'Jack':4765,
	       'Duck':3432}
	for name,phone in table.items():
		print '%10s |-> %10d' %(name,phone)
	print '\n',vars(),'\n'
TEST()
