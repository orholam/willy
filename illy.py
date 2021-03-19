print("Hello World!")

with open('posts.txt') as posts:
    lines = posts.readlines()
print(lines)

something = raw_input("would you like to add a line?")
print("you said "+something)
my_file = open('posts.txt',"a")
my_file.write("\n"+something)
print("great!")
