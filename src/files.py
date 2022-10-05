import os.path
import download_files, run_files

if __name__ == "__main__":
    filepath = 'files.json'
    if os.path.isfile(filepath):
        download_files.go(filepath)
        run_files.go(filepath)
    else:
        print('files.json does not exists inside the path')