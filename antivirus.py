import os,time,sys
from datetime import datetime
check_dir=r'D:\\'
file_log=r'C:\\Users\\jaglug\desktop\\log.txt'
time_border=87000
date_format = '%d.%m.%Y %H:%M:%S'


def clear_log():
    f=open(file_log,'w')
    f.close()


def find_virus(find_directory):
    for root,dirs, files in os.walk(find_directory):
        for name in files:
            file=os.path.join(root,name)
            if check(file):
                add_to_log(file)


def check(file):
    current_ts=time.time()
    change_time=get_change_time(file)
    return current_ts-change_time < time_border
    

def get_change_time(file):
    m_time=os.stat(file).st_mtime
    a_time=os.stat(file).st_atime
    c_time=os.stat(file).st_ctime
    return max(m_time,a_time,c_time)


def add_to_log(file):
    adding_string=file+": " + datetime.fromtimestamp(get_change_time(file)).strftime(date_format) + "\n"
    f=open(file_log, 'a')
    f.write(adding_string)
    f.close




if __name__=='__main__':
    clear_log()
    if len(sys.argv) >1:
        directory=sys.argv[1]
        find_virus(check_dir)

    find_virus(check_dir)