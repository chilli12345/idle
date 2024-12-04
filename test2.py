import tkinter as tk
from tkinter import simpledialog, messagebox

def read_lines(file_path, num_lines):
    lines = []
    with open(file_path, 'r') as file:
        for _ in range(num_lines):
            line = file.readline()
            if not line:
                break
            lines.append(line.strip())
    return lines

pre_teen = read_lines(r'C:\Users\Admin\Desktop\questions.txt', 18)
teen = read_lines(r'C:\Users\Admin\Desktop\questions.txt', 36)
y_adult = read_lines(r'C:\Users\Admin\Desktop\questions.txt', 54)
adult = read_lines(r'C:\Users\Admin\Desktop\questions.txt', 72)
o_adult = read_lines(r'C:\Users\Admin\Desktop\questions.txt', 90)
old = read_lines(r'C:\Users\Admin\Desktop\questions.txt', 108)

ans = []

sol1 = read_lines(r'C:\Users\Admin\Desktop\solutions.txt', 3)
sol2 = read_lines(r'C:\Users\Admin\Desktop\solutions.txt', 21)
sol3 = read_lines(r'C:\Users\Admin\Desktop\solutions.txt', 42)

# Initialize Tkinter root
root = tk.Tk()
root.withdraw()  # Hide the root window

# Introductions
messagebox.showinfo(
    "Introduction",
    "Hi there! I hope you're doing okay.\n"
    "It's great that you're taking this step—it shows a lot of strength and self-awareness.\n"
    "Remember, this test is just a tool to help understand how you're feeling, and there's no judgment in whatever the results may be.\n"
    "Take your time, and know that support is always available."
)

# Input data of person
name = simpledialog.askstring("Input", "Enter your name:")
gender = simpledialog.askstring("Input", "Enter your gender:")
age = simpledialog.askinteger("Input", "Enter your age:")

# Function to ask questions and collect responses
def ask_questions(questions, start_index):
    for i in range(start_index, len(questions)):
        response = simpledialog.askinteger(
            "Question",
            f"{questions[i]}\n\n1: Never\n2: Sometimes\n3: Often\n4: Always",
            minvalue=1,
            maxvalue=4
        )
        ans.append(response)
def read_solutions(solutions,start_index):
    for i in range(start_index, len(solutions)):
        response = messagebox.showinfo(
            "Solutions:",
            f"{solutions[i]}\n"
            )

# Determine the set of questions based on age and ask questions
if age >= 12 and age <= 14:
    ask_questions(pre_teen, 4)
elif age >= 15 and age <= 17:
    ask_questions(teen, 22)
elif age >= 18 and age <= 26:
    ask_questions(y_adult, 40)
elif age >= 27 and age <= 36:
    ask_questions(adult, 58)
elif age >= 37 and age <= 45:
    ask_questions(o_adult, 76)
else:
    ask_questions(old, 93)

# Calculate stress level and show results with solutions
slvl = sum(ans)
if slvl <= 30:
    solutions = "\n".join(sol1)
    messagebox.showinfo("Stress Level: Normal", f"Your stress level is normal.\n\nSolutions:\n{solutions}")
elif slvl >= 31 and slvl <= 45:
    solutions = "\n".join(sol2)
    messagebox.showinfo("Stress Level: Elevated (Manageable)", f"Your stress level is elevated but manageable.\n\nSolutions:\n{solutions}")
elif slvl >= 46 and slvl <= 60:
    solutions = "\n".join(sol3)
    messagebox.showinfo("Stress Level: High", f"Your stress level is high.\n\nSolutions:\n{solutions}")

# Close the Tkinter root
root.destroy()
