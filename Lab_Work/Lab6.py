def main():
    file_name = input("Enter the file name: ")
    my_dictionary = {}
    age_dict = {}

    with open(file_name) as my_file:
        content = my_file.readlines()
        name_list = [x.strip() for x in content]

        i = 0
        while i < len(name_list):
            if name_list[i].isdigit():
                age = name_list[i]
                i += 1
                names = [name_list[i]]
                i += 1
                while i < len(name_list) and not name_list[i].isdigit():
                    names.append(name_list[i])
                    i += 1

                if age in age_dict:
                    age_dict[age].extend(names)
                else:
                    age_dict[age] = names

        for age, names in age_dict.items():
            if len(names) > 1:
                combined_names = " and ".join(names)
                my_dictionary[age] = combined_names
            else:
                my_dictionary[age] = names[0]

    # Sorting dictionary by age in descending order
    sorted_dict = dict(sorted(my_dictionary.items(), key=lambda x: int(x[0]), reverse=True))

    # Writing sorted dictionary to output_age_group.txt
    with open("output_age_group.txt", "w") as age_group_file:
        for age, names in sorted_dict.items():
            age_group_file.write(f"{age}: {names}\n")

    # Extracting names from dictionary
    all_names = [names.split(" and ") if " and " in names else [names] for names in sorted_dict.values()]
    all_names = [name for sublist in all_names for name in sublist]

    # Sorting names in reverse alphabetical order
    all_names.sort(reverse=True)

    # Writing sorted names to output_names.txt
    with open("output_names.txt", "w") as names_file:
        for name in all_names:
            names_file.write(f"{name}\n")

    print("Output files generated successfully...")


if __name__ == "__main__":
    main()
