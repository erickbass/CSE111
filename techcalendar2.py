import tkinter as tk

# Define an empty dictionary to store the appointments
calendar = {}

# Function to add an appointment to the calendar
def add_appointment():
    date = date_entry.get()
    appointment = appointment_entry.get()
    if date in calendar:
        calendar[date].append(appointment)
    else:
        calendar[date] = [appointment]
    date_entry.delete(0, tk.END)
    appointment_entry.delete(0, tk.END)
    print("Appointment added successfully.")

# Function to display the calendar
def display_calendar():
    output_text.delete("1.0", tk.END)
    for date in calendar:
        appointments = ", ".join(calendar[date])
        output_text.insert(tk.END, date + ": " + appointments + "\n")

# Create main window
window = tk.Tk()
window.title("Technical Support Calendar")

# Create GUI elements
date_label = tk.Label(window, text="Date (dd/mm/yyyy):")
date_entry = tk.Entry(window)
appointment_label = tk.Label(window, text="Appointment description:")
appointment_entry = tk.Entry(window)
add_button = tk.Button(window, text="Add appointment", command=add_appointment)
display_button = tk.Button(window, text="Display calendar", command=display_calendar)
output_text = tk.Text(window)

# Place elements in the window
date_label.grid(row=0, column=0)
date_entry.grid(row=0, column=1)
appointment_label.grid(row=1, column=0)
appointment_entry.grid(row=1, column=1)
add_button.grid(row=2, column=0)
display_button.grid(row=2, column=1)
output_text.grid(row=3, column=0, columnspan=2)

# Run the main window
window.mainloop()
