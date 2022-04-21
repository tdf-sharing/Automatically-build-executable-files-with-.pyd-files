import os
import secrets
import sys

s_name = sys.argv[1]
os.chdir(os.getcwd())
if s_name[len(s_name) - 1] == 'w':
    d_name = 'FINAL.pyw'
else:
    if s_name[len(s_name) - 1] == 'y':
        d_name = 'FINAL.py'
    else:
        print('\n文件格式不支持！\n')
        os.system('pause')
        sys.exit()
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
    if line.find('import') != -1 or line == '\n':
        f_w.write(line)
    else:
        break
f_w.write('import UNF\nUNF')
f_w.close()
os.system('echo F | XCOPY %s UNF.py' % s_name)
os.system('cythonize -3 -i -f UNF.py')
os.system('del UNF.py')
os.system('ren UNF.*.pyd UNF.pyd')
os.system('pyinstaller -F -i "NONE" --key=%s %s' % (secrets.token_hex(8), d_name))
os.system('copy dist\\FINAL.exe %s' % s_name.strip('.py').strip('.pyw') + '.exe')
os.system('del %s' % d_name)
os.system('del FINAL.spec')
os.system('del UNF.c')
os.system('del UNF.pyd')
os.system('rd /S /Q dist')
os.system('rd /S /Q build')
os.system('rd /S /Q __pycache__')
print('---------------------')
os.system('pause')
