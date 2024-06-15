import glob
import json

# based on https://stackoverflow.com/a/52879570
# todo: see how this can be done with proper melange tooling

apk_index_files = glob.glob("**/APKINDEX.json", recursive=True)
output_list = []

for f in apk_index_files:
    with open(f, "rb") as infile:
        output_list.append(json.load(infile))

merged_apk_index = {}
all_packages = []
for json_file in output_list:
   all_packages.extend(json_file['Packages'])

merged_apk_index['Packages'] = all_packages

textfile_merged = open('repo/APKINDEX.json', 'w')
textfile_merged.write(json.dumps(merged_apk_index))