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
course MIE210 for the Winter 2024 semester.

Note: Each course has a separate file.

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

# Copyright (c) 2024, Ibrahim Hassan
# Created on: January 13, 2024
# Version: 1.0.0., January 13, 2024
# Let me know if there are any errors or incorrect data is being generated.
# Data is accurate as of January 13, 2024


from datetime import datetime
from PIL import Image, ImageDraw, ImageFont

lab_schedule = {
    1: ["26-Jan", "9-Feb", "1-Mar", "15-Mar"],
    2: ["2-Feb", "16-Feb", "8-Mar", "22-Mar"],
    3: ["22-Jan", "5-Feb", "26-Feb", "11-Mar"],
    4: ["29-Jan", "12-Feb", "4-Mar", "18-Mar"],
    5: ["26-Jan", "9-Feb", "1-Mar", "15-Mar"],
    6: ["2-Feb", "16-Feb", "8-Mar", "22-Mar"],
    7: ["25-Jan", "8-Feb", "29-Feb", "14-Mar"],
    8: ["1-Feb", "15-Feb", "7-Mar", "21-Mar"],
    9: ["23-Jan", "6-Feb", "27-Feb", "12-Mar"],
    10: ["30-Jan", "13-Feb", "5-Mar", "19-Mar"],
    11: ["22-Jan", "5-Feb", "26-Feb", "11-Mar"],
    12: ["29-Jan", "12-Feb", "4-Mar", "18-Mar"]
}

def get_lab_schedule(practical_section):
    practical_section = int(practical_section)
    if practical_section in lab_schedule:
        return lab_schedule[practical_section]
    else:
        return None

def format_date(date_str, lab_number):
    date_obj = datetime.strptime(date_str + "-2024", "%d-%b-%Y")
    return "Lab {}: {} ".format(lab_number, date_obj.strftime("%A, %B %d, %Y"))

def save_output_to_image(output_text):
    image = Image.new('RGB', (400, 400), color='white')  # change colour if you want
    draw = ImageDraw.Draw(image)

    font = ImageFont.load_default()

    draw.text((10, 10), output_text, font=font, fill='black')

    image.save("MIE210_Schedule.png")
    print("Image generated and saved as 'MIE210_Schedule'")

# Take user input
practical_section_input = input("Enter your MIE210 practical section number (1-12): ")
course_name = "MIE210 (Thermodynamics)"

# Get lab schedule for the entered practical section
lab_dates = get_lab_schedule(practical_section_input)

# Generate output
output_text = ""
if lab_dates:
    output_text += '//////////////////////////////////////////////////////\n'
    output_text += "{}:\nPractical/Lab schedule for PRA0{}:\n".format(course_name, practical_section_input)
    for i, date_str in enumerate(lab_dates, start=1):
        formatted_date = format_date(date_str, i)
        output_text += formatted_date + '\n'
    output_text += '------------------------------------------------------\n'
    output_text += 'Quizzes (in your tutorials):\n'
    output_text += 'Quiz 1 (Feb 12, in tutorials, 40 min long)\n'
    output_text += 'Quiz 2 (Apr 1, in tutorials, 40 min long)\n'
    output_text += '------------------------------------------------------\n'
    output_text += 'Midterm:\n'
    output_text += 'Midterm (Mar 6, in EX 100, 90 min long, 4:10-5:40 pm)\n'
    output_text += '//////////////////////////////////////////////////////\n'

    # Display the output
    print(output_text)

    generate_image = input("Do you want to generate an image of the output? (yes/no): ").lower() == 'yes'

    if generate_image:
        save_output_to_image(output_text)
else:
    print("Invalid practical section number")
