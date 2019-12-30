from textwrap import TextWrapper
from logger import CYAN, RESET

wrapper = TextWrapper(width=70)
note = wrapper.fill(text=CYAN + 'Text wrapped notes: '
                                'I made this custom image-scraper in order to learn more Python. '
                                'It uses Bash as well and is meant for MacOS and Linux systems. '
                                'However, it was tested on MacOS only.' + RESET + ' Done.')
