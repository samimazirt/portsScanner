# portsScanner

Description du projet 

L'objectif de ce projet est de développer un script Python qui peut être exécuté sur n'importe quel système Linux. Le script effectuera des scans de réseau en acceptant une adresse IP ou une plage d'adresses IP en tant que paramètre d'entrée. Les types de scans inclus sont ARP, ICMP, TCP et UDP. Le script doit également permettre la spécification de ports pour les scans TCP et UDP.

##################################

Fonctionnalités 

Le script doit prendre en charge les fonctionnalités suivantes : 

    * Accepter une adresse IP, une plage d'adresses IP ou une notation CIDR en tant que paramètre d'entrée. Exemples: mainscan.py -x [a,i,u,t] -ip 192.168.1.7-192.168.1.19 -p 89
    * Prendre en charge les types de scans suivants : 

    	- ARP scan avec l'option "-x a".

    	- ICMP scan avec l'option "-x i".

    	- TCP scan avec l'option "-x t".

    	- UDP scan avec l'option "-x u".

    * Si l'utilisateur utilise les options -t ou -u, accepter le paramètre -p pour spécifier les ports à scanner. Les notations de ports suivantes doivent être prises en charge: 

    	- "-p x" : scanner le port x. 

    	- "-p x,y" : scanner les ports x et y. 

    	- "-p x,y,..." : scanner tous les ports spécifiés, séparés par des virgules. 

    	- "-p x-y" : scanner tous les ports entre x et y. 

    	- "-p x-y,z" : prendre en charge la combinaison de plages et de ports spécifiques. 

    * Générer un rapport avec les résultats des scans. 

#######################################

Bonus 


Implémenter une interface graphique 


####################################

Contraintes techniques 

    * Le script doit être écrit en Python et compatible avec les systèmes Linux. 

    * Le script doit être bien documenté, y compris des commentaires explicatifs pour les parties clés du code. 

    * Le code doit être propre et respecter les bonnes pratiques de programmation. 

#######################################

Livrables 

Le projet doit inclure les éléments suivants : 

    * Git (script, readme, …) 

    * Le rapport généré par le script. 

    * Présentation. 

########################################

Calendrier 

Le projet devra être achevé avant le 27 novembre. 

############################################

Critères de réussite 

Le projet sera considéré comme réussi si toutes les fonctionnalités spécifiées sont implémentées de manière fonctionnelle, si le code est bien documenté et respecte les bonnes pratiques de programmation, et si le script est capable de générer des rapports précis et informatifs. 
