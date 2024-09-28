
def get_content(filename):
    with open(filename, 'r') as content_file:
        content = content_file.read()
    return content


