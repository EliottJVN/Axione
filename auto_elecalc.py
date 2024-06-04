import pyautogui
import time
pyautogui.FAILSAFE = False

time.sleep(2)
sleep = 1

coord = {
    'white_project' : (257,447),
    'norme' : (1870, 114),
    'create_project' : (1713, 245),
    'power_source' : (339, 333),
    'power_source_nom' : (250, 650),
    'close_power_source_nom' : (250, 716),
    'EC_menu':(28,32),
    'Note_calc':(100,350),
    'gene_rapp':(280,830),
    'save':(276,888)
}

# Attendre 2 secondes avant d'exécuter l'action
time.sleep(sleep)

def move(posi):
    pyautogui.moveTo(posi[0],posi[1])

def click(posi):
    move(posi)
    pyautogui.click(button='left')
    time.sleep(sleep)
    
# Creer le projet
click(coord['white_project'])
click(coord['create_project'])

# Exemple creer des composants
click(coord['power_source'])
click(coord['power_source_nom'])
pyautogui.click(clicks=2)
pyautogui.write('50', interval=0.2)
click(coord['close_power_source_nom'])

# Génération de NDC
click(coord['EC_menu'])
click(coord['Note_calc'])
click(coord['gene_rapp'])
time.sleep(sleep)
time.sleep(sleep)
click(coord['save'])

pyautogui.write('NDC Axione', interval=0.1)