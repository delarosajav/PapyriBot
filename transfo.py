import os
import subprocess


# Chemins d'entrée et sortie
input_directory = "./corpus"  # Remplacez par le chemin du dossier contenant les fichiers XML
xsl_file = "./Stylesheets-master/start-txt.xsl"  # Remplacez par votre fichier XSL
output_directory = "./txt"  # Remplacez par le dossier où stocker les fichiers TXT
saxon_jar = "./SaxonHE12-5J/saxon-he-12.5.jar"  # Remplacez par le chemin vers le fichier saxon9he.jar

# Fonction pour appliquer la transformation et maintenir la structure des sous-dossiers
def transform_xml_files(input_dir, output_dir):
    for root, dirs, files in os.walk(input_dir):  # Parcours du répertoire source
        for file in files:
            if file.endswith(".xml"):  # Seulement les fichiers XML
                xml_file_path = os.path.join(root, file)
                
                # Crée un chemin de sortie correspondant à la structure du répertoire source
                relative_path = os.path.relpath(root, input_dir)  # Chemin relatif
                output_subdir = os.path.join(output_dir, relative_path)  # Crée le sous-dossier dans le répertoire de sortie
                os.makedirs(output_subdir, exist_ok=True)  # Crée les sous-dossiers si nécessaire
                
                # Chemin de sortie pour le fichier transformé
                output_file_path = os.path.join(output_subdir, file.replace(".xml", ".txt"))
                
                try:
                    # Commande Java pour exécuter Saxon
                    command = [
                        "java", "-jar", saxon_jar,
                        "-s:" + xml_file_path,
                        "-xsl:" + xsl_file,
                        "-o:" + output_file_path
                    ]
                    
                    # Exécuter la commande
                    subprocess.run(command, check=True)
                    print(f"Transformation appliquée à {xml_file_path} -> {output_file_path}")
                    
                except subprocess.CalledProcessError as e:
                    print(f"Erreur lors de la transformation du fichier {xml_file_path}: {e}")

# Exécuter la transformation
transform_xml_files(input_directory, output_directory)