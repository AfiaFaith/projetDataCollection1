# projetDataCollection1
Premier projet de data collection

Nous avons utilisé Python 3.10.6.64 bits pour compiler nos codes. Pour la creation de la base de données on a utilisé MySQL. Pour pouvoir tester ou utiliser ce projet ; vous aurez besoin d’installer les différentes librairies python nécessaire comme pandas ,requests …
Le dossier est structuré de la manière suivante:
ProjectDC: qui est le dossier de base
	DATABASES: contient les différentes sources de données utilisées dans le projet
	MODULE5: contient les codes répondant aux différentes questions posées dans le projet ( dans le fichier a_faire.txt)
		Le fichier countries.py contient le code utilisé pour collecter les informations des pays et drapeaux sur le site web: 'https://restcountries.com/v2/all' 
		Le fichier database.py contient le code permettant d’établir une connexion entre la base contenant les informations collectées au cours du projet et les stocker dans la table : ‘tb_projet’
		Les fichiers datacsv.py , datajson.py et datahlml.py contiennent les données collectées à partir des fichiers contenus dans le dossier DATABASES 
		Le fichier factories permet de faire la concaténation entre les données contenues dans datacsv.py , datajson.py et datahlml.py
		Le fichier runcode.py contient les codes pour compiler le code du fichier factories
		Le fichier devisesbceao.py contient le code pour collecter les données demandées par le projet sur le site web de la BCEAO (PATH_URL = 'cours/cours-des-devises-contre-Franc-CFA-appliquer-aux-transferts') 
		Le fichier rest_countries.py permet de faire un mapping entre les pays sélectionnés et leur drapeaux et aussi de stocker ces informations dans une base de données MySQL.
		



