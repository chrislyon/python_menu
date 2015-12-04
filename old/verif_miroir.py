##
## Verification specifique 
##

import commands

lsvg_rootvg = commands.getoutput('lsvg -l rootvg').split('\n')

for l in lsvg_rootvg[2:]:
	lv, typ, lp, pp, pv, etat, mnt = l.split()
	print "lv=%s typ=%s etat=%s mnt=%s" % (lv, typ, etat, mnt)
