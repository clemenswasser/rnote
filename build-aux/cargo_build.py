#!/usr/bin/python

import sys
import os
import shutil
import subprocess

project_build_root = sys.argv[1]
project_src_root = sys.argv[2]
cargo_env = sys.argv[3]
cargo_cmd = sys.argv[4]
cargo_options = sys.argv[5]
bin_output = sys.argv[6]
output_file = sys.argv[7]

print(f"""
###
executing cargo_build.py with arguments:

project_build_root: {project_build_root}
project_src_root: {project_src_root}
cargo_env: {cargo_env}
cargo_cmd: {cargo_cmd}
cargo_options: {cargo_options}
bin_output: {bin_output}
output_file: {output_file}

###
""")

subprocess.run([cargo_cmd, "build"] + cargo_options.split(), check=True)
shutil.copy(bin_output, output_file)