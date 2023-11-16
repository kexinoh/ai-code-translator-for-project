import os
from scanconfig import languages_import_statements
import config
def scan_directory(directory, temp_directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            temp_file_path = os.path.join(temp_directory, os.path.relpath(file_path, directory))
            os.makedirs(os.path.dirname(temp_file_path), exist_ok=True)
            if get_language(file_path) is None:
                continue
            with open(file_path, 'r', encoding='utf-8') as file:
                lines = file.readlines()
            with open(temp_file_path, 'w', encoding='utf-8') as temp_file:
                for line in lines:
                    if any(keyword in line for keyword in languages_import_statements.get(get_language(file_path), [])):
                        temp_file.write(line)

def get_language(file_path):
    extension = os.path.splitext(file_path)[1].lower()
    return {
        '.py': 'python',
        '.lua': 'lua',
        '.c': 'c',
        '.cpp': 'cpp',
        '.js': 'javascript',
        '.java': 'java',
        '.rs': 'rust',
        '.php': 'php',
        '.go': 'go'
    }.get(extension)



if __name__ == '__main__':
    scan_directory('example', config.temp_file_path)