import tkinter as tk
import tkinter.ttk as ttk

def get_table_names(cursor):
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = [table[0] for table in cursor.fetchall()]
    return tables

def query_database(root, cursor, table_name):
    cursor.execute(f'SELECT * FROM {table_name}')
    field_names = [i[0] for i in cursor.description]
    results = cursor.fetchall()
    display_table(root, table_name, field_names, results)

def display_table(parent, table_name, field_names, results):
    top = tk.Toplevel(parent)
    top.title(table_name)
    tree = ttk.Treeview(top, columns=field_names)
    tree.pack()
    for i, field_name in enumerate(field_names):
        tree.heading(i, text=field_name)
        tree.column(i, width=100)
    for result in results:
        tree.insert('', 'end', values=result)

def run_custom_command(root, cursor, custom_command_entry):
    custom_command = custom_command_entry.get()
    cursor.execute(custom_command)
    field_names = [i[0] for i in cursor.description]
    results = cursor.fetchall()
    display_table(root, "Custom Command Result", field_names, results)

def add_row_to_table(root, cursor, table_name, conn):
    top = tk.Toplevel(root)
    top.title(f'Add Row to {table_name}')
    cursor.execute(f'PRAGMA table_info({table_name})')
    field_info = cursor.fetchall()

    entries = []
    for i, field in enumerate(field_info):
        field_name = field[1]
        label = tk.Label(top, text=field_name)
        entry = tk.Entry(top)
        label.grid(row=i, column=0, padx=5, pady=5)
        entry.grid(row=i, column=1, padx=5, pady=5)
        entries.append(entry)

    def insert_row():
        values = [entry.get() for entry in entries]
        placeholders = ', '.join(['?'] * len(values))
        query = f'INSERT INTO {table_name} VALUES ({placeholders})'
        cursor.execute(query, values)
        conn.commit()
        top.destroy()

    button = tk.Button(top, text='Add Row', command=insert_row)
    button.grid(row=len(field_info), column=0, columnspan=2, padx=5, pady=5)
