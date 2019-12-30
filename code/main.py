import sys
from view_notes import note
from processing import activate_wrapped_downloader
from logger import *


def main():
    clear()
    print(BLUE + 'Custom Image Scraper' + RESET)
    while 1:
        try:
            print("1. Custom scraping from Google (using google_images_download).\n"
                  "2. View notes.")
            choice = int(input("Enter your choice: "))
        except ValueError as e:
            clear()
            log.error(e)
            continue
        else:
            if choice == 1:
                activate_wrapped_downloader()
                break
            elif choice == 2:
                clear()
                print(note)
                break
            else:
                clear()
                print('Non-existent option, try again please.')
                continue


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
    sys.exit()
