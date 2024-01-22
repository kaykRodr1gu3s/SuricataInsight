import os

class directory: 
    '''
    This function, will change th current directory. 

    Argument >>> os.listdir()
    '''

    os.chdir('csv_file')
    def __init__(self, dir_content) -> None:
        self.dir_content = dir_content


    