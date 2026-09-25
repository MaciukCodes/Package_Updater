# %%
import subprocess
import json

# %%
def get_updates():
    '''Creates an object with a dictionary loaded with the packages that are out of date inside the environment it was ran in'''

    dusty_old = subprocess.run(['pip', 'list', '--outdated','--format=json'], capture_output=True, text=True).stdout
    clean_old = json.loads(dusty_old)

    return clean_old
    
def to_update(clean_old, to_keep):
    '''Takes a list of dictionaries and a list, of the old packages and ones to keep, and consolidates them into a dictionary of packages to update.
    
        Args:
            clean_old: list of dictionaries containing the keys:
                                                               name,
                                                               version,
                                                               latest_version,
                                                               latest_filetype
            
            to_keep: list of packages to remove fromt the dictioary.
        
                                                
        Returns:
            change: List of dictionaries with the same format as clean_old without the packages described in to_keep.
            '''
    
    change = []

    for row in clean_old:
        if row['name'] not in to_keep:
            change.append(row)

    return change

def updates(change):
    '''Takes the list of dictioaries and updates them to their latest version.'''
    for package in change:
        subprocess.run(['pip','install', package['name'], '-U', '--upgrade'])