#/usr/bin/python3
# Made by TypicalCrusader
# Patron Doctrine Automation Script
# Part of Typical's Crusader Kings III Automation Scripts (TCK3AS)
# For use with Elder Kings II Patron Gods Mechanic combined with The Four Nations CK3 implementation of it

import sys, os


def main():

    # Gets 7 Variables from user input
    doctrine_name_1, doctrine_name_2, doctrine_name_3, triggerinos, sin, virtue, name_of_god_loc = get_input_from_user()

    # Convert into output strings list for file
    output_strings = get_output_strings_for_writing(doctrine_name_1, doctrine_name_2, doctrine_name_3, triggerinos,
                                                    sin, virtue)

    # Convert into output strings loc list for file
    output_locs = get_output_loc_for_writing(doctrine_name_1, doctrine_name_2, doctrine_name_3, name_of_god_loc)

    # Check if files exist and write them if applicable
    write_files_to_system(output_strings, output_locs)


def get_input_from_user():
    doctrine_name_1 = input("input the type of god ie: death_god\n")
    if not doctrine_name_1:
        while not doctrine_name_1:
            doctrine_name_1 = input("No input found, input the type of god ie: death_god\n")

    name_of_god_loc = input("input the name of god ie: Father of Threads\n")

    doctrine_name_2 = name_of_god_loc.replace(" ", "_")
    doctrine_name_2 = doctrine_name_2.strip().lower()

    gods_for_doctrine_2_if = ["high_god", "devil"]

    if doctrine_name_2 and not any(god in doctrine_name_1 for god in gods_for_doctrine_2_if):

        doctrine_name_3 = input("input whether the good is good or evil (good/evil)\n")
        doctrine_name_3 = doctrine_name_3.strip()[:4].lower()

        if doctrine_name_3 != "good" and doctrine_name_3 != "evil":
            while doctrine_name_3 != "good" and doctrine_name_3 != "evil":
                print("Invalid input, please try again")
                doctrine_name_3 = input("input whether the good is good or evil (good/evil)\n")
                doctrine_name_3 = doctrine_name_3.strip()[:4].lower()

    else:
        doctrine_name_3 = ""

    triggerinos = input("write any additional trigger like flag:doctrine_doctrine_polytheism = "
                        "{ is_in_list = selected_doctrines }\n")

    gods_for_triggerinos_if = ["devil", "war_god", "main_god", "fate_god"]

    if triggerinos and not any(god in doctrine_name_1 for god in gods_for_triggerinos_if):
        virtue = input("write one virtue trait\n")
        if virtue:
            sin = input("write one sin trait\n")
    else:
        virtue = ""
        sin = ""

    return doctrine_name_1, doctrine_name_2, doctrine_name_3, triggerinos, virtue, sin, name_of_god_loc


def get_output_strings_for_writing(doctrine_name_1, doctrine_name_2, doctrine_name_3, triggerinos, virtue, sin):
    left_curly_brace = "{"
    right_curly_brace = "}"

    if not doctrine_name_3:
        output_string_1 = f"\n\tpantheon_{doctrine_name_1}_{doctrine_name_2} = " \
                          f"{left_curly_brace}"
        output_string_3 = ""
        output_string_4 = ""

    else:
        output_string_1 = f"\n\tpantheon_{doctrine_name_1}_{doctrine_name_2}_{doctrine_name_3} = " \
                          f"{left_curly_brace}"
        if "good" in doctrine_name_3:
            output_string_3 = f"\n\n\t\tparameters = {left_curly_brace}" \
                              f"\n\t\t\tpantheon_adds_diety_{doctrine_name_2} = yes" \
                              f"\n\t\t{right_curly_brace}"
        else:
            output_string_3 = ""

        if virtue:
            output_string_4 = f"\n\t\ttraits = {left_curly_brace}" \
                              f"\n\t\t\tvirtues = {left_curly_brace}" \
                              f"\n\t\t\t\t{virtue}" \
                              f"\n\t\t\t{right_curly_brace}" \
                              f"\n\t\t\tsins = {left_curly_brace}" \
                              f"\n\t\t\t\t{sin}" \
                              f"\n\t\t\t{right_curly_brace}" \
                              f"\n\t\t{right_curly_brace}"
        else:
            output_string_4 = ""

    output_string_2 = f"\n\t\tcan_pick = {left_curly_brace}" \
                          f"\n\t\t\t{triggerinos}" \
                          f"\n\t\t{right_curly_brace}"
    output_string_5 = f"\n\t{right_curly_brace}"

    return [output_string_1, output_string_2, output_string_3, output_string_4, output_string_5]


