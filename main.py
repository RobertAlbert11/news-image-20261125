"""Ship the committed front page: copy entry.png to the output dir, byte-exact.

Stdlib only. The render (gen_news.py) happens at build time; this script is
what the competition runner executes. It resolves the source next to itself,
creates the destination directory if needed, copies the file, then verifies
the destination byte-for-byte against the source, fsyncs it, and prints the
result. Any failure exits non-zero.
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.environ.get('MAKEFUN_OUTPUT_DIR', '/output')


def main():
    src = os.path.join(HERE, 'entry.png')
    os.makedirs(OUT, exist_ok=True)
    dst = os.path.join(OUT, 'entry.png')
    shutil.copyfile(src, dst)
    with open(src, 'rb') as a, open(dst, 'rb') as b:
        if a.read() != b.read():
            sys.exit('ERROR: {} does not match source {}'.format(dst, src))
    with open(dst, 'rb') as f:
        os.fsync(f.fileno())
    print('entry.png ->', OUT, '(verified byte-identical)')


if __name__ == '__main__':
    main()
