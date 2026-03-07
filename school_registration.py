import json
from datetime import datetime

class SchoolRegistration:
    # every new school is designed to start with a different set of students
    def __init__(self, school_name): # __init__ confused me at first but it means "this is what you do when you are created." to the code class
        self.school_name = school_name # store the school name
        self.students = [] # we have initialised an empty student list

    def add_student(self):
        # while True loops keep asking until the correct input is added, hence preventing bad data
        # age is not stored here as it will be calculated later
        print("\nAdding a new student...")
        name = input("Full Name: ").strip().title() # Get name, removes extra spaces, capitalises first letters of each name if not done already

        # using validation on date of birth
        while True:
            dob_str = input("Date Of Birth (dd/mm/yyyy): ").strip() # imput string data as 12/05/2005
            try:
                dob = datetime.strptime(dob_str, "%d/%m/%Y") # changes our string into a date time object
                break
            except ValueError:
                print("✗ Invalid date format! Use dd/mm/yyyy.")

        # using validation on gender
        while True:
            gender = input("Gender (Male/Female): ").strip().capitalize()
            if gender in ["Male", "Female"]:
                break
            print("✗ Invalid gender! Enter Male or Female.")

        # school level first
        while True:
            level = input("Primary or Secondary? (P/S): ").strip().upper()
            if level in ["P", "S"]:
                break
            print("✗ Invalid! Enter P or S.")

        # class based on level
        if level == "P":
            classes = ["P1","P2","P3","P4","P5","P6","P7"]
        else:
            classes = ["S1","S2","S3","S4","S5","S6"]

        while True:
            # the code below will look something like Class(P1,P2,P3...)
            class_level = input(f"Class({','.join(classes)}):").strip().upper()
            if class_level in classes:
                break
            print(f"✗ Invalid class! Choose from {','.join(classes)}.")

        # parent's number (simple string, no deep validation)
        parent_number = input("Parent's Phone Number: ").strip()

        # Accommodation
        while True:
            Accommodation = input("Accommodation (Boarding/Day): ").strip().capitalize()
            if Accommodation in ["Boarding", "Day"]:
                break
            print("✗ Invalid! Enter Boarding or Day.")

        # create student dictionary
        student = {
            'name': name,
            'dob': dob, 
            'gender': gender,
            'class_level': class_level,
            'parent_number': parent_number,
            'Accommodation': Accommodation
        }
        self.students.append(student) # adds to list
        print(f"✓ Student '{name}' added successfully!")
        
    # we're gonna use a private method (_calculate_age) to well, calculate the age
    def _calculate_age(self, dob):
        if not isinstance(dob, datetime):
            return "Invalid"
        today = datetime.now()
        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
        return age
        
    def list_students(self):
        print(f"\n{self.school_name} Registration System")
        print("-"*50)
        print("ID | Name | DoB | Gender | Class | Parent's Number | Accommodation | Age")

        if not self.students:
            print("No students registered yet.")
        else:
            for i, student in enumerate(self.students, 1):
                age = self._calculate_age(student['dob'])
                print(f"{i:03d} - {student['name']}, {student['dob'].strftime('%d/%m/%Y')}, {student['gender']}, "
                      f"{student['class_level']}, {student['parent_number']}, "
                      f"{student['Accommodation']}, {age}")
                
        print("-"*50)

        total = len(self.students)
        if total > 0:
            # gender split
            males = sum(1 for s in self.students if s['gender'] == "Male")
            females = total - males
            print(f"Total Number of Students - {total}")
            print(f"Male Students - {males}, Female Students - {females}")

            # Accommodation split
            boarding = sum(1 for s in self.students if s['Accommodation'] == "Boarding")
            day = total - boarding
            print(f"Boarding Students - {boarding}, Day Students - {day}")
        else:
            print("No data available!")

    def delete_student(self):
        self.list_students() # show list first
        if not self.students: # if the list is empty, "not self.students" becomes true 
            return
        while True:
            try:
                num = int(input("Enter Student ID to delete (0 to cancel): "))
                if num == 0:
                    break
                if 1 <= num <= len(self.students):
                    deleted = self.students.pop(num - 1) # List is 0 indexed
                    print(f"✓ Deleted '{deleted['name']}' from {self.school_name} Registry")
                    break
                else:
                    print("✗ Invalid Student ID")
            except ValueError:
                print("✗ Enter a number!")

    def update_student(self):
        self.list_students()
        if not self.students:
            return
        while True:
            try:
                num = int(input("\nEnter Student ID to update (0 to cancel): "))
                if num == 0:
                    break
                if 1 <= num <= len(self.students):
                    student = self.students[num - 1]
                    print(f"Updating '{student['name']}'")
                    print("Fields: 1-Name, 2-DOB, 3-Gender, 4-Class, 5-Parent Number, 6-Accommodation")
                    field = input("Choose field (1-6): ").strip()

                    if field == "1":
                        student['name'] = input("New Name:").strip().title()
                    elif field == "2":
                        while True:
                            dob_str = input("New DOB (dd/mm/yyyy): ").strip()
                            try:
                                student['dob'] = datetime.strptime(dob_str, "%d/%m/%Y")
                                break
                            except ValueError:
                                print("✗ Invalid date!")
                    elif field == "3":
                        while True:
                            gender = input("New Gender (Male/Female): ").strip().capitalize()
                            if gender in ["Male", "Female"]:
                                student['gender'] = gender
                                break
                            print("✗ Invalid!")
                    elif field == "4":
                        while True:
                            level = input("Primary or Secondary? (P/S): ").strip().upper()
                            if level in ["P", "S"]:
                                break
                            print("✗ Invalid! Enter P or S.")

                        if level == "P":
                            classes = ["P1","P2","P3","P4","P5","P6","P7"]
                        else:
                            classes = ["S1","S2","S3","S4","S5","S6"]

                        while True:
                            student['class_level'] = class_level
                            class_level = input(f"Class({','.join(classes)}):").strip().upper()
                            if class_level in classes:
                                student['class_level'] = class_level
                                break
                            print(f"✗ Invalid class! Choose from {','.join(classes)}.")
                    elif field == "5":
                        student['parent_number'] = input("New Parent Number: ").strip()
                    elif field == "6":
                        while True:
                            acc = input("New Accommodation (Boarding/Day)").strip().capitalize()
                            if acc in ["Boarding", "Day"]:
                                student['Accommodation'] = acc
                                break
                            print("✗ Invalid!")
                    else:
                        print("✗ Invalid field!")
                    print("✓ Updated Successfully!")
                    break
                else:
                    print("✗ Invalid number!")
            except ValueError:
                print("✗ Enter a number!")

    def save_to_json(self, filename="school_data.json"):
        data = {
            "school_name": self.school_name,
            "students": [
                {**student, 'dob':student['dob'].strftime("%d/%m/%Y")} for student in self.students
            ]
        }
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4) # indent=4 for a readable JSON
        print(f"✓ Saved to {filename}")

    def load_from_json(self, filename="school_data.json"):
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                self.school_name = data.get("school_name", self.school_name) # sets to default value
                self.students = []
                for student in data.get("students", []):
                    try:
                        parsed_dob = datetime.strptime(student['dob'], "%d/%m/%Y")
                        self.students.append({**student, 'dob': parsed_dob})
                    except ValueError:
                        print(f"✗ Invalid DOB format in JSON for student '{student.get('name', 'Unknown')}'—skipping.")
            print(f"✓ Loaded from {filename}")
        except FileNotFoundError:
            print(f"✗ File not found!")
        except json.JSONDecodeError:
            print("✗ Invalid JSON!")

    def save_to_txt(self):
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"school_report_{timestamp}.txt"
        with open(filename, 'w') as f:
            f.write(f"{self.school_name} Registration System\n")
            f.write("-"*50 +"\n")
            f.write("No, Name, Date, Gender, Class, Parent’s Number, Accommodation, Age\n")
            if not self.students:
                f.write("No students registered yet.\n")
            else:
                for i, student in enumerate(self.students, 1):
                    age = self._calculate_age(self.students['dob'])
                    f.write(f"{i:03d} - {student['name']}, {student['dob'].strftime('%d/%m/%Y')}, {student['gender']}, "
                      f"{student['class_level']}, {student['parent_number']}, "
                      f"{student['Accommodation']}, {age}\n")
            f.write("-"*50 +"\n")
            total = len(self.students)
            if total > 0:
                males = sum(1 for s in self.students if s['gender'] == "Male")
                females = total - males
                f.write(f"Total Number of Students - {total}")
                f.write(f"Male Students - {males}, Female Students - {females}")
                boarding = sum(1 for s in self.students if s['Accommodation'] == "Boarding")
                day = total - boarding
                f.write(f"Boarding Students - {boarding}, Day Students - {day}")
        print(f"✓ Report saved to {filename}")      

