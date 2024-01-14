'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
...................... |||\\\ ///||| \\\\|//// ||||||||| ..........................
...................... ||| \\|// |||    |||    |||       ..........................
...................... |||  \|/  |||    |||    ||||||||  ..........................
...................... |||       |||    |||    |||       ..........................
...................... |||       ||| ////|\\\\ ||||||||| ..........................
...................................................................................
... ///||\\\  /////// |||  ||| |||||||| |||||\\  |||   ||| |||      |||||||| ......
... |||      ///      |||  ||| |||      |||   \\ |||   ||| |||      |||      ......
... \\\\\    ||       |||||||| ||||||   |||   || |||   ||| |||      ||||||   ......
...    ///// \\\      |||  ||| |||      |||   // |||   ||| |||      |||      ......
... \\\||///  \\\\\\\ |||  ||| |||||||| |||||//   \\\|///  |||||||| |||||||| ......
...................................................................................
. /////// |||||||| ||\\   || |||||||| ||||||\\  ///|\\\ ||||||||| ///\\\  ||||||\\.
.//       |||      |||\\  || |||      |||   || |||   |||   |||   |||  ||| |||   ||.
.||   \\\ ||||||   ||| \\ || ||||||   |||///// |||||||||   |||   |||  ||| |||/////.
.||    || |||      |||  \\|| |||      |||  \\  |||   |||   |||   |||  ||| |||  \\ .
.\\\\|/// |||||||| |||   \|| |||||||| |||   \\ |||   |||   |||    \\\///  |||   \\.
...................................................................................

This Python script retrieves stored schedule data and lists the schedules for
labs/practicals, tutorials, quizzes, and midterms for defined sections, for the
course MIE221 for the Winter 2024 semester.

Note: Each course has a separate file.

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

# Copyright (c) 2024, Ibrahim Hassan
# Created on: January 13, 2024
# Version: 1.0.0., January 13, 2024
# Let me know if there are any errors or incorrect data is being generated.
# Data is accurate as of January 13, 2024

################################################################################
import datetime
from PIL import Image, ImageDraw, ImageFont

# Define the start and end dates of the calendar
start_date = datetime.date(2024, 1, 1)
end_date = datetime.date(2024, 12, 31)

# Get the student's last name
student_name = input('Enter your SURNAME (NOT First): ')

# Get the practical number
practical_number = int(input('Enter your MIE221 practical section (1-5): '))

