import os 

class directory: 
    '''
    This function, will change th current directory. 

    Argument >>> os.listdir()
    '''

    os.chdir('csv_file')
    def __init__(self):
        self.dir_content = os.listdir()
    
    def new_csv_folder():
        os.chdir("../")
        os.chdir('new_csv_file')
