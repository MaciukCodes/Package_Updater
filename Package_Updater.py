# %%
import subprocess
import json

# %%
# testing purposes so I don't acidently forget to set versions
subprocess.run(['pip', 'install', 'idna==3.16','six==1.16'])

# %%
def get_updates():
    dusty_old = subprocess.run(['pip', 'list', '--outdated','--format=json'], capture_output=True, text=True).stdout
    clean_old = json.loads(dusty_old)

    return clean_old
    
def to_update(clean_old, to_keep):
    change = []

    for row in clean_old:
        # atm to_keep  only takes a list of the names of packages 
        if row['name'] not in to_keep:
            change.append(row)

    return change

def updates(change):
    for package in change:
        subprocess.run(['pip','install', package['name'], '-U', '--upgrade'])
    


current = get_updates()

print('Before', current)

to_keep = ['idna']

change = to_update(current, to_keep)

updates(change)

print('after', get_updates())

# def update(change):


