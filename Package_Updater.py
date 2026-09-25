
# %%
from update_helpers import get_updates, to_update, updates
import subprocess


# %%
# testing purposes so I don't acidently forget to set versions
subprocess.run(['pip', 'install', 'idna==3.16','six==1.16'])


# %%

## TO DO
# run file thorugh pep 8 checker (or look up pep 8)


# these are just an example of the functions to do a quick check

current = get_updates()

print('Before', current)

to_keep = []

change = to_update(current, to_keep)

updates(change)

print('after', get_updates())



