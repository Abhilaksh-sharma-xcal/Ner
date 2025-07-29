import os
total_files = []
def list_files_in_directory(directory_path): 
    try:
        entries = os.listdir(directory_path) 
        found_files = False
        for entry in entries:
            full_path = os.path.join(directory_path, entry)

            if os.path.isfile(full_path):
                total_files.append(entry)
                print(entry)
                found_files = True
        
        if not found_files:
            print("No files found in this directory.")

    except FileNotFoundError:
        print(f"Error: The directory '{directory_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":

    
    folder_to_scan = r"D:\xcaliber\study\database\synt_database"
    
    list_files_in_directory(folder_to_scan)
    
    print(total_files)