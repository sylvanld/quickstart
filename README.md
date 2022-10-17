# Quickstart CLI

Quickstart is a command line tools that help you quickly creating project from templates folder.

## Usage

Install a new template from a github repository

```
quickstart template install github-action                                                 \
          --tar https://github.com/sylvanld/action-storage/archive/refs/tags/v1.tar.gz
```

List available templates

```
quickstart template list
```

Create a new project from this template

```
quickstart project create my-action --from github-action
```
