import json
import os
import fire

def main(file_path):
    if not os.path.exists(file_path):
        print('File does not exist')
        return
    
    print('Cleaning names in file: ' + file_path)
    with open(file_path, 'r', encoding='utf8') as f:
        data = json.loads(f.read())
        items = data['items']
        
        for item in items:
            if 'login' not in item:
                continue
            if 'uris' not in item['login']:
                continue
            first_url = item['login']['uris'][0] if len(item['login']['uris']) > 0 else None
            if first_url is None:
                continue
            try:
                domain = first_url['uri'].split('/')[2]
            except IndexError as e:
                print('Error parsing domain for url: ' + first_url['uri'])
            item['name'] = domain
        
        save_file(file_path, data)

def save_file(file_path, data):
    path, ext = os.path.splitext(file_path)
    path = path + '_cleaned' + ext
    with open(path, 'w', encoding='utf8') as f:
        f.write(json.dumps(data, indent=2))
        print('Saved file: ' + path)
        
if __name__ == '__main__':
    fire.Fire(main)