def get_output_loc_for_writing(doctrine_name_1, doctrine_name_2, doctrine_name_3, name_of_god_loc):
    if not doctrine_name_3:
        output_loc_1 = f"l_english:\n "
        output_loc_2 = f"pantheon_{doctrine_name_1}_{doctrine_name_2}_name: \"" \
                       f"{name_of_god_loc}\"" \
                       f"\n pantheon_{doctrine_name_1}_{doctrine_name_2}_desc: """ \
                       f"doctrine_parameter_pantheon_adds_diety_{doctrine_name_2}: \"Adds {name_of_god_loc} " \
                       f"to the pantheon\""
    else:
        output_loc_1 = f"l_english:\n "
        output_loc_2 = f"pantheon_{doctrine_name_1}_{doctrine_name_2}_{doctrine_name_3}_name: \"" \
                   f"{name_of_god_loc}\"" \
                   f"\n pantheon_{doctrine_name_1}_{doctrine_name_2}_{doctrine_name_3}_desc: """ \
                   f"doctrine_parameter_pantheon_adds_diety_{doctrine_name_2}: \"Adds {name_of_god_loc} " \
                   f"to the pantheon\""
    return [output_loc_1, output_loc_2]


def write_files_to_system(output_strings, output_locs):
    pathname = os.path.dirname(sys.argv[0])

    # If the path does not exist, write with reckless abandon
    if not os.path.exists(pathname + "/p_doctrine.txt"):
        with open('p_doctrine.txt', 'x', encoding="utf_8_sig") as output_file:
            output_file.writelines(output_strings)
            print("created doctrine file")
            output_file.close()
        with open('p_doctrine_l_english.yml', 'x', encoding="utf_8_sig") as loc_file:
            loc_file.writelines(output_locs)
            print("created doctrine loc file")
            loc_file.close()

    # If the path does exist, ask the user what to do
    elif os.path.exists(pathname + "/p_doctrine.txt"):
        # Capture if the user wants to overwrite the whole file
        bool_for_write = input("The Output file already exists do you wish to override it y/n\n"
                               "y: will overwrite the whole file\n"
                               "n: will append to the file\n")
        # take only the first letter of the answer and convert it to lowercase for easy comparison
        bool_for_write = bool_for_write.strip()[:1].lower()

        # Check if the answer is y or n
        if not bool_for_write == "y" and not bool_for_write == "n":
            # Since the user didn't input y or n, keep capturing until they give you an answer
            while not bool_for_write == "y" and not bool_for_write == "n":
                print("Invalid answer, please try again.")
                bool_for_write = input("The Output file already exists do you wish to override it y/n\n"
                                       "y: will overwrite the whole file\n"
                                       "n: will append to the file\n")
                # take only the first letter of the answer and convert it to lowercase for easy comparison
                bool_for_write = bool_for_write.strip()[:1].lower()

        # If user wants to override the whole file, set the write mode to w
        if bool_for_write == "y":
            with open('p_doctrine.txt', 'w', encoding="utf_8_sig") as output_file:
                output_file.writelines(output_strings)
                print("Overwritten doctrine file")
                output_file.close()
            with open('p_doctrine_l_english.yml', 'w', encoding="utf_8_sig") as loc_file:
                loc_file.writelines(output_locs)
                print("Overwritten doctrine loc file")
                loc_file.close()

        # If they don't want to override the whole file, set the write mode to a
        elif bool_for_write == "n":
            with open('p_doctrine.txt', 'a', encoding="utf_8_sig") as output_file:
                output_file.writelines(output_strings)
                print("Updated doctrine file")
                output_file.close()
            with open('p_doctrine_l_english.yml', 'a', encoding="utf_8_sig") as loc_file:
                loc_file.writelines(output_locs)
                print("Updated doctrine loc file")
                loc_file.close()
        else:
            print("something went wrong with writing files")


if __name__ == "__main__":
    main()
