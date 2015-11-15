import hexchat
import itertools
import re
import random
import urllib2
import json
import sys

__module_name__ = 'Jadisco'
__module_version__ = '1.0'
__module_description__ = 'Skrypt do obslugi czatu Jadisco. Napisz /jd by uzyskac informacje o skrypcie.'

hexchat.prnt('Zaladowano Jadisco')

colors = ['02','03','04','05','06','07','08','09','10','11','12','13']

DEVELOPER_KEY = "YOUTUBE_API_KEY"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"


def death_counter(word, word_eol, user_data):
    if len(word_eol[1]) < 1:
        print("Podaj ilosc cmierci")
    else:
        hexchat.command('say \002Death Counter: \00304' + word_eol[1])
    return hexchat.EAT_ALL

def r_n_g(word, word_eol, user_data):
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

def info(word, word_eol, user_data):
    print("\002\00304Informacje skryptu Jadisco.")
    print("")
    print("\002KOMENDY")
    print("1. \002\035dc\035\002 - Death Counter, wymaga argumentu czyli ilosci smierci.")
    print("2. \002\035rng\035\002 - Status RNG Macka, wymaga argumentu.")
    print("3. \002\035mj\035\002 - MJUZIK!!!1one, wymaga podania linku do muzyki z YouTube.")
    print("")
    return hexchat.EAT_ALL   

hexchat.hook_command('dc', death_counter)
hexchat.hook_command('rng', r_n_g)
hexchat.hook_command('mj', mj)
hexchat.hook_command('jd', info)
