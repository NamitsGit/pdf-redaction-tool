import subprocess

filepath = 'statement_sample1-Copy1.PDF' # Can change the filename HERE

cmd = 'python3 fitzcli.py gettext '+filepath

p = subprocess.Popen(cmd)
# out, err = p.communicate()
# result = out.split('\n')
# for lin in result:
#     if not lin.startswith('#'):
#         print(lin)