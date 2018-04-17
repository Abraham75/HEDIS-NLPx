from datetime import datetime
from config import XML_DIRECTORY
from config import JSON_DIRECTORY
import glob
import os.path
from xml_to_text import chief as xml_2_text



def main():
    run = True
    no_of_files = 0
    print('started', datetime.now())
    for xml_path in glob.glob(r'{0}\/*.xml'.format(XML_DIRECTORY)):
        if run:
            file_name = xml_path.split('\\')[-1]
            file_name = file_name[:-3] + "json"
            print("file name--> ", file_name)
            try:
                res = xml_2_text(xml_path)
                res = res.replace('"',"").replace('\\',"")
                json_doc = '{"DOC":"' + res +'"}'
                f = open(os.path.join(JSON_DIRECTORY,file_name),"w+")
                f.write(json_doc)
                f.close
                no_of_files += 1
            except Exception as e:
                print('Error', e)
    print('end', datetime.now())

main()