# Define the list of events and their respective dates
events = {
    'Lab 1': {
        2: {'A': datetime.date(2024, 1, 19), 'B': datetime.date(2024, 1, 19), 'C': datetime.date(2024, 1, 19),
            'D': datetime.date(2024, 1, 19), 'E': datetime.date(2024, 1, 19), 'F': datetime.date(2024, 1, 19),
            'G': datetime.date(2024, 1, 19), 'H': datetime.date(2024, 1, 19), 'I': datetime.date(2024, 1, 19),
            'J': datetime.date(2024, 1, 19), 'K': datetime.date(2024, 1, 19), 'L': datetime.date(2024, 1, 26),
            'M': datetime.date(2024, 1, 26), 'N': datetime.date(2024, 1, 26), 'O': datetime.date(2024, 1, 26),
            'P': datetime.date(2024, 1, 26), 'Q': datetime.date(2024, 1, 26), 'R': datetime.date(2024, 1, 26),
            'S': datetime.date(2024, 1, 26), 'T': datetime.date(2024, 1, 26), 'U': datetime.date(2024, 1, 26),
            'V': datetime.date(2024, 1, 26), 'W': datetime.date(2024, 1, 26), 'X': datetime.date(2024, 1, 26),
            'Y': datetime.date(2024, 1, 26), 'Z': datetime.date(2024, 1, 26)},
        3: {'A': datetime.date(2024, 1, 22), 'B': datetime.date(2024, 1, 22), 'C': datetime.date(2024, 1, 22),
            'D': datetime.date(2024, 1, 22), 'E': datetime.date(2024, 1, 22), 'F': datetime.date(2024, 1, 22),
            'G': datetime.date(2024, 1, 22), 'H': datetime.date(2024, 1, 22), 'I': datetime.date(2024, 1, 22),
            'J': datetime.date(2024, 1, 22), 'K': datetime.date(2024, 1, 22), 'L': datetime.date(2024, 1, 29),
            'M': datetime.date(2024, 1, 29), 'N': datetime.date(2024, 1, 29), 'O': datetime.date(2024, 1, 29),
            'P': datetime.date(2024, 1, 29), 'Q': datetime.date(2024, 1, 29), 'R': datetime.date(2024, 1, 29),
            'S': datetime.date(2024, 1, 29), 'T': datetime.date(2024, 1, 29), 'U': datetime.date(2024, 1, 29),
            'V': datetime.date(2024, 1, 29), 'W': datetime.date(2024, 1, 29), 'X': datetime.date(2024, 1, 29),
            'Y': datetime.date(2024, 1, 29), 'Z': datetime.date(2024, 1, 29)},
        1: {'A': datetime.date(2024, 1, 23), 'B': datetime.date(2024, 1, 23), 'C': datetime.date(2024, 1, 23),
            'D': datetime.date(2024, 1, 23), 'E': datetime.date(2024, 1, 23), 'F': datetime.date(2024, 1, 23),
            'G': datetime.date(2024, 1, 23), 'H': datetime.date(2024, 1, 23), 'I': datetime.date(2024, 1, 23),
            'J': datetime.date(2024, 1, 23), 'K': datetime.date(2024, 1, 23), 'L': datetime.date(2024, 1, 30),
            'M': datetime.date(2024, 1, 30), 'N': datetime.date(2024, 1, 30), 'O': datetime.date(2024, 1, 30),
            'P': datetime.date(2024, 1, 30), 'Q': datetime.date(2024, 1, 30), 'R': datetime.date(2024, 1, 30),
            'S': datetime.date(2024, 1, 30), 'T': datetime.date(2024, 1, 30), 'U': datetime.date(2024, 1, 30),
            'V': datetime.date(2024, 1, 30), 'W': datetime.date(2024, 1, 30), 'X': datetime.date(2024, 1, 30),
            'Y': datetime.date(2024, 1, 30), 'Z': datetime.date(2024, 1, 30)},
        4: {'A': datetime.date(2024, 1, 24), 'B': datetime.date(2024, 1, 24), 'C': datetime.date(2024, 1, 24),
            'D': datetime.date(2024, 1, 24), 'E': datetime.date(2024, 1, 24), 'F': datetime.date(2024, 1, 24),
            'G': datetime.date(2024, 1, 24), 'H': datetime.date(2024, 1, 24), 'I': datetime.date(2024, 1, 24),
            'J': datetime.date(2024, 1, 24), 'K': datetime.date(2024, 1, 24), 'L': datetime.date(2024, 1, 31),
            'M': datetime.date(2024, 1, 31), 'N': datetime.date(2024, 1, 31), 'O': datetime.date(2024, 1, 31),
            'P': datetime.date(2024, 1, 31), 'Q': datetime.date(2024, 1, 31), 'R': datetime.date(2024, 1, 31),
            'S': datetime.date(2024, 1, 31), 'T': datetime.date(2024, 1, 31), 'U': datetime.date(2024, 1, 31),
            'V': datetime.date(2024, 1, 31), 'W': datetime.date(2024, 1, 31), 'X': datetime.date(2024, 1, 31),
            'Y': datetime.date(2024, 1, 31), 'Z': datetime.date(2024, 1, 31)},
        5: {'A': datetime.date(2024, 1, 26), 'B': datetime.date(2024, 1, 26), 'C': datetime.date(2024, 1, 26),
            'D': datetime.date(2024, 1, 26), 'E': datetime.date(2024, 1, 26), 'F': datetime.date(2024, 1, 26),
            'G': datetime.date(2024, 1, 26), 'H': datetime.date(2024, 1, 26), 'I': datetime.date(2024, 1, 26),
            'J': datetime.date(2024, 1, 26), 'K': datetime.date(2024, 1, 26), 'L': datetime.date(2024, 2, 2),
            'M': datetime.date(2024, 2, 2), 'N': datetime.date(2024, 2, 2), 'O': datetime.date(2024, 2, 2),
            'P': datetime.date(2024, 2, 2), 'Q': datetime.date(2024, 2, 2), 'R': datetime.date(2024, 2, 2),
            'S': datetime.date(2024, 2, 2), 'T': datetime.date(2024, 2, 2), 'U': datetime.date(2024, 2, 2),
            'V': datetime.date(2024, 2, 2), 'W': datetime.date(2024, 2, 2), 'X': datetime.date(2024, 2, 2),
            'Y': datetime.date(2024, 2, 2), 'Z': datetime.date(2024, 2, 2)}
    },
    'Lab 2': {
        3: {'A': datetime.date(2024, 2, 5), 'B': datetime.date(2024, 2, 5), 'C': datetime.date(2024, 2, 5),
            'D': datetime.date(2024, 2, 5), 'E': datetime.date(2024, 2, 5), 'F': datetime.date(2024, 2, 5),
            'G': datetime.date(2024, 2, 5), 'H': datetime.date(2024, 2, 5), 'I': datetime.date(2024, 2, 5),
            'J': datetime.date(2024, 2, 5), 'K': datetime.date(2024, 2, 5), 'L': datetime.date(2024, 2, 12),
            'M': datetime.date(2024, 2, 12), 'N': datetime.date(2024, 2, 12), 'O': datetime.date(2024, 2, 12),
            'P': datetime.date(2024, 2, 12), 'Q': datetime.date(2024, 2, 12), 'R': datetime.date(2024, 2, 12),
            'S': datetime.date(2024, 2, 12), 'T': datetime.date(2024, 2, 12), 'U': datetime.date(2024, 2, 12),
            'V': datetime.date(2024, 2, 12), 'W': datetime.date(2024, 2, 12), 'X': datetime.date(2024, 2, 12),
            'Y': datetime.date(2024, 2, 12), 'Z': datetime.date(2024, 2, 12)},
        1: {'A': datetime.date(2024, 2, 6), 'B': datetime.date(2024, 2, 6), 'C': datetime.date(2024, 2, 6),
            'D': datetime.date(2024, 2, 6), 'E': datetime.date(2024, 2, 6), 'F': datetime.date(2024, 2, 6),
            'G': datetime.date(2024, 2, 6), 'H': datetime.date(2024, 2, 6), 'I': datetime.date(2024, 2, 6),
            'J': datetime.date(2024, 2, 6), 'K': datetime.date(2024, 2, 6), 'L': datetime.date(2024, 2, 13),
            'M': datetime.date(2024, 2, 13), 'N': datetime.date(2024, 2, 13), 'O': datetime.date(2024, 2, 13),
            'P': datetime.date(2024, 2, 13), 'Q': datetime.date(2024, 2, 13), 'R': datetime.date(2024, 2, 13),
            'S': datetime.date(2024, 2, 13), 'T': datetime.date(2024, 2, 13), 'U': datetime.date(2024, 2, 13),
            'V': datetime.date(2024, 2, 13), 'W': datetime.date(2024, 2, 13), 'X': datetime.date(2024, 2, 13),
            'Y': datetime.date(2024, 2, 13), 'Z': datetime.date(2024, 2, 13)},
        4: {'A': datetime.date(2024, 2, 7), 'B': datetime.date(2024, 2, 7), 'C': datetime.date(2024, 2, 7),
            'D': datetime.date(2024, 2, 7), 'E': datetime.date(2024, 2, 7), 'F': datetime.date(2024, 2, 7),
            'G': datetime.date(2024, 2, 7), 'H': datetime.date(2024, 2, 7),  'I': datetime.date(2024, 2, 7),
            'J': datetime.date(2024, 2, 7), 'K': datetime.date(2024, 2, 7), 'L': datetime.date(2024, 2, 14),
            'M': datetime.date(2024, 2, 14), 'N': datetime.date(2024, 2, 14), 'O': datetime.date(2024, 2, 14),
            'P': datetime.date(2024, 2, 14), 'Q': datetime.date(2024, 2, 14), 'R': datetime.date(2024, 2, 14),
            'S': datetime.date(2024, 2, 14), 'T': datetime.date(2024, 2, 14), 'U': datetime.date(2024, 2, 14),
            'V': datetime.date(2024, 2, 14), 'W': datetime.date(2024, 2, 14), 'X': datetime.date(2024, 2, 14),
            'Y': datetime.date(2024, 2, 14), 'Z': datetime.date(2024, 2, 14)},
        5: {'A': datetime.date(2024, 2, 9), 'B': datetime.date(2024, 2, 9), 'C': datetime.date(2024, 2, 9),
            'D': datetime.date(2024, 2, 9), 'E': datetime.date(2024, 2, 9), 'F': datetime.date(2024, 2, 9),
            'G': datetime.date(2024, 2, 9), 'H': datetime.date(2024, 2, 9), 'I': datetime.date(2024, 2, 9),
            'J': datetime.date(2024, 2, 9), 'K': datetime.date(2024, 2, 9), 'L': datetime.date(2024, 2, 16),
            'M': datetime.date(2024, 2, 16), 'N': datetime.date(2024, 2, 16), 'O': datetime.date(2024, 2, 16),
            'P': datetime.date(2024, 2, 16), 'Q': datetime.date(2024, 2, 16), 'R': datetime.date(2024, 2, 16),
            'S': datetime.date(2024, 2, 16), 'T': datetime.date(2024, 2, 16), 'U': datetime.date(2024, 2, 16),
            'V': datetime.date(2024, 2, 16), 'W': datetime.date(2024, 2, 16), 'X': datetime.date(2024, 2, 16),
            'Y': datetime.date(2024, 2, 16), 'Z': datetime.date(2024, 2, 16)},
        2: {'A': datetime.date(2024, 2, 9), 'B': datetime.date(2024, 2, 9), 'C': datetime.date(2024, 2, 9),
            'D': datetime.date(2024, 2, 9), 'E': datetime.date(2024, 2, 9), 'F': datetime.date(2024, 2, 9),
            'G': datetime.date(2024, 2, 9), 'H': datetime.date(2024, 2, 9), 'I': datetime.date(2024, 2, 9),
            'J': datetime.date(2024, 2, 9), 'K': datetime.date(2024, 2, 9), 'L': datetime.date(2024, 2, 16),
            'M': datetime.date(2024, 2, 16), 'N': datetime.date(2024, 2, 16), 'O': datetime.date(2024, 2, 16),
            'P': datetime.date(2024, 2, 16), 'Q': datetime.date(2024, 2, 16), 'R': datetime.date(2024, 2, 16),
            'S': datetime.date(2024, 2, 16), 'T': datetime.date(2024, 2, 16), 'U': datetime.date(2024, 2, 16),
            'V': datetime.date(2024, 2, 16), 'W': datetime.date(2024, 2, 16), 'X': datetime.date(2024, 2, 16),
            'Y': datetime.date(2024, 2, 16), 'Z': datetime.date(2024, 2, 16)},
        3: {'A': datetime.date(2024, 2, 12), 'B': datetime.date(2024, 2, 12), 'C': datetime.date(2024, 2, 12),
            'D': datetime.date(2024, 2, 12), 'E': datetime.date(2024, 2, 12), 'F': datetime.date(2024, 2, 12),
            'G': datetime.date(2024, 2, 12), 'H': datetime.date(2024, 2, 12), 'I': datetime.date(2024, 2, 12),
            'J': datetime.date(2024, 2, 12), 'K': datetime.date(2024, 2, 12), 'L': datetime.date(2024, 2, 19),
            'M': datetime.date(2024, 2, 19), 'N': datetime.date(2024, 2, 19), 'O': datetime.date(2024, 2, 19),
            'P': datetime.date(2024, 2, 19), 'Q': datetime.date(2024, 2, 19), 'R': datetime.date(2024, 2, 19),
            'S': datetime.date(2024, 2, 19), 'T': datetime.date(2024, 2, 19), 'U': datetime.date(2024, 2, 19),
            'V': datetime.date(2024, 2, 19), 'W': datetime.date(2024, 2, 19), 'X': datetime.date(2024, 2, 19),
            'Y': datetime.date(2024, 2, 19), 'Z': datetime.date(2024, 2, 19)}
    },
    'Lab 3': {
        1: {'A': datetime.date(2024, 2, 27        ), 'B': datetime.date(2024, 2, 27), 'C': datetime.date(2024, 2, 27),
            'D': datetime.date(2024, 2, 27), 'E': datetime.date(2024, 2, 27), 'F': datetime.date(2024, 2, 27),
            'G': datetime.date(2024, 2, 27), 'H': datetime.date(2024, 2, 27), 'I': datetime.date(2024, 2, 27),
            'J': datetime.date(2024, 2, 27), 'K': datetime.date(2024, 2, 27), 'L': datetime.date(2024, 3, 5),
            'M': datetime.date(2024, 3, 5), 'N': datetime.date(2024, 3, 5), 'O': datetime.date(2024, 3, 5),
            'P': datetime.date(2024, 3, 5), 'Q': datetime.date(2024, 3, 5), 'R': datetime.date(2024, 3, 5),
            'S': datetime.date(2024, 3, 5), 'T': datetime.date(2024, 3, 5), 'U': datetime.date(2024, 3, 5),
            'V': datetime.date(2024, 3, 5), 'W': datetime.date(2024, 3, 5), 'X': datetime.date(2024, 3, 5),
            'Y': datetime.date(2024, 3, 5), 'Z': datetime.date(2024, 3, 5)},
        4: {'A': datetime.date(2024, 2, 28), 'B': datetime.date(2024, 2, 28), 'C': datetime.date(2024, 2, 28),
            'D': datetime.date(2024, 2, 28), 'E': datetime.date(2024, 2, 28), 'F': datetime.date(2024, 2, 28),
            'G': datetime.date(2024, 2, 28), 'H': datetime.date(2024, 2, 28), 'I': datetime.date(2024, 2, 28),
            'J': datetime.date(2024, 2, 28), 'K': datetime.date(2024, 2, 28), 'L': datetime.date(2024, 3, 6),
            'M': datetime.date(2024, 3, 6), 'N': datetime.date(2024, 3, 6), 'O': datetime.date(2024, 3, 6),
            'P': datetime.date(2024, 3, 6), 'Q': datetime.date(2024, 3, 6), 'R': datetime.date(2024, 3, 6),
            'S': datetime.date(2024, 3, 6), 'T': datetime.date(2024, 3, 6), 'U': datetime.date(2024, 3, 6),
            'V': datetime.date(2024, 3, 6), 'W': datetime.date(2024, 3, 6), 'X': datetime.date(2024, 3, 6),
            'Y': datetime.date(2024, 3, 6), 'Z': datetime.date(2024, 3, 6)},
        5: {'A': datetime.date(2024, 3, 1), 'B': datetime.date(2024, 3, 1), 'C': datetime.date(2024, 3, 1),
            'D': datetime.date(2024, 3, 1), 'E': datetime.date(2024, 3, 1), 'F': datetime.date(2024, 3, 1),
            'G': datetime.date(2024, 3, 1), 'H': datetime.date(2024, 3, 1), 'I': datetime.date(2024, 3, 1),
            'J': datetime.date(2024, 3, 1), 'K': datetime.date(2024, 3, 1), 'L': datetime.date(2024, 3, 8),
            'M': datetime.date(2024, 3, 8), 'N': datetime.date(2024, 3, 8), 'O': datetime.date(2024, 3, 8),
            'P': datetime.date(2024, 3, 8), 'Q': datetime.date(2024, 3, 8), 'R': datetime.date(2024, 3, 8),
            'S': datetime.date(2024, 3, 8), 'T': datetime.date(2024, 3, 8), 'U': datetime.date(2024, 3, 8),
            'V': datetime.date(2024, 3, 8), 'W': datetime.date(2024, 3, 8), 'X': datetime.date(2024, 3, 8),
            'Y': datetime.date(2024, 3, 8), 'Z': datetime.date(2024, 3, 8)},
        2: {'A': datetime.date(2024, 3, 1), 'B': datetime.date(2024, 3, 1), 'C': datetime.date(2024, 3, 1),
            'D': datetime.date(2024, 3, 1), 'E': datetime.date(2024, 3, 1), 'F': datetime.date(2024, 3, 1),
            'G': datetime.date(2024, 3, 1), 'H': datetime.date(2024, 3, 1), 'I': datetime.date(2024, 3, 1),
            'J': datetime.date(2024, 3, 1), 'K': datetime.date(2024, 3, 1), 'L': datetime.date(2024, 3, 8),
            'M': datetime.date(2024, 3, 8), 'N': datetime.date(2024, 3, 8), 'O': datetime.date(2024, 3, 8),
            'P': datetime.date(2024, 3, 8), 'Q': datetime.date(2024, 3, 8), 'R': datetime.date(2024, 3, 8),
            'S': datetime.date(2024, 3, 8), 'T': datetime.date(2024, 3, 8), 'U': datetime.date(2024, 3, 8),
            'V': datetime.date(2024, 3, 8), 'W': datetime.date(2024, 3, 8), 'X': datetime.date(2024, 3, 8),
            'Y': datetime.date(2024, 3, 8), 'Z': datetime.date(2024, 3, 8)},
        3: {'A': datetime.date(2024, 3, 4), 'B': datetime.date(2024, 3, 4), 'C': datetime.date(2024, 3, 4),
            'D': datetime.date(2024, 3, 4), 'E': datetime.date(2024, 3, 4), 'F': datetime.date(2024, 3, 4),
            'G': datetime.date(2024, 3, 4), 'H': datetime.date(2024, 3, 4), 'I': datetime.date(2024, 3, 4),
            'J': datetime.date(2024, 3, 4), 'K': datetime.date(2024, 3, 4), 'L': datetime.date(2024, 3, 11),
            'M': datetime.date(2024, 3, 11), 'N': datetime.date(2024, 3, 11), 'O': datetime.date(2024, 3, 11),
            'P': datetime.date(2024, 3, 11), 'Q': datetime.date(2024, 3, 11), 'R': datetime.date(2024, 3, 11),
            'S': datetime.date(2024, 3, 11), 'T': datetime.date(2024, 3, 11), 'U': datetime.date(2024, 3, 11),
            'V': datetime.date(2024, 3, 11), 'W': datetime.date(2024, 3, 11), 'X': datetime.date(2024, 3, 11),
            'Y': datetime.date(2024, 3, 11), 'Z': datetime.date(2024, 3, 11)}
    },
    'Lab 4': {
    3: {'A': datetime.date(2024, 3, 18), 'B': datetime.date(2024, 3, 18), 'C': datetime.date(2024, 3, 18),
        'D': datetime.date(2024, 3, 18), 'E': datetime.date(2024, 3, 18), 'F': datetime.date(2024, 3, 18),
        'G': datetime.date(2024, 3, 18), 'H': datetime.date(2024, 3, 18), 'I': datetime.date(2024, 3, 18),
        'J': datetime.date(2024, 3, 18), 'K': datetime.date(2024, 3, 18), 'L': datetime.date(2024, 3, 25),
        'M': datetime.date(2024, 3, 25), 'N': datetime.date(2024, 3, 25), 'O': datetime.date(2024, 3, 25),
        'P': datetime.date(2024, 3, 25), 'Q': datetime.date(2024, 3, 25), 'R': datetime.date(2024, 3, 25),
        'S': datetime.date(2024, 3, 25), 'T': datetime.date(2024, 3, 25), 'U': datetime.date(2024, 3, 25),
        'V': datetime.date(2024, 3, 25), 'W': datetime.date(2024, 3, 25), 'X': datetime.date(2024, 3, 25),
        'Y': datetime.date(2024, 3, 25), 'Z': datetime.date(2024, 3, 25)},
    1: {'A': datetime.date(2024, 3, 19), 'B': datetime.date(2024, 3, 19), 'C': datetime.date(2024, 3, 19),
        'D': datetime.date(2024, 3, 19), 'E': datetime.date(2024, 3, 19), 'F': datetime.date(2024, 3, 19),
        'G': datetime.date(2024, 3, 19), 'H': datetime.date(2024, 3, 19), 'I': datetime.date(2024, 3, 19),
        'J': datetime.date(2024, 3, 19), 'K': datetime.date(2024, 3, 19), 'L': datetime.date(2024, 3, 26),
        'M': datetime.date(2024, 3, 26), 'N': datetime.date(2024, 3, 26), 'O': datetime.date(2024, 3, 26),
        'P': datetime.date(2024, 3, 26), 'Q': datetime.date(2024, 3, 26), 'R': datetime.date(2024, 3, 26),
        'S': datetime.date(2024, 3, 26), 'T': datetime.date(2024, 3, 26), 'U': datetime.date(2024, 3, 26),
        'V': datetime.date(2024, 3, 26), 'W': datetime.date(2024, 3, 26), 'X': datetime.date(2024, 3, 26),
        'Y': datetime.date(2024, 3, 26), 'Z': datetime.date(2024, 3, 26)},
    4: {'A': datetime.date(2024, 3, 13), 'B': datetime.date(2024, 3, 13), 'C': datetime.date(2024, 3, 13),
        'D': datetime.date(2024, 3, 13), 'E': datetime.date(2024, 3, 13), 'F': datetime.date(2024, 3, 13),
        'G': datetime.date(2024, 3, 13), 'H': datetime.date(2024, 3, 13), 'I': datetime.date(2024, 3, 13),
        'J': datetime.date(2024, 3, 13), 'K': datetime.date(2024, 3, 13), 'L': datetime.date(2024, 3, 20),
        'M': datetime.date(2024, 3, 20), 'N': datetime.date(2024, 3, 20), 'O': datetime.date(2024, 3, 20),
        'P': datetime.date(2024, 3, 20), 'Q': datetime.date(2024, 3, 20), 'R': datetime.date(2024, 3, 20),
        'S': datetime.date(2024, 3, 20), 'T': datetime.date(2024, 3, 20), 'U': datetime.date(2024, 3, 20),
        'V': datetime.date(2024, 3, 20), 'W': datetime.date(2024, 3, 20), 'X': datetime.date(2024, 3, 20),
        'Y': datetime.date(2024, 3, 20), 'Z': datetime.date(2024, 3, 20)},
    2: {'A': datetime.date(2024, 3, 20), 'B': datetime.date(2024, 3, 20), 'C': datetime.date(2024, 3, 20),
        'D': datetime.date(2024, 3, 20), 'E': datetime.date(2024, 3, 20), 'F': datetime.date(2024, 3, 20),
        'G': datetime.date(2024, 3, 20), 'H': datetime.date(2024, 3, 20), 'I': datetime.date(2024, 3, 20),
        'J': datetime.date(2024, 3, 20), 'K': datetime.date(2024, 3, 20), 'L': datetime.date(2024, 3, 27),
        'M': datetime.date(2024, 3, 27), 'N': datetime.date(2024, 3, 27), 'O': datetime.date(2024, 3, 27),
        'P': datetime.date(2024, 3, 27), 'Q': datetime.date(2024, 3, 27), 'R': datetime.date(2024, 3, 27),
        'S': datetime.date(2024, 3, 27), 'T': datetime.date(2024, 3, 27), 'U': datetime.date(2024, 3, 27),
        'V': datetime.date(2024, 3, 27), 'W': datetime.date(2024, 3, 27), 'X': datetime.date(2024, 3, 27),
        'Y': datetime.date(2024, 3, 27), 'Z': datetime.date(2024, 3, 27)},
    5: {'A': datetime.date(2024, 3, 16), 'B': datetime.date(2024, 3, 16), 'C': datetime.date(2024, 3, 16),
        'D': datetime.date(2024, 3, 16), 'E': datetime.date(2024, 3, 16), 'F': datetime.date(2024, 3, 16),
        'G': datetime.date(2024, 3, 16), 'H': datetime.date(2024, 3, 16), 'I': datetime.date(2024, 3, 16),
        'J': datetime.date(2024, 3, 16), 'K': datetime.date(2024, 3, 16), 'L': datetime.date(2024, 3, 23),
        'M': datetime.date(2024, 3, 23), 'N': datetime.date(2024, 3, 23), 'O': datetime.date(2024, 3, 23),
        'P': datetime.date(2024, 3, 23), 'Q': datetime.date(2024, 3, 23), 'R': datetime.date(2024, 3, 23),
        'S': datetime.date(2024, 3, 23), 'T': datetime.date(2024, 3, 23), 'U': datetime.date(2024, 3, 23),
        'V': datetime.date(2024, 3, 23), 'W': datetime.date(2024, 3, 23), 'X': datetime.date(2024, 3, 23),
        'Y': datetime.date(2024, 3, 23), 'Z': datetime.date(2024, 3, 23)}
    },
    'Midterm': datetime.date(2024, 2, 13)
}

