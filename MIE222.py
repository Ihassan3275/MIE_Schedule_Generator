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
course MIE222 for the Winter 2024 semester.

Note: Each course has a separate file.

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

# Copyright (c) 2024, Ibrahim Hassan
# Created on: January 13, 2024
# Version: 1.0.0., January 13, 2024
# Let me know if there are any errors or incorrect data is being generated.
# Data is accurate as of January 13, 2024

################################################################################
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont

# Provided data for Practical Section
data = [
    ["Date", "Practical Section", "Experiment-1 - FEA", "Experiment-2 - Mechanical Testing", "Experiment-3 - Failure and Fracture", "Experiment-4 - Strain Gauges", "Experiment-5 - Photoelasticity"],
    ["", "Groups", "Groups", "Groups", "Groups", "Groups"],
    ["16-Jan", 4, "34-36", "37-38", "39-40", "41-42", "43-44"],
    ["18-Jan", 2, "12-14", "15-16", "17-18", "19-20", "21-22"],
    ["23-Jan", 3, "23-25", "26-27", "28-29", "30-31", "32-33"],
    ["25-Jan", 1, "1-3", "4-5", "6-7", "8-9", "10-11"],
    ["30-Jan", 4, "37-38", "39-40", "41-42", "43-44", "34-36"],
    ["01-Feb", 2, "15-16", "17-18", "19-20", "21-22", "12-14"],
    ["06-Feb", 3, "26-27", "28-29", "30-31", "32-33", "23-25"],
    ["08-Feb", 1, "4-5", "6-7", "8-9", "10-11", "1-3"],
    ["13-Feb", 4, "39-40", "41-42", "43-44", "34-36", "37-38"],
    ["15-Feb", 2, "17-18", "19-20", "21-22", "12-14", "15-16"],
    ["27-Feb", 3, "28-29", "30-31", "32-33", "23-25", "26-27"],
    ["29-Feb-2024", 1, "6-7", "8-9", "10-11", "1-3", "4-5"],
    ["05-Mar", 4, "41-42", "43-44", "34-36", "37-38", "39-40"],
    ["07-Mar", 2, "19-20", "21-22", "12-14", "15-16", "17-18"],
    ["12-Mar", 3, "30-31", "32-33", "23-25", "26-27", "28-29"],
    ["14-Mar", 1, "8-9", "10-11", "1-3", "4-5", "6-7"],
    ["19-Mar", 4, "43-44", "34-36", "37-38", "39-40", "41-42"],
    ["21-Mar", 2, "21-22", "12-14", "15-16", "17-18", "19-20"],
    ["26-Mar", 3, "32-33", "23-25", "26-27", "28-29", "30-31"],
    ["28-Mar", 1, "10-11", "1-3", "4-5", "6-7", "8-9"],
]

# Provided data for Tutorial Section
tutorial_data = [
    ["Date", "Tutorial Section"],
    ["16-Jan", 3],
    ["18-Jan", 1],
    ["23-Jan", 4],
    ["25-Jan", 2],
    ["30-Jan", 3],
    ["01-Feb", 1],
    ["06-Feb", 4],
    ["08-Feb", 2],
    ["13-Feb", 3],
    ["15-Feb", 1],
    ["12-Mar", 4],
    ["14-Mar", 2],
    ["19-Mar", 3],
    ["21-Mar", 1],
    ["09-Apr", 4],
    ["11-Apr", 2],
]

# Provided data for Quizzes
quiz_data = [
    ["Date", "Tutorial-section", "Event"],
    ["27-Feb", 4, "Quiz 1: Torsion and Tension"],
    ["29-Feb-2024", 2, "Quiz 1: Torsion and Tension"], #enter year for leap year
    ["05-Mar", 3, "Quiz 1: Torsion and Tension"],
    ["07-Mar", 1, "Quiz 1: Torsion and Tension"],
    ["26-Mar", 4, "Quiz 2: Bending, Compound Stress States, Thin & Thick Cylinders"],
    ["28-Mar", 2, "Quiz 2: Bending, Compound Stress States, Thin & Thick Cylinders"],
    ["02-Apr", 3, "Quiz 2: Bending, Compound Stress States, Thin & Thick Cylinders"],
    ["04-Apr", 1, "Quiz 2: Bending, Compound Stress States, Thin & Thick Cylinders"],
]

def find_scheduled_experiments(practical_section, group_number):
    scheduled_experiments = []

    for row in data[2:]:
        date, section, *groups = row
        if int(section) == practical_section:
            for i, group_range in enumerate(groups):
                if '-' in group_range:
                    start, end = map(int, group_range.split('-'))
                    if start <= group_number <= end:
                        try:
                            formatted_date = datetime.strptime(date, "%d-%b").strftime("%a, %b %d")
                        except ValueError:
                            try:
                                formatted_date = datetime.strptime(date, "%d-%b-%y").strftime("%a, %b %d")
                            except ValueError:
                                # Use format '%d-%b-%Y' for parsing '29-Feb-2024' (considering leap year)
                                formatted_date = datetime.strptime(date, "%d-%b-%Y").strftime("%a, %b %d")
                        scheduled_experiments.append((formatted_date, data[0][i + 2]))
                else:
                    if group_number == int(group_range):
                        try:
                            formatted_date = datetime.strptime(date, "%d-%b").strftime("%a, %b %d")
                        except ValueError:
                            try:
                                formatted_date = datetime.strptime(date, "%d-%b-%y").strftime("%a, %b %d")
                            except ValueError:
                                formatted_date = datetime.strptime(date, "%d-%b-%Y").strftime("%a, %b %d")
                        scheduled_experiments.append((formatted_date, data[0][i + 2]))

    return scheduled_experiments

