from colorama import Fore
import signal
from time import sleep
import rainbowtext,pyfiglet
import os
import sys

os.system ("clear")


print (Fore.GREEN+"\t\tSEX OR CODE OR MOKHAREB")

print(rainbowtext.text(pyfiglet.figlet_format('CODE')))
print (Fore.RED+"CODED BY"+" "+Fore.GREEN+"HEMI THE GOD")

print ("\t\t1 = CODE FILTER")
print ("\t\t2 = LINK SEXI")
print ("\t\t3 = LINK MOKHAREB")
print ("\t\t00 = exit")


F = input (Fore.RED+f"\t[*] ~> {Fore.GREEN}ENTER THE NUMBER({Fore.RED}1 {Fore.GREEN}OR {Fore.RED}2 {Fore.GREEN}OR {Fore.RED}3{Fore.GREEN})==>{Fore.RED} ")

kop = f""" 

{Fore.GREEN}[1]     {Fore.WHITE}   [2]    {Fore.RED}     [3]

"""
for c in kop:
    sys.stdout.write(c)
    sys.stdout.flush()
    sleep(0.06)


print (Fore.RED)

print ("\tSTART !\n")

sleep(1)

code_filter = '1'
link_sexi = '2'
link_mokhareb = '3'
exit = '00'

if F == code_filter:
    f = open ("/sdcard/code_filteri.txt", "r")
    for i in f:
    	sleep(0.09)
    	print (i)
		
elif F == link_sexi:
	f1 = open ("/sdcard/sex.txt", "r")
	for i in (f1):
		sleep(0.09)
		print (i)
elif F == link_mokhareb:
	f2 = open ("/sdcard/link.txt", "r")
	for i in f2:
		sleep(0.09)
		print (i)

		
while F != exit:
	def ctrl_handller(signumber, frem):
		print ("you can not kill me")
	print ("\ninstall signal handller")
	print ("done")
	
	signal.signal(signal.SIGINT,ctrl_handller)
	
	while True:
		pass