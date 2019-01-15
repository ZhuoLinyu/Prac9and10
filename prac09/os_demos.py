import shutil

import os

def main():

    print("Starting directory is: {}".format(os.getcwd()))

    os.chdir('Lyrics/Christmas')

    print("Files in {}:\n{}\n".format(os.getcwd(), os.listdir('.')))



    try:

        os.mkdir('temp')

    except FileExistsError:

        print('File already exists')

    for filename in os.listdir('.'):

        if os.path.isdir(filename):

            continue


        new_name = get_fixed_filename(filename)

        print("Renaming {} to {}".format(filename, new_name))

        os.rename(filename, new_name)



def get_fixed_filename(filename):

    new_name = filename.replace(" ", "_").replace(".TXT", ".txt")



    modified_new_name = ''

    for index in range(len(new_name.split('.')[0]) - 1):

        if new_name[index].islower() and new_name[index + 1].isupper():

            modified_new_name += new_name[index] + '_'

        else:

            modified_new_name += new_name[index]

    modified_new_name += '.txt'

    return modified_new_name





def demo_walk():

    os.chdir('Lyrics')

    for directory_name, subdirectories, filenames in os.walk('.'):

        print("Directory:", directory_name)

        print("\tcontains subdirectories:", subdirectories)

        print("\tand files:", filenames)

        print("(Current working directory is: {})".format(os.getcwd()))

        for filename in os.listdir(directory_name):

            if os.path.isdir(filename):

                continue

            new_name = get_fixed_filename(filename)

            print("Renaming {} to {}".format(filename, new_name))



demo_walk()