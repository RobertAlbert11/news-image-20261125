"""Ship the committed front page: copy entry.png to the output dir, byte-exact.

Round-5 edition. Stdlib only. The render (gen_news.py) happens at build time;
this script is what the competition runner executes.
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.environ.get('MAKEFUN_OUTPUT_DIR', '/output')


def main():
    src = os.path.join(HERE, 'entry.png')
    if not os.path.isfile(src):
        sys.exit('ERROR: source entry.png missing at {}'.format(src))
    os.makedirs(OUT, exist_ok=True)
    dst = os.path.join(OUT, 'entry.png')
    shutil.copyfile(src, dst)
    with open(src, 'rb') as a, open(dst, 'rb') as b:
        if a.read() != b.read():
            sys.exit('ERROR: {} does not match source {}'.format(dst, src))
    with open(dst, 'rb') as f:
        os.fsync(f.fileno())
    print('entry.png ->', OUT, '(verified byte-identical, {})'.format(
        os.path.getsize(dst)))


if __name__ == '__main__':
    main()
