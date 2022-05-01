"""
Running this script alone executes the entire project. 
The script sequentially runs all the project scripts.
"""

import subprocess

program_list = ['src/get_data.py', 'src/data_analysis.py', 'src/prepare_data.py', 'src/split_data.py', 'src/model_data.py']

for program in program_list:
    subprocess.call(['python3', program])
    print("Finished:" + program)

app = 'app/app.py'
subprocess.call(['streamlit', 'run',  app])
print("Finished:" + app)
