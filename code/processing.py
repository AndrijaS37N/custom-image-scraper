from google_images_download import google_images_download
import subprocess
from organizer import *

array_arguments = list()
result_target_directory = 'downloads/combined'

if not os.path.exists(result_target_directory):
    os.makedirs(result_target_directory)


def activate_wrapped_downloader():
    clear()
    while 1:
        try:
            array_size = int(input('Enter how many arguments you want to search for: '))
            sample_size = int(input('Enter the limit of sample sizes: '))
        except ValueError as e:
            clear()
            log.error(e)
            continue
        else:
            clear()
            print('Arguments:', CYAN + str(array_size) + RESET, '\nSamples per argument:', CYAN + str(sample_size) + RESET)
            break

    for i in range(array_size):
        element = input('Argument #%d: ' % (i + 1))
        while 1:
            # Don't really need 'if not tag_*.strip()'.
            if element == '':
                print('Empty input is not valid. Try again.')
                element = input('Argument #%d: ' % (i + 1))
            else:
                break

        array_arguments.append(element)

    clear()
    print(CYAN + 'Searching for these arguments:' + RESET, array_arguments)

    # Possible additions in the future to make arguments user entered variables.
    downloader_response = google_images_download.googleimagesdownload()
    downloader_arguments = {"keywords": (','.join(map(str, array_arguments))), "limit": sample_size, "print_urls": True,
                            # "aspect_ratio": "square",
                            "format": "jpg",
                            "chromedriver": "/Users/andrijadjuric/PycharmProjects/chromedriver"}

    # Path - input your own path to the "chromedriver" executable.
    # Node: "aspect_ratio": "square", "format": "jpg" -> no aspect ratio included currently.

    paths = downloader_response.download(downloader_arguments)
    print(CYAN + 'Check your new images in the downloads folder.' + RESET)
    view_paths = input('View paths (Y/n): ')
    if view_paths == 'Y' or view_paths == 'y':
        print('The download paths are:', paths)

    # Console result.
    c_result = subprocess.check_output('pwd')
    c_result = c_result.decode('utf-8')
    c_result = c_result[:-1]
    to_combined_path = '%s/downloads/combined' % c_result

    # Sometimes it get's an error while moving files.
    try:
        organizer = Organizer(array_arguments, "", c_result, list(), to_combined_path)
        organizer.resolve_files()

        if os.listdir(result_target_directory):
            combined_folder_reference()

        print(CYAN + "Check the samples manually and delete those that don't fit your standards." + RESET, 'Done.')
    except BaseException as e:
        clear()
        log.error(e)


def combined_folder_reference():
    print('\nNow do you want to rename/resize the files in the combined folder?')
    while 1:
        try:
            print('1. Yes.\n'
                  '2. No.')
            choice = int(input('Enter your choice: '))
        except ValueError as e:
            log.error(e)
            continue
        else:
            if choice == 1:
                bash_script_activation('combined')
                break
            elif choice == 2:
                print('Okay!')
                break
            else:
                print('Invalid input. Try again please.')
