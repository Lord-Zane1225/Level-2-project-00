
# create file to hold data (add txt extension)

file_name = "write experiment"
write_to = "{}.txt".format(file_name)

text_file = open(write_to, "w+")

# strings to write to file
heading = "=== MFF Test ===\n"
content = "Random content"
more = "A bit more content"


# list of strings...
to_write = [heading, content, more]

# print output
for item in to_write:
    print(item)


# write the item to the file
for item in to_write:
    text_file.write(item)
    text_file.write("\n")
