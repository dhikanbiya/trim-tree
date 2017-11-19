import sys
import glob


def get_files(path):
    p = path + '/**/*.txt'
    pt = list()
    for filename in glob.iglob(p, recursive=True):
        # file += os.path.basename(filename).split()
        pt += filename.split()
    return pt


if __name__ == '__main__':
    get_files(sys.argv[1])
