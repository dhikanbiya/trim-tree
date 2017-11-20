import sys
import subprocess
from list_files import get_files

def main(i,f,dest):
    cmd = "php remove_comments.php " + f + " " + dest + " " + str(i)
    #call php script
    print(f)
    proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    script_response = proc.stdout.read()

if __name__ == '__main__':
    src = get_files(sys.argv[1])
    dest = sys.argv[2]
    for i,f in enumerate(src):
        main(i,f,dest)
