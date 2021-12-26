#/usr/bin/python3
# Made by TypicalCrusader
# Patron Mechanic Automation Script
# Part of Typical's Crusader Kings III Automation Scripts (TCK3AS)
# For use with Elder Kings II Patron Gods Mechanic

# POSSIBLE ISSUES
# 1. Scripts imples that trait name is p_god_(god_name) so you might need to change output lines,
#   Possible fix remove _god part and just write it while writing name of the god


import sys, os

def main():
    left_curly_brace = "{"
    right_curly_brace = "}"
    left_square_brace = "["
    right_square_brace = "]"
    left_circle_brace = "("
    right_circle_brace = ")"
    comma = ","
    apostrophe ="\'"
    quotation = "\""

    # needed for later
    pathname = os.path.dirname(sys.argv[0])

    index_of_trait = int(input("Write an trait index\nNote:must be an intiger\n"))
    if index_of_trait >= 1:
        name_of_god_loc = input("Write a name of the god in a same way you would localise it\nie: Father of Threads\n")
        name_of_god = name_of_god_loc.replace(" ", "_")
        name_of_god = name_of_god.strip().lower()

        # fuck python for not appending this otherwise
        # Trait Strings
        output_line_1 = f"p_god_{name_of_god} = {left_curly_brace}\n\tindex = {index_of_trait}"
        output_line_2 = f"\n\tshown_in_ruler_designer = no\n\n"
        output_line_3 = f"\n\tname = {left_curly_brace}\n\t\tfirst_valid = {left_curly_brace}" \
                        f"\n\t\t\ttriggered_desc = {left_curly_brace}" \
                        f"\n\t\t\t\ttrigger = {left_curly_brace} NOT = {left_curly_brace} exists = this" \
                        f"{right_curly_brace} {right_curly_brace}\n\t\t\t\tdesc = trait_p_god_{name_of_god}_base\n" \
                        f"\n\t\t\t{right_curly_brace}\n\t\tdesc = trait_p_{name_of_god}\n\t\t{right_curly_brace}" \
                        f"\n\t{right_curly_brace}"
        output_line_4 = f"\n\tdesc = {left_curly_brace}" \
                        f"\n\t\tfirst_valid = {left_curly_brace}" \
                        f"\n\t\t\ttriggered_desc = {left_curly_brace}" \
                        f"\n\t\t\t\ttrigger = {left_curly_brace} NOT = {left_curly_brace} exists = this " \
                        f"{right_curly_brace}" \
                        f"{right_curly_brace}" \
                        f"\n\t\t\t\tdesc = trait_p_god_{name_of_god}_null" \
                        f"\n\t\t\t{right_curly_brace}" \
                        f"\n\t\t\tdesc = trait_p_god_{name_of_god}_character_desc" \
                        f"\n\t\t{right_curly_brace}" \
                        f"\n\t{right_curly_brace}"
        output_line_5 = f"\n\ticon = {left_curly_brace}" \
                        f"\n\t\tfirst_valid = {left_curly_brace}" \
                        f"\n\t\t\ttriggered_desc = {left_curly_brace}" \
                        f"\n\t\t\t\ttrigger = {left_curly_brace} NOT = {left_curly_brace} exists = this " \
                        f"{right_curly_brace} " \
                        f"{right_curly_brace}" \
                        f"\n\t\t\t\tdesc = {quotation}{left_square_brace}Select_CString{left_circle_brace} " \
                        f"GetPlayer.MakeScope.Var{left_circle_brace}"\
                        f"{apostrophe}faith_window{apostrophe}).IsSet{comma} " \
                        f"GetPlayer.Custom{left_circle_brace}{apostrophe}get_god_{name_of_god}_icon{apostrophe}" \
                        f"{right_circle_brace}{comma}" \
                        f"{apostrophe}p_god_{name_of_god}.dds{apostrophe} {right_circle_brace}{right_square_brace}" \
                        f"{quotation}" \
                        f"\n\t\t\t{right_curly_brace}" \
                        f"\n\t\t\tdesc = p_god_{name_of_god}.dds" \
                        f"\n\t\t{right_curly_brace}" \
                        f"\n\t{right_curly_brace}"
        output_line_6 = f"\n{right_curly_brace}\n\n"

        # Custom Localisation Strings
        output_custom_loc_get_god = f"get_god_{name_of_god} = {left_curly_brace}"\
                                    f"\n\ttype = character #replace faith"\
                                    f"\n\ttext = {left_curly_brace}"\
                                    f"\n\t\ttrigger = {left_curly_brace} always = no {right_curly_brace}"\
                                    f"\n\t\tfallback = yes"\
                                    f"\n\t\tlocalization_key = \"_god_{name_of_god}\""\
                                    f"\n\t{right_curly_brace}"\
                                    f"\n{right_curly_brace}\n\n"

        # Localisation Strings
        output_localisation = f"l_english:"
        output_localisation_append = f"\n #Trait Loc"\
                                     f"\n trait_p_god_{name_of_god}_base: \"{name_of_god_loc}\"" \
                                     f"\n trait_p_god_{name_of_god}: \"{name_of_god_loc}\"" \
                                     f"\n trait_p_god_{name_of_god}_null:\"\"" \
                                     f"\n trait_p_god_{name_of_god}_character_desc: \"\"\n" \
                                     f"\n #Custom Loc" \
                                     f"\n god_{name_of_god}: \"{name_of_god_loc}\"" \
                                     f"\n god_god_{name_of_god}_name: \"{name_of_god_loc}\"" \
                                     f"\n desc_god_{name_of_god}: \"\"\n"

        # Scripted Triggers strings
        patron_trait_master_trigger_string_write = f"patron_trait_master_trigger = {left_curly_brace}" \
                                                   f"\n\tOR = {left_curly_brace}" \
                                                   f"\n\t\t#POINTER FOR GENERATOR" \
                                                   f"\n\t\t$TRIGGER$ = {left_curly_brace} TRAIT = _god_{name_of_god}" \
                                                   f"{right_curly_brace}" \
                                                   f"\n\t{right_curly_brace}" \
                                                   f"\n{right_curly_brace}"
        patron_trait_master_trigger_string_append = f"\t$TRIGGER$ = {left_curly_brace} TRAIT = _god_{name_of_god}" \
                                                    f"{right_curly_brace}"
        patron_god_name_valid = f"\n\npatron_god_{name_of_god}_valid = {left_curly_brace}" \
                                f"\n\tpatron_PATRON_valid = {left_curly_brace} PATRON = god_{name_of_god} " \
                                f"{right_curly_brace}" \
                                f"\n{right_curly_brace}"

        # Scripted Effects strings
        patron_trait_master_effect_string_write = f"patron_trait_master_effect = {left_curly_brace}" \
                                                  f"\n\tOR = {left_curly_brace}" \
                                                  f"\n\t\t#POINTER FOR GENERATOR" \
                                                  f"\n\t\t$EFFECT$ = {left_curly_brace} TRAIT = _god_{name_of_god}" \
                                                  f"{right_curly_brace}" \
                                                  f"\n\t{right_curly_brace}" \
                                                  f"\n{right_curly_brace}"
        patron_trait_master_effect_string_append = f"\t$EFFECT$ = {left_curly_brace} TRAIT = _god_{name_of_god}" \
                                                   f"{right_curly_brace}"

        if not os.path.exists(pathname + "/p_traits.txt"):
            with open('p_traits.txt', 'x', encoding="utf_8_sig") as output_file:
                output_file.writelines([output_line_1, output_line_2, output_line_3, output_line_4,
                                        output_line_5, output_line_6])
                print("written traits file")
                output_file.close()
            with open('p_cus_loc.txt', 'x', encoding="utf_8_sig") as cus_loc_file:
                cus_loc_file.writelines([output_custom_loc_get_god])
                print("written cus loc file")
                cus_loc_file.close()
            with open('p_traits_loc_l_english.yml', 'x', encoding="utf_8_sig") as loc_file:
                loc_file.writelines([output_localisation])
                print("written loc file")
                loc_file.close()
            with open('p_scripted_triggers.txt', 'x', encoding="utf_8_sig") as trigger_file:
                trigger_file.writelines([patron_trait_master_trigger_string_write, patron_god_name_valid])
                print("written trigger file")
                trigger_file.close()
            with open('p_scripted_effects.txt', 'x', encoding="utf_8_sig") as effect_file:
                effect_file.writelines([patron_trait_master_effect_string_write])
                print("written effect file")
                effect_file.close()
        elif os.path.exists(pathname + "/p_traits.txt"):
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
                        with open('p_traits.txt', 'w', encoding="utf_8_sig") as output_file:
                            output_file.writelines([output_line_1, output_line_2, output_line_3, output_line_4,
                                                    output_line_5, output_line_6])
                            print("written traits file")
                            output_file.close()
                        with open('p_cus_loc.txt', 'w', encoding="utf_8_sig") as cus_loc_file:
                            cus_loc_file.writelines([output_custom_loc_get_god])
                            print("written cus loc file")
                            cus_loc_file.close()
                        with open('p_traits_loc_l_english.yml', 'w', encoding="utf_8_sig") as loc_file:
                            loc_file.writelines([output_localisation, output_localisation_append])
                            print("written loc file")
                            loc_file.close()
                        with open('p_scripted_triggers.txt', 'w', encoding="utf_8_sig") as trigger_file:
                            trigger_file.writelines([patron_trait_master_trigger_string_write, patron_god_name_valid])
                            print("written trigger file")
                            trigger_file.close()
                        with open('p_scripted_effects.txt', 'w', encoding="utf_8_sig") as effect_file:
                            effect_file.writelines([patron_trait_master_effect_string_write])
                            print("written effect file")
                            effect_file.close()
                        break

                    elif bool_for_write == "n":
                        with open('p_traits.txt', 'a', encoding="utf_8_sig") as output_file:
                            output_file.writelines([output_line_1, output_line_2, output_line_3, output_line_4,
                                                    output_line_5, output_line_6])
                            print("written traits file")
                            output_file.close()
                        with open('p_cus_loc.txt', 'a', encoding="utf_8_sig") as cus_loc_file:
                            cus_loc_file.writelines([output_custom_loc_get_god])
                            print("written cus loc file")
                            cus_loc_file.close()
                        with open('p_traits_loc_l_english.yml', 'a', encoding="utf_8_sig") as loc_file:
                            loc_file.writelines([output_localisation_append])
                            print("written loc file")
                            loc_file.close()
                        with open('p_scripted_triggers.txt', 'r+', encoding="utf_8_sig") as trigger_file:
                            lines = trigger_file.readlines()
                            for i, line in enumerate(lines):
                                if line.startswith('\t\t#POINTER FOR GENERATOR'):
                                    print("Pointer found")
                                    lines[i] = lines[i] + f'\t{patron_trait_master_trigger_string_append}\n'
                            trigger_file.seek(0)
                            for line in lines:
                                trigger_file.write(line)
                            print("written trigger file")
                            trigger_file.close()
                        with open('p_scripted_triggers.txt', 'a', encoding="utf_8_sig") as trigger_file_2:
                            trigger_file_2.writelines([patron_god_name_valid])
                            trigger_file_2.close()
                        with open('p_scripted_effects.txt', 'r+', encoding="utf_8_sig") as effect_file:
                            lines = effect_file.readlines()
                            for i, line in enumerate(lines):
                                if line.startswith('\t\t#POINTER FOR GENERATOR'):
                                    print("Pointer found")
                                    lines[i] = lines[i] + f'\t{patron_trait_master_effect_string_append}\n'
                            effect_file.seek(0)
                            for line in lines:
                                effect_file.write(line)
                            print("written effect file")
                            effect_file.close()
                        break
                    else:
                        bool_for_write = "Answer is invalid"
            else:
                if bool_for_write == "y":
                    with open('p_traits.txt', 'w', encoding="utf_8_sig") as output_file:
                        output_file.writelines([output_line_1, output_line_2, output_line_3, output_line_4,
                                                output_line_5, output_line_6])
                        print("written traits file")
                        output_file.close()
                    with open('p_cus_loc.txt', 'w', encoding="utf_8_sig") as cus_loc_file:
                        cus_loc_file.writelines([output_custom_loc_get_god])
                        print("written cus loc file")
                        cus_loc_file.close()
                    with open('p_traits_loc_l_english.yml', 'w', encoding="utf_8_sig") as loc_file:
                        loc_file.writelines([output_localisation, output_localisation_append])
                        print("written loc file")
                        loc_file.close()
                    with open('p_scripted_triggers.txt', 'w', encoding="utf_8_sig") as trigger_file:
                        trigger_file.writelines([patron_trait_master_trigger_string_write, patron_god_name_valid])
                        print("written trigger file")
                        trigger_file.close()
                    with open('p_scripted_effects.txt', 'w', encoding="utf_8_sig") as effect_file:
                        effect_file.writelines([patron_trait_master_effect_string_write])
                        print("written effect file")
                        effect_file.close()

                elif bool_for_write == "n":
                    with open('p_traits.txt', 'a', encoding="utf_8_sig") as output_file:
                        output_file.writelines([output_line_1, output_line_2, output_line_3, output_line_4,
                                                output_line_5, output_line_6])
                        print("written traits file")
                        output_file.close()
                    with open('p_cus_loc.txt', 'a', encoding="utf_8_sig") as cus_loc_file:
                        cus_loc_file.writelines([output_custom_loc_get_god])
                        print("written cus loc file")
                        cus_loc_file.close()
                    with open('p_traits_loc_l_english.yml', 'a', encoding="utf_8_sig") as loc_file:
                        loc_file.writelines([output_localisation_append])
                        print("written loc file")
                        loc_file.close()
                    with open('p_scripted_triggers.txt', 'r+', encoding="utf_8_sig") as trigger_file:
                        lines = trigger_file.readlines()
                        for i, line in enumerate(lines):
                            if line.startswith('\t\t#POINTER FOR GENERATOR'):
                                print("Pointer found")
                                lines[i] = lines[i] + f'\t{patron_trait_master_trigger_string_append}\n'
                        trigger_file.seek(0)
                        for line in lines:
                            trigger_file.write(line)
                        print("written trigger file")
                        trigger_file.close()
                    with open('p_scripted_triggers.txt', 'a', encoding="utf_8_sig") as trigger_file_2:
                        trigger_file_2.writelines([patron_god_name_valid])
                        trigger_file_2.close()
                    with open('p_scripted_effects.txt', 'r+', encoding="utf_8_sig") as effect_file:
                        lines = effect_file.readlines()
                        for i, line in enumerate(lines):
                            if line.startswith('\t\t#POINTER FOR GENERATOR'):
                                print("Pointer found")
                                lines[i] = lines[i] + f'\t{patron_trait_master_effect_string_append}\n'
                        effect_file.seek(0)
                        for line in lines:
                            effect_file.write(line)
                        print("written effect file")
                        effect_file.close()


if __name__ == "__main__":
    main()