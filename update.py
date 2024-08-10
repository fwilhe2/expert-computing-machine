import sys
import requests
import json
import urllib.request
import hashlib

from yaml import load, dump
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

if __name__ == '__main__':
    package = sys.argv[1]
    file_content = ''
    old_version = ''
    new_version = ''
    old_sha = ''
    new_sha = ''
    with open(f'manifests/{package}.yaml', 'r') as f:
        file_content = str(f.read())
    with open(f'manifests/{package}.yaml', 'r') as f:

        manifest = load(f, Loader=Loader)
        old_version = manifest['package']['version']

        update = manifest['update']
        update_enabled = update['enabled']
        if update_enabled:
            if 'release-monitor' in update:
                # Based on https://github.com/wolfi-dev/wolfictl/blob/be08e074314d863a8d614e1c85c35b7254491a07/pkg/update/releaseMonitor.go#L1
                release_monitor = update['release-monitor']
                identifier = release_monitor['identifier']
                url = f'https://release-monitoring.org/api/v2/versions/?project_id={identifier}'
                response = requests.get(url)
                latest_versions = json.loads(response.content)
                print(latest_versions['latest_version'])
                new_version = latest_versions['latest_version']

                download_coordinates = manifest['pipeline'][0]['with']
                if not download_coordinates:
                    raise('error')
                uri_template: str = download_coordinates['uri']
                old_sha = download_coordinates['expected-sha256']

                uri = uri_template.replace('${{package.version}}', new_version)
                (path, response) = urllib.request.urlretrieve(uri)
                print(uri)
                print(path)
                with open(path, 'rb', buffering=0) as f:
                    new_sha = hashlib.file_digest(f, 'sha256').hexdigest()
                    print(old_sha)
                    print(new_sha)

            if 'github' in update:
                github = update['github']
                identifier = github['identifier']
                strip_prefix = github['strip-prefix']
                tag_filter = github['tag-filter']

    new_file_content = file_content\
        .replace(old_version, new_version)\
        .replace(old_sha, new_sha)
    with open(f'manifests/{package}.yaml', 'w') as f:
        f.write(new_file_content)