#!/usr/bin/python
from copy import deepcopy
import random
import sys
random.seed()
xdhkl = open('xd.hkl','r').readlines()
xdhkl_header = xdhkl.pop(0)
try:
    batches = int(sys.argv[1])
except:
    batches = int(raw_input('Number of batches: '))
xdbatch = {}
shelxbatch = {}
batch_length = int(len(xdhkl)/batches)
for i in xrange(batches):
    xdbatch[i]=[]
    shelxbatch[i]=[]
i = 0
while len(xdbatch[i]) <= batch_length and not len(xdhkl)==0:
    rngesus = xdhkl.pop(random.randint(0,len(xdhkl)-1))
    xdbatch[i].append(rngesus)
    splitgesus = rngesus.split()
    for l in xrange(batches):
        if l == i:
	    shelxbatch[l].append(' {0:>3s} {1:>3s} {2:>3s} {3:>7.2f} {4:>7.2f} {5:>3s}\n'.format(splitgesus[0],splitgesus[1],splitgesus[2],float(splitgesus[4]),float(splitgesus[5]),'-1'))
	else:
	    shelxbatch[l].append(' {0:>3s} {1:>3s} {2:>3s} {3:>7.2f} {4:>7.2f} {5:>3s}\n'.format(splitgesus[0],splitgesus[1],splitgesus[2],float(splitgesus[4]),float(splitgesus[5]),'1'))
    i+=1
    if i>batches-1:
        i=0
for i in xrange(batches):
    print len(xdbatch[i])
    xdfreehkl = open('xdfree{:>02}.hkl'.format(i+1),'w')
    xdworkhkl = open('xdwork{:>02}.hkl'.format(i+1),'w')
    shelxhkl = open('rfree{:>02}.hkl'.format(i+1),'w')
    xdworkhkl.write(xdhkl_header)
    xdfreehkl.write('{}{}'.format(xdhkl_header,''.join(xdbatch[i])))
    shelxhkl.write(''.join(shelxbatch[i]))
    for j in xrange(batches):
        if i != j:
	    xdworkhkl.write(''.join(xdbatch[j]))