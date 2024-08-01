import os
import subprocess
import mido
from mido import MidiFile
import time
import threading

os.environ['TERM'] = 'xterm-256color'

def get_cwd():
        return os.getcwd()

def navigate():
        listdir = []
        x = 0
        for path in os.listdir(get_cwd()):
                if path == ".idea":
                        pass
                if path[0] == ".":
                        pass
                elif path == "main.py":
                        pass
                elif path == "CPUA.sh":
                        pass
                elif path == "cdpy.py":
                        pass
                elif path == "venv":
                        pass
                elif path == "__pycache__":
                        pass
                elif path == ".DS_Store":
                        pass
                elif path == "code":
                        pass
                else:
                        x += 1
                        print(x, path)
                        listdir.append(path)
        x = int(input()) - 1
        subprocess.call("clear")
        x = listdir[x]
        if os.path.isdir(x) == True:
                os.chdir(x)
                navigate()
        if os.path.isfile(x) == True:
               return x

cores = os.cpu_count()
totalpercent = cores * 100
output = []
output2 = []
output3 = []
output4 = []
subprocess.call("clear")


def find_5_highest(numbers):
    numbers.sort()
    numbers = numbers[-5:]
    numbers = mean(numbers)
    numbers2 = (numbers / totalpercent) * 100
    numbers = round(numbers)
    numbers2 = round(numbers2)
    return numbers, numbers2


def find_10_highest(numbers):
    numbers.sort()
    numbers = numbers[-10:]
    numbers = mean(numbers)
    numbers2 = (numbers / totalpercent) * 100
    numbers = round(numbers)
    numbers2 = round(numbers2)
    return numbers, numbers2


def find_25_highest(numbers):
    numbers.sort()
    numbers = numbers[-25:]
    numbers = mean(numbers)
    numbers2 = (numbers / totalpercent) * 100
    numbers = round(numbers)
    numbers2 = round(numbers2)
    return numbers, numbers2


def convert_to_float(numbers):
    for z in range(len(numbers)):
        numbers[z] = float(numbers[z])
    return numbers


def mean(numbers):
    return sum(numbers) / len(numbers)


def outliers(numbers):
    numbers.sort()
    numbers = numbers[-1]
    numbers2 = (numbers / totalpercent) * 100
    return numbers, numbers2


user = subprocess.check_output('whoami').decode('utf-8')
user = user.splitlines()[0]
print('Welcome to the CPU Usage Analyzer ' + user + '!', "\n")

port = mido.open_output(name='foo', virtual=True)

# Choose MIDI Port
x = 0
for port in mido.get_output_names():
    x += 1
    print(x, port)
print()
port = int(input("Which port do you want to use? \n"))
subprocess.call("clear")
uport = mido.open_output(mido.get_output_names()[port - 1])

# Choose MIDI File
print("Navigate to the midi file do you want to use: ")
mid = navigate()
subprocess.call("clear")
mid = MidiFile(mid)
mid.type = 1

# Choose a PID to use
print("Which PID do you want to use?")
PID = subprocess.check_output('top -l 2 -ncols 2 -n 10 -user '+ user, shell=True).decode('utf-8').splitlines()[33:]
PID = [i.split() for i in PID]
for i in PID:
    print(' '.join(i))
UPID = input()
subprocess.call("clear")
UPID = int(UPID)


def get_cpu_usage():
    output = subprocess.check_output('top -pid ' + str(UPID) + ' -stats cpu -l 200 -s 0 -i 2', shell=True).decode(
        'utf-8').splitlines()
    output = output[12:]
    for i in output:
        output2.append(i.strip())
    output3 = output2[::13]
    output3 = output3[3:-3]
    for i in output3:
        output4.append(float(i))
    return output3


def play_midi():
    time.sleep(3)
    print("MIDI Started")
    for msg in mid.play():
        uport.send(msg)
    print("MIDI Ended")
    return None


def run_process():
    subprocess.call("clear")
    print('This machine has ' + str(cores) + ' cores.', "\n")
    print('CPU Usage Per Core')
    print('Highest Value: ', outliers(output4)[0])
    print('Avg of top 25: ', find_25_highest(output4)[0])
    print('Avg of top 10: ', find_10_highest(output4)[0])
    print('Avg of top 5: ', find_5_highest(output4)[0], "\n")
    print('CPU Usage For Whole System')
    print('Highest Value: ', outliers(output4)[1])
    print('Avg of top 25: ', find_25_highest(output4)[1])
    print('Avg of top 10: ', find_10_highest(output4)[1])
    print('Avg of top 5: ', find_5_highest(output4)[1])
    return None


def threadingfunc():
    print("Test Started")
    Thread1 = threading.Thread(target=get_cpu_usage)
    Thread2 = threading.Thread(target=play_midi)
    Thread1.start()
    Thread2.start()
    Thread1.join()
    Thread2.join()
    subprocess.call("clear")
    return None


threadingfunc()
run_process()
