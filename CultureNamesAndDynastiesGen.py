# Todo
# todo fix "new file" writing
# todo additional error checking
# todo Something for ethnicities. Maybe ask if they want to do ethnicities, and have them type the item, then the weight
# todo make name generation cutoff per line "smart" @ 115 characters max
# todo Allow some sort of rng generation of mercenary company names
# todo graphical cultures inside of cultures
# todo mercenary names inside of cultures

import sys
import os
from enum import Enum
input_path_folder = 'culture_input'
output_path_folder = 'culture_output'
cwd = os.getcwd()
input_path = os.path.join(cwd, input_path_folder)
output_path = os.path.join(cwd, output_path_folder)


class Gender(str, Enum):
    male = "male"
    female = "female"


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
    male_names = read_input_file(male_names_file, split_at_spaces=True)
    # Read female_names file
    female_names = read_input_file(female_names_file, split_at_spaces=True)
    # Ask for input on found_name_dynasties
    dynasty_of_location_prefix = dynasty_of_location_prefix_option()
    bastard_dynasty_prefix = bastard_dynasty_prefix_option()
    founder_named_dynasties = founder_named_dynasties_option()
    dynasty_title_names = dynasty_title_names_option()
    dynasty_name_first = dynasty_name_first_option()
    male_ancestor_names_chance = ancestor_name_options(Gender.male)
    female_ancestor_names_chance = ancestor_name_options(Gender.female)
    male_patronyms = get_patronyms_options(Gender.male)
    female_patronyms = get_patronyms_options(Gender.female)
    always_use_patronyms = always_use_patronyms_option()
    # Ask for input on Ethnicities
    # ethnicities = get_ethnicities_options()
    # Generate code output for file
    output_lines = get_output_lines(culture_name, culture_color, dynasty_names, male_names,
                                    female_names, culture_group, graphical_cultures, mercenary_names,
                                    write_mode=path_append_override_new,
                                    founder_named_dynasties=founder_named_dynasties,
                                    dynasty_title_names=dynasty_title_names,
                                    dynasty_name_first=dynasty_name_first,
                                    dynasty_of_location_prefix=dynasty_of_location_prefix,
                                    bastard_dynasty_prefix=bastard_dynasty_prefix,
                                    male_ancestor_names_chance=male_ancestor_names_chance,
                                    female_ancestor_names_chance=female_ancestor_names_chance,
                                    male_patronym_options=male_patronyms,
                                    female_patronym_options=female_patronyms,
                                    always_use_patronyms=always_use_patronyms)

    # Write code to file
    write_to_file(output_lines, culture_group, path_exists, path_append_override_new)


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
        while ('a' not in append_override_new[:1] and 'o' not in append_override_new[:1] and
               'n' not in append_override_new[:1]):
            print(f"Invalid Input: {append_override_new}")
            append_override_new = input('Do you want to (a)ppend, (o)verride, or create a (n)ew file?')
        return culture_group, path_exists, append_override_new


def read_input_file(filepath, strip=True, replace_spaces=False, split_at_spaces=False) -> list:
    print(f"reading & formatting file: {filepath}")
    # Open the file and read the lines
    with open(filepath, 'r') as file:
        lines = file.readlines()

    # Strip extra whitespace if argument key. Note doing this twice is "inefficient" but more readable
    if strip:
        lines = [line.strip() for line in lines]

    # allow splitting at spaces for files like names which commonly are separated this way
    if split_at_spaces:
        split_lines = []
        for line in lines:
            words = line.split()
            for word in words:
                split_lines.append(word)
        lines = split_lines

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
        ynd = input("Do you want a dynasty_of_location_prefix? (y)/(n), (d) for description")
        if ynd[:1].lower() == "y":
            yn = True
        elif ynd[:1].lower() == "d":
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


def bastard_dynasty_prefix_option() -> str:
    yn = None
    while yn is None:
        ynd = input("Do you want a bastard_dynasty_prefix? (y)/(n), (d) for description")
        if ynd[:1].lower() == "y":
            yn = True
        elif ynd[:1].lower() == "d":
            print("Property Description: \n"
                  "Optional, Prefix for bastard dynasties ie: John 'Snow'")
        else:
            yn = False

    bastard_dynasty_prefix = ""
    if yn is True:
        while not bastard_dynasty_prefix:
            bastard_dynasty_prefix = input("Enter the bastard_dynasty_prefix, ie: snow")
    return bastard_dynasty_prefix


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


