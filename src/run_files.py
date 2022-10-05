import json, os

def go(filepath):
    with open (filepath) as files_object:
        data = json.load(files_object)
        for file in data['installationFiles']:
            filename = file['fileName']
            print('Opening', file['name'], 'installer')
            try:
                if os.path.isfile(filename):
                    os.system(filename)
            except:
                print('Something happened while installing', filename)