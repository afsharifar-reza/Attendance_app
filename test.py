from back_end.database import get_connection
from back_end.models.class_model import ClassModel

def main():
    conn = get_connection()
    if not conn:
        print("Failed to connect to the database.")
        return

    # Create table (only needs to run once)
    class_model = ClassModel(conn)
    class_model.create_table()

    # Add a new class
    grade = "10th"
    field = "Mechanics"
    new_class_id = class_model.add_class(grade, field)

    if new_class_id:
        print(f"New class added with ID: {new_class_id} -> {grade} {field}")
    else:
        print("Error adding new class.")

    # Show all classes
    all_classes = class_model.get_all_classes()
    for c in all_classes:
        print(f"ID: {c[0]}, Grade: {c[1]}, Field: {c[2]}, Name: {c[3]}")

    conn.close()

if __name__ == "__main__":
    main()
