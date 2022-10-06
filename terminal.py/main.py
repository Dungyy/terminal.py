import time

print("\nI N I S I A T I N G    S Y S T E M")
print("------------------------------------")
time.sleep(0.3)
print("Updating all the services ..\n")
time.sleep(0.3)
print("IP Address FOUND -> 192.168.200.100 \n")
time.sleep(0.3)
print("All Set! System load completed.\n")
time.sleep(0.3)
print("Launching the Machine ...\n")
time.sleep(0.5)

from rich.progress import Progress
from rich import align

with Progress() as progress:
    task1 = progress.add_task("[blue]ACTIVATING HACKER DUNGY ...", total=1000)
    #    task2 = progress.add_task("[white]Processing...", total=1000)
    #    task3 = progress.add_task("[green]Cooking...", total=1000)

    while not progress.finished:
        progress.update(task1, advance=7)
        #        progress.update(task2, advance=2.5)
        #        progress.update(task3, advance=2)
        time.sleep(0.02)