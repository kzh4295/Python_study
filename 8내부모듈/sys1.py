import sys

#파일만 올렸으니, 파일에서 클리어를 찾아 사용
import mysys
mysys.clear()

# 파일에서 clear를 올렸으니 클리어만 바로 사용하면 됨
from mysys import clear
clear()

print(sys.argv, len(sys.argv))

def print_sys_vars():
  for i in [sys.version, sys.copyright, sys.platform]:
    print("--->", i)

sa = sys.argv
