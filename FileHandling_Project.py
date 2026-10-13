from pathlib import Path
import os


def readfileandfolder():
    path = Path("")

    items = list(path.rglob("*"))

    for i, item in enumerate(items):
        print(f"{i + 1}: {item}")


def createfile():
    try:
        readfileandfolder()

        name = input("Please tell your file name: ").strip()

        if not name:
            print("File name cannot be empty.")
            return

        p = Path(name)

        if p.exists():
            print("File or folder already exists.")
            return

        # Parent folder must already exist
        if not p.parent.exists():
            print("The specified folder does not exist.")
            return

        if not p.parent.is_dir():
            print("The specified parent path is not a folder.")
            return

        with open(p, "w", encoding="utf-8") as fs:
            data = input("What do you want to write in this file? ")
            fs.write(data)

        print("File created successfully!")

    except (OSError, ValueError) as err:
        print(f"An error occurred: {err}")


def readfile():
    try:
        readfileandfolder()

        name = input("Which file do you want to read? ").strip()

        if not name:
            print("File name cannot be empty.")
            return

        p = Path(name)

        if p.exists() and p.is_file():
            with open(p, "r", encoding="utf-8") as fs:
                data = fs.read()
                print("\nFile content:")
                print(data)

            print("File read successfully!")

        else:
            print("File does not exist or the path is not a file.")

    except (OSError, ValueError) as err:
        print(f"An error occurred: {err}")


def updatefile():
    try:
        readfileandfolder()

        name = input("Which file do you want to update? ").strip()

        if not name:
            print("File name cannot be empty.")
            return

        p = Path(name)

        if not p.exists() or not p.is_file():
            print("File does not exist or the path is not a file.")
            return

        print("\nPress 1 to rename the file")
        print("Press 2 to overwrite the file content")
        print("Press 3 to append content to the file")

        try:
            res = int(input("Tell your response: "))
        except ValueError:
            print("Invalid input! Please enter a number.")
            return

        if res == 1:
            name2 = input("Tell your new file name: ").strip()

            if not name2:
                print("New file name cannot be empty.")
                return

            p2 = Path(name2)

            if p2.exists():
                print("A file or folder with this name already exists.")
                return

            if not p2.parent.exists() or not p2.parent.is_dir():
                print("The destination folder does not exist.")
                return

            p.rename(p2)
            print("File renamed successfully!")

        elif res == 2:
            data = input("Tell your new content: ")

            with open(p, "w", encoding="utf-8") as fs:
                fs.write(data)

            print("File content overwritten successfully!")

        elif res == 3:
            data = input("Tell the content you want to append: ")

            with open(p, "a", encoding="utf-8") as fs:
                fs.write(" " + data)

            print("Content appended successfully!")

        else:
            print("Invalid choice! Please select 1, 2, or 3.")

    except (OSError, ValueError) as err:
        print(f"An error occurred: {err}")


def deletefile():
    try:
        readfileandfolder()

        name = input("Which file do you want to delete? ").strip()

        if not name:
            print("File name cannot be empty.")
            return

        p = Path(name)

        if p.exists() and p.is_file():
            confirm = input(
                f"Are you sure you want to delete '{p}'? (yes/no): "
            ).strip().lower()

            if confirm == "yes":
                os.remove(p)
                print("File deleted successfully!")

            else:
                print("File deletion cancelled.")

        else:
            print("File does not exist or the path is not a file.")

    except (OSError, ValueError) as err:
        print(f"An error occurred: {err}")


def main():
    while True:
        print("\n===== FILE MANAGEMENT SYSTEM =====")
        print("1. Create a file")
        print("2. Read a file")
        print("3. Update a file")
        print("4. Delete a file")
        print("5. Exit")

        try:
            check = int(input("Please select an option: "))
        except ValueError:
            print("Invalid input! Please enter a number from 1 to 5.")
            continue

        if check == 1:
            createfile()

        elif check == 2:
            readfile()

        elif check == 3:
            updatefile()

        elif check == 4:
            deletefile()

        elif check == 5:
            print("Thank you for using File Management System!")
            break

        else:
            print("Invalid choice! Please select a number from 1 to 5.")


if __name__ == "__main__":
    main()

