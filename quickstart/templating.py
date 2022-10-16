import os
from typing import Any, Dict
import click

from jinja2 import Environment, FileSystemLoader, StrictUndefined, Template
from quickstart.settings import VERBOSE

class PrefixBlacklist:
    def __init__(self):
        self.__blacklist = set()
        
    def add(self, path_prefix: str):
        self.__blacklist.add(path_prefix)
    
    def contains(self, path: str):
        if not path:
            return False
        for path_prefix in self.__blacklist:
            if path.startswith(path_prefix):
                return True
        return False
    
    
class FolderTemplatingEngine:
    def __init__(self, source: str, context: Dict[str, Any]):
        self.source = os.path.abspath(source)
        self.context = context
        
        self.filename_env = Environment(undefined=StrictUndefined)
        self.template_env = Environment(loader=FileSystemLoader(source))
        
    def render_filename(self, s: Template):
        return self.filename_env.from_string(s).render(self.context)
    
    def render_template_file(self, src_relative_path: str, output_path: str):
        dst_relative_path = self.render_filename(src_relative_path)
        dst_absolute_path = os.path.join(output_path, dst_relative_path)
        with open(dst_absolute_path, 'w') as output:
            output.write(
            self.template_env.get_template(src_relative_path).render(self.context)
            )
        if VERBOSE:
            click.echo("[file  ] %s" % dst_absolute_path)
        
    def render_template_folder(self, destination: str):
        blacklist = PrefixBlacklist()
        destination = os.path.abspath(destination)
        
        for parent_folder, folder_names, filenames in os.walk(self.source):
            parent_folder = parent_folder[len(self.source)+1:]
            
            for folder_name in folder_names:
                folder = os.path.join(parent_folder, folder_name)
                
                if self.render_filename(folder_name):
                    folder_path = os.path.join(destination, self.render_filename(folder))
                    os.makedirs(folder_path)
                    if VERBOSE:
                        click.echo("[folder] %s" % folder_path)
                else:
                    blacklist.add(folder)
                    
            for filename in filenames:
                file_path_pattern = os.path.join(parent_folder, filename)
                
                if blacklist.contains(file_path_pattern):
                    continue
                
                if not self.render_filename(filename):
                    continue
                
                self.render_template_file(file_path_pattern, destination)
