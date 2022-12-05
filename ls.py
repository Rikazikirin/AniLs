#!/usr/bin/python3

# IMPORT MODULE
import sys,os
from datetime import datetime
from getpass import getpass
import time

# DATE AND TIME
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

# Function to create list in txt

# If choose 1
def Als():
    os.system('clear')
    os.system('python banner2.py')
    print (now)
    print ("\n \033[0;32m choose above what you want\033[0m\n")
    print ("\t[01]:\033[0;33m append your last seen list.\033[0m\n")
    print ("\t[02]:\033[0;33m change your last seen episode.\033[0m\n")
    ls = int(input("\033[0;32m enter your number:\033[0m"))
    if ls == 2:
        with open('lastseen.txt', 'rt') as als:
             os.system('cat lastseen.txt')
             data = als.read()
             aft = input('\033[0;33m enter anime and last seen episode: \033[0m ')
             bef = input('\033[0;33m enter your previous episode: \033[0m ')
             data = data.replace(bef,aft)
             als.close()

             als = open('lastseen.txt', 'wt')
             als.write(data)
             als.close()
    elif ls == 1:
       anime = input("\033[0;33m Append your list here: \033[0m")
       open('lastseen.txt', 'a').writelines(anime + '\n')
    else:
        print ("\033[0;31m Are you okay?\033[0m")

# If choose 2
def AC():
    os.system('clear')
    os.system('python banner4.py')
    print (now)
    print ("""\n\n\t \t\t\033[0;36m Even if you're the main character,
 \t\t\t you can still die...
 \t\t\t I better be careful-ttebayo.
            \t\t -Sakata Gintoki\033[0m""")

    enter = input("\033[0;33m press enter \033[0m")
    if enter != 0:
       completed = input("\033[0;33m enter your completed anime list here: \033[0m")
       open('completed.txt', 'a').writelines(completed + '\n')
    else:
       os.system('exit')
       sys.exit()

# Main code to run
def main():
    global choice,lastseen,completed
    os.system('clear')
    os.system('python banner3.py')
    print(now)
    print ("\n \033[0;36m enjoy your hobbies, don't think about people think and says!\033[0m\n")
    print ("\t[01]:\033[0;33m for write your last seen anime\n  \033[0m")
    print ("\t[02]:\033[0;33m for append your completed anime\n \033[0m")
    choice = int(input("\033[0;32m Select your options: \033[0m"))


    if choice == 1:
       open('lastseen.txt', 'a')
       Als()

    elif choice == 2:
       open('completed.txt', 'a')
       AC()
    else:
       print("\033[0;31m You have a something wrong in your brain\033[0m")

main()
