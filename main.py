import sys
from list_files import get_files
from trim import *

def main(f,gen_path,vul):
    trim(f,gen_path,vul)

if __name__ == '__main__':    
    tr_path = get_files(sys.argv[1])
    gen_path = sys.argv[2]
    vul = sys.argv[3]
    for f in tr_path:
        main(f,gen_path,vul)
    

