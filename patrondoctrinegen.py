#/usr/bin/python3
# Made by TypicalCrusader
# Patron Doctrine Automation Script
# Part of Typical's Crusader Kings III Automation Scripts (TCK3AS)
# For use with Elder Kings II Patron Gods Mechanic combined with The Four Nations CK3 implementation of it

#TODO: break script out into different functions to call to allow integration with other scripts or gui
#      Make it loop if they don't put a god name in, instead of throwing it to a clean exit
#      Make it clear that not overriding it will append it, since appending seems the more likely choice every time
#      BUG: if you do "high_god" or "devil" it was not assigning output 2,3,4,5. Currently blank.
import sys, os


def main():
    left_curly_brace = "{"
    right_curly_brace = "}"

    # needed for later
    pathname = os.path.dirname(sys.argv[0])

    doctrine_name_1 = input("input the type of god ie: death_god\n")
    if not doctrine_name_1:
        print("You need to put a god name, run the script again")
        exit(1)

    name_of_god_loc = input("input the name of god ie: Father of Threads\n")

    doctrine_name_2 = name_of_god_loc.replace(" ", "_")
    doctrine_name_2 = doctrine_name_2.strip().lower()

    gods_for_doctrine_2_if = ["high_god", "devil"]

    if doctrine_name_2 and not any(god in doctrine_name_1 for god in gods_for_doctrine_2_if):
        doctrine_name_3 = input("input whether the good is good or evil (good/evil)\n")
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

    if not doctrine_name_3:
        output_string_1 = f"\n\tpantheon_{doctrine_name_1}_{doctrine_name_2} = " \
                          f"{left_curly_brace}"
        output_loc_1 = f"l_english:\n "
        output_loc_2 = f"pantheon_{doctrine_name_1}_{doctrine_name_2}_name: \"" \
                       f"{name_of_god_loc}\"" \
                       f"\n pantheon_{doctrine_name_1}_{doctrine_name_2}_desc: """ \
                       f"doctrine_parameter_pantheon_adds_diety_{doctrine_name_2}: \"Adds {name_of_god_loc} " \
                       f"to the pantheon\""
        output_string_2 = ""
        output_string_3 = ""
        output_string_4 = ""
        output_string_5 = ""
    else:
        output_string_1 = f"\n\tpantheon_{doctrine_name_1}_{doctrine_name_2}_{doctrine_name_3} = " \
                          f"{left_curly_brace}"
        if "good" in doctrine_name_3:
            output_string_3 = f"\n\n\t\tparameters = {left_curly_brace}" \
                              f"\n\t\t\tpantheon_adds_diety_{doctrine_name_2} = yes" \
                              f"\n\t\t{right_curly_brace}"
        else:
            output_string_3 = ""
        output_string_2 = f"\n\t\tcan_pick = {left_curly_brace}" \
                          f"\n\t\t\t{triggerinos}" \
                          f"\n\t\t{right_curly_brace}"
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
        output_string_5 = f"\n\t{right_curly_brace}"

        output_loc_1 = f"l_english:\n "
        output_loc_2 = f"pantheon_{doctrine_name_1}_{doctrine_name_2}_{doctrine_name_3}_name: \"" \
                       f"{name_of_god_loc}\"" \
                       f"\n pantheon_{doctrine_name_1}_{doctrine_name_2}_{doctrine_name_3}_desc: """ \
                       f"doctrine_parameter_pantheon_adds_diety_{doctrine_name_2}: \"Adds {name_of_god_loc} " \
                       f"to the pantheon\""


    if not os.path.exists(pathname + "/p_doctrine.txt"):
        with open('p_doctrine.txt', 'x', encoding="utf_8_sig") as output_file:
            output_file.writelines(
                [output_string_1, output_string_2, output_string_3, output_string_4,
                    output_string_5])
            print("created doctrine file")
            output_file.close()
        with open('p_doctrine_l_english.yml', 'x', encoding="utf_8_sig") as loc_file:
            loc_file.writelines([output_loc_1, output_loc_2])
            print("created doctrine loc file")
            loc_file.close()
    elif os.path.exists(pathname + "/p_doctrine.txt"):
        # Capture if the user wants to overwrite the whole file
        bool_for_write = input("The Output file already exists do you wish to override it ")
        # take only the first letter of the answer and convert it to lowercase for easy comparison
        bool_for_write = bool_for_write.strip()[:1].lower()
        # print(bool_for_write)
        if not bool_for_write == "y" and not bool_for_write == "n":
            while not bool_for_write == "y" and not bool_for_write == "n":

                bool_for_write = input("Invalid answer, please try again."
                                       "The Output file already exists do you wish to override it? ")
                # take only the first letter of the answer and convert it to lowercase for easy comparison
                bool_for_write = bool_for_write.strip()[:1].lower()
                if bool_for_write == "y":
                    with open('p_doctrine.txt', 'w', encoding="utf_8_sig") as output_file:
                        output_file.writelines(
                            [output_string_1, output_string_2, output_string_3, output_string_4,
                             output_string_5])
                        print("created doctrine file")
                        output_file.close()
                    with open('p_doctrine_l_english.yml', 'w', encoding="utf_8_sig") as loc_file:
                        loc_file.writelines([output_loc_1, output_loc_2])
                        print("created doctrine loc file")
                        loc_file.close()
                    break

                elif bool_for_write == "n":
                    with open('p_doctrine.txt', 'a', encoding="utf_8_sig") as output_file:
                        output_file.writelines(
                            [output_string_1, output_string_2, output_string_3, output_string_4,
                             output_string_5])
                        print("created doctrine file")
                        output_file.close()
                    with open('p_doctrine_l_english.yml', 'a', encoding="utf_8_sig") as loc_file:
                        loc_file.writelines([output_loc_2])
                        print("created doctrine loc file")
                        loc_file.close()
                    break
                else:
                    bool_for_write = "Answer is invalid"
        else:
            if bool_for_write == "y":
                with open('p_doctrine.txt', 'w', encoding="utf_8_sig") as output_file:
                    output_file.writelines(
                        [output_string_1, output_string_2, output_string_3, output_string_4,
                         output_string_5])
                    print("created doctrine file")
                    output_file.close()
                with open('p_doctrine_l_english.yml', 'w', encoding="utf_8_sig") as loc_file:
                    loc_file.write([output_loc_1, output_loc_2])
                    print("created doctrine loc file")
                    loc_file.close()
            elif bool_for_write == "n":
                with open('p_doctrine.txt', 'a', encoding="utf_8_sig") as output_file:
                    output_file.writelines(
                        [output_string_1, output_string_2, output_string_3, output_string_4,
                         output_string_5])
                    print("created doctrine file")
                    output_file.close()
                with open('p_doctrine_l_english.yml', 'a', encoding="utf_8_sig") as loc_file:
                    loc_file.writelines([output_loc_2])
                    print("created doctrine loc file")
                    loc_file.close()


if __name__ == "__main__":
    main()
