def read_from_text_file(path):
    file1 = open(path,"r") 
    print(file1.readlines())
    file1.close()

read_from_text_file("plain.txt")