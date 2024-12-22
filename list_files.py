def list_files(parent_directory:dict, current_filepath=""):
    result = []
    if(current_filepath == None):
        return
    for path,file in parent_directory.items():
        
        if(file != None):
            result.extend(list_files(file,current_filepath+"/"+path))
        elif file == None:
            aa = current_filepath+"/"+path
            result.append(aa)

    return result




print(list_files({
            "Work": {
                "ProjectA": {
                    "Documentation": {"README.md": None, "GUIDE.md": None},
                    "Source": {"main.py": None, "util.py": None},
                },
                "ProjectB": {"Presentation.pptx": None},
            }
        }))