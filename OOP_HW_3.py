def write_file (list_for_sort,name_directory):
    my_dict = {}
    for i in list_for_sort:
        with open(i , 'r', encoding='utf-8') as file:
            my_dict[i] = len(file.readlines())
    sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1]))
    for d,v in sorted_dict.items():
        lol = open(d,'r',encoding='utf-8')
        with open(name_directory,'a',encoding='utf-8') as f:
            f.write(d+'\n')
            f.write(str(v)+'\n')
            for i in lol:
                f.write(i.rstrip()+'\n')
        



my_list = ['1.txt','2.txt','3.txt']
write_file(my_list,'result.txt')