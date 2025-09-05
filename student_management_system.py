import sqlite3

# Connect to database (or create if it doesn't exist)
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

# Create table if not exists
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    grade TEXT NOT NULL
)
""")

# Function to add a new student
def add_student(name, age, grade):
    cursor.execute("INSERT INTO students (name, age, grade) VALUES (?, ?, ?)", (name, age, grade))
    conn.commit()
    print(f"Student {name} added successfully.")

# Function to view all students
def view_students():
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    if students:
        print("\n--- Student Records ---")
        for student in students:
            print(student)
    else:
        print("No student records found.")

# Function to update a student's grade
def update_student(student_id, new_grade):
    cursor.execute("UPDATE students SET grade = ? WHERE id = ?", (new_grade, student_id))
    conn.commit()
    print(f"Student with ID {student_id} updated successfully.")

# Function to delete a student
def delete_student(student_id):
    cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
    conn.commit()
    print(f"Student with ID {student_id} deleted successfully.")

# Example usage
if __name__ == "__main__":
    add_student("Chethana", 19, "A")
    add_student("Heshani", 18, "B")
    view_students()
    update_student(1, "A+")
    view_students()
    delete_student(2)
    view_students()

    # Close connection
    conn.close()
