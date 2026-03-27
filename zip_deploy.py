import os
import zipfile

def zip_project(output_filename, source_dir):
    exclude_dirs = {'venv', '.git', '__pycache__', '.vscode', 'media'}
    with zipfile.ZipFile(output_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(source_dir):
            dirs[:] = [d for d in dirs if d not in exclude_dirs]
            for file in files:
                if file.endswith('.pyc') or file == output_filename or file == 'zip_deploy.py':
                    continue
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, source_dir)
                zipf.write(file_path, arcname)

if __name__ == '__main__':
    zip_project('deploy.zip', '.')
    print("Created deploy.zip successfully!")
