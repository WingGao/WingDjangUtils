import requests
import os
import re


def download(url, filename=None, create_dirs=False, can_down_func=None):
    if filename is None:
        local_filename = url.split('/')[-1]
    else:
        local_filename = filename

    if create_dirs:
        dir_name = os.path.dirname(os.path.abspath(filename))
        if not os.path.exists(dir_name):
            os.makedirs(dir_name)

    r = requests.get(url, stream=True, headers={
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'})
    if (can_down_func is not None and can_down_func(r)) or (can_down_func is None and r.status_code == 200):
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
        return local_filename
    else:
        return None


def auto_encoding(rep):
    """
    :param requests.Response request:
    :return:
    """
    charlist = re.findall(r'<meta http-equiv="Content-Type".*?content="[^"]*?charset=([\w\-]+)', rep.text)
    if len(charlist) > 0:
        rep.encoding = charlist[0]
        return

    charlist = re.findall(r'<meta.*?charset="([^"]+)"', rep.text)
    if len(charlist) > 0:
        rep.encoding = charlist[0]
        return

    return rep.encoding
