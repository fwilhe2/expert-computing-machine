import glob
import json
from pathlib import Path

# based on https://stackoverflow.com/a/52879570
# todo: see how this can be done with proper melange tooling

def merge_json(platform):
    apk_index_files_json = glob.glob("**/{platform}/APKINDEX.json", recursive=True)
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

    textfile_merged_json = open(f'repo/{platform}/APKINDEX.json', 'w')
    textfile_merged_json.write(json.dumps(merged_apk_index_json))

def merge_plain(platform):
    apk_index_files = glob.glob(f"**/*-APKINDEX-{platform}", recursive=True)

    out = ''

    for f in apk_index_files:
        print(f)
        out = out + Path(f).read_text() + '\n'

    print(out)

    textfile_merged = open(f'repo/{platform}/APKINDEX', 'w')
    textfile_merged.write(out)

merge_json('x86_64')
merge_json('aarch64')

merge_plain('x86_64')
merge_plain('aarch64')
