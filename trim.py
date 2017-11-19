import sys
import os

def vul_type(vt):
    variables = []
    sans = []
    if vt == 'sqli':
        variables = ['mysql_query', 'pg_query', 'sqlite_query', 'sql']
        sans = ['mysql_real_escape_string','pg_escape_string' 'sqlite_escape_string', 'escape','mysql_escape']
    elif vt == 'xss':
        variables = ['_GET', '_POST', '_COOKIE', '_REQUEST', '_SERVER', '_FILES']
        sans = ['htmlspecialchars', 'htmlentities', 'strip_tags']
    
    return variables,sans

def trim(fl,path,vt): 
    vr,sns = vul_type(vt)
    nw_fl = []
    name = os.path.basename(fl)
    # vul = [f.strip() for f in open(fl).readlines()]
    with open(fl, 'rb') as f:
        ln = f.read()
        vul = ln.decode('utf-8', 'replace').splitlines()

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
    rs = path+'/'+name+'_trimmed.txt'
    with open(rs,'w') as res:
        for rr in result:
            res.write(rr+"\n")
    print(rs)

if __name__ == '__main__':
    fl = sys.argv[1]
    path = sys.argv[2]
    vt = sys.argv[3]
    
    trim(fl,path,vt)
