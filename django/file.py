def write_file_from_request(uploadfile, dst_path):
    with open(dst_path, 'wb') as f:
        if uploadfile.multiple_chunks():
            for ck in uploadfile.chunks():
                f.write(ck)
        else:
            f.write(uploadfile.read())
