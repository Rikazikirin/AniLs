# /!/usr/bin/python3

# IMPORT MODULE
import sys,os
from datetime import datetime
import time

# DATE AND TIME
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

# Function to create list in txt

def exit():
    os.system('clear')
    print ("""\033[0;32m You want to exit\n or you want to return?\033[0m\n""")
    print (""" \033[0;33m   [press "ls" to last seen]
    [press "cp" to completed]
    [press any key to exit]\033[0m""")
    print ('\n')
    ex = str(input('\033[0;33myou want to return?:\033[0m '))
    if ex == "ls":
        return Als()

    elif ex == "cp":
        return AC()

    else:
        os.system('exit')
        sys.exit()

# If choose 1
def Als():
    os.system('clear')
    print ("""\033[0;36m

                                        .
             i                         ;W
            LE              ..        f#E GEEEEEEEL
           L#E             ;W,      .E#f  ,;;L#K;;.
          G#W.            j##,     iWW;      t#E
         D#K.            G###,    L##Lffi    t#E
        E#K.           :E####,   tLLG##L     t#E
      .E#E.           ;W#DG##,     ,W#i      t#E
     .K#E            j###DW##,    j#E.       t#E
    .K#D            G##i,,G##,  .D#j         t#E
   .W#G           :K#K:   L##, ,WK,          t#E
  :W##########Wt ;##D.    L##, EG.            fE
  :,,,,,,,,,,,,,.,,,      .,,  ,               :
                                                   \033[0;36m""")

    print ("""\033[0;36m

           .        ,;        ,;L.
          ;W      f#i       f#i EW:        ,ft
         f#E    .E#t      .E#t  E##;       t#E
       .E#f    i#W,      i#W,   E###t      t#E
      iWW;    L#D.      L#D.    E#fE#f     t#E
     L##Lffi:K#Wfff;  :K#Wfff;  E#t D#G    t#E
    tLLG##L i##WLLLLt i##WLLLLt E#t  f#E.  t#E
      ,W#i   .E#L      .E#L     E#t   t#K: t#E
     j#E.      f#E:      f#E:   E#t    ;#W,t#E
   .D#j         ,WW;      ,WW;  E#t     :K#D#E
  ,WK,           .D#;      .D#; E#t      .E##E
  EG.              tt        tt ..         G#E
  ,                                         fE
                                             ,\033[0m""")

    print (now)
    print ("\n \033[0;32m choose above what you want\033[0m\n")
    print ("\t[01]:\033[0;33m append your last seen list.\033[0m\n")
    print ("\t[02]:\033[0;33m change your last seen episode.\033[0m\n")
    ls = str(input("\033[0;32m enter your number:\033[0m"))
    if ls == "2":
        with open('lastseen.txt', 'rt') as als:
             os.system('cat lastseen.txt')
             data = als.read()
             aft = input('\033[0;33m enter anime and latest episode: \033[0m ')
             bef = input('\033[0;33m enter your anime and previous episode: \033[0m ')
             data = data.replace(bef,aft)
             als.close()

             als = open('lastseen.txt', 'wt')
             als.write(data)
             als.close()
             print ("\033[0;32m Success! Your list has been update!\033[0m")
             os.system('cat lastseen.txt')
             print ('\n')
             time.sleep(7)
             return exit()
    elif ls == "1":
       anime = input("\033[0;33m Append your list here: \033[0m")
       open('lastseen.txt', 'a').writelines(anime + '\n')
       print ("\033[0;32m Success! Your list has been save!\033[0m")
       os.system('cat lastseen.txt')
       time.sleep(7)
       return exit()
    else:
        print ("\033[0;31m Are you okay?\033[0m")
        os.system('exit')
        sys.exit()

