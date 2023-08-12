import tkinter as tk
import tkinter.ttk as ttk
import sqlite3
import functions

# Connect to the SQLite database
conn = sqlite3.connect('SuperMarketDB.sqlite')
cursor = conn.cursor()

# Create the Tkinter window
root = tk.Tk()
root.title('Supermarket Database Management Software')
root.iconbitmap("icon.ico")

# Create a frame for the query and add row sections
query_frame = tk.Frame(root)
query_frame.pack()

# Create a label and dropdown widget for the table name
table_name_label = tk.Label(query_frame, text='Table Name:')
table_name_label.grid(row=0, column=0, padx=5, pady=5)
table_name_entry = ttk.Combobox(query_frame, values=functions.get_table_names(cursor))
table_name_entry.grid(row=0, column=1, padx=5, pady=5)

# Create a button to execute the query
display_table_button = tk.Button(query_frame, text='Display The Complete Table',
                                 command=lambda: functions.query_database(root, cursor, table_name_entry.get()))
display_table_button.grid(row=0, column=2, padx=5, pady=5)

# Create a button to add a row to the table
add_row_button = tk.Button(query_frame, text='Add Row',
                           command=lambda: functions.add_row_to_table(root, cursor, table_name_entry.get(), conn))
add_row_button.grid(row=0, column=3, padx=5, pady=5)

# Create a frame for the custom command section
command_frame = tk.Frame(root)
command_frame.pack()

# Create a label and entry widget for the custom command
custom_command_label = tk.Label(command_frame, text='Custom Command:')
custom_command_entry = tk.Entry(command_frame)
custom_command_label.grid(row=1, column=0, padx=5, pady=5)
custom_command_entry.grid(row=1, column=1, padx=5, pady=5)

# Create a button to execute the custom command
custom_command_button = tk.Button(command_frame, text='Execute',
                                  command=lambda: functions.run_custom_command(root, cursor, custom_command_entry))
custom_command_button.grid(row=1, column=2, padx=5, pady=5)

# Run the Tkinter loop
root.mainloop()

# Close the connection to the database
conn.close()
