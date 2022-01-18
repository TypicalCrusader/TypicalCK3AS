# Todo
# todo actually allow write options
# todo additional error checking
# todo help documentation(py <script> help)
# todo Patronyms???
# todo Something for ethnicities. Maybe ask if they want to do ethnicities, and have them type the item, then the weight
# todo make name generation cutoff per line "smart" @ 115 characters max
# todo Allow some sort of rng generation of mercenary company names
# todo dynasty_of_location_prefix option
# todo graphical cultures inside of cultures
# todo mercenary names inside of cultures

import sys
import os
input_path_folder = 'culture_input'
output_path_folder = 'culture_output'
cwd = os.getcwd()
input_path = os.path.join(cwd, input_path_folder)
output_path = os.path.join(cwd, output_path_folder)


def main():
    # Check Python Version to make sure this script will run successfully
    check_python_version()
    create_culture()
    while True:
        yn = input("Do you want to run the script again? (y)/(n)")
        if yn[:1].lower() == "y":
            create_culture()
        else:
            exit(0)


def create_culture():
    # Checks that the script can actually run successfully
    (graphical_cultures_file, mercenary_names_file, dynasty_names_file,
     male_names_file, female_names_file) = check_input_files()
    # Checks file for culture group, and options related to that
    culture_group, path_exists, path_append_override_new = check_or_create_culture_group()
    # if the path doesn't exist, or we're not appending, we need to do graphical cultures for the group
    if not path_exists or path_append_override_new[:1] != 'a':
        graphical_cultures = read_input_file(graphical_cultures_file)
        mercenary_names = read_input_file(mercenary_names_file)
    else:
        graphical_cultures = []
        mercenary_names = []

    # Ask for input for culture name
    culture_name = get_culture_name()
    # Ask for input for culture color
    culture_color = get_culture_color()
    # Read dynasty_names file
    dynasty_names = read_input_file(dynasty_names_file)
    # Read male_names file
    male_names = read_input_file(male_names_file)
    # Read female_names file
    female_names = read_input_file(female_names_file)
    # Ask for input on found_name_dynasties
    dynasty_of_location_prefix = dynasty_of_location_prefix_option()
    founder_named_dynasties = founder_named_dynasties_option()
    dynasty_title_names = dynasty_title_names_option()
    dynasty_name_first = dynasty_name_first_option()
    # Ask for input on patronyms
    # patronyms = get_patronyms_options()
    # Ask for input on Ethnicities
    # ethnicities = get_ethnicities_options()
    # Generate code output for file
    output_lines = get_output_lines(culture_name, culture_color, dynasty_names, male_names,
                                    female_names, culture_group, graphical_cultures, mercenary_names,
                                    founder_named_dynasties=founder_named_dynasties,
                                    dynasty_title_names=dynasty_title_names,
                                    dynasty_name_first=dynasty_name_first,
                                    dynasty_of_location_prefix=dynasty_of_location_prefix)

    # Write code to file
    write_to_file(output_lines, culture_group)


def check_input_files():
    print("Checking input files")
    graphical_cultures_file = os.path.join(input_path, 'graphical_cultures.txt')
    mercenary_names_file = os.path.join(input_path, 'mercenary_names.txt')
    dynasty_names_file = os.path.join(input_path, 'dynasty_names.txt')
    male_names_file = os.path.join(input_path, 'male_names.txt')
    female_names_file = os.path.join(input_path, 'female_names.txt')
    files = [graphical_cultures_file, mercenary_names_file, dynasty_names_file,
             male_names_file, female_names_file]
    # Debug lines, remove later
    for file in files:
        print(f"Path: {file}")
    # end remove
    valid_files = 0
    for file in files:
        valid_files += check_input_file(file)
    if valid_files != len(files):
        print("Not all required input files were available. They have been Created. Please fill them out.")
        exit(1)
    else:
        print("All input files exist!")
    return files[0], files[1], files[2], files[3], files[4]


def check_input_file(filepath):
    print(f"checking {filepath}")
    exists = os.path.exists(filepath)
    if exists:
        return 1
    else:
        print(f"{filepath[2:]} does not exist")
        with open(filepath, 'w'):
            pass
        print(f"{filepath} has been created")
        return 0


