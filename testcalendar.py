# Import the necessary modules
import unittest
import tkinter as tk
from techcalendar2 import add_appointment, display_calendar

class TestSupportCalendar(unittest.TestCase):

    def setUp(self):
        # Create a new Tkinter window
        self.window = tk.Tk()
        self.window.title("Test Support Calendar")
        
        # Create GUI elements
        self.date_entry = tk.Entry(self.window)
        self.appointment_entry = tk.Entry(self.window)
        self.add_button = tk.Button(self.window, text="Add appointment", command=add_appointment)
        self.display_button = tk.Button(self.window, text="Display calendar", command=display_calendar)
        self.output_text = tk.Text(self.window)
        
        # Place elements in the window
        self.date_entry.grid(row=0, column=0)
        self.appointment_entry.grid(row=1, column=0)
        self.add_button.grid(row=2, column=0)
        self.display_button.grid(row=3, column=0)
        self.output_text.grid(row=4, column=0)
        
    def test_add_appointment(self):
        # Enter a new appointment and click the "Add appointment" button
        self.date_entry.insert(0, "01/04/2023")
        self.appointment_entry.insert(0, "Fix printer")
        self.add_button.invoke()
        
        # Check that the appointment was added to the calendar
        expected_calendar = {"01/04/2023": ["Fix printer"]}
        self.assertEqual(calendar, expected_calendar)
        
    def test_display_calendar(self):
        # Add some appointments to the calendar
        calendar = {"01/04/2023": ["Fix printer", "Install software"],
                    "02/04/2023": ["Network troubleshooting"]}
        
        # Display the calendar and check that the output is correct
        self.output_text.delete("1.0", tk.END)
        display_calendar()
        expected_output = "01/04/2023: Fix printer, Install software\n02/04/2023: Network troubleshooting\n"
        self.assertEqual(self.output_text.get("1.0", tk.END), expected_output)
        
    def tearDown(self):
        # Destroy the Tkinter window
        self.window.destroy()

if __name__ == '__main__':
    unittest.main()
