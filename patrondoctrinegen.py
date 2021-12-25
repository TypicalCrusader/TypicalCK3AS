#/usr/bin/python3
# Made by TypicalCrusader
# Patron Doctrine Automation Script
# Part of Typical's Crusader Kings III Automation Scripts (TCK3AS)

import sys, os


def main():
    left_curly_brace = "{"
    right_curly_brace = "}"

    # needed for later
    pathname = os.path.dirname(sys.argv[0])

    doctrine_name_1 = input("input the type of god ie: death_god\n")
    if doctrine_name_1:
        doctrine_name_2 = input("input the name of god ie: father_of_threads\n")
        if doctrine_name_2 and not "high_god" or "devil" in doctrine_name_1:
            doctrine_name_3 = input("input whether the good is good or evil (good/evil)\n")
            if doctrine_name_3:
                triggerinos = input("write any additional trigger like flag:doctrine_doctrine_polytheism = "
                                    "{ is_in_list = selected_doctrines }\n")
        else:
            triggerinos = input("write any additional trigger like flag:doctrine_doctrine_polytheism = "
                                "{ is_in_list = selected_doctrines }\n")
            doctrine_name_3 = ""
        if triggerinos and "devil" or "war_god" in doctrine_name_1 or "main_god" in doctrine_name_1 or "fate_god" \
                in doctrine_name_1 :
            virtue = input("write one virtue trait\n")
            if virtue:
                sin = input("write one sin trait\n")

                if not doctrine_name_3:
                    output_string_1 = f"\n\tpantheon_{doctrine_name_1}_{doctrine_name_2} = " \
                                      f"{left_curly_brace}"
                else:
                    output_string_1 = f"\n\tpantheon_{doctrine_name_1}_{doctrine_name_2}_{doctrine_name_3} = " \
                                      f"{left_curly_brace}"
                    if "good" in doctrine_name_3:
                        output_string_3 = f"\n\n\t\tparameters = {left_curly_brace}" \
                                            f"\n\t\t\tpantheon_adds_diety_{doctrine_name_2} = yes" \
                                            f"\n\t\t{right_curly_brace}"
                output_string_2 = f"\n\t\tcan_pick = {left_curly_brace}" \
                                  f"\n\t\t\t{triggerinos}" \
                                  f"\n\t\t{right_curly_brace}"
                output_string_4 = f"\n\t\ttraits = {left_curly_brace}" \
                                    f"\n\t\t\tvirtues = {left_curly_brace}" \
                                    f"\n\t\t\t\t{virtue}" \
                                    f"\n\t\t\t{right_curly_brace}" \
                                    f"\n\t\t\tsins = {left_curly_brace}" \
                                    f"\n\t\t\t\t{sin}" \
                                    f"\n\t\t\t{right_curly_brace}" \
                                    f"\n\t\t{right_curly_brace}"
                output_string_5 = f"\n\t{right_curly_brace}"

                name_of_god_loc = doctrine_name_2.replace("_", " ")

                if not doctrine_name_3:
                    output_loc_1 = f"l_english:\n " \
                                   f"pantheon_{doctrine_name_1}_{doctrine_name_2}_name: \"" \
                                   f"{name_of_god_loc}\"" \
                                   f"\n pantheon_{doctrine_name_1}_{doctrine_name_2}_desc: \"\""
                else:
                    output_loc_1 = f"l_english:\n " \
                                   f"pantheon_{doctrine_name_1}_{doctrine_name_2}_{doctrine_name_3}_name: \"" \
                                   f"{name_of_god_loc}\"" \
                                   f"\n pantheon_{doctrine_name_1}_{doctrine_name_2}_{doctrine_name_3}_desc: """\
                                   f"doctrine_parameter_pantheon_adds_diety_{doctrine_name_2}: \"Adds {name_of_god_loc} " \
                                   f"to the pantheon\""

        if not os.path.exists(pathname + "/p_doctrine.txt"):
            with open('p_doctrine.txt', 'w', encoding="utf_8_sig") as output_file:
                if "good" in doctrine_name_3:
                    output_file.writelines(
                        [output_string_1, output_string_2, output_string_3, output_string_4,
                         output_string_5])
                    print("created doctrine file")
                else:
                    output_file.writelines([output_string_1, output_string_2, output_string_4,
                                            output_string_5])
                    output_file.close()
            with open('p_doctrine_l_english.yml', 'w', encoding="utf_8_sig") as loc_file:
                loc_file.writelines(output_loc_1)
                print("created doctrine loc file")
                loc_file.close()
        elif os.path.exists(pathname + "/p_doctrine.txt"):
            # Capture if the user wants to overwrite the whole file
            bool_for_write = input("The Output file already exists do you wish to override it? ")
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
                            if "good" in doctrine_name_3 and doctrine_name_3:
                                output_file.writelines(
                                    [output_string_1, output_string_2, output_string_3, output_string_4,
                                     output_string_5])
                                print("created doctrine file")
                            else:
                                output_file.writelines([output_string_1, output_string_2, output_string_4,
                                                        output_string_5])
                        with open('p_doctrine_l_english.yml', 'w', encoding="utf_8_sig") as loc_file:
                            loc_file.writelines(output_loc_1)
                            print("created doctrine loc file")
                            loc_file.close()
                        break

                    elif bool_for_write == "n":
                        with open('p_doctrine.txt', 'w', encoding="utf_8_sig") as output_file:
                            if "good" in doctrine_name_3:
                                output_file.writelines(
                                    [output_string_1, output_string_2, output_string_3, output_string_4,
                                     output_string_5])
                                print("created doctrine file")
                            else:
                                output_file.writelines([output_string_1, output_string_2, output_string_4,
                                                        output_string_5])
                                output_file.close()
                        with open('p_doctrine_l_english.yml', 'w', encoding="utf_8_sig") as loc_file:
                            loc_file.writelines(output_loc_1)
                            print("created doctrine loc file")
                            loc_file.close()
                        break
                    else:
                        bool_for_write = "Answer is invalid"
            else:
                if bool_for_write == "y":
                    with open('p_doctrine.txt', 'w', encoding="utf_8_sig") as output_file:
                        if "good" in doctrine_name_3:
                            output_file.writelines(
                                [output_string_1, output_string_2, output_string_3, output_string_4,
                                 output_string_5])
                            print("created doctrine file")
                        else:
                            output_file.writelines([output_string_1, output_string_2, output_string_4,
                                                    output_string_5])
                    with open('p_doctrine_l_english.yml', 'w', encoding="utf_8_sig") as loc_file:
                        loc_file.write(output_loc_1)
                        print("created doctrine loc file")
                        loc_file.close()
                elif bool_for_write == "n":
                    with open('p_doctrine.txt', 'w', encoding="utf_8_sig") as output_file:
                        if "good" in doctrine_name_3:
                            output_file.writelines(
                                [output_string_1, output_string_2, output_string_3, output_string_4,
                                 output_string_5])
                            print("created doctrine file")
                        else:
                            output_file.writelines([output_string_1, output_string_2, output_string_4,
                                                    output_string_5])
                    with open('p_doctrine_l_english.yml', 'w', encoding="utf_8_sig") as loc_file:
                        loc_file.writelines(output_loc_1)
                        print("created doctrine loc file")
                        loc_file.close()


if __name__ == "__main__":
    main()
