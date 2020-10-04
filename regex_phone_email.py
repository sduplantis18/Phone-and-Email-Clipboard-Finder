import re
import pyperclip

# email regex
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?              # area code
    (\s|-|\.)?                      # seperator
    (\d{3})                         # first 3 digits
    (\s|-|\.)                       # seperator
    (\d{4})                         # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?  #extension 
    )''', re.VERBOSE)

# Email Regex
emailRegex = re.compile(r'''(
    [a-zA-z0-9._%+-]+               # username
    @                               # @ symbol
    [a-zA-Z0-9.-]+                  # domain name
    (\.[a-zA-Z]{2,4})               # dot something (i.e .com)
    )''', re.VERBOSE)

# TODO Find matches in clipboard text
# TODO Copy results to the clipboard





