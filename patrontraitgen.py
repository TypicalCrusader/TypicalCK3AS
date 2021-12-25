#/usr/bin/python3
# Made by TypicalCrusader
# Updated for Publishing by RadSquirrel

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
    index_of_trait = int(input("Write an trait index\nNote:must be an intiger"))
    if index_of_trait >= 1:
        name_of_god = input("Write a name of the god in lowercase if the god name has space then repalce space with _\nie:"
                            "Father of Threads will become father_of_threads")
        #fuck python for not appending this shit
        output_line_1 = f"p_god_{name_of_god} = {left_curly_brace}\n\tindex = {index_of_trait}"
        output_line_2 = f"\n\tshown_in_ruler_designer = no\n\n"
        output_line_3 = f"\n\tname = {left_curly_brace}\n\t\tfirst_valid = {left_curly_brace}\n\t\t\ttriggered_desc = " \
                        f"{left_curly_brace}\n\t\t\t\ttrigger = {left_curly_brace} NOT = {left_curly_brace} exists = this" \
                        f"{right_curly_brace} {right_curly_brace}\n\t\t\t\tdesc = trait_p_god_{name_of_god}_base\n" \
                        f"\n\t\t\tright_curly_brace\n\t\tdesc = trait_p_{name_of_god}\n\t\t{right_curly_brace}" \
                        f"\n\t{right_curly_brace}"
        output_line_4 = f"\n\tdesc = {left_curly_brace}" \
                        f"\n\t\tfirst_valid = {left_curly_brace}" \
                        f"\n\t\t\ttriggered_desc = {left_curly_brace}" \
                        f"\n\t\t\t\ttrigger = {left_curly_brace} NOT = {left_curly_brace} exists = this {right_curly_brace}" \
                        f"{right_curly_brace}" \
                        f"\n\t\t\t\tdesc = trait_p_god_{name_of_god}_null" \
                        f"\n\t\t\t{right_curly_brace}" \
                        f"\n\t\t\tdesc = trait_p_god_{name_of_god}_character_desc" \
                        f"\n\t\t{right_curly_brace}" \
                        f"\n\t{right_curly_brace}"
        output_line_5 = f"\n\ticon = {left_curly_brace}" \
                        f"\n\t\tfirst_valid = {left_curly_brace}" \
                        f"\n\t\t\ttriggered_desc = {left_curly_brace}" \
                        f"\n\t\t\t\ttrigger = {left_curly_brace} NOT = {left_curly_brace} exists = this {right_curly_brace} " \
                        f"{right_curly_brace}" \
                        f"\n\t\t\t\tdesc = {quotation}{left_square_brace}Select_CString{left_circle_brace} GetPlayer.MakeScope.Var{left_circle_brace}"\
                        f"{apostrophe}faith_window{apostrophe}).IsSet{comma} " \
                        f"GetPlayer.Custom{left_circle_brace}{apostrophe}get_god_{name_of_god}_icon{apostrophe}{right_circle_brace}{comma}" \
                        f"{apostrophe}p_god_{name_of_god}.dds{apostrophe} {right_circle_brace}{right_square_brace}{quotation}" \
                        f"\n\t\t\t{right_curly_brace}" \
                        f"\n\t\t\tdesc = p_god_{name_of_god}.dds" \
                        f"\n\t\t{right_curly_brace}" \
                        f"\n\t{right_curly_brace}"
        output_line_6 = f"\n{right_curly_brace}"

        if not os.path.exists(pathname + "/p_traits.txt"):
            with open('p_traits.txt', 'x') as output_file:
                output_file.writelines([output_line_1, output_line_2, output_line_3, output_line_4,
                                        output_line_5, output_line_6])
                output_file.close()
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
                        with open('p_traits.txt', 'w') as output_file:
                            output_file.writelines([output_line_1, output_line_2, output_line_3, output_line_4,
                                                    output_line_5, output_line_6 ])
                        break

                    elif bool_for_write == "n":
                        with open('p_traits.txt', 'a') as output_file:
                            output_file.writelines([output_line_1, output_line_2, output_line_3, output_line_4,
                                                    output_line_5, output_line_6 ])
                        break
                    else:
                        bool_for_write = "Answer is invalid"
            else:
                if bool_for_write == "y":
                    with open('p_traits.txt', 'w') as output_file:
                        output_file.writelines([output_line_1, output_line_2, output_line_3, output_line_4,
                                                output_line_5, output_line_6 ])
                        output_file.close()
                elif bool_for_write == "n":
                    with open('p_traits.txt', 'a') as output_file:
                        output_file.writelines([output_line_1, output_line_2, output_line_3, output_line_4,
                                                output_line_5, output_line_6 ])
                        output_file.close()
if __name__ == "__main__":
    main()