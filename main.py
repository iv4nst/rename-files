import os
from pathlib import Path


def total_files_to_rename() -> int:
    """
    Total number of files to be renamed.

    Decreases when file renamed.
    :return: number of files (int)
    """
    global name_prefix

    total = 0

    for file in os.listdir(os.getcwd()):
        if not file.startswith(name_prefix):
            total += 1

    return total


def list_files() -> None:
    """
    Print files to be renamed.

    :return: None
    """
    global name_prefix

    print('\nFiles')
    for file in os.listdir(os.getcwd()):
        if not file.startswith(name_prefix):
            print(file)


def rename_file(file_name: str) -> None:
    """
    Rename a file.

    :param file_name: file name (starts with)
    :return: None
    """
    global starting_num, files_left

    file_renamed = False

    # get number of files to be renamed
    similarly_named_files = 0
    for file in os.listdir(os.getcwd()):
        if file.startswith(file_name):
            similarly_named_files += 1

    # renaming
    for file in os.listdir(os.getcwd()):
        if file.startswith(file_name):
            file_ext = Path(file).suffix  # get extension (e.g. -> .jpg, .MP4, ...)

            new_name = name_prefix + str(starting_num) + file_ext

            # rename
            if similarly_named_files == 1:
                os.rename(file, new_name)
                file_renamed = True
                print(f'"{file}" renamed to "{new_name}"')
            else:
                print('More than 1 file start like that. Try again!')
                break
    else:
        # check if renamed
        if file_renamed:
            starting_num += 1
            files_left -= 1
        else:
            print('No file starts like that.')


def main_menu() -> None:
    """
    Main menu.

    :return: None
    """
    global files_left

    while True:
        # list all photos & videos (to be renamed)
        list_files()

        # break if all files renamed
        if files_left == 0:
            print('No more files left.')
            break

        file_name = input('\nSelect file to rename: ')

        if file_name == 'q':
            print('Goodbye!')
            break
        else:
            rename_file(file_name)


if __name__ == '__main__':
    # set path
    location = input('Folder path: ')
    if not os.path.isdir(location):
        print('Invalid directory. Try again!')
    else:
        os.chdir(location)  # change directory

        # set starting name
        name_prefix = input('Name prefix (e.g. IMG_): ')
        starting_num = int(input('Start at number: '))  # e.g. 3054

        # get total number of files (to be renamed)
        files_left = total_files_to_rename()

        main_menu()
