"""Copy the committed 2026-11-25 news front page to /output/entry.png (deterministic)."""
import os
import shutil

src = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'entry.png')
dst_dir = os.environ.get('MAKEFUN_OUTPUT_DIR', '/output')
os.makedirs(dst_dir, exist_ok=True)
shutil.copyfile(src, os.path.join(dst_dir, 'entry.png'))
print('entry.png written')
