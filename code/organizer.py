import os
import shutil
from bash_script_activation import bash_script_activation
from logger import *

CORRECT_CHOICES = ('1', '2', '3')


class Organizer(object):
    def __init__(self, array_arguments, last_argument_source, c_result, files, to_combined_path):
        self.array_arguments = array_arguments
        self.last_argument_source = last_argument_source
        self.c_result = c_result
        self.files = files
        self.to_combined_path = to_combined_path

    # Some getters, these could be commented out.
    def get_array_arguments(self):
        return self.array_arguments

    def get_last_argument_source(self):
        return self.last_argument_source

    def get_files(self):
        return self.files

    # The main operation of this class.
    def resolve_files(self):
        # Copying/moving.
        print('\n1. Rename/resize the files in each folder.\n'
              '2. Move files to a combined folder and delete the originals.\n'
              '3. Move 10% of the images to a combined folder and leave the rest in their original dirs (must have at '
              'least 10 images per group).')

        while 1:
            try:
                choice_about_files = (input('Input your choice: '))
                # If it's not a valid input, don't even start reading the paths and files, kinda saves time.
                if choice_about_files in CORRECT_CHOICES:
                    # Read all the paths and files.
                    for i in range(len(self.array_arguments)):
                        self.last_argument_source = '%s/downloads/%s/' % (self.c_result, self.array_arguments[i])
                        print('\nSource folder:', CYAN + self.last_argument_source + RESET)
                        self.files = os.listdir(self.last_argument_source)
                        # ... print('Files ready to copy: ', self.files) ...

                        if choice_about_files == '1':
                            bash_script_activation(self.array_arguments[i])
                        elif choice_about_files == '2':
                            for j in self.files:
                                try:
                                    j.replace(' ', '')
                                    shutil.move(self.last_argument_source + j, self.to_combined_path)
                                except FileNotFoundError as e:
                                    log.error(e)
                                    continue

                            # Don't try removedirs().
                            try:
                                os.rmdir(self.last_argument_source[:-1])
                            except FileNotFoundError as e:
                                log.error(e)
                                continue

                            print("Moving and deleting is finished. The combined folder now has this folder's images.")
                        else:
                            counter = 0
                            files_count = len(self.files)
                            for j in self.files:
                                counter += 1
                                try:
                                    # Here we do 10% off.
                                    if counter <= (files_count / 10):
                                        j.replace(' ', '')
                                        shutil.move(self.last_argument_source + j, self.to_combined_path)
                                except FileNotFoundError as e:
                                    log.error(e)
                                    continue
                            print('10% of the files in this folder were sent to the combined folder.')
                            bash_script_activation(self.array_arguments[i])
                    break
                else:
                    raise UserWarning('Options are: ' + (','.join(map(str, CORRECT_CHOICES))))

            except UserWarning as e:
                log.error(e)
                continue
