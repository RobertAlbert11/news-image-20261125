"""Ship the committed front page: copy entry.png to the output dir, byte-exact.

Stdlib only. The render (gen_news.py) is done at build time; this script is
what the competition runner executes.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
src = os.path.join(HERE, 'entry.png')
out_dir = os.environ.get('MAKEFUN_OUTPUT_DIR', '/output')
os.makedirs(out_dir, exist_ok=True)
shutil.copyfile(src, os.path.join(out_dir, 'entry.png'))
print('entry.png ->', out_dir)