def check_or_create_culture_group():
    print("Ready to ask about culture_group information")
    # Ask user for the culture_group they want to edit
    # This is used for the filename, and if it's created from scratch
    culture_group = input("What is the name of the culture_group you want to create/edit?")
    # While loop if they just hit enter with no text entered until they enter text
    while not culture_group:
        print("No text entered, please enter the name of the culture_group")
        culture_group = input("What is the name of the culture_group you want to create/edit?")

    # Create culture group filename based off of culture_group
    culture_group_filename = culture_group + ".txt"
    # Verify the path exists
    path_exists = os.path.exists(os.path.join(output_path, culture_group_filename))
    # If the path doesn't exist, this is easy, we're writing the file
    if not path_exists:
        return culture_group, path_exists, ""
        pass
    # If it does exist...Ask the user if they want to append, override, or create a new file
    else:
        append_override_new = input('Do you want to (a)ppend, (o)verride, or create a (n)ew file?')
        while (append_override_new[:1] != "a" or append_override_new[:1] != "o" or
               append_override_new[:1] != "n"):
            print(f"Invalid Input: {append_override_new}")
            append_override_new = input('Do you want to (a)ppend, (o)verride, or create a (n)ew file?')
        return culture_group, path_exists, append_override_new


def read_input_file(filepath, strip=True, replace_spaces=False) -> list:
    print(f"reading & formatting file: {filepath}")
    # Open the file and read the lines
    with open(filepath, 'r') as file:
        lines = file.readlines()

    # Strip extra whitespace if argument key. Note doing this twice is "inefficient" but more readable
    if strip:
        lines = [line.strip() for line in lines]

    if replace_spaces:
        lines = [line.replace(' ', '_') for line in lines]

    # check for blank lines and remove them
    for index, line in enumerate(lines):
        if not line:
            lines.pop(index)

    return lines


def get_culture_name() -> str:
    print("Asking about culture")
    # Get the culture name from input
    culture_name = input("What is the name of the culture you'd like to generate?")
    while not culture_name:
        print("No culture input. This is required")
        culture_name = input("What is the name of the culture you'd like to generate?")
    # Sanitize the input a little
    culture_name.strip().replace(" ", "_")
    return culture_name


def get_culture_color() -> str:
    print("Asking about the color of the culture")
    culture_color = input("Please input a CK III color value. Example: 0.44 0.018 0.11")
    while not culture_color:
        print("Culture color not entered")
        yn = input("if you would like to skip entering a color type y,"
                   " otherwise hit any key to get the color input again")
        # Check to make sure there's actually input
        if yn:
            # if first key entered is y, don't just exit the loop, return from the function since they don't care
            if yn[:1] == 'y':
                return ""
        else:
            culture_color = input("Please input a CK III color value. Example: 0.44 0.018 0.11")
    # Strip the input
    culture_color.strip()
    # Split at the spaces
    culture_colors = culture_color.split(" ")
    # Do sanitization on each color
    for index, color in enumerate(culture_colors):
        # Verify the color is a float
        if not is_float(color):
            print("One of the colors entered was not valid")
            return get_culture_color()
        # More sanitization. Strip string of leading zeros, convert it to a float, round it, convert back to a string.
        culture_colors[index] = str(round(float(color.lstrip("0")), 3))
    culture_color = ' '.join(culture_colors)
    return culture_color


def dynasty_of_location_prefix_option() -> str:
    yn = None
    while yn is None:
        yn = input("Do you want a dynasty_of_location_prefix? (y)/(n), (d) for description")
        if yn[:1].lower() == "y":
            yn = True
        elif yn[:1].lower() == "d":
            print("Property Description: \n"
                  "Cultural equivalent of 'of', when followed by a placename, e.g "
                  "- Geoffrey 'of' Monmouth, Chrétien 'de' Troyes (Christian 'of' Troyes)")
        else:
            yn = False

    dynasty_of_location_prefix = ""
    if yn is True:
        while not dynasty_of_location_prefix:
            dynasty_of_location_prefix = input("Enter the dynasty_of_location_prefix, ie: dynnp_von")
    return dynasty_of_location_prefix


def founder_named_dynasties_option() -> bool:
    founder_named_dynasties = None
    while founder_named_dynasties is None:
        yn = input("Do you want founder_named_dynasties? (y)/(n), (d) for description")
        if yn[:1].lower() == "y":
            founder_named_dynasties = True
        elif yn[:1].lower() == "d":
            print("Property Description:\n"
                  "Optional (default is no), uses dynasty name rather than title name when appropriate")
        else:
            founder_named_dynasties = False
    return founder_named_dynasties


def dynasty_name_first_option() -> bool:
    dynasty_name_first = None
    while dynasty_name_first is None:
        yn = input("Do you want dynasty_name_first option? (y)/(n), (d) for description")
        if yn[:1].lower() == "y":
            dynasty_name_first = True
        elif yn[:1].lower() == "d":
            print("Property Description:\n"
                  "Optional (default is no), dynasty name comes before given name (Far-East Style)")
        else:
            dynasty_name_first = False
    return dynasty_name_first


