"""
Running this script alone executes the entire project. 
The script sequentially runs all the project scripts.
"""

import subprocess

program_list = ['get_data.py', 'data_analysis.py', 'prepare_data.py', 'split_data.py', 'model_data.py']

for program in program_list:
    subprocess.call(['python3', program])
    print("Finished:" + program)

app = '../app/app.py'
subprocess.call(['streamlit', 'run',  app])
print("Finished:" + app)