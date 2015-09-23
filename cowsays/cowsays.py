import random
import subprocess
import sys

def main(file):
    line = random.choice(open(file).readlines()).rstrip().replace('\"','\'')
    cmd = "cowsay \"%s\" | lolcat" % line
    subprocess.call("clear", shell=True)
    subprocess.call(cmd, shell=True)

if __name__ == '__main__':
   main(str(sys.argv[1]))
