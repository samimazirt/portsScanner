import tkinter as tk
from tkinter import ttk, font
import subprocess

def execute_scan():
    # Recup de chaque champ
    scan_type = scan_type_var.get()
    ip_address = ip_address_entry.get()
    port = port_entry.get()

    # Correspondre chaque scan à sa lettre (pour l'execution de la ligne de commande)
    scan_type_mapping = {"TCP": "t", "UDP": "u", "ARP": "a", "ICMP": "i"}
    scan_type_code = scan_type_mapping.get(scan_type, "")

    # Vérifier si le scan est ICMP ou ARP pour ne pas inclure de port
    if scan_type_code in ["i", "a"]:
        port = ""

    # Construire la commande pour exécuter le scan
    command = f"sudo python3 mainscan.py -x {scan_type_code} -i {ip_address} -p {port}"
    result = subprocess.getoutput(command)

    # Afficher la zone d'output, effacer son contenu et y insérer le résultat
    output_text.config(state=tk.NORMAL)
    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, f"{result}")
    output_text.config(state=tk.DISABLED)

def clear_output():
    output_text.config(state=tk.NORMAL)
    output_text.delete(1.0, tk.END)
    output_text.config(state=tk.DISABLED)

def new_scan():
    # Effacer l'output, les champs IP et port, et définir le type de scan sur ICMP par défaut
    clear_output()
    ip_address_entry.delete(0, tk.END)
    port_entry.delete(0, tk.END)
    scan_type_combobox.set("ICMP")

# Créer la fenêtre principale
root = tk.Tk()
root.title("Analyseur de Ports")

# Appliquer un thème sombre
style = ttk.Style()
style.theme_use("clam")

# Configurer un mode sombre pour le widget de texte et la police
style.configure("TText", background="black", foreground="white")
output_text_font = tk.font.Font(family='Courier', size=10)

# Créer et positionner les widgets et boutons
scan_type_label = ttk.Label(root, text="Type de Scan :")
scan_type_var = tk.StringVar()
scan_type_combobox = ttk.Combobox(root, textvariable=scan_type_var, values=["ICMP", "TCP", "UDP", "ARP"])
scan_type_combobox.set("ICMP")

ip_address_label = ttk.Label(root, text="Entrer l'Adresse IP ou la Plage :")
ip_address_entry = ttk.Entry(root, font=('Arial', 12))

port_label = ttk.Label(root, text="Entrer le Port ou la Plage de Ports :")
port_entry = ttk.Entry(root, font=('Arial', 12))

scan_button = ttk.Button(root, text="Analyser", command=execute_scan, style="TButton")

output_text = tk.Text(root, height=10, width=80, state=tk.DISABLED, font=output_text_font)

rescan_button = ttk.Button(root, text="Nouveau Scan", command=execute_scan, style="TButton")
clear_button = ttk.Button(root, text="Effacer", command=clear_output, style="TButton")
new_scan_button = ttk.Button(root, text="Nouvelle Analyse", command=new_scan, style="TButton")

# Disposition de la grille
scan_type_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
scan_type_combobox.grid(row=0, column=1, padx=10, pady=5, sticky="w")

ip_address_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
ip_address_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")

port_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
port_entry.grid(row=2, column=1, padx=10, pady=5, sticky="w")

scan_button.grid(row=3, column=0, columnspan=2, pady=10)

output_text.grid(row=4, column=0, columnspan=2, padx=10, pady=5, sticky="w")

rescan_button.grid(row=5, column=0, pady=5)
clear_button.grid(row=5, column=1, pady=5)
new_scan_button.grid(row=6, column=0, columnspan=2, pady=10)

# Exécuter la boucle principale de Tkinter
root.mainloop()