# Create the calendar
calendar = {}
for event, event_dates in events.items():
    if isinstance(event_dates, dict):
        lab_event = f'{event}'
        for date_letter, event_date in event_dates[practical_number].items():
            if start_date <= event_date <= end_date and date_letter.upper() == student_name[0].upper():
                calendar[event_date] = lab_event
    else:
        if start_date <= event_dates <= end_date:
            calendar[event_dates] = event

# Print the schedule
print('//////////////////////////////////////////////////////')
print('MIE221 (Manufacturing Engineering):')
for date, event in sorted(calendar.items()):
    print(f'{event}: {date.strftime("%B %d, %Y")}')
print('_______________________________________')
print('Note: There are no tutorials for MIE221')
print('//////////////////////////////////////////////////////')

# Ask the user to generate an image
generate_image = input('Do you want to generate an image of the schedule? (yes/no): ')
if generate_image.lower() == 'yes':
    image_width, image_height = 400, 400
    image = Image.new('RGB', (image_width, image_height), color='white')
    draw = ImageDraw.Draw(image)
    font = ImageFont.load_default()

    header_text = 'MIE221 (Manufacturing Engineering):'
    draw.text((50, 10), header_text, fill='black', font=font)

    y_position = 50
    for date, event in sorted(calendar.items()):
        draw.text((50, y_position), f'{event}: {date.strftime("%B %d, %Y")}', fill='black', font=font)
        y_position += 30

    image.save('MIE221_Schedule.png')
    print('Schedule saved as "MIE221_Schedule.png"')
else:
    print('Image was not generated.')
