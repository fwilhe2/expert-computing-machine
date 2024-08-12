import glob
import json
from pathlib import Path

sbom_files = glob.glob("rootfs/var/lib/db/sbom/*.json")

package_list = []

for f in sbom_files:
    with open(f, 'r') as ff:
        sbom = json.load(ff)
        packages = sbom['packages']
        for p in packages:
            package_list.append(f"| {p['name']} | {p['versionInfo']} | {p['licenseDeclared']} |")

package_list.sort()

print("# SBOM")

print("| Package Name | Version | Declared Licenses |")
print("| --- | --- | --- |")

for p in package_list:
    print(p)
