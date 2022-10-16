import setuptools

from {{project_key}}.__about__ import __version__ as project_version
from {{project_key}}.__about__ import __description__ as project_description

setuptools.setup(
    name="{{project_key}}",
    description=project_description,
    version=project_version,
    packages=setuptools.find_packages(),
    entrypoints={
        "console_scripts": ["{{project_key}}.cli:CLI"]
    }
)
