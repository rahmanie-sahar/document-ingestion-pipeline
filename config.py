import os, sys

root_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(root_dir)

data_dir = os.path.join(root_dir, 'examples', 'data')
os.makedirs(data_dir, exist_ok=True)