def find_scheduled_tutorials_and_quizzes(tutorial_section):
    scheduled_tutorials = []
    scheduled_quizzes = []

    for row in tutorial_data[1:]:
        date, section = row
        if int(section) == tutorial_section:
            try:
                formatted_date = datetime.strptime(date, "%d-%b").strftime("%a, %b %d")
            except ValueError:
                try:
                    formatted_date = datetime.strptime(date, "%d-%b-%y").strftime("%a, %b %d")
                except ValueError:
                    formatted_date = datetime.strptime(date, "%d-%b-%Y").strftime("%a, %b %d")
            scheduled_tutorials.append((formatted_date))

    for row in quiz_data[1:]:
        date, section, event = row
        if int(section) == tutorial_section:
            try:
                formatted_date = datetime.strptime(date, "%d-%b").strftime("%a, %b %d")
            except ValueError:
                try:
                    formatted_date = datetime.strptime(date, "%d-%b-%y").strftime("%a, %b %d")
                except ValueError:
                    formatted_date = datetime.strptime(date, "%d-%b-%Y").strftime("%a, %b %d")
            scheduled_quizzes.append((formatted_date, event))

    return scheduled_tutorials, scheduled_quizzes

# User input for Practical Section, Group Number, Tutorial Section, and Quiz Section
practical_section = int(input("Enter your MIE222 practical section (1-4): "))
group_number = int(input("Enter your group number (1-44): "))
tutorial_section_combined = int(input("Enter your MIE222 tutorial section (1-4): "))

# Find and display the result for Practical Section
scheduled_experiments = find_scheduled_experiments(practical_section, group_number)
if scheduled_experiments:
    print('//////////////////////////////////////////////////////')
    print('MIE222 (Solid Mechanics):')
    print(f"Scheduled practicals for PRA010{practical_section} and Group Number {group_number}:")
    for date, experiment_type in scheduled_experiments:
        print(f"{date}: {experiment_type}")
    print('------------------------------------------------------')
else:
    print("No matching records found for the given practical section.")

# Find and display the result for Tutorial Section
scheduled_tutorials_combined, scheduled_quizzes_combined = find_scheduled_tutorials_and_quizzes(tutorial_section_combined)

if scheduled_tutorials_combined or scheduled_quizzes_combined:
    print(f"Scheduled MIE222 tutorials for TUT010{tutorial_section_combined}:")
    for date in scheduled_tutorials_combined:
        print(date)
    print('------------------------------------------------------')

    print(f"Scheduled MIE222 quizzes for TUT010{tutorial_section_combined}:")
    for date, event in scheduled_quizzes_combined:
        print(f"{date}: {event}")
    print('------------------------------------------------------')
else:
    print("No matching records found for the given tutorial section.")
print('Midterm: TBA')
print('//////////////////////////////////////////////////////')

# Function to create an image of the schedule
def create_schedule_image(practical_section, group_number, tutorial_section_combined, scheduled_experiments, scheduled_tutorials_combined, scheduled_quizzes_combined):
    # Create a blank image
    image = Image.new('RGB', (500, 400), 'white')
    draw = ImageDraw.Draw(image)
    font = ImageFont.load_default()

    # Draw schedule for Practical Section
    draw.text((10, 10), 'MIE222 (Solid Mechanics):', font=font, fill='black')
    draw.text((10, 30), 'Practicals Schedule:', font=font, fill='black')
    for date, experiment_type in scheduled_experiments:
        experiment_index = data[0].index(experiment_type) - 1
        draw.text((10, 45 + 15 * experiment_index), f"{date}: {experiment_type}", font=font, fill='blue')

    # Draw schedule for Tutorial and Quiz Sections
    draw.text((10, 160), 'Tutorial and Quiz Schedule:', font=font, fill='black')
    y_offset = 180
    for date in scheduled_tutorials_combined:
        draw.text((10, y_offset), f"{date}: Tutorial", font=font, fill='green')
        y_offset += 15
    for date, event in scheduled_quizzes_combined:
        draw.text((10, y_offset), f"{date}: {event}", font=font, fill='red')
        y_offset += 15

    # Save the image to a file
    image.save('MIE222_Schedule.png')
    print("Image generated successfully.")

# User input for generating an image
generate_image = input("Do you want to generate an image? (yes/no): ").lower()

if generate_image == 'yes':
    # Call the function to create the image
    create_schedule_image(practical_section, group_number, tutorial_section_combined, scheduled_experiments, scheduled_tutorials_combined, scheduled_quizzes_combined)
else:
    print("No image generated.")
