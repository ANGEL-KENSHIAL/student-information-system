"""
STUDENT INFORMATION SYSTEM
--------------------------
Demonstrates input collection, string manipulation, explicit string concatenation,
and dynamic border generation.
"""

from datetime import datetime
from textwrap import wrap

def generate_border(char, length):
    """Generates a dynamic border string using pure string concatenation."""
    border = ""
    for _ in range(length):
        border = border + char
    return border

def format_row(label, value, width=78):
    """Formats one profile field into fixed-width table rows."""
    value_width = width - 28
    padded_label = label
    while len(padded_label) < 22:
        padded_label = padded_label + " "
    value_lines = wrap(str(value), width=value_width) or [""]
    rows = []
    for line_number, value_line in enumerate(value_lines):
        row_label = padded_label if line_number == 0 else " " * 22
        row = "| " + row_label + " | " + value_line.ljust(value_width) + "|"
        rows.append(row)
    return rows

def get_non_empty_input(prompt_text):
    """Validates that user input is not empty or just whitespace."""
    user_input = input(prompt_text).strip()
    while len(user_input) == 0:
        print("  [!] Input cannot be empty. Please try again.")
        user_input = input(prompt_text).strip()
    return user_input

def generate_username(full_name, student_id):
    """Build a username from the first three letters of a student's name and ID."""
    clean_name = full_name.replace(" ", "").lower()
    name_prefix = clean_name[0:3] if len(clean_name) >= 3 else clean_name
    return name_prefix + str(student_id)

def save_profile(username, profile_text):
    """Save a copy of the displayed profile using the generated username."""
    file_name = username + "_profile.txt"
    with open(file_name, "w", encoding="utf-8") as profile_file:
        profile_file.write(profile_text)
    return file_name

def main():
    width = 78
    border_double = generate_border("=", width)
    border_single = generate_border("-", width)

    print("\n" + border_double)
    print("|" + "STUDENT INFORMATION SYSTEM - PROFILE GENERATOR".center(width - 2) + "|")
    print(border_double)
    print("Please enter the student details below:\n")

    # 1. Input Collection
    full_name = get_non_empty_input("Enter Full Name                 : ")
    student_id = get_non_empty_input("Enter Student ID                : ")
    programme = get_non_empty_input("Enter Programme of Study        : ")
    level = get_non_empty_input("Enter Level (e.g., 100, 200)    : ")
    age = get_non_empty_input("Enter Age                       : ")
    fav_language = get_non_empty_input("Enter Favourite Language        : ")
    hall = get_non_empty_input("Enter Hall of Residence         : ")

    # 2. STRING CONCATENATION LOGIC
    # Generate Username: First 3 letters of name (lowercase) + Student ID
    generated_username = generate_username(full_name, student_id)

    # Generate Domain and Email via Concatenation
    domain = "@st.ug.edu.gh"
    generated_email = generated_username + domain

    # Modern Feature: Contact Line Concatenation (Developer B ready)
    CONTACT_LINE = "Reach " + full_name + " (" + programme + ") at " + generated_email + ", " + hall

    # Modern Feature: System Status String Concatenation
    STATUS_BADGE = "[STATUS: ACTIVE] " + full_name.upper() + " | LEVEL " + str(level)

    # Theme Customization Selection
    print("\nSelect Output Theme Mode:")
    print("1. Standard Classic Theme")
    print("2. UG Legacy Blue Theme")
    theme_choice = input("Choice (1/2, default 1): ").strip()

    prefix = ""
    suffix = ""
    if theme_choice == "2":
        # ANSI Escape Codes for Cobalt Blue Header
        prefix = "\033[1;34m"
        suffix = "\033[0m"

    # 3. FORMATTED DISPLAY PROFILE
    generated_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    profile_lines = []
    profile_lines.extend(format_row("Full Name", full_name))
    profile_lines.extend(format_row("Student ID", student_id))
    profile_lines.extend(format_row("Programme", programme))
    profile_lines.extend(format_row("Level", level))
    profile_lines.extend(format_row("Age", age))
    profile_lines.extend(format_row("Hall of Residence", hall))
    profile_lines.extend(format_row("Favourite Language", fav_language))
    profile_lines.append(border_single)
    profile_lines.extend(format_row("Generated Username", generated_username))
    profile_lines.extend(format_row("Generated Email", generated_email))
    profile_lines.extend(format_row("Contact Line", CONTACT_LINE))
    profile_lines.extend(format_row("Profile generated at", generated_at))
    profile_text = "\n".join(profile_lines)

    print("\n" + prefix + border_double)
    print("|" + " STUDENT INFORMATION SYSTEM".center(width - 2) + "|")
    print("|" + " STUDENT PROFILE".center(width - 2) + "|")
    print(border_double + suffix)
    print(profile_text)
    print(border_single)
    print(STATUS_BADGE)
    print(border_double)
    print("|" + " UNIVERSITY OF GHANA".center(width - 2) + "|")
    print(border_double + "\n")

    save_choice = input("Save this profile to a text file? (y/n): ").strip().lower()
    if save_choice == "y":
        file_name = save_profile(generated_username, profile_text)
        print("Profile saved to " + file_name)

if __name__ == "__main__":
    main()