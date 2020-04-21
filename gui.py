from tkinter import *
from tkinter import ttk

from src.util.main import Main


def click():
    ppr = txt_people_per_room.get()
    ep10 = txt_num_employees_per_10_rooms.get()
    mwi = txt_min_wage_inflation_percentage.get()
    nc = txt_nightly_compensation.get()

    output_title.configure(state='normal')
    output_vals.configure(state='normal')
    
    output_title.delete(0.0, END)
    output_vals.delete(0.0, END)
    
    output_vars = "Assuming hotels house " + str(ppr) + " people per room, use " + str(
        ep10) + " employees per 10 rooms, inflate the miniumum wage for thier state by " + str(
        mwi) + "% for each employee, and are compensated $" + str(
        nc) + " per night per room: \n"
    
    output_title.insert(END, output_vars)
    output_title.tag_add("title", "1.0", "1.end")
    output_title.tag_config("title", font = ("Arial",15, "bold"), justify="center")

    df = Main(ppr, ep10, mwi / 100, nc).durational_total_state_costs()

    sum_1 = df["1_day"].sum()
    sum_15 = df["15_days"].sum()
    sum_30 = df["30_days"].sum()
    sum_45 = df["45_days"].sum()
    sum_60 = df["60_days"].sum()

    one = "The total duratoinal cost and percent of the passed $2 trillion stimulus bill would be as follows: \n\n"

    two = "Housing for 1 Night Cost: ${:,.2f} --> Percentage of stimulus bill {}% \n".format(sum_1, sum_1 / 2000000000000 * 100.0)

    three = "Housing for 15 Nights Cost: ${:,.2f} --> Percentage of stimulus bill {}% \n".format(sum_15, sum_15 / 2000000000000 * 100.0)

    four = "Housing for 30 Nights Cost: ${:,.2f} --> Percentage of stimulus bill {}% \n".format(sum_30, sum_30 / 2000000000000 * 100.0)

    five = "Housing for 45 Nights Cost: ${:,.2f} --> Percentage of stimulus bill {}% \n".format(sum_45, sum_45 / 2000000000000 * 100.0)

    six = "Housing for 60 Nights Cost: ${:,.2f} --> Percentage of stimulus bill {}% \n".format(sum_60, sum_60 / 2000000000000 * 100.0)
    
    final_output = one+two+three+four+five+six
    
    output_vals.insert(END, final_output)
    output_vals.tag_add("vals", "1.0", END)
    output_vals.tag_config("vals", font=("Arial", 14), justify="center")

    output_title.configure(state='disabled')
    output_vals.configure(state='disabled')

    
window = Tk()

width = 850
height = 450

window.title("Sheltering the Homeless During a Pandemic")
window.geometry(str(width) + "x" + str(height))

# style = ttk.Style()
# style.theme_create('st', settings={
#     ".": {
#         "configure": {
#             "background": "white",
#         }
#     },
#     "TNotebook": {
#         "configure": {
#             "tabmargins": [2, 5, 0, 0],
#         }
#     },
#     "TNotebook.Tab": {
#         "configure": {
#             "padding": [10, 2]
#         },
#         "map": {
#             "background": [("selected", "#D3D3D3")],
#             "expand": [("selected", [1, 1, 1, 0])]
#         }
#     },
# })
# style.theme_use('st')

#Create Tab Control
tab_control = ttk.Notebook(window)
#Tab1
tab1 = ttk.Frame(tab_control)
tab_control.add(tab1, text='National Level')
#Tab2
tab2 = ttk.Frame(tab_control)
tab_control.add(tab2, text='State Level')
tab_control.pack(expand=1, fill="both")

#Tab Name Labels
ttk.Label(tab1, text="This is Tab 1").grid(column=0, row=0, padx=10, pady=10)
ttk.Label(tab2, text="This is Tab 2").grid(column=0, row=0, padx=10, pady=10)

# Define the Input Labels
lbl_people_per_room = Label(tab1, text="People Per Room: ", pady=20)
lbl_people_per_room.grid(row=0, column=0)

lbl_num_employees_per_10_rooms = Label(tab1, text="Employees Per 10 Rooms: ")
lbl_num_employees_per_10_rooms.grid(row=0, column=2)

lbl_min_wage_inflation_percentage = Label(tab1, text="Miniumum Wage Inflation Percentage: ")
lbl_min_wage_inflation_percentage.grid(row=1, column=0)

lbl_nightly_compensation = Label(tab1, text="Nightly Hotel Compensation")
lbl_nightly_compensation.grid(row=1, column=2)

# Define the Entries
txt_people_per_room = DoubleVar(value=2)
entry_ppr = Entry(tab1, textvariable=txt_people_per_room)
entry_ppr.grid(row=0, column=1)

txt_num_employees_per_10_rooms = DoubleVar(value=1)
entry_ep10 = Entry(tab1, textvariable=txt_num_employees_per_10_rooms)
entry_ep10.grid(row=0, column=3)

txt_min_wage_inflation_percentage = DoubleVar(value=50)
entry_mwi = Entry(tab1, textvariable=txt_min_wage_inflation_percentage)
entry_mwi.grid(row=1, column=1)

txt_nightly_compensation = DoubleVar(value=72.05)
entry_nc = Entry(tab1, textvariable=txt_nightly_compensation)
entry_nc.grid(row=1, column=3)

# spacer
lbl_spacer = Label(tab1, text="")
lbl_spacer.grid(row=2, column=0, columnspan=4)

style1 = ttk.Style()
btn_calculate = ttk.Button(tab1, text="Calculate", width=15,  command=click)
btn_calculate.grid(row=3, column=0, columnspan=4)

# spacer
lbl_spacer = Label(tab1, text="")
lbl_spacer.grid(row=4, column=0, columnspan=4)

# Output text box

output_title = Text(tab1, width=110, height=5, wrap=WORD, background="white", padx=10)
output_title.tag_configure("center", justify='center')
output_title.configure(state='disabled')
output_title.grid(row=5, column=0, columnspan=4)

output_vals = Text(tab1, width=110, height=10, wrap=WORD, background="white", padx=10)
output_vals.grid(row=6, column=0, columnspan=4)
output_vals.configure(state='disabled')

    
window.mainloop()