def dynasty_title_names_option() -> bool:
    dynasty_title_names = None
    while dynasty_title_names is None:
        yn = input("Do you want dynasty_title_names? (y)/(n), (d) for description")
        if yn[:1].lower() == "y":
            dynasty_title_names = True
        elif yn[:1].lower() == "d":
            print("Property Description:\n"
                  "Optional (default is no), uses dynasty name rather than title name when appropriate")
        else:
            dynasty_title_names = False
    return dynasty_title_names


def get_patronyms_options():
    pass


def get_ethnicities_options():
    pass


def get_output_lines(culture_name: str, culture_color: str, dynasty_names: list[str], male_names: list[str],
                     female_names: list[str], group_culture: str = None, graphical_cultures: list = None,
                     mercenary_names: list = None, ethnicities: list = None,
                     founder_named_dynasties: bool = None, dynasty_name_first: bool = None,
                     dynasty_title_names: bool = None, dynasty_of_location_prefix: str = "") -> list[str]:
    # Quick note about curly braces and strings. inside a normal string, curly braces are curly braces
    # However inside formatted strings (f'') and (f"") curly braces ({}) are special.
    # You can bypass the restrictions by doing a double curly brace ({{ or }})
    output_lines = []

    # Group Culture
    if group_culture:
        # noinspection PyArgumentList
        output_lines.append(f"{group_culture}_group = {{")

    # Graphical Cultures
    output_lines.append("\tgraphical_cultures = {")
    if graphical_cultures:
        for item in graphical_cultures:
            output_lines.append(f"\t\t{item}")
    output_lines.append("\t}")
    output_lines.append("")

    # Mercenary names
    if mercenary_names:
        output_lines.append("\tmercenary_names = {")
        for item in mercenary_names:
            output_lines.append(f"\t\t{{ name = \"{item}\" }}")
        output_lines.append("\t}")
        output_lines.append("")

    # Culture
    output_lines.append(f"\t{culture_name} = {{")

    # Culture Color
    output_lines.append(f"\t\tcolor = hsv{{ {culture_color} }}")
    output_lines.append("")

    # Cadet Dynasty Names
    output_lines.append("\t\tcadet_dynasty_names = {")
    for item in dynasty_names:
        output_lines.append(f"\t\t\t\"dynn_{item}\"")
    output_lines.append("\t\t}")
    output_lines.append("")

    # Dynasty Names
    output_lines.append("\t\tdynasty_names = {")
    for item in dynasty_names:
        output_lines.append(f"\t\t\t\"dynn_{item}\"")
    output_lines.append("\t\t}")
    output_lines.append("")

    # Male Names
    output_lines.append("\t\tmale_names = {")
    male_names = " ".join(male_names)
    output_lines.append(f"\t\t\t{male_names}")
    output_lines.append("\t\t}")
    output_lines.append("")

    # Female Names
    output_lines.append("\t\tfemale_names = {")
    female_names = " ".join(female_names)
    output_lines.append(f"\t\t\t{female_names}")
    output_lines.append("\t\t}")
    output_lines.append("")

    # Dynasty of location prefix option
    if dynasty_of_location_prefix:
        output_lines.append(f"\t\tdynasty_of_location_prefix = \"{dynasty_of_location_prefix}\"")

    # Patronym Options for later...

    # Name display options
    if founder_named_dynasties:
        output_lines.append("\t\tfounder_named_dynasties = yes")

    if dynasty_title_names:
        output_lines.append("\t\tdynasty_title_names = yes")

    if dynasty_name_first:
        output_lines.append("\t\tdynasty_name_first = yes")

    # Ethnicity Options
    if ethnicities:
        output_lines.append("\t\tethnicities = {")
        for item in ethnicities:
            output_lines.append(f"\t\t\t{item}")
        output_lines.append("\t\t}")
        output_lines.append("")

    # File End
    output_lines.append("\t}")
    output_lines.append("}")

    # Add newlines so I don't have to
    output_lines = [line+"\n" for line in output_lines]

    return output_lines


def write_to_file(output_list: list[str], file_name: str):
    output_file = os.path.join(output_path, file_name + ".txt")
    with open(output_file, 'w') as file:
        file.writelines(output_list)
    print(f"{output_file} written!")


def is_float(string) -> bool:
    try:
        float(string)
        return True
    except ValueError:
        return False


def check_python_version() -> None:
    major = int(sys.version_info.major)
    minor = int(sys.version_info.minor)
    if major == 3 and minor >= 9:
        return
    else:
        print(f"The minimum python version to run this script is 3.9, your version is: {major}.{minor}")


if __name__ == "__main__":
    main()
