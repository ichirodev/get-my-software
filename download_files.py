import requests, json, os.path

def get_file(url, filename):
    r = requests.get(url)
    with open (filename, 'wb' ) as f:
        f.write(r.content)

def go(filepath):
    with open (filepath) as files_object:
        data = json.load(files_object)
        for file in data['installationFiles']:
            name = file['name']
            filename = file['fileName']
            print('> [', name, ']')
            if os.path.isfile(filename):
                print('\t- File already downloaded')
            else:
                print('\t- Downloading...')
                try:   
                    get_file(file['url'], filename)
                except:
                    print('\t- Something happened while trying to download', name)
                print('\t- Download complete!')
        print('Finished downloading files...')