import sys

def vul_type(vt):
    variables = []
    sans = []
    if vt == 'sqli':
        variables = ['mysql_query', 'pg_query', 'sqlite_query', 'sql']
        sans = ['mysql_real_escape_string','pg_escape_string' 'sqlite_escape_string', 'escape']
    elif vt == 'xss':
        variables = ['_GET', '_POST', '_COOKIE', '_REQUEST', '_SERVER', '_FILES']
        sans = ['htmlspecialchars', 'htmlentities', 'strip_tags']
    
    return variables,sans

def main(fl,vt): 
    vr,sns = vul_type(vt)
    nw_fl = []
    vul = [f.strip() for f in open(fl).readlines()]
    for i,f in enumerate(vul):
        for s in vr:
            if f.find(s) > 0:
                # print('line',i,vul[i])
                nw_fl.append(vul[i])
            # else:
            #     print(f)
            #     print("not found")
    # print(nw_fl)
    
    excl = []
    for ii, nw in enumerate(nw_fl):
        for san in sns:
            if nw.find(san) > 0:
               excl.append(nw_fl[ii])
    
    result = [r for r in nw_fl if r not in excl]
    # print("========")
    print(result)

if __name__ == '__main__':
    vt = sys.argv[2]
    fl = sys.argv[1]
    main(fl,vt)
