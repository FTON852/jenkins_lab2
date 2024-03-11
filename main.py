some_string = "This massage from jenkins artifact"
with open ("artifact.txt", "w") as file:
    file.writelines(some_string)
