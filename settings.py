import os

UTF8_ENCODING = 'utf-8'
WINDOWS_ENCODING = 'windows-1250'

BAD_ANS_TEXT = 'Jesteś dupa! Prawidłowa odpowiedź to: '
BAD_ANS_COLOR = 'red'
GOOD_ANS_TEXT = 'Brawo!'
GOOD_ANS_COLOR = 'green'
DEFAULT_COLOR = 'black'

WINDOW_GEOMETRY = [
    10,
    10,
    640,
    480,
]

ROOT_PATH = os.getcwd()
DATA_PATH = os.path.join(ROOT_PATH, 'data')

EXCLUDED_EXTENSIONS = ['.swp']
IGNORED_LINES = [
    '\n',
]

WINDOW_RESIZABLE = False

try:
    import local_settings
except ImportError:
    pass
