import glob
import json
from pathlib import Path

# based on https://stackoverflow.com/a/52879570
# todo: see how this can be done with proper melange tooling

apk_index_files_json = glob.glob("**/APKINDEX.json", recursive=True)
output_list_json = []

for f in apk_index_files_json:
    print(f)
    with open(f, "rb") as infile:
        output_list_json.append(json.load(infile))

merged_apk_index_json = {}
all_packages = []
for json_file in output_list_json:
   all_packages.extend(json_file['Packages'])

merged_apk_index_json['Packages'] = all_packages

textfile_merged_json = open('repo/x86_64/APKINDEX.json', 'w')
textfile_merged_json.write(json.dumps(merged_apk_index_json))


apk_index_files = glob.glob("**/*-APKINDEX", recursive=True)

out = ''

for f in apk_index_files:
    print(f)
    out = out + Path(f).read_text() + '\n'

print(out)

textfile_merged = open('repo/x86_64/APKINDEX', 'w')
textfile_merged.write(out)