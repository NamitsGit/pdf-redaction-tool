import subprocess

filepath = 'statement_sample1-Copy1.PDF' # Can change the filename HERE

cmd = 'python3 fitzcli.py gettext '+filepath

p = subprocess.Popen(cmd)
