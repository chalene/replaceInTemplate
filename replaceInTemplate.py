# coding: utf-8
'''

功能： 把 Dictionary 填入准备好的 template.xml 中，生成一个新的 doc 文件

参数input:
    - res 
    - templatefile
    - outputfilename

路径设置
    - input_file_path
    - output_file_path

It was written by Chalene Yuan, who can be contacted via chalene.yuan[at]gmail.com
'''

import sys  
import os.path
from string import Template

def replace_dict_in_template(res,templatefile,outputfilename):

    input_file_path = "./" #PROJECT_ROOT+"/media/order/"  
    output_file_path = "./" #PROJECT_ROOT+"/media/order/doc/"
    if not os.path.exists(output_file_path):
        os.makedirs(output_file_path)


    # print templatefile
    input_file = file(input_file_path+templatefile, 'r')
    output_file = file(output_file_path+outputfilename+".doc", 'w')
    # #print infile.read()

    s = Template(input_file.read().decode("utf-8"))
    output = s.safe_substitute(res)
    # #print output
    output_file.write(output.encode("utf-8"))
    output_file.close()
    return output_file

def main():
    res = {}
    templatefile = "template.xml"
    outputfilename = "example"
    replace_dict_in_template(res,templatefile,outputfilename)

if __name__ == '__main__':
    main()
