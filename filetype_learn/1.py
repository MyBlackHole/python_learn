import filetype

def main():
    with open("./1.deb", "rb") as f:
        bytes = f.read()

    kind = filetype.guess(bytes)
    # kind = filetype.guess("./1.deb")
    if kind is None:
        print('Cannot guess file type!')
        return

    print('File extension: %s' % kind.extension)
    print('File MIME type: %s' % kind.mime)

if __name__ == '__main__':
    main()
