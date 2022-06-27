import os
import secrets
import shutil
import sys


def getalllist(path: str):
    all_dir = []
    all_file = []
    for root, dirs, files in os.walk(path, followlinks=False):
        for name in dirs:
            all_dir.append(os.path.join(root, name))
        for name in files:
            all_file.append(os.path.join(root, name))
    return all_dir, all_file


def clean(odir: list, ofile: list, path: str):
    all_dir, all_file = getalllist(path)
    n_ad = list(set(all_dir) - set(odir))
    n_af = list(set(all_file) - set(ofile))
    n_ad.sort()
    for path in n_af:
        try:
            os.remove(path)
        except:
            pass
    for path in n_ad:
        try:
            shutil.rmtree(path)
        except:
            pass


s_name = sys.argv[1]
print('运行期间切勿对目录进行操作!\n----------------------------')
currentpath = os.getcwd()
if s_name[len(s_name) - 1] == 'w':
    d_name = 'X' + secrets.token_hex(16) + '.pyw'
else:
    if s_name[len(s_name) - 1] == 'y':
        d_name = 'X' + secrets.token_hex(16) + '.py'
    else:
        print('\n文件格式不支持！\n')
        os.system('pause')
        sys.exit()
o_dir, o_file = getalllist(currentpath)
o_file.append(os.path.join(currentpath, s_name.strip('.py').strip('.pyw') + '.exe'))
try:
    try:
        with open(s_name, 'r', encoding="utf-8") as f_r:
            code = f_r.readlines()
    except:
        with open(s_name, 'r') as f_r:
            code = f_r.readlines()
except:
    print('\n无法打开文件！\n')
    os.system('pause')
    sys.exit()
f_w = open(d_name, 'a+')
for line in code:
    while 1:
        if line.startswith('    '):
            line = line.replace('    ', '', 1)
        else:
            break
    if line.startswith('import ') or line.startswith('from '):
        f_w.write(line)
t_name = 'X' + secrets.token_hex(16)
f_w.write('import %s\n%s' % (t_name, t_name))
f_w.close()
os.system('echo F | XCOPY %s %s' % (s_name, t_name + '.py'))
os.system('cythonize -3 -i -f %s' % (t_name + '.py'))
os.system('del %s' % (t_name + '.py'))
os.system('pyinstaller -F -i "NONE" --key=%s %s' % (secrets.token_hex(8), d_name))
os.system('copy dist\\%s.exe %s' % (d_name.strip('.py').strip('.pyw'), s_name.strip('.py').strip('.pyw') + '.exe'))
clean(o_dir, o_file, currentpath)
print('----------------------------')
os.system('pause')
