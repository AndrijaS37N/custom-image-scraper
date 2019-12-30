import subprocess
from logger import *


def bash_script_activation(target_dir):
    script_name = 'renaming_resizing_script.sh'
    target_dir = 'downloads/' + target_dir
    while 1:
        try:
            print("1. 'Rename + resize with percentage' option.\n"
                  "2. 'Rename + resize with specific width and height' option.\n"
                  "3. 'Just rename' option.")
            choice = int(input('Enter your choice: '))
        except ValueError as e:
            log.error(e)
            continue
        else:
            while 1:
                try:
                    print('This should be your target directory for this loop:', target_dir)
                    if target_dir == "":
                        raise NotADirectoryError('Target folder string is not a directory.', 'Whoops!')
                except NotADirectoryError as e:
                    log.error(e)
                    continue
                else:
                    break

            if choice == 1:
                while 1:
                    try:
                        percentage = int(input('\nEnter by how much percentage do you want to scale down the images: '))
                    except ValueError as e:
                        log.error(e)
                        continue
                    else:
                        print('\nUsing:', script_name,
                              '\nBelow is described the usage of this script when activated independently.')
                        subprocess.call(
                            ['bash', script_name, str(percentage), target_dir])
                        print('\n')
                        break
            elif choice == 2:
                while 1:
                    try:
                        image_width = int(input('\nEnter image width: '))
                        image_height = int(input('\nEnter image height: '))
                    except ValueError as e:
                        log.error(e)
                        continue
                    else:
                        print('\nUsing:', script_name,
                              '\nBelow is described the usage of this script when activated independently.')
                        subprocess.call(['bash', script_name, str(image_width), str(image_height), target_dir])
                        print('\n')
                        break
            elif choice == 3:
                print('\nUsing:', CYAN + script_name + RESET,
                      '\nBelow is described the usage of this script when activated independently.')
                subprocess.call(['bash', script_name, target_dir])
                print('\n')
                break
            else:
                print('Not a valid input, try again please.\n')
                continue

            break
