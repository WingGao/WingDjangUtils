import requests
import os


def download(url, filename=None, create_dirs=False):
    if filename is None:
        local_filename = url.split('/')[-1]
    else:
        local_filename = filename

    if create_dirs:
        dir_name = os.path.dirname(os.path.abspath(filename))
        if not os.path.exists(dir_name):
            os.makedirs(dir_name)

    r = requests.get(url, stream=True)
    if r.status_code == 200:
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
        return local_filename
    else:
        return None
