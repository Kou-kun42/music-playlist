from LinkedList import LinkedList


# Make new list
new_list = LinkedList()

# Append stuff to it
new_list.append("song1")
new_list.append("song2")
new_list.append("song3")

# Print out list
new_list.print_songs()
# Print a line break
print("--------------")

# Prepend stuff to it
new_list.prepend("song4")
new_list.prepend("song5")
new_list.prepend("song6")

# Print out list
new_list.print_songs()
# Print a line break
print("--------------")

# Delete from head
new_list.delete_from_head()

# Print out list
new_list.print_songs()
# Print a line break
print("--------------")

# Delete from tail
new_list.delete_from_tail()

# Print out list
new_list.print_songs()
# Print a line break
print("--------------")

# Test find()
print(new_list.find("song1"))
print(new_list.find("song2"))
print(new_list.find("song3"))
print(new_list.find("song4"))
print(new_list.find("song5"))
print(new_list.find("song6"))
# Print a line break
print("--------------")

# General Delete
new_list.delete("song5")
new_list.delete("song1")

# Print out list
new_list.print_songs()
# Print a line break
print("--------------")

# Delete the rest, and also try to delete something that's not there
new_list.delete("song2")
new_list.delete("song4")
new_list.delete("song3")
new_list.delete_from_head()
new_list.delete_from_tail()
print(new_list.find("song4"))

# Print out list
new_list.print_songs()
# Print a line break
print("--------------")

# Try adding stuff to the empty list
new_list.append("song7")

# Print out list
new_list.print_songs()
# Print a line break
print("--------------")

# Delete it and try prepending the empty list
new_list.delete_from_tail()
new_list.prepend("song8")

# Print out list
new_list.print_songs()
# Print a line break
print("--------------")

# Delete it from head and check if there's anything left
new_list.delete_from_head()
print(new_list.find("song8"))

# Print out list
new_list.print_songs()
