# -*- coding: utf-8 -*-
# Natural Language Toolkit: Generating from a CFG
#
# Copyright (C) 2001-2014 NLTK Project
# Author: Steven Bird <stevenbird1@gmail.com>
#         Peter Ljunglöf <peter.ljunglof@heatherleaf.se>
# URL: <http://nltk.org/>
# For license information, see LICENSE.TXT
#
from __future__ import print_function

import datetime
today = datetime.date.today()
import itertools
import sys
from nltk.grammar import Nonterminal
from nltk.parse.generate import generate


path = "Cliclaques"
demo_grammar = open(path+".txt", "r", encoding='utf-8').read()


def demo(N=1000):
    import nltk
    from nltk.grammar import CFG
    from nltk import grammar, parse

    print('Generating the first %d sentences for demo grammar:' % (N,))
    print(demo_grammar+"\n")
    grammar =  grammar.CFG.fromstring(demo_grammar)

    for sentence in generate(grammar,n=10):
        print(' '.join(sentence))


    exit(0)
    #grammar = nltk.grammar.ContextFreeGrammar.productions(demo_grammar)
    for n, sent in enumerate(generate(grammar, n=N), 1):
        #print ('captura_generated.txt\n')
        print ('%3d. %s' % (n, ' '.join(sent)))
    import datetime
    today = datetime.date.today()
    date = str(today).replace("-","")
    fileout = open(path+"_sent"+".txt", "w")
    for sent in generate(grammar, n=N):
        fileout.write(' '.join(sent)+"\n")
    fileout.close()

    
if __name__ == '__main__':
    demo()
