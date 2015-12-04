import os
import commands
import pdb

def tput(p):
	return commands.getoutput('tput %s ' % p)

l = []
for x in range(0, 15):
	l.append( "Libelle %0d" % x )

#pdb.set_trace()

cols=int(tput('cols'))
ligs=int(tput('lines'))
nbl_ent = 3 #2 + 1 Ligne de marge
nbl_bas = 4	#3 + 1 ligne de marge
nbl_lib = ligs-nbl_bas-nbl_ent
## Entete
for x in range(1,nbl_ent):
	print "Entete %d" % x
print
for x in range(1, nbl_lib):
	print "Lib %d " % x
print
print "0 - Deconnexion Fin"
print
for x in range(1,nbl_bas-1):
	print "Bas %d " % x
a = raw_input("Choix")
