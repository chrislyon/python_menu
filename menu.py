#! /bin/python2.7
# -*- coding: UTF8 -*-
##----------------------------------------------------
## Projet        : MENU EN PYTHON
## Version       :  Alpha 0.0
## Auteur        :  chris
## Date Creation : 16/2/2010 repris en 2015
## Objet         : En remplacement de GESMENU
## MAJ           : 
## Bug Report    : 
## Todo List     : 
##----------------------------------------------------
## $Id :$
##----------------------------------------------------
## (c)  chris
##----------------------------------------------------
"""
	Gesmenu est un menu texte historique chez ADONIX/SPEMI
	Ecrit par le glorieux B. Letemplier et Grand Gourou parmi
	les gourous
	Les sources ont ete perdus et sont en C 
	De nos jours des langages plus sympa sont accessible
	aussi allons y
	-- Note de derniere minute (Aout 2010)
	les sources ont ete retrouves mais maintenant (chez DURLIN/SNPE)
	il faudrait les compiler ...
	Decembre 2015 : on a reussi a rendre windows utilisable grace
	a mobaxterm on retrouve tout ce qu'il nous faut vi le shell
	meme git et python

"""
# import 
import sys
import os
import time
import datetime
import pdb
# constants
cols = 80
ligs = 24
# exception class
# interface function
# classes
# internal function and classes
def cls():
	os.system('clear')

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

def menu( entete, libel ):
	"""
		Affichage du menu proprement dit
	"""
	cls()
	## Nblig pour affichage du menu -2 entete et -3 bas de page
	nbl_menu = ligs-2-3
	print entete_menu(entete)
	l = len(libel)
	nbl = 0
	for x in range(0, (nbl_menu-(l*2))/2):
		nbl += 1
		print
	n = 0
	sp = " " * 30
	for l in libel:
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

def prompt():
	machine = 'MobaxTerm'
	tty = '/dev/tty'
	identite = 'MenuPython'
	m = """\
Identite : %-10s                                         (c) Chris / SRA
Terminal : %-10s                                                2010
""" % (identite, tty)
	return m+"Machine  : %-10s            Votre Choix : " % machine

def espace(l='Tapez Entree'):
	raw_input('\t%s' % l)

## ---------------------------------
## Lancement d'un environemment ADX
## ---------------------------------
def appli_DF():
	cls()
	cmd = "adoinge3 DF"
	os.system(cmd)

def appli_IMMODF():
	cls()
	cmd = "adoinge3 IMMODF"
	os.system(cmd)

def appli_ENTREPRISE():
	cls()
	cmd = "adoinge3"
	os.system(cmd)

def appli_TEST():
	cls()
	print " Environnement de DEV"
	time.sleep(1)
	cmd = "/ado/bin/adx_env_dev"
	os.system(cmd)

def telnet_ancien_serveur():
	cls()
	cmd = "telnet old"
	os.system(cmd)

def non_implementee():
	cls()
	print """
		FONCTION NON IMPLEMENTEE
		========================
	"""
	espace()

def menu_main():
	entete = "MENU DEV/TEST"
	libel = [ "Activite VO / DF" ,
				"IMMO DF",
				"ADONIX ENTREPRISE",
				"CONNEXION ANCIEN SERVEUR"
			 ]
	fnc = {
		'1':appli_DF,
		'2':appli_IMMODF,
		'3':appli_ENTREPRISE,
		'4':telnet_ancien_serveur,
		}
	return entete, libel, fnc

def main():
	""" 
	La fonction principale
	de gestion du menu
	"""
	while True:
		entete, libel, fnc = menu_main()
		menu( entete, libel )
		cmd = raw_input( prompt() )
		if cmd in fnc.keys():
			fnc[cmd]()
		elif cmd == '0':
			break

if __name__ == '__main__':
	#pdb.set_trace()
	main()
