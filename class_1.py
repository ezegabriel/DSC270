a = open("candy_data_grabbed_from_html.txt", mode = 'r')
line = a.readlines()

del line[0]

i_count, l_temp, l_double_list = 0, [], []
for i in line:
    i = i.rstrip("\n")
    if "mg" in i:
        i = i.strip("mg")
    
    if "g" in i:
        i = i.strip("g")
   
    l_temp.append(i)
    i_count +=1
    if i_count == 9:
        l_double_list.append(l_temp)
        i_count, l_temp = 0, []
        
for index in range(len(l_double_list)):
    a = l_double_list[index][1][:-2] + ")"
    l_double_list[index][1] = a
    l_double_list[index].append("")
    l_double_list[index].append("")
    
print()
#print(l_double_list)



choco = open("chocolate.txt", mode = "r")
nut = open("nuts.txt", mode = "r")

l_choco = choco.readlines()
l_nut = nut.readlines()

for i in range(len(l_choco)):
    try:
        l_choco[i] = l_choco[i].strip("\n")
        l_nut[i] = l_nut[i].strip("\n")
    except IndexError:
        continue
print(l_choco)
print()
print(l_nut)

l_all_candy, l_no_chocolate = [], []

for i in range(len(l_double_list)):
    if l_double_list[i][0] in l_choco:
        l_double_list[i][-2] = "True"
    else:
        l_double_list[i][-2] = "False"
        
    if l_double_list[i][0] in l_nut:
        l_double_list[i][-1] = "True"
    else:
        l_double_list[i][-1] = "False"
    l_all_candy.append(l_double_list[i][0])
print(l_double_list)

for i in range(len(l_double_list)):
    if l_double_list[i][-2] == "False":
        l_no_chocolate.append(l_double_list[i][0])

    
f_all = open("all.csv", mode = "w")
f_no_chocolate = open("chocolate_free.csv", mode = "w")

for item in l_all_candy:
    f_all.write(item + "\n")
for item in l_no_chocolate:
    f_no_chocolate.write(item + "\n")
    
f_all.close()
f_no_chocolate.close()

for index in range(len(l_double_list)):
    l_double_list[index].append("")
    l_double_list[index].append("")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    