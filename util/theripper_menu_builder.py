import os
import pathlib
import re


def strip_html_tags(subject):
    if subject == '':
        return ''
    else:
        return re.sub("<[^>]*>", "", subject)

def main():
    print('String Menu Builder Run...')
    pwd_win = input("Enter path containing the source files: ")
    dir_out = input("Enter path to write files to: ")
    pwd = str(pathlib.Path(pwd_win))
    conceptList = {}

    for filename in os.listdir(pwd.replace('\\', '/')):
        if filename.endswith('.' + 'html'):
            # dest_file_name = dir_out + "/" + filename
            print("Reading... " + filename)
            src_file = open(filename, "r")
            # print("Writing... " + dest_file_name)
            # dest_file = open(dest_file_name, 'w')
            subject = src_file.read()
            # Do first replacement
            reobj = re.compile('<div class="jsConcepts">\r*?(.*?)\r*?</div>', re.DOTALL | re.MULTILINE)
            match = reobj.search(subject)
            if match:
                result = match.group(1)
                conceptList[result] = {}
                print("***"+match)
            # Do 2nd replacement - subconcept

    print(conceptList)

# Main
if __name__ == '__main__':
    # Calling main() function
    main()
