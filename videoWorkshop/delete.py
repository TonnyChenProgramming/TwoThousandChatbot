def delete(file_path):
    #this function delet a file
    import os
    try:
        os.remove(file_path)
        print(f"File '{file_path}' deleted successfully.")
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except PermissionError:
        print(f"Permission error. You may not have the required permissions to delete the file.")
    except Exception as e:
        print(f"An error occurred: {e}")
