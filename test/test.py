#!/usr/bin/env python
def max(a):
	if (len(a)>0):result,i=a[0],0
	else : return "pusto"
	for i in xrange(len(a)):
		if (result<a[i]): result=a[i]
	return result

def f(a,l= None):
	if (l is None):
		l=[]
	l.append(a)
	return l

def f1(a, l=[]):
	l.append(a)
	return l
