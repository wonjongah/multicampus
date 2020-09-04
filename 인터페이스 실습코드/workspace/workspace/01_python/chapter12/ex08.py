import sys

syst = {"버전":sys.version, "플랫폼":sys.platform, "바이트경로":sys.byteorder, "모듈경로":sys.path}


for a, b in syst.items():
    print(a, b)

for path in sys.path:
    print(path)

sys.exit(-1)

# exit(종료코드) 이후에는 못씀 sys

print(sys.path)