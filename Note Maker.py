## Tasks to Notepad Program

print("Welcome to Ethan's personal notepad converter. In this program, you will be able to write down quick notes which will be automatically converted into a text file and saved to reduce the hassle for you.") # intro
    
def notes():
    while True:
        userNotes = str(input("\nWhat would you like to write in the text file? (type done if finished): "))
        userNotes = userNotes.lower()
        if userNotes == "done":
            print("\nCheck the file for the notes you have just written...")
            break
        else:
            notes_to_text_file(userNotes)
    return True

def notes_to_text_file(userNotes):
    with open('Notes.txt','a') as textFile:
        textFile.write(userNotes)
        textFile.write("\n")
    return True

def main():
    notes()

main()
    



