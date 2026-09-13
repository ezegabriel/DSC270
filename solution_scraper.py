
def get_list_of_files():
    l_files = []
    input_file = open("pages.txt", "r")
    file_names = input_file.readlines()
    input_file.close()
    for item in file_names:
        new_name = item.strip()
        l_files.append(new_name)
    return l_files


def main():
    print("starting")
    l_file_names = get_list_of_files()
    l_keep_these_lines = []
    d_image_links = {}

    for item in l_file_names:
        input_file = open(item, "r")
        line = input_file.readline()
        while line != "":
            # if line not empty

            # see if I want to keep it
            line = line.strip()
            if line.find("<img src") >= 0:
                l_keep_these_lines.append(line) 

            # get next line
            line = input_file.readline()
        
        input_file.close()

        #print("=====\n\n")

        for line in l_keep_these_lines:
            #print(line)
            l_pieces = line.split('"')
            #print(l_pieces[1])
            if l_pieces[1] not in d_image_links:
                d_image_links[l_pieces[1]] = 1
            else:
                d_image_links[l_pieces[1]] = d_image_links[l_pieces[1]] + 1


    for key in d_image_links.keys():
        print(key, d_image_links[key])
        
    print("done")

main()

