import os
import subprocess
import re

saxon_jar = "./SaxonHE12-5J/saxon-he-12.5.jar"  # Remplacez par le chemin vers le fichier saxon9he.jar
xsl_file = "./Stylesheets-master/start-txt.xsl"  # Remplacez par votre fichier XSL
corpus = 'corpus/DDB_EpiDoc_XML/'
path_list = []

for root, dirs, files in os.walk(corpus):
    if len(files)>0:
        path_list.append(root)
if not os.path.isdir('training_texts/'):
    os.makedirs('training_texts/')
for root in path_list:
    inputdir = root
    outdir = re.sub('^corpus/', 'training_texts/', root)
    if not os.path.isdir(outdir):
        os.makedirs(outdir)
    #print(root)
    command = [
        "java", "-jar", saxon_jar,
        "-s:" + root,
        "-xsl:" + xsl_file,
        "-o:" + outdir
    ]

    # Exécuter la commande
    subprocess.run(command, check=True)
    