def main():
    school_name = "Kampala International School" # You can change this
    system = SchoolRegistration(school_name)
    print("\n")
    print(f"\n{school_name} Registration System")

    while True:
        print("-"*50)
        print("MENU")
        print(f"Current Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("="*50)
        print("1. Add Student")
        print("2. Delete Student")
        print("3. Update Student")
        print("4. List Students")
        print("5. Save to JSON")
        print("6. Load from JSON")
        print("7. Save to TXT")
        print("8. Exit")
        print("="*50)
        
        try:
            choice = input("Choose (1-8): ").strip()
        except KeyboardInterrupt:
            print("\nProgram interrupted. Goodbye!")
            break

        if choice == "1":
            system.add_student()
        elif choice == "2":
            system.delete_student()
        elif choice == "3":
            system.update_student()
        elif choice == "4":
            system.list_students()
        elif choice == "5":
            filename = input("Filename (default: school_data.json): ").strip() or "school_data.json"
            system.save_to_json(filename)
        elif choice == "6":
            filename = input("Filename (default: school_data.json): ").strip() or "school_data.json"
            system.load_from_json(filename)
        elif choice == "7":
            system.save_to_txt()
        elif choice == "8":
            print("\nGoodbye!")
            break
        else:
            print("✗ Invalid choice!")

if __name__ == "__main__":
    main()