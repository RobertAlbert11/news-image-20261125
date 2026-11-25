"""Ship the committed front page: copy entry.png to the output dir, byte-exact.

Stdlib only. The render (gen_news.py) is done at build time; this script is
what the competition runner executes. After copying, the destination is
verified byte-for-byte against the source and fsynced before exit.
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
src = os.path.join(HERE, 'entry.png')
dst = os.path.join(os.environ.get('MAKEFUN_OUTPUT_DIR', '/output'), 'entry.png')

os.makedirs(os.path.dirname(dst), exist_ok=True)
shutil.copyfile(src, dst)

if not os.path.isfile(dst):
    sys.exit('ERROR: copy failed, {} was not created'.format(dst))
if open(src, 'rb').read() != open(dst, 'rb').read():
    sys.exit('ERROR: {} does not match source {} byte-for-byte'.format(dst, src))

with open(dst, 'rb') as f:
    os.fsync(f.fileno())
print('entry.png ->', os.path.dirname(dst), '(verified byte-identical)')
