import os
import sys
import click
import subprocess

from circleci.api import Api
from urllib.parse import quote_plus

WORKING_DIR = 'test-results'
circleci = Api(os.environ.get("CIRCLE_TOKEN"))

def extract_build_info(url):
    split = url.split('/')

    if (split[-4] == 'gh'):
        vcs = 'github'
    elif (split[-4] == 'bb'):
        vcs = 'bitbucket'
    else:
        sys.exit('Unknown vcs')

    build_info = {
        'build_num' : split[-1],
        'repo' : split[-2],
        'org' : split[-3],
        'vcs' : vcs
    }

    return build_info

def download_test_resuts(build_info):
    artifacts = circleci.get_artifacts(
        username = build_info['org'],
        project = build_info['repo'],
        build_num = build_info['build_num'],
        vcs_type = build_info['vcs']
    )

    for artifact in artifacts:
        circleci.download_artifact(
            url = artifact['url'],
            destdir = WORKING_DIR,
            filename = quote_plus(artifact['url'])
        )

@click.command()
@click.argument('url')
def run(url):
    if not os.path.exists(WORKING_DIR):
        os.makedirs(WORKING_DIR)
    else:
        subprocess.Popen(['rm', '-rf', WORKING_DIR]).wait()
        os.makedirs(WORKING_DIR)

    build_info = extract_build_info(url)
    download_test_resuts(build_info)

    subprocess.Popen(['node', 'validate.js']).wait()

if __name__ == '__main__':
    run()