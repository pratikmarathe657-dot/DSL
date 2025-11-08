class TextEditor:
    def __init__(self):
        self.document = ""          
        self.undo_stack = []       
        self.redo_stack = []        

    def make_change(self, new_text):
        
        self.undo_stack.append(self.document)
        self.document = new_text
        
        self.redo_stack.clear()
        print("Change applied successfully!")

    def undo_action(self):
        if not self.undo_stack:
            print("No action to undo!")
            return
        
        self.redo_stack.append(self.document)
        
        self.document = self.undo_stack.pop()
        print("Undo successful!")

    def redo_action(self):
        if not self.redo_stack:
            print("No action to redo!")
            return
        
        self.undo_stack.append(self.document)
        
        self.document = self.redo_stack.pop()
        print("Redo successful!")

    def display(self):
        print("\nCurrent Document State:")
        print("-------------------------")
        print(self.document)
        print("-------------------------\n")



if __name__ == "__main__":
    editor = TextEditor()

    while True:
        print("Choose Operation:")
        print("1. Make a Change")
        print("2. Undo")
        print("3. Redo")
        print("4. Display Document")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            new_text = input("Enter new document text: ")
            editor.make_change(new_text)
        elif choice == '2':
            editor.undo_action()
        elif choice == '3':
            editor.redo_action()
        elif choice == '4':
            editor.display()
        elif choice == '5':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")