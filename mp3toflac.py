import os
import sys
from subprocess import call


# show variables (for troubleshooting)
def show_vars(target_dir):
    print('target_dir = ' + target_dir)
    print('target_dir (absolute) = ' + os.path.abspath(target_dir))


#get full list of mp3 files from your target directory
def get_mp3_list(target_dir):
    mp3_list = []
    for root, dirs, files in os.walk(target_dir):
        #print('root ',root)
        for file in files:
            path = root + file
            #print('path ', path)
            if file.endswith(".mp3"):
                mp3_list.append(path)
    return mp3_list


#convert mp3 to flac if the flac target file does not already exist
def convert_mp3(mp3_list):
    for mp3 in mp3_list:
        print('mp3 ',mp3)
        flac = mp3[:-4] + ".flac"
        if os.path.isfile(flac):
            print('File ' + flac + ' already exists')
        else:
            call(["ffmpeg", "-i", mp3, flac])


#main function: controls script flow
def main():
    target_dir = "C:\\Users\\PC\\Desktop\\music\\python-scripts\\musics\\"
    show_vars(target_dir)
    mp3_list = get_mp3_list(target_dir)
    print('----------------mp3 list------------')
    print(mp3_list,'\n')
    convert_mp3(mp3_list)


#call main funciont
if __name__ == '__main__':
    main()