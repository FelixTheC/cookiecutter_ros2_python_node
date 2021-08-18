#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 14.08.21
@author: felix
"""
import os
from pathlib import Path
import shutil

source_dir = Path.cwd() / Path("{{cookiecutter.node_file_name}}.py")
target_dir = "{{ cookiecutter.final_destination }}"

shutil.move(source_dir.as_posix(), target_dir)

os.chdir(Path.cwd().parent)
for folder in Path.cwd().glob('*'):
    if folder.name.startswith('ros2_node_'):
        shutil.rmtree(folder)
