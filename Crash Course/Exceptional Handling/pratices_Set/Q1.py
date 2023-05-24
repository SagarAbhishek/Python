def readfile(filename):
    try:
        with open(filename,'r')as f:
            print(f.read())
    except FileNotFoundError as e:
        print(f"file {filename} is not found.")
    else:
        print(f"File read successfully.")



readfile("Crash Course\\Exceptional Handling\\pratices_Set\\1.txt")
readfile('Crash Course\\Exceptional Handling\\pratices_Set\\2.txt')
readfile('Crash Course\\Exceptional Handling\\pratices_Set\\3.txt')