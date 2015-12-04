#! /bin/python2.7

##
## MENU2
##

import os
import datetime


##
## constantes
##

cols=80
ligs=24

class LigMenu():
	""" Ligne de Menu :
		typ = 1 = Menu / 2 = os.system sans conf / 3 avec conf
		libel = libelle de l'option
		fnc = le nom de la fonction a executer
		a voir => conf / espace 
	"""
	def __init__(self, typ=1, libel = "Option1", fnc='dumb'):
		self.typ = typ
		self.libel = libel
		self.fnc = fnc

	def __repr__(self):
		return "<LigMenu:%s:%s:%s>" % (self.typ, self.libel, self.fnc)

class Menu():
	""" Classe Menu
	container pour les lignes de menu avec une entete
	"""
	def __init__( self, entete="<Entete Menu>", lines = [] ):
		self.entete = entete
		self.lines = lines

	def libel(self):
		return [ x.libel for x in self.lines ]

	def fnc(self):
		return [ x.fnc for x in self.lines ]

	def __repr__(self):
		return "<Menu:%s>" % self.entete

def entete_menu(titre):
	d = datetime.datetime.now()
	date = d.strftime("%d %B %Y")
	heure = d.strftime("%H:%M:%S")
	m = "MENU v0.0"
	titre = titre.center(53)
	m += titre
	m += "%15s" % date
	m += "\n"
	m += "%79s" % heure
	return m

def prompt():
	machine = 'MobaxTerm'
	tty = '/dev/tty'
	identite = 'MenuPython'
	m = """\
Identite : %-10s                                         (c) Chris / SRA
Terminal : %-10s                                                2010
""" % (identite, tty)
	return m+"Machine  : %-10s            Votre Choix : " % machine

def display(menu):
	cls()
	## Nblig pour affichage du menu -2 entete et -3 bas de page
	nbl_menu = ligs-2-3
	print entete_menu(menu.entete)
	l = len(menu.libel())
	nbl = 0
	for x in range(0, (nbl_menu-(l*2))/2):
		nbl += 1
		print
	n = 0
	sp = " " * 30
	for l in menu.libel():
		n += 1
		print sp+"%d) %-40s" % (n,l)
		nbl += 1
		print
		nbl += 1
		#print "%d) %-40s".center(79) % (n, l)
	print
	nbl += 1
	print
	nbl += 1
	print "0) Deconnexion / Fin".center(79)
	nbl += 1
	for x in range(0, nbl_menu-nbl+1):
		print
	print prompt()
	

def cls():
	os.system("clear")

def espace(l='Tapez Entree'):
    raw_input('\t%s' % l)

def dumb():
	cls()
	print "Fonction Bidon"
	espace()

def test2():
	l = []
	l.append(LigMenu(typ=1, libel='Menu1'))
	l.append(LigMenu(typ=1, libel='Menu2'))
	l.append(LigMenu(typ=1, libel='Menu3'))
	l.append(LigMenu(typ=1, libel='Menu4'))
	l.append(LigMenu(typ=1, libel='Menu5'))
	l.append(LigMenu(typ=1, libel='Menu6'))
	l.append(LigMenu(typ=1, libel='Menu7'))
	l.append(LigMenu(typ=1, libel='Menu8'))
	l.append(LigMenu(typ=1, libel='Menu9'))
	l.append(LigMenu(typ=1, libel='MenuA'))
	M = Menu( entete="MENU TEST2", lines=l)
	display(M)
	espace()


def test():

	l = [ LigMenu() ]
	M = Menu( entete="MENU TEST/DEV", lines=l)

	print l
	print M
	print M.libel()


if __name__ == '__main__':
	#test()
	test2()
