import os
import re


corpus = 'training_texts/DDB_EpiDoc_XML/'

path_list = []
for root, dirs, files in os.walk(corpus):
    if len(files)>0:
        #print(root)
        path_list.append(root)

for p in path_list:
    froot = p +'/'
    for f in os.listdir(p):
        fin = froot+f
        fout = re.sub('xml$', 'txt', fin)
        print(fout)
        os.rename(fin, fout)
