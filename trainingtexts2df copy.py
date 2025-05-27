import os
import pandas as pd
#from cltk.languages.pipelines import GreekPipeline
#from cltk import NLP
import regex

#model_gk = GreekPipeline()
#print(model_gk.processes)

"""nlp_gk = NLP(language='grc')
nlp_gk.pipeline.processes.pop(-1)
nlp_gk.pipeline.processes.pop(-1)"""
#print(nlp_gk.pipeline.processes)
def tok(text):
    txt_files = 'training_texts2/'
    dict = {'text': [], 'text_':[]}
    for f in os.listdir(txt_files):
        fpath = txt_files+f
        raw = open(fpath).read()
        noblank = regex.sub('^\s+', '', raw)
        noblank = regex.sub('\s+$', '', noblank)
        if len(noblank)>0:
            toks = regex.split('\s', noblank)
            ntoks = []
            for tok in toks:
                if regex.search('.+[·.,]$',tok):
                    #print(regex.search('.+[·.,]$',tok).group(0))
                    groups_re = '(?P<tok1>.+)(?P<tok2>[·.,])$'
                    groups = regex.match(groups_re, tok)
                    tok1 = groups.group('tok1')
                    tok2 = groups.group('tok2')
                    if regex.fullmatch('[.]+', tok1):
                        ntoks.append(tok)
                        #print(tok)
                    else:
                        ntoks+=[tok1, tok2]
                    #print(groups.groupdict())
                elif len(tok)==0:
                    continue
                else:
                    ntoks.append(tok)
            print(ntoks, '\n\n\n')
            #print(toks)
            #cltk_doc = nlp_gk.analyze(text=noblank)
            #print(f'\nINPUT:\n{noblank}\n\nOUTPUT:\n{ntoks}\n')
            