# If choose 2
def AC():
    os.system('clear')
    print ("""\033[0;36m                                                                                            ;
               :                                                                            ED.
        .,    t#,                                                      ,;                 ,;E#Wi
       ,Wt   ;##W.                        t                   i      f#i                f#i E###G.
      i#D.  :#L:WE             ..       : ED.                LE    .E#t  GEEEEEEEL    .E#t  E#fD#W;
     f#f   .KG  ,#D           ,W,     .Et E#K:              L#E   i#W,   ,;;L#K;;.   i#W,   E#t t##L
   .D#i    EE    ;#f         t##,    ,W#t E##W;            G#W.  L#D.       t#E     L#D.    E#t  .E#K,
  :KW,    f#.     t#i       L###,   j###t E#E##t          D#K. :K#Wfff;     t#E   :K#Wfff;  E#t    j##f
  t#f     :#G     GK      .E#j##,  G#fE#t E#ti##f        E#K.  i##WLLLLt    t#E   i##WLLLLt E#t    :E#K:
   ;#G     ;#L   LW.     ;WW; ##,:K#i E#t E#t ;##D.    .E#E.    .E#L        t#E    .E#L     E#t   t##L
    :KE.    t#f f#:     j#E.  ##f#W,  E#t E#ELLE##K:  .K#E        f#E:      t#E      f#E:   E#t .D#W;
     .DW:    f#D#;    .D#L    ###K:   E#t E#L;;;;;;, .K#D          ,WW;     t#E       ,WW;  E#tiW#G.
       L#,    G#t    :K#t     ##D.    E#t E#t       .W#G            .D#;    t#E        .D#; E#K##i
        jt     t     ...      #G      ..  E#t      :W##########Wt     tt     fE          tt E##D.
                              j                    :,,,,,,,,,,,,,.            :             E#t
                                                                                            L:          \033[0m""")
    print (now)
    print ("""\n\n\t \t\t\033[0;36m Even if you're the main character,
 \t\t\t you can still die...
 \t\t\t I better be careful-ttebayo.
            \t\t -Sakata Gintoki\033[0m""")

    enter = input("\033[0;33m press enter \033[0m")
    if enter != 0:
       completed = input("\033[0;33m enter your completed anime list here: \033[0m")
       open('completed.txt', 'a').writelines(completed + '\n')
       print ("\033[0;32m Success! Your list has been save!\033[0m")
       os.system('cat completed.txt')
       time.sleep(7)
       return exit()
    else:
       os.system('exit')
       sys.exit()

# Main code to run
def main():
    global choice,lastseen,completed
    os.system('clear')
    print ("""\033[0;36m

                L.                                         .
                EW:        ,ft t              i           ;W
             .. E##;       t#E Ej            LE          f#E
            ;W, E###t      t#E E#,          L#E        .E#f
           j##, E#fE#f     t#E E#t         G#W.       iWW;
          G###, E#t D#G    t#E E#t        D#K.       L##Lffi
        :E####, E#t  f#E.  t#E E#t       E#K.       tLLG##L
       ;W#DG##, E#t   t#K: t#E E#t     .E#E.          ,W#i
      j###DW##, E#t    ;#W,t#E E#t    .K#E           j#E.
     G##i,,G##, E#t     :K#D#E E#t   .K#D          .D#j
   :K#K:   L##, E#t      .E##E E#t  .W#G          ,WK,
  ;##D.    L##, ..         G#E E#t :W##########Wt EG.
  ,,,      .,,              fE ,;. :,,,,,,,,,,,,,.,
                             ,                              \033[0m""")

    print(now)
    print ("\n \033[0;36m enjoy your hobbies, don't think about people think and says!\033[0m\n")
    print ("\t[01]:\033[0;33m for write your last seen anime\n  \033[0m")
    print ("\t[02]:\033[0;33m for append your completed anime\n \033[0m")
    choice = str(input("\033[0;32m Select your options: \033[0m"))


    if choice == "1":
       open('lastseen.txt', 'a')
       Als()

    elif choice == "2":
       open('completed.txt', 'a')
       AC()
    else:
       print(str("\033[0;31m select error : "+choice))
       print("\033[0;31m You have a something wrong in your brain\033[0m")
       os.system('exit')
       sys.exit()

main()
