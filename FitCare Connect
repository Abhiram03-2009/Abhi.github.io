import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import json
import os
import matplotlib.pyplot as plt

class FitnessApp:
    def __init__(self, root):
        self.root = root
        self.root.title("FitCare Connect")
        self.root.geometry("800x600")

        # Create gradient background
        self.canvas = tk.Canvas(root, width=800, height=600)
        self.canvas.pack(fill="both", expand=True)
        self.create_gradient()

        self.main_frame = tk.Frame(self.canvas, bg='lightblue')
        self.main_frame.place(relwidth=1, relheight=1)

        # Title with weightlifting emojis
        title = tk.Label(self.main_frame, text="🏋‍♂ FitCare Connect 🏋‍♀", font=('Arial', 36), bg='lightblue', fg='gold')
        title.pack(pady=20)

        self.calories_consumed = 0
        self.calories_burned = 0
        self.food_entries = []
        self.activity_entries = []
        self.user_profile = {"name": "User", "age": "", "weight": "", "height": ""}
        self.goals = {"weight_loss": 0, "muscle_gain": 0}

        # Load user data
        self.load_data()

        # Status Bar
        self.status_label = tk.Label(self.root, text="", bg='lightblue', fg='gold', font=('Arial', 14))
        self.status_label.pack(side='bottom', fill='x')

        # Hamburger menu button
        self.hamburger_button = tk.Button(self.root, text="☰", command=self.toggle_menu, bg='blue', fg='gold', font=('Arial', 20))
        self.hamburger_button.place(x=10, y=10)

        self.menu_frame = None
        self.create_home_screen()

    def create_gradient(self):
        for i in range(600):
            color = f'#{int(255 - (i * 0.4)):02x}{int(255 - (i * 0.2)):02x}ff'
            self.canvas.create_line(0, i, 800, i, fill=color)

    def toggle_menu(self):
        if self.menu_frame:
            self.menu_frame.destroy()
            self.menu_frame = None
        else:
            self.create_menu()

    def create_menu(self):
        self.menu_frame = tk.Frame(self.main_frame, bg='silver', width=200)
        self.menu_frame.pack(side='left', fill='y')

        buttons = [
            ("Home", self.create_home_screen),
            ("Calorie Tracker", self.calorie_tracker_screen),
            ("Activity Tracker", self.activity_tracker_screen),
            ("User Profile", self.user_profile_screen),
            ("Goals", self.goals_screen),
            ("Progress Statistics", self.progress_statistics_screen),
            ("Graphs", self.graphs_screen),
            ("BMI Calculator", self.bmi_calculator_screen)
        ]

        for text, command in buttons:
            button = self.create_button(text, self.navigate_to(command))
            button.pack(pady=5, padx=10)

    def create_button(self, text, command):
        return tk.Button(self.menu_frame, text=text, command=command, bg='blue', fg='white', font=('Arial', 14), width=20)

    def navigate_to(self, command):
        def inner():
            self.clear_frame()
            command()
            if self.menu_frame:
                self.menu_frame.destroy()
                self.menu_frame = None
        return inner

    def clear_frame(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    def create_home_screen(self):
        self.clear_frame()
        tk.Label(self.main_frame, text="🏋‍♂ FitCare Connect 🏋‍♀", font=('Arial', 36), bg='lightblue', fg='gold').pack(pady=20)
        tk.Label(self.main_frame, text="Welcome to FitCare Connect! Get Fit, Stay Healthy!", font=('Arial', 24), bg='lightblue', fg='gold').pack()

    def calorie_tracker_screen(self):
        self.clear_frame()
        tk.Label(self.main_frame, text="Calorie Tracker", font=('Arial', 28), bg='lightblue', fg='gold').pack(pady=10)

        tk.Button(self.main_frame, text="Add Food Entry", command=self.open_food_entry_window, bg='blue', fg='white', font=('Arial', 16), width=25).pack(pady=10)
        tk.Button(self.main_frame, text="View Food Log", command=self.view_food_log, bg='blue', fg='white', font=('Arial', 16), width=25).pack(pady=10)
        tk.Button(self.main_frame, text="Back", command=self.create_home_screen, bg='blue', fg='white', font=('Arial', 16), width=25).pack(pady=5)

    def open_food_entry_window(self):
        self.food_entry_window = tk.Toplevel(self.root)
        self.food_entry_window.title("Add Food Entry")
        self.food_entry_window.geometry("400x300")

        tk.Label(self.food_entry_window, text="Enter Food Item:", font=('Arial', 14)).pack(pady=5)
        self.food_item_entry = tk.Entry(self.food_entry_window, font=('Arial', 14))
        self.food_item_entry.pack(pady=5)

        tk.Label(self.food_entry_window, text="Enter Calories:", font=('Arial', 14)).pack(pady=5)
        self.calories_entry = tk.Entry(self.food_entry_window, font=('Arial', 14))
        self.calories_entry.pack(pady=5)

        tk.Label(self.food_entry_window, text="Enter Serving Size (g):", font=('Arial', 14)).pack(pady=5)
        self.serving_size_entry = tk.Entry(self.food_entry_window, font=('Arial', 14))
        self.serving_size_entry.pack(pady=5)

        tk.Button(self.food_entry_window, text="Add Entry", command=self.add_food_entry_from_window, bg='blue', fg='white', font=('Arial', 14), width=13).pack(pady=2)
        tk.Button(self.food_entry_window, text="Cancel", command=self.food_entry_window.destroy, bg='blue', fg='white', font=('Arial', 14), width=13).pack(pady=2)

    def add_food_entry_from_window(self):
        food_item = self.food_item_entry.get()
        calories = self.calories_entry.get()
        serving_size = self.serving_size_entry.get()

        if food_item and calories.isdigit() and serving_size.isdigit():
            calories = int(calories)
            serving_size = int(serving_size)
            self.food_entries.append((food_item, calories, serving_size))
            self.calories_consumed += calories
            self.update_status(f"{food_item} added with {calories} calories.")
            self.save_data()
            self.food_item_entry.delete(0, tk.END)
            self.calories_entry.delete(0, tk.END)
            self.serving_size_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Input Error", "Please fill in all fields correctly.")

    def view_food_log(self):
        self.clear_frame()
        tk.Label(self.main_frame, text="Food Log", font=('Arial', 28), bg='lightblue', fg='gold').pack(pady=10)

        table_frame = tk.Frame(self.main_frame, bg='lightblue')
        table_frame.pack(pady=10)

        headers = ["Food Item", "Calories", "Serving Size (g)"]
        for header in headers:
            tk.Label(table_frame, text=header, bg='lightblue', fg='cyan', font=('Arial', 14)).grid(row=0, column=headers.index(header), padx=5, pady=5)

        for idx, (food_item, calories, serving_size) in enumerate(self.food_entries, start=1):
            tk.Label(table_frame, text=food_item, bg='lightblue', fg='black').grid(row=idx, column=0, padx=5, pady=5)
            tk.Label(table_frame, text=str(calories), bg='lightblue', fg='black').grid(row=idx, column=1, padx=5, pady=5)
            tk.Label(table_frame, text=str(serving_size), bg='lightblue', fg='black').grid(row=idx, column=2, padx=5, pady=5)

        tk.Button(self.main_frame, text="Back", command=self.calorie_tracker_screen, bg='blue', fg='white', font=('Arial', 16), width=25).pack(pady=5)

    def activity_tracker_screen(self):
        self.clear_frame()
        tk.Label(self.main_frame, text="Activity Tracker", font=('Arial', 28), bg='lightblue', fg='gold').pack(pady=10)

        tk.Button(self.main_frame, text="Add Activity Entry", command=self.open_activity_entry_window, bg='blue', fg='white', font=('Arial', 16), width=25).pack(pady=10)
        tk.Button(self.main_frame, text="View Activity Log", command=self.view_activity_log, bg='blue', fg='white', font=('Arial', 16), width=25).pack(pady=10)
        tk.Button(self.main_frame, text="Back", command=self.create_home_screen, bg='blue', fg='white', font=('Arial', 16), width=25).pack(pady=5)

    def open_activity_entry_window(self):
        self.activity_entry_window = tk.Toplevel(self.root)
        self.activity_entry_window.title("Add Activity Entry")
        self.activity_entry_window.geometry("400x300")

        tk.Label(self.activity_entry_window, text="Enter Activity Name:", font=('Arial', 14)).pack(pady=5)
        self.activity_name_entry = tk.Entry(self.activity_entry_window, font=('Arial', 14))
        self.activity_name_entry.pack(pady=5)

        tk.Label(self.activity_entry_window, text="Enter Calories Burned:", font=('Arial', 14)).pack(pady=5)
        self.activity_calories_entry = tk.Entry(self.activity_entry_window, font=('Arial', 14))
        self.activity_calories_entry.pack(pady=5)

        tk.Button(self.activity_entry_window, text="Add Entry", command=self.add_activity_entry_from_window, bg='blue', fg='white', font=('Arial', 16), width=15).pack(pady=10)
        tk.Button(self.activity_entry_window, text="Cancel", command=self.activity_entry_window.destroy, bg='blue', fg='white', font=('Arial', 16), width=15).pack(pady=5)

    def add_activity_entry_from_window(self):
        activity_name = self.activity_name_entry.get()
        calories_burned = self.activity_calories_entry.get()

        if activity_name and calories_burned.isdigit():
            calories_burned = int(calories_burned)
            self.activity_entries.append((activity_name, calories_burned))
            self.calories_burned += calories_burned
            self.update_status(f"{activity_name} added with {calories_burned} calories burned.")
            self.save_data()
            self.activity_name_entry.delete(0, tk.END)
            self.activity_calories_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Input Error", "Please fill in all fields correctly.")

    def view_activity_log(self):
        self.clear_frame()
        tk.Label(self.main_frame, text="Activity Log", font=('Arial', 28), bg='lightblue', fg='gold').pack(pady=10)

        table_frame = tk.Frame(self.main_frame, bg='lightblue')
        table_frame.pack(pady=10)

        headers = ["Activity", "Calories Burned"]
        for header in headers:
            tk.Label(table_frame, text=header, bg='lightblue', fg='gold', font=('Arial', 14)).grid(row=0, column=headers.index(header), padx=5, pady=5)

        for idx, (activity_item, calories_burned) in enumerate(self.activity_entries, start=1):
            tk.Label(table_frame, text=activity_item, bg='lightblue', fg='black').grid(row=idx, column=0, padx=5, pady=5)
            tk.Label(table_frame, text=str(calories_burned), bg='lightblue', fg='black').grid(row=idx, column=1, padx=5, pady=5)

        tk.Button(self.main_frame, text="Back", command=self.activity_tracker_screen, bg='blue', fg='white', font=('Arial', 16), width=25).pack(pady=5)

    def user_profile_screen(self):
        self.clear_frame()
        tk.Label(self.main_frame, text="User Profile", font=('Arial', 28), bg='lightblue', fg='gold').pack(pady=10)

        # Display current profile information
        tk.Label(self.main_frame, text=f"Name: {self.user_profile.get('name', 'N/A')}", bg='lightblue', fg='black', font=('Arial', 14)).pack(pady=5)
        tk.Label(self.main_frame, text=f"Age: {self.user_profile.get('age', 'N/A')}", bg='lightblue', fg='black', font=('Arial', 14)).pack(pady=5)
        tk.Label(self.main_frame, text=f"Weight: {self.user_profile.get('weight', 'N/A')} lbs", bg='lightblue', fg='black', font=('Arial', 14)).pack(pady=5)
        tk.Label(self.main_frame, text=f"Height: {self.user_profile.get('height', 'N/A')} inches", bg='lightblue', fg='black', font=('Arial', 14)).pack(pady=5)

        tk.Button(self.main_frame, text="Edit Profile", command=self.edit_profile_screen, bg='blue', fg='white', font=('Arial', 16), width=25).pack(pady=10)
        tk.Button(self.main_frame, text="Back", command=self.create_home_screen, bg='blue', fg='white', font=('Arial', 16), width=25).pack(pady=5)

    def edit_profile_screen(self):
        self.clear_frame()
        tk.Label(self.main_frame, text="Edit Profile", font=('Arial', 28), bg='lightblue', fg='gold').pack(pady=10)

        # Use similar entry fields as before for editing
        tk.Label(self.main_frame, text="Name:", bg='lightblue', fg='black', font=('Arial', 14)).pack(pady=5)
        self.name_entry = tk.Entry(self.main_frame, font=('Arial', 14))
        self.name_entry.insert(0, self.user_profile.get("name", ""))
        self.name_entry.pack(pady=5)

        tk.Label(self.main_frame, text="Age:", bg='lightblue', fg='black', font=('Arial', 14)).pack(pady=5)
        self.age_entry = tk.Entry(self.main_frame, font=('Arial', 14))
        self.age_entry.insert(0, self.user_profile.get("age", ""))
        self.age_entry.pack(pady=5)

        tk.Label(self.main_frame, text="Weight (lbs):", bg='lightblue', fg='black', font=('Arial', 14)).pack(pady=5)
        self.weight_entry = tk.Entry(self.main_frame, font=('Arial', 14))
        self.weight_entry.insert(0, self.user_profile.get("weight", ""))
        self.weight_entry.pack(pady=5)

        tk.Label(self.main_frame, text="Height (inches):", bg='lightblue', fg='black', font=('Arial', 14)).pack(pady=5)
        self.height_entry = tk.Entry(self.main_frame, font=('Arial', 14))
        self.height_entry.insert(0, self.user_profile.get("height", ""))
        self.height_entry.pack(pady=5)

        tk.Button(self.main_frame, text="Save Changes", command=self.save_user_profile, bg='blue', fg='white', font=('Arial', 16), width=25).pack(pady=10)
        tk.Button(self.main_frame, text="Back", command=self.user_profile_screen, bg='blue', fg='white', font=('Arial', 16), width=25).pack(pady=5)

    def save_user_profile(self):
        # Logic to save the updated user profile
        self.user_profile["name"] = self.name_entry.get()
        self.user_profile["age"] = self.age_entry.get()
        self.user_profile["weight"] = self.weight_entry.get()
        self.user_profile["height"] = self.height_entry.get()
    
        # Optionally, refresh the profile screen to show updated information
        self.user_profile_screen()


    def goals_screen(self):
        self.clear_frame()
        tk.Label(self.main_frame, text="Goals", font=('Arial', 28), bg='lightblue', fg='gold').pack(pady=10)
        tk.Button(self.main_frame, text="Set Goals", command=self.set_goals, bg='blue', fg='white', font=('Arial', 16), width=25).pack(pady=10)
        tk.Button(self.main_frame, text="Back", command=self.create_home_screen, bg='blue', fg='white', font=('Arial', 16), width=25).pack(pady=5)

    def set_goals(self):
        # Create the frame for setting goals
        self.clear_frame()
        tk.Label(self.main_frame, text="Set Your Goals", font=('Arial', 28), bg='lightblue', fg='gold').pack(pady=10)

        tk.Label(self.main_frame, text="Weight Loss Goal (lbs):", font=('Arial', 16), bg='lightblue').pack(pady=5)
        self.weight_loss_goal_entry = tk.Entry(self.main_frame, font=('Arial', 16))
        self.weight_loss_goal_entry.pack(pady=5)

        tk.Label(self.main_frame, text="Muscle Gain Goal (lbs):", font=('Arial', 16), bg='lightblue').pack(pady=5)
        self.muscle_gain_goal_entry = tk.Entry(self.main_frame, font=('Arial', 16))
        self.muscle_gain_goal_entry.pack(pady=5)

        tk.Button(self.main_frame, text="Save Goals", command=self.save_goals, bg='blue', fg='white', font=('Arial', 16)).pack(pady=10)
        tk.Button(self.main_frame, text="View Current Goals", command=self.display_goals, bg='blue', fg='white', font=('Arial', 16)).pack(pady=5)
        tk.Button(self.main_frame, text="Back", command=self.create_home_screen, bg='blue', fg='white', font=('Arial', 16)).pack(pady=5)

    def save_goals(self):
        weight_loss_goal = self.weight_loss_goal_entry.get()
        muscle_gain_goal = self.muscle_gain_goal_entry.get()

        if weight_loss_goal.isdigit() and muscle_gain_goal.isdigit():
            self.goals["weight_loss"] = int(weight_loss_goal)
            self.goals["muscle_gain"] = int(muscle_gain_goal)
            self.update_status("Goals set successfully!")
            self.save_data()
        else:
            messagebox.showerror("Input Error", "Please enter valid numerical goals.")

    def display_goals(self):
        self.clear_frame()
        tk.Label(self.main_frame, text="Current Goals", font=('Arial', 28), bg='lightblue', fg='gold').pack(pady=10)

        tk.Label(self.main_frame, text=f"Weight Loss Goal: {self.goals.get('weight_loss', 'Not set')} lbs", font=('Arial', 16), bg='lightblue').pack(pady=5)
        tk.Label(self.main_frame, text=f"Muscle Gain Goal: {self.goals.get('muscle_gain', 'Not set')} lbs", font=('Arial', 16), bg='lightblue').pack(pady=5)

        tk.Button(self.main_frame, text="Edit Goals", command=self.set_goals, bg='blue', fg='white', font=('Arial', 16)).pack(pady=10)
        tk.Button(self.main_frame, text="Back", command=self.create_home_screen, bg='blue', fg='white', font=('Arial', 16)).pack(pady=5)

    def progress_statistics_screen(self):
        self.clear_frame()
        tk.Label(self.main_frame, text="Progress Statistics", font=('Arial', 28), bg='lightblue', fg='gold').pack(pady=10)

        tk.Label(self.main_frame, text=f"Calories Consumed: {self.calories_consumed}", font=('Arial', 20), bg='lightblue', fg='black').pack(pady=5)
        tk.Label(self.main_frame, text=f"Calories Burned: {self.calories_burned}", font=('Arial', 20), bg='lightblue', fg='black').pack(pady=5)

        tk.Button(self.main_frame, text="Back", command=self.create_home_screen, bg='blue', fg='white', font=('Arial', 16), width=25).pack(pady=5)

    def graphs_screen(self):
        self.clear_frame()
        tk.Label(self.main_frame, text="Graphs", font=('Arial', 28), bg='lightblue', fg='gold').pack(pady=10)

        tk.Button(self.main_frame, text="View Activity Graph", command=self.plot_activity_graph, bg='blue', fg='white', font=('Arial', 16), width=25).pack(pady=5)
        tk.Button(self.main_frame, text="View Calorie Graph", command=self.plot_calorie_graph, bg='blue', fg='white', font=('Arial', 16), width=25).pack(pady=5)
        tk.Button(self.main_frame, text="Back", command=self.create_home_screen, bg='blue', fg='white', font=('Arial', 16), width=25).pack(pady=5)

    def plot_activity_graph(self):
        if not self.activity_entries:
            messagebox.showinfo("No Data", "No activity data available.")
            return

        activities = [entry[0] for entry in self.activity_entries]
        calories = [entry[1] for entry in self.activity_entries]

        plt.bar(activities, calories, color='blue')
        plt.title("Calories Burned by Activity")
        plt.xlabel("Activities")
        plt.ylabel("Calories Burned")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    def plot_calorie_graph(self):
        if not self.food_entries:
            messagebox.showinfo("No Data", "No food data available.")
            return

        foods = [entry[0] for entry in self.food_entries]
        calories = [entry[1] for entry in self.food_entries]

        plt.bar(foods, calories, color='green')
        plt.title("Calories Consumed by Food Item")
        plt.xlabel("Food Items")
        plt.ylabel("Calories")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    def bmi_calculator_screen(self):
        self.clear_frame()
        tk.Label(self.main_frame, text="BMI Calculator", font=('Arial', 28), bg='lightblue', fg='gold').pack(pady=10)

        tk.Label(self.main_frame, text="Weight (lbs):", bg='lightblue', fg='black', font=('Arial', 14)).pack(pady=5)
        self.bmi_weight_entry = tk.Entry(self.main_frame, font=('Arial', 14))
        self.bmi_weight_entry.pack(pady=5)

        tk.Label(self.main_frame, text="Height (inches):", bg='lightblue', fg='black', font=('Arial', 14)).pack(pady=5)
        self.bmi_height_entry = tk.Entry(self.main_frame, font=('Arial', 14))
        self.bmi_height_entry.pack(pady=5)

        tk.Button(self.main_frame, text="Calculate BMI", command=self.calculate_bmi, bg='blue', fg='white', font=('Arial', 16), width=25).pack(pady=10)
        tk.Button(self.main_frame, text="Back", command=self.create_home_screen, bg='blue', fg='white', font=('Arial', 16), width=25).pack(pady=5)

    def calculate_bmi(self):
        weight = self.bmi_weight_entry.get()
        height = self.bmi_height_entry.get()

        if weight.isdigit() and height.isdigit():
            weight = int(weight)
            height = int(height)
            bmi = weight/(height*height)*703

            messagebox.showinfo("BMI Result", f"Your BMI is {bmi:.2f}.")
        else:
            messagebox.showerror("Input Error", "Please enter valid numerical values for weight and height.")

    def update_status(self, message):
        self.status_label.config(text=message)

    def load_data(self):
        if os.path.exists("user_data.json"):
            with open("user_data.json", "r") as file:
                data = json.load(file)
                self.food_entries = data.get("food_entries", [])
                self.activity_entries = data.get("activity_entries", [])
                self.user_profile = data.get("user_profile", self.user_profile)
                self.goals = data.get("goals", self.goals)
                self.calories_consumed = sum(entry[1] for entry in self.food_entries)
                self.calories_burned = sum(entry[1] for entry in self.activity_entries)

    def save_data(self):
        data = {
            "food_entries": self.food_entries,
            "activity_entries": self.activity_entries,
            "user_profile": self.user_profile,
            "goals": self.goals
        }
        with open("user_data.json", "w") as file:
            json.dump(data, file)

if __name__ == "__main__":
    root = tk.Tk()
    app = FitnessApp(root)
    root.mainloop()
