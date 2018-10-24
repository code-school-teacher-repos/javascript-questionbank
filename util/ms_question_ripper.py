import re
import os
import pathlib


# This utility was built to rip the key components from MS JavaScript certification test bank
# Function to rename multiple files
def main():
    global out_htm
    template_file = open('theripper.htm', 'r')
    template_contents = template_file.read()
    pwd_win = input("Enter path containing the source files: ")
    dir_out = input("Enter path to write files to: ")

    pwd = str(pathlib.Path(pwd_win))

    for filename in os.listdir(pwd.replace('\\', '/')):
        if filename.endswith('.' + 'html'):
            dest_file_name = dir_out + "/" + filename
            print("Reading... " + filename)
            src_file = open(filename, "r")
            print("Writing... " + dest_file_name)
            dest_file = open(dest_file_name, 'w')
            subject = src_file.read()
            # Do first replacement
            reobj = re.compile("<p>Objective:</p><p>(.*?)</p>")
            match = reobj.search(subject)
            if match:
                result = match.group(1)
                # Replace tags
                out_htm = template_contents.replace("#CONCEPT#", result)
            # Do 2nd replacement - subconcept
            reobj = re.compile("<p>(SubObjective:</p><p>(.*?))</p>")
            match = reobj.search(subject)
            if match:
                result = match.group(1)
                # Replace tags
                out_htm = out_htm.replace("#SUBCONCEPT#", result)
                print(out_htm)
            # Do 3rd replacement The Question
            reobj = re.compile(r'(<div id="questionStem"[\s\S]*?</div>)')
            match = reobj.search(subject)
            if match:
                result = match.group(1)
                # Replace tags
                result = result.replace('style="height: 1239px;', "")
                out_htm = out_htm.replace("#QUESTION#", result)

            # Do 4th replacement: available answers
            reobj = re.compile(r'((<div id="application"[\s\S]*)?(?=<div id="explanationDiv"))')
            match = reobj.search(subject)
            if match:
                result = match.group(1)
                # Replace tags
                result = result.replace("height: 600px;", "")
                out_htm = out_htm.replace("#ANSWERS#", result)

            # Do 5th replacement: available answers
            reobj = re.compile(r'((<div id="explanationDiv"[\s\S]*)?(?=<div id="growlMessage"))')
            match = reobj.search(subject)
            if match:
                result = match.group(1)
                # Replace tags
                out_htm = out_htm.replace("#EXPLANATION#", result)

            dest_file.write(out_htm)
            dest_file.close()


# Main
if __name__ == '__main__':
    # Calling main() function
    main()
