code="""
import os
import json
import csv
import pickle


def traverse_directory(directory):
    results = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            results.append({
                'Path': f'{root}/{file}',
                'Type': 'File',
                'Size': os.path.getsize(file_path)
            })
        for dir in dirs:
            dir_path = os.path.join(root, dir)
            dir_size = get_dir_size(dir_path)
            results.append({
                'Path': f'{root}/{dir}',
                'Type': 'Directory',
                'Size': dir_size
            })
    return results

def get_dir_size(directory):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(directory):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
        for d in dirnames:
            total_size += get_dir_size(os.path.join(dirpath, d))
    return total_size

def save_results_to_json(data, output_file):
    with open(output_file, 'w') as file:
        json.dump(data, file, indent=4)


def save_results_to_csv(data, output_file):
    with open(output_file, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)


def save_results_to_pickle(data, output_file):
    with open(output_file, 'wb') as file:
        pickle.dump(data, file)
"""
with open('__init__.py', 'w', encoding='utf-8') as f:
    f.write(code)