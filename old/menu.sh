#! /bin/sh
## -------------------------
## Menu Info
## (c) Chris SRA Info 2004
## -------------------------

MENU_DIR=.
PATH=$PATH:$MENU_DIR

DISQUE_SPACE="df -k"

TS_DATE=$(date "+%d-%m-%Y")
TS_TIME=$(date "+%H:%M:%S")
TTY=$(tty)
TTY=$(printf "%-10.10s" $TTY)
HOSTNAME=$(hostname)
HOSTNAME=$(printf "%-20.20s" $HOSTNAME)
LOGNAME=root
USER=$(printf "%-10.10s" $LOGNAME)


my_pg()
{
        #pg -p'Appuyez sur la touche ENTREE'
        #less -P'Appuyez sur la touche ESPACE'
        #more
	echo -n "APPUYEZ sur RETURN"
        read $bidon
}

##
## Erreur Menu
##
err_menu()
{
	clear
	echo
	echo "OPTION DE MENU INCORRECTE"
	echo
	my_pg
}

display() {

        clear
cat <<!!

MENU v0.0           MENU PRINCIPAL                                 $TS_DATE
                                                                   $TS_TIME

                    1) X3V5

                    2) X3V6

                    0) Fin


Identite : $USER                                        (c) Chris SRA
Terminal : $TTY                                         2010/2012
Machine  : $HOSTNAME
!!
}


while true
do
        display
        echo -n "                   Votre choix :"
        read bidon
        case $bidon in
        0) exit ;;
        1) menu_x3v5.sh;;
        2) menu_x3v6.sh;;
        *) err_menu;;
        esac
done