def ancestor_name_options(gender: Gender) -> dict[str]:
    # Final value to return, use for primary ask/description loop
    use_ancestor_names_chance = None
    # Check gender we're looking at end using description & values related to this
    if gender == Gender.male:
        gender_parent_descriptor = "father"
    else:
        gender_parent_descriptor = "mother"

    while use_ancestor_names_chance is None:
        yn = input(f"Do you want to set up {gender} ancestor name chance? (y)/(n), (d) for description")
        if yn[:1].lower() == "y":
            use_ancestor_names_chance = True
        elif yn[:1].lower() == "d":
            print(f"Chance of {gender} children being named after their paternal or maternal "
                  f"grand{gender_parent_descriptor}, or their {gender_parent_descriptor}. "
                  f"Sum must not exceed 100")
        else:
            use_ancestor_names_chance = {}
    if use_ancestor_names_chance:
        pat_grd_name_chance = None
        while not pat_grd_name_chance:
            pat_grd_name_chance = input(f"Enter paternal grand{gender_parent_descriptor} name % chance")
        mat_grd_name_chance = None
        while not mat_grd_name_chance:
            mat_grd_name_chance = input(f"Enter maternal grand{gender_parent_descriptor} name % chance")
        parent_name_chance = None
        while not parent_name_chance:
            parent_name_chance = input(f"Enter {gender_parent_descriptor} name % chance")
        use_ancestor_names_chance = {
            "pat_grd_name_chance": pat_grd_name_chance,
            "mat_grd_name_chance": mat_grd_name_chance,
            "parent_name_chance": parent_name_chance
        }
    return use_ancestor_names_chance


def get_patronyms_options(gender: Gender) -> dict[str]:
    use_patronyms = None
    while use_patronyms is None:
        yn = input(f"Do you want to set up {gender} patronym localizations? (y)/(n), (d) for description")
        if yn[:1].lower() == "y":
            use_patronyms = True
        elif yn[:1].lower() == "d":
            print(f"Names after the primary {gender} parent. "
                  f"Can use both prefix and suffix together ie: '(Mc)David(son)'. "
                  f"Vowel is used for when the {gender} parent's name starts with a vowel.")
        else:
            use_patronyms = {}

        if use_patronyms:
            use_patronyms = {}
            patronym_prefix = input(f"Enter a patronym prefix for "
                                    f"{gender} parent localization ie: '{gender[0]}_patronym'. "
                                    f"Press Enter to skip this value")
            patronym_prefix_vowel = input(f"Enter a patronym prefix vowel for "
                                          f"{gender} parent localization ie: '{gender[0]}v_patronym'. "
                                          f"Press Enter to skip this value")
            patronym_suffix = input(f"Enter a patronym suffix  for "
                                    f"{gender} parent localization ie: '{gender[0]}_patronym_s'. "
                                    f"Press Enter to skip this value")
            use_patronyms["patronym_prefix"] = patronym_prefix
            use_patronyms["patronym_prefix_vowel"] = patronym_prefix_vowel
            use_patronyms["patronym_suffix"] = patronym_suffix

    return use_patronyms


def always_use_patronyms_option() -> bool:
    always_use_patronyms = None
    while always_use_patronyms is None:
        yn = input("Do you want to always use patronyms? (y)/(n), (d) for description")
        if yn[:1].lower() == "y":
            always_use_patronyms = True
        elif yn[:1].lower() == "d":
            print("Property Description:\n"
                  "Optional (default is no), whether or not a culture always displays Patronyms. "
                  "(Patronyms can also be turned on from government/liege's government)")
        else:
            always_use_patronyms = False
    return always_use_patronyms

def get_ethnicities_options():
    pass


