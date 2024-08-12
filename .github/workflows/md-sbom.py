import glob
import json
from pathlib import Path

sbom_files = glob.glob("rootfs/var/lib/db/sbom/*.json")

print("# SBOM")

print("| Package Name | Version | Declared Licenses |")
print("| --- | --- | --- |")

for f in sbom_files:
    with open(f, 'r') as ff:
        sbom = json.load(ff)
        packages = sbom['packages']
        for p in packages:
            print(f"| {p['name']} | {p['versionInfo']} | {p['licenseDeclared']} |")