import os
import shutil

import click

from quickstart.plugins.base import CLIPlugin
from quickstart.settings import TEMPLATES_FOLDER


class TarIntallPlugin(CLIPlugin):
    key = "tar"
    help = "URL used to download plugin compressed as tar/tgz"

    def __call__(self, tar_url: str, template_name: str, **options):
        click.echo("Install compressed template from URL: %s" % tar_url)

        import tarfile
        import urllib.request

        tmp_extract_folder = os.path.join(TEMPLATES_FOLDER, ".tmptemplate")

        tar_object = tarfile.open(fileobj=urllib.request.urlopen(tar_url), mode="r|gz")
        tar_object.extractall(tmp_extract_folder)

        extracted_template_folder = tmp_extract_folder

        files = os.listdir(tmp_extract_folder)
        if len(files) == 1:
            unique_file = os.path.join(tmp_extract_folder, files[0])
            if os.path.isdir(unique_file):
                extracted_template_folder = unique_file

        shutil.move(
            extracted_template_folder, os.path.join(TEMPLATES_FOLDER, template_name)
        )
        shutil.rmtree(tmp_extract_folder, ignore_errors=True)


class GitIntallPlugin(CLIPlugin):
    key = "git"
    help = "URI used to clone template from a git repository"

    def __call__(self, git_repo_uri: str, template_name: str, **options):
        click.echo("Install template from git repo: %s" % git_repo_uri)
        raise NotImplementedError