def get_output_lines(culture_name: str, culture_color: str, dynasty_names: list[str], male_names: list[str],
                     female_names: list[str], group_culture: str = None, graphical_cultures: list = None,
                     mercenary_names: list = None, write_mode: str = "", ethnicities: list = None,
                     founder_named_dynasties: bool = None, dynasty_name_first: bool = None,
                     dynasty_title_names: bool = None, dynasty_of_location_prefix: str = "",
                     bastard_dynasty_prefix: str = "", male_ancestor_names_chance: dict[str]= {},
                     female_ancestor_names_chance: dict[str] = {}, male_patronym_options: dict[str] = {},
                     female_patronym_options: dict[str] = {}, always_use_patronyms: bool = False) -> list[str]:
    # Quick note about curly braces and strings. inside a normal string, curly braces are curly braces
    # However inside formatted strings (f'') and (f"") curly braces ({}) are special.
    # You can bypass the restrictions by doing a double curly brace ({{ or }})
    output_lines = []

    # Check to see if we're appending an existing file. If so, we can skip culture_group levelitems
    if 'a' not in write_mode:
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

    if bastard_dynasty_prefix:
        output_lines.append(f"\t\tbastard_dynasty_prefix = \"{bastard_dynasty_prefix}\"")

    # Ancestor parental name chances
    if male_ancestor_names_chance:
        output_lines.append(f"\t\tpat_grf_name_chance = {male_ancestor_names_chance['pat_grd_name_chance']}")
        output_lines.append(f"\t\tmat_grf_name_chance = {male_ancestor_names_chance['mat_grd_name_chance']}")
        output_lines.append(f"\t\tfather_name_chance = {male_ancestor_names_chance['parent_name_chance']}")

    if female_ancestor_names_chance:
        output_lines.append(f"\t\tpat_grm_name_chance = {female_ancestor_names_chance['pat_grd_name_chance']}")
        output_lines.append(f"\t\tmat_grm_name_chance = {female_ancestor_names_chance['mat_grd_name_chance']}")
        output_lines.append(f"\t\tmother_name_chance = {female_ancestor_names_chance['parent_name_chance']}")

    # Patronym Name Options
    if male_patronym_options:
        if male_patronym_options["patronym_prefix"]:
            output_lines.append(f"\t\tpatronym_prefix_male = "
                                f"\"{male_patronym_options['patronym_prefix']}\"")
        if male_patronym_options["patronym_prefix_vowel"]:
            output_lines.append(f"\t\tpatronym_prefix_male_vowel = "
                                f"\"{male_patronym_options['patronym_prefix_vowel']}\"")
        if male_patronym_options["patronym_suffix"]:
            output_lines.append(f"\t\tpatronym_suffix_male = "
                                f"\"{male_patronym_options['patronym_suffix']}\"")

    if female_patronym_options:
        if female_patronym_options["patronym_prefix"]:
            output_lines.append(f"\t\tpatronym_prefix_female = "
                                f"\"{female_patronym_options['patronym_prefix']}\"")
        if female_patronym_options["patronym_prefix_vowel"]:
            output_lines.append(f"\t\tpatronym_prefix_female_vowel = "
                                f"\"{female_patronym_options['patronym_prefix_vowel']}\"")
        if female_patronym_options["patronym_suffix"]:
            output_lines.append(f"\t\tpatronym_suffix_female = "
                                f"\"{female_patronym_options['patronym_suffix']}\"")

    if always_use_patronyms:
        output_lines.append(f"\t\talways_use_patronym = yes")

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

    # End of culture
    output_lines.append("\t}")

    # End of culture group, if we're not appending to an existing file
    if 'a' not in write_mode:
        output_lines.append("}")

    # Add newlines so I don't have to
    output_lines = [line+"\n" for line in output_lines]

    return output_lines


def write_to_file(output_lines: list[str], file_name: str, path_exists: bool, write_option: str):
    file_name = os.path.join(output_path, file_name + ".txt")

    # if the user wants to create a new file using the same culture, add a number to it
    if write_option == 'n':
        file_digit = 0
        # split the filename by _ to see if there's #'s at the end
        split_output_file_name = file_name.split('_')
        # See if there actually is #s at the end
        if split_output_file_name[len(split_output_file_name)-1].isdigit():
            # store this digit
            file_digit = int(split_output_file_name[len(split_output_file_name) - 1])

        if file_digit:
            file_name = split_output_file_name[0] + '_' + str(file_digit + 1)
        else:
            file_name += '_1'

    # This is to bypass using seek and bytes
    if write_option == 'a':
        # Open for reading at the start of the file.
        with open(file_name, 'r') as file:
            # Read the lines
            old_lines = file.readlines()
            # Declare variable to find in the loop
            last_curly_brace_index = None
            # Loop to find the line index of the last curly brace
            for index, line in enumerate(old_lines):
                # FIND THE CLOSING CURLY BRACE
                if '}' in line:
                    # It doesn't matter that it'll find every one, it'll only keep the last one
                    last_curly_brace_index = index
            # Get the index to insert the output lines into the file
            insert_index = last_curly_brace_index
            # create the new_lines list for name sanity
            new_lines = old_lines
            # Slice the output_lines into the list
            new_lines[insert_index:insert_index] = output_lines
            # set output_lines to the new_lines list that was updated for later writing
            output_lines = new_lines

    # We don't have to care about what was in the file so throw it away and write a new file
    with open(file_name, 'w') as file:
        # Finally write the file
        file.writelines(output_lines)
    # Let the user know
    print(f"{file_name} written!")


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

