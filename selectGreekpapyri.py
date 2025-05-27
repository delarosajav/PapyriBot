import sqlite3
import re
import os
import shutil

con = sqlite3.connect('LPHD.db')
cur = con.cursor()

sql_fisgreek = '''SELECT DDB_isGREEK.ID_DDB, DDB_fpath.fpath 
    FROM DDB_isGREEK 
    INNER JOIN DDB_fpath 
    ON DDB_isGREEK.ID_DDB=DDB_fpath.ID_DDB 
    WHERE IsGreek="yes";'''

res_fisgreek = cur.execute(sql_fisgreek)
fisgreek = res_fisgreek.fetchall()

if not os.path.isdir('training_texts2'):
    os.makedirs('training_texts2')
for idpap, path in fisgreek:
    corpusf = re.sub('^idp\.data', 'training_texts', path)
    corpusf = re.sub('xml$', 'txt', corpusf)
    nfname = 'training_texts2/'+ re.search('[^/]+\.txt', corpusf).group(0)
    if os.path.exists(corpusf):
        shutil.copyfile(corpusf, nfname)

