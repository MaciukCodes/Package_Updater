
# %%
# Sorry if this import hurts just give me the giggles to do it
from func_update import get_updates, to_update, updates, subprocess


# testing purposes so I don't acidently forget to set versions
subprocess.run(['pip', 'install', 'idna==3.16','six==1.16'])

# def update(change):

# %%
current = get_updates()

print('Before', current)

to_keep = ['six']

change = to_update(current, to_keep)

updates(change)

print('after', get_updates())



