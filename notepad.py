import mysql.connector
conn = mysql.connector.connect(
    host="localhost", user="root", password="garg0709@ankur", database="notepad")
# if(conn.is_connected()):
#     print("Connection established")
# else:
#     print("Error")
ptr = conn.cursor()


def create_note():
    noteId = int(input("Enter a unique id for your note:\n"))
    ptr.execute("SELECT noteId from notes where noteID=%s", (noteId,))
    id = ptr.fetchone()
    if (id is None):
        noteTitle = input("Enter the title of your note:\n")
        noteContent = input("Enter the content of your note:\n")
        ptr.execute("INSERT INTO notes (noteID,title, content) VALUES (%s, %s,%s)",
                    (noteId, noteTitle, noteContent))
        conn.commit()
        print("Data inserted successfully.")
    else:
        print("noteId already exists.Choose any other")


def view_note():
    noteId = int(input("Enter the id of note you want to see: "))
    ptr.execute("SELECT * from notes where noteID=%s", (noteId,))
    note = ptr.fetchone()
    if (note is not None):
        print(f" Note ID: {note[0]} \n Title: {note[1]} \n content: {note[2]}")
    else:
        print("Note does not exists")

def edit_note():
    noteId = int(input("Enter the id of note you want to edit: "))
    ptr.execute("SELECT noteId from notes where noteID=%s", (noteId,))
    id = ptr.fetchone()
    if(id is not None):
      ptr.execute("SELECT * from notes where noteID=%s", (noteId,))
      note = ptr.fetchone()
      print("Existing note: \n")
      print(f" Note ID: {note[0]} \n Title: {note[1]} \n content: {note[2]}")
      newId=input("Enter the new id: ")
      ptr.execute("SELECT noteId from notes where noteID=%s", (newId,))
      id = ptr.fetchone()
      if(id is None):
        newTitle=input("Enter the new title: ")
        newContent=input("Enter the new content: ")
        ptr.execute("UPDATE notes set noteID=%s,title=%s,content=%s where noteID=%s", (newId, newTitle, newContent,noteId))
        conn.commit()
        print("Data updated successfully.")
      else:
        print("note id already exist.Try again ")
    else:
       print("Note id does not exist.try another one")

def delete_note():
    noteId = int(input("Enter the id of note you want to delete: "))
    ptr.execute("SELECT noteId from notes where noteID=%s", (noteId,))
    id = ptr.fetchone()
    if(id is not None):
      ptr.execute("SELECT * from notes where noteID=%s", (noteId,))
      note = ptr.fetchone()
      print(" note to delete: \n")
      print(f" Note ID: {note[0]} \n Title: {note[1]} \n content: {note[2]}")
      confirm=input("Are you sure you want to delete the note?(y/n):")
      if(confirm=="y" or confirm=="Y"):
         ptr.execute("DELETE FROM notes WHERE noteID = %s", (noteId,))
         conn.commit()
         print("Note deleted successfully.")
      else:
         print("Deletion abort..")
    else:
       print("Note does not exists.Try again")

   
while True:
    print("\nOptions:")
    print("1. Create Note")
    print("2. View Notes")
    print("3. Edit Note")
    print("4. Delete Note")
    print("5. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        create_note()
    elif choice == "2":
        view_note()
    elif choice == "3":
        edit_note()
    elif choice == "4":
        delete_note()
    elif choice == "5":
        break
    else:
        print("Invalid choice. Please try again.")

conn.close()


