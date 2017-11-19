import sys
def main(fl):
    s_variables = ['mysql_query', 'pg_query', 'sqlite_query','sql']
    s_sans = ['mysql_real_escape_string', 'pg_escape_string' 'sqlite_escape_string']

    nw_fl = []
    vul = [f.strip() for f in open(fl).readlines()]
    for i,f in enumerate(vul):
        for s in s_variables:
            if f.find(s) > 0:
                print('line',i,fl[i])
                # nw_fl.append(fl)
            else:
                print(f)
                print("not found")

if __name__ == '__main__':
    fl = sys.argv[1]
    main(fl)
