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
course MIE234 for the Winter 2024 semester. Everyone had similar quiz and midterm schedules and therefore, this script will only

Note: Each course has a separate file.

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

# Copyright (c) 2024, Ibrahim Hassan
# Created on: January 13, 2024
# Version: 1.1.0., January 14, 2024
# Let me know if there are any errors or incorrect data is being generated.
# Data is accurate as of January 14, 2024
# Version history:
# Version: 1.0.0., January 13, 2024: Original
# Version: 1.1.0., January 14, 2024: updated to display exact Quiz dates instead of Quiz week dates.

################################################################################
import datetime
from PIL import Image, ImageDraw, ImageFont

# Dates have been updated since V1.0.0 to display exact Quiz dates instead of Quiz week dates.
# Updated IDE link is here: 
# Define the data for Tutorial sections 1 and 3
tutorial_1_3_data = {
    "Quiz 1": "Jan 24, 2024, 12-1:30pm",
    "Quiz 2": "Jan 31, 2024, 12-1:30pm",
    "Midterm 1": "Feb 5, 2024",
    "Quiz 3": "March 6, 2024, 12-1:30pm",
    "Quiz 4": "March 13, 2024, 12-1:30pm",
    "Midterm 2": "March 18, 2024",
    "Quiz 5": "April 3, 2024, 12-1:30pm",
    "Quiz 6": "April 10, 2024, 12-1:30pm",
}

# Define the data for Tutorial sections 2 and 4
tutorial_2_4_data = {
    "Quiz 1": "Jan 24, 2024, 1:30-3pm",
    "Quiz 2": "Jan 31, 2024, 1:30-3pm",
    "Midterm 1": "Feb 5, 2024, Time-unknown",
    "Quiz 3": "March 6, 2024, 1:30-3pm",
    "Quiz 4": "March 13, 2024, 1:30-3pm",
    "Midterm 2": "March 18, 2024, Time-unknown",
    "Quiz 5": "April 3, 2024, 1:30-3pm",
    "Quiz 6": "April 10, 2024, 1:30-3pm",
}

# Function to get and validate user input
def get_tutorial_section():
    while True:
        try:
            section = int(input("Enter tutorial section (1-4): "))
            if 1 <= section <= 4:
                return section
            else:
                print("Please enter a valid tutorial section (1-4).")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Function to display quiz and midterm schedule for a given tutorial section
def display_schedule(tutorial_section, data):
    print('//////////////////////////////////////////////////////')
    print('MIE234 (Differential Equations):')
    print(f"Quiz and Midterm schedule for tutorial section {tutorial_section}:")
    for quiz_midterm, date_time in data.items():
        print(f"{quiz_midterm}: {date_time}")
    print('//////////////////////////////////////////////////////')

# Get user input for tutorial section
tutorial_section_input = get_tutorial_section()

# Display schedule based on user input
if tutorial_section_input == 1 or tutorial_section_input == 3:
    display_schedule(tutorial_section_input, tutorial_1_3_data)
elif tutorial_section_input == 2 or tutorial_section_input == 4:
    display_schedule(tutorial_section_input, tutorial_2_4_data)


def generate_image(tutorial_section, data):
    print('MIE234 (Differential Equations):')
    output_text = f"MIE234 (Differential Equations):\nQuiz and Midterm schedule for TUT010{tutorial_section}:\n\n"
    for quiz_midterm, date_time in data.items():
        output_text += f"{quiz_midterm}: {date_time}\n"

    # Create image with white background
    image = Image.new("RGB", (300, 300), "white")
    draw = ImageDraw.Draw(image)

    # Use a basic font
    font = ImageFont.load_default()

    # Add text to the image
    draw.text((10, 10), output_text, font=font, fill="black")

    # Save the image
    image.save('MIE234_Schedule.png')
    print("Image generated and saved as MIE234_Schedule.png")

# Function to ask the user if they want to generate an image
def ask_generate_image():
    while True:
        user_input = input("Do you want to generate an image? (yes/no): ").lower()
        if user_input == "yes":
            return True
        elif user_input == "no":
            return False
        else:
            print("Please enter 'yes' or 'no'.")

# Get user input for generating image
generate_image_flag = ask_generate_image()

# Display schedule based on user input
if tutorial_section_input == 1 or tutorial_section_input == 3:
    display_schedule(tutorial_section_input, tutorial_1_3_data)
    if generate_image_flag:
        generate_image(tutorial_section_input, tutorial_1_3_data)
elif tutorial_section_input == 2 or tutorial_section_input == 4:
    display_schedule(tutorial_section_input, tutorial_2_4_data)
    if generate_image_flag:
        generate_image(tutorial_section_input, tutorial_2_4_data)

