import hexchat
import itertools
import re
import random
import urllib2
import json
import sys
import os
reload(sys);
sys.setdefaultencoding("utf8")


__module_name__ = 'Jadisco'
__module_version__ = '2.5'
__module_author__ = "cbool222"
__module_description__ = 'Skrypt do obsługi czatu Jadisco. Napisz /jd by uzyskac informacje o skrypcie.'

hexchat.prnt('Załadowano Jadisco')

colors = ['02','03','04','05','06','07','08','09','10','11','12','13']
rainbow = [4,7,8,9,11,12,13,6]
rainbow2 = ["04","07","08","09","11","12","13","06"]

DEVELOPER_KEY = "API_KEY"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

rngfile = "C:/Users/cbool/AppData/Roaming/HexChat/addons/rngobjects.txt"

def info(word, word_eol, user_data):
    print("\002\00304Informacje skryptu Jadisco.")
    print("")
    print("\002KOMENDY")
    print("1. \002\035dc\035\002 - Death Counter, wymaga argumentu czyli ilości śmierci.")
    print("2. \002\035rng\035\002 - Status RNG Maćka, wpisz /rng info by uzyskać więcej informacji.")
    print("3. \002\035mj\035\002 - MJUZIK!!!1one, wymaga podania linku do muzyki z YouTube.")
    print("4. \002\035r\035\002 - Wypisuje tekst w kolorze tęczy")
    print("5. \002\035tencza\035\002 - TENCZA!!!")
    print("")
    print("")
    return hexchat.EAT_ALL 

def death_counter(word, word_eol, user_data):
    if len(word_eol) < 2:
        print("Podaj ilosc śmierci")
    else:
        hexchat.command('say \002Death Counter: \00304' + word_eol[1])
    return hexchat.EAT_ALL

def rng(word, word_eol, user_data):
    if len(word_eol) < 2:
        f = open(rngfile,'r')
        line = next(f)
        for num, aline in enumerate(f):
            if random.randrange(num + 2): continue
            line = aline.rstrip()
        hexchat.command("say \002Status RNG: " + "\003" +random.choice(colors) + line)        
    elif word[1] == "add":
        f = open(rngfile,"a")
        f.write(word_eol[2]+"\n")
        print("Dodano " + word_eol[2] + " do spisu")
        f.close
    elif word[1] == "info":
        print("\002\00304Informacje o funkcji RNG.")
        print("")
        print("\002ARGUMENTY")
        print("1. \002\035brak\035\002 - Wypisuje podany status z losowym kolorem")
        print("2. \002\035add\035\002 - Dodaje podany status do spisu")
        print("3. \002\035list\035\002 - Wypisuje wszystkie statusy z spisu")
        print("")
    elif word[1] == "list":
        print("Lista statusów RNG")
        print("")
        lines = [line.rstrip('\n') for line in open(rngfile)]
        for element in lines:
            print(element)
    else:
        hexchat.command('say \002Status RNG: '+ "\003" +random.choice(colors) + word_eol[1])
    return hexchat.EAT_ALL

def mj(word, word_eol, user_data):
    id = word_eol[1][-11:]
    getinfo = ("https://www.googleapis.com/youtube/v3/videos?id=%s&key=%s&part=snippet,contentDetails,statistics,status" % (id, DEVELOPER_KEY))
    response = urllib2.urlopen(getinfo)
    page_data = json.load(response)
    for video in page_data['items']:
        hexchat.command("say \002\00304Mjuzik: %s\003 :: \00309URL: https://youtu.be/"  % video['snippet']['title'] + id)
    return hexchat.EAT_ALL

def Rainbow(text,offset):
	rainbowed = ""

	for i in range(len(text)):
		rainbowed += "\x03{}{}".format(rainbow[(i+offset)%len(rainbow)], text[i])
	return rainbowed

def rainbowcmd(word,word_eol,userdata):
	try:
		count = int(word[-1])
		text = ' '.join(word[1:-1])
	except ValueError:
		count = 1
		text = ' '.join(word[1:])
	for i in range(0,count):
		(hexchat.get_context()).command("say {}".format(Rainbow(text,i)))

def tencza(word, word_eol, user_data):
    test = ""
    for element in rainbow2:
        test += "\003" + element +"█"
    hexchat.command("say " + test)
    return hexchat.EAT_ALL

hexchat.hook_command('dc', death_counter)
hexchat.hook_command('rng', rng)
hexchat.hook_command('mj', mj)
hexchat.hook_command('jd', info)
hexchat.hook_command('r', rainbowcmd)
hexchat.hook_command('tencza', tencza)
