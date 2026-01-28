records = {}
id_set = set()
FILENAME = "records.txt"

def load_records():
    try:
        file = open(FILENAME, "r")
        for line in file:
            data = line.strip().split("|")
            sid = int(data[0])
            name = data[1]
            marks = list(map(int, data[2].split(",")))
            
            records[sid] = {
                "info": (sid, name),
                "marks": marks
            }
            id_set.add(sid)
        file.close()
    except:
        pass

def save_records():
    file = open(FILENAME, "w")
    for sid, data in records.items():
        marks_str = ",".join(map(str, data["marks"]))
        file.write(f"{sid}|{data['info'][1]}|{marks_str}\n")
    file.close()
    
def add_records():
    sid = int(input("Enter Student Id: "))
    if sid in id_set:
        print("Id already exists!")
        return
    
    name = input("Enter Student Name: ")
    
    marks = []
    for i in range(3):
        marks.append(int(input(f"Enter Marks {i+1}: ")))
        
    records[sid] = {
        "info": (sid, name),
        "marks": marks
    }
    id_set.add(sid)
    save_records()
    print("Record Added Successfully!")
    
def view_records():
    if not records:
        print("No Records Found!")
        return
    
    for sid, data in records.items():
        total = sum(data["marks"])
        percentage = total / len(data["marks"])
        
        print("\nID:", sid)
        print("Name:", data["info"][1])
        print("Marks:", data["marks"])
        print("Total:", total)
        print("Percentage:", int(percentage))
        
def update_records():
    sid = int(input("Enter Student Id to Update: "))
    if sid not in records:
        print("Record Not Found!")
        return

    marks = []
    for i in range(3):
        marks.append(int(input(f"Enter new marks {i+1}: ")))
        
    records[sid]["marks"] = marks
    save_records()
    print("Record Updated Successfully!")
    
def delete_records():
    sid = int(input("Enter Student Id to Delete: "))
    if sid in records:
        del records[sid]
        id_set.remove(sid)
        save_records()
        print("Record Deleted!")
    else:
        print("Record Not Found!")
        
load_records()

while True:
    print("\n--- Student Record Management ---")
    print("1. Add Record")
    print("2. View Records")
    print("3. Update Record")
    print("4. Delete Record")
    print("5. Exit")
    
    choice = input("Enter choice: ")
    
    if choice == "1":
        add_records()
    elif choice == "2":
        view_records()
    elif choice == "3":
        update_records()
    elif choice == "4":
        delete_records()
    elif choice == "5":
        print("Exiting Program....")
        break
    else:
        print("Invalid Choice!")