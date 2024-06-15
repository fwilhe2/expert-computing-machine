import glob
import json

# based on https://stackoverflow.com/a/52879570
# todo: see how this can be done with proper melange tooling

apk_index_files_json = glob.glob("**/APKINDEX.json", recursive=True)
output_list_json = []

for f in apk_index_files_json:
    with open(f, "rb") as infile:
        output_list_json.append(json.load(infile))

merged_apk_index_json = {}
all_packages = []
for json_file in output_list_json:
   all_packages.extend(json_file['Packages'])

merged_apk_index_json['Packages'] = all_packages

textfile_merged_json = open('repo/x86_64/APKINDEX.json', 'w')
textfile_merged_json.write(json.dumps(merged_apk_index_json))




apk_index_files = glob.glob("**/APKINDEX", recursive=True)
output_list = []

for f in apk_index_files:
    with open(f, "rb") as infile:
        output_list.append(infile)

merged = '\n'.join(output_list)

textfile_merged = open('apk-index-temp/APKINDEX', 'w')
textfile_merged.write(merged)