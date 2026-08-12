import os

def filesArrange(files,ext):
    files_with_ext=[file for file in files if file.endswith(ext)]
    for i, file in enumerate(files_with_ext):
        os.rename(file,f'photo{i}{ext}')
    

if __name__ == '__main__':
    files=os.listdir()
    filesArrange(files,'.jpg')
