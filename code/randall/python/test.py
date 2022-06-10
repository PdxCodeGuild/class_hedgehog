
# declaring string variables
str1 = 'Understanding'
str2 = '%s'
str3 = 'at'
str4 = 'GeeksforGeeks'
  
# concatenating strings but %s not equal to string variables
final_str = "%s %s %s %s" % (str1, str3, str4)
  
# printing the final string
print("Concatenating multiple strings using Python '%s' operator:\n")
print(final_str)