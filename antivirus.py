import os
check_dir=r'D:\\albert'
file_log=r'D:\\albert\\log.txt'
def clear_log():
    f=open(file_log,'w')
    f.close()
def find_virus(find_directory):
    for root,dirs, files in os.walk(find_directory):
        for name in files:
            file=os.path.join(root,name)
            print(name)




if __name__=='__main__':
    clear_log()
    find_virus(check_dir)