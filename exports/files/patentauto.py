#! /usr/bin/python

__author__="LCDR Kris Kearton"
__date__ ="$Aug 24, 2009 7:42:41 PM$"
# class: CS4920 ADOMEX
# System info: Running on OS 10.6 python ver 2.6.2
# Setup information:
#   (1) Install MozRepl Plugin at:
#       http://wiki.github.com/bard/mozrepl
#       Once installed, ensure in Firefox under tools MozRepl is started
#
# Summary: MozRepl needs to telnet to the browser via port 4242.  Once connected the port can program
# can issue commands directly to the web browser.  This program gets the list of urls from the text file.
# Then randomly picks a URL and surfs it for background noise.

import time
import csv
import telnetlib
import robotparser
import os
import random

#
#connect to MozRepl and fetch HTML
#
def connect_mozrepl(url_addr):
    quit = False
    t = telnetlib.Telnet("localhost", 4242)
    t.read_until("repl>")

    #verifies page was accepted
    rp = robotparser.RobotFileParser()
    fetched = rp.can_fetch("*", url_addr)
    print fetched
    state = True
    while(state==True):
        if fetched==True:
            rdm = random.random()*20
            print rdm
            time.sleep(rdm) #WAIT FOR WEBPAGE TO LOAD
            str =  "content.location.href='"+url_addr.strip()+"'\n"
            print str
            t.write(str)
            body = t.read_until("repl>")
            state = False
        else:
            state = False
            print "unable to fetch web page, exiting!!!"
            quit = True
            break
    t.write("content.document.body.innerHTML\n")
    body = t.read_until("repl>")

    t.close()

    return body, quit

def urlMain():
    quitflag = False
    url = open("urls.txt", "r")

    #this goes through every url in the ???.txt file
    for line in url:
        #print line
        hour = time.localtime()[3]
        if (hour >= 9 and hour < 10) or (hour >= 13 and hour < 14) or (hour >= 16 and hour < 17):
            html_body, quitflag = connect_mozrepl(line)
            if quitflag==True:
                break
        else:
            break
    print "Done\n"
    
def patentMain():
        quitflag = False
        url = open("patentterms.txt", "r")

        #this goes through every url in the ???.txt file
        for line in url:
            #print line
            hour = time.localtime()[3]
            if (hour >= 10 and hour < 12) or (hour >= 13 and hour < 16):
                rdm = random.random() * int(line.split(',')[1])
                #http://patft.uspto.gov/netacgi/nph-Parser?Sect1=PTO2&Sect2=HITOFF&p=1&u=%2Fnetahtml%2FPTO%2Fsearch-bool.html&r=3343&f=G&l=50&co1=AND&d=PTXT&s1=cryptography&OS=cryptography&RS=cryptography
                print 'http://patft.uspto.gov/netacgi/nph-Parser?Sect1=PTO2&Sect2=HITOFF&p=1&u=%2Fnetahtml%2FPTO%2Fsearch-bool.html&r='+repr(rdm)+'&f=G&l=50&co1=AND&d=PTXT&s1='+line.split(',')[0]+'&OS='+line.split(',')[0]+'&RS='+line.split(',')[0]
                html_body, quitflag = connect_mozrepl('http://patft.uspto.gov/netacgi/nph-Parser?Sect1=PTO2&Sect2=HITOFF&p=1&u=%2Fnetahtml%2FPTO%2Fsearch-bool.html&r='+repr(rdm)+'&f=G&l=50&co1=AND&d=PTXT&s1='+line.split(',')[0]+'&OS='+line.split(',')[0]+'&RS='+line.split(',')[0])    
                if quitflag==True:
                    break
            else:
                break
        print "Done\n"

if __name__ == "__main__":
    while(1):
        hour = time.localtime()[3]
        if (hour >= 9 and hour < 10) or (hour >= 14 and hour < 14) or (hour >= 16 and hour < 17):
            print "Visiting Persona URLs..."
            urlMain()
        if (hour >= 10 and hour < 12) or (hour >= 13 and hour < 16):
            print "Patent Searching..."
            patentMain()
