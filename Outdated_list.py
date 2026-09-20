
import subprocess

outdated = subprocess.run(['pip', 'list', '--outdated'], capture_output=True, text=True)

print(outdated.stdout)
