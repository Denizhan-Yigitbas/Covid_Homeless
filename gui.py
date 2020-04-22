from tkinter import *
from tkinter import ttk

from src.util.main import Main

#
# def click():
#     ppr = txt_people_per_room.get()
#     ep10 = txt_num_employees_per_10_rooms.get()
#     mwi = txt_min_wage_inflation_percentage.get()
#     nc = txt_nightly_compensation.get()
#
#     output_title.configure(state='normal')
#     output_vals.configure(state='normal')
#
#     output_title.delete(0.0, END)
#     output_vals.delete(0.0, END)
#
#     output_vars = "Assuming hotels house " + str(ppr) + " people per room, use " + str(
#         ep10) + " employees per 10 rooms, inflate the minimum wage for their state by " + str(
#         mwi) + "% for each employee, and are compensated $" + str(
#         nc) + " per night per room: \n"
#
#     output_title.insert(END, output_vars)
#     output_title.tag_add("title", "1.0", "1.end")
#     output_title.tag_config("title", font = ("Arial",15, "bold"), justify="center")
#
#     df = Main(ppr, ep10, mwi / 100, nc).durational_total_state_costs()
#
#     sum_1 = df["1_day"].sum()
#     sum_15 = df["15_days"].sum()
#     sum_30 = df["30_days"].sum()
#     sum_45 = df["45_days"].sum()
#     sum_60 = df["60_days"].sum()
#
#     one = "The total durational cost and percent of the passed $2 trillion stimulus bill would be as follows: \n\n"
#
#     two = "Housing for 1 Night Cost: ${:,.2f} --> Percentage of stimulus bill {:3.4f}% \n".format(sum_1, sum_1 / 2000000000000 * 100.0)
#
#     three = "Housing for 15 Nights Cost: ${:,.2f} --> Percentage of stimulus bill {:3.4f}% \n".format(sum_15, sum_15 / 2000000000000 * 100.0)
#
#     four = "Housing for 30 Nights Cost: ${:,.2f} --> Percentage of stimulus bill {:3.4f}% \n".format(sum_30, sum_30 / 2000000000000 * 100.0)
#
#     five = "Housing for 45 Nights Cost: ${:,.2f} --> Percentage of stimulus bill {:3.4f}% \n".format(sum_45, sum_45 / 2000000000000 * 100.0)
#
#     six = "Housing for 60 Nights Cost: ${:,.2f} --> Percentage of stimulus bill {:3.4f}% \n".format(sum_60, sum_60 / 2000000000000 * 100.0)
#
#     final_output = one+two+three+four+five+six
#
#     output_vals.insert(END, final_output)
#     output_vals.tag_add("vals", "1.0", END)
#     output_vals.tag_config("vals", font=("Arial", 14), justify="center")
#
#     output_title.configure(state='disabled')
#     output_vals.configure(state='disabled')
#
# def click_state():
#     ppr = txt_people_per_room_state.get()
#     ep10 = txt_num_employees_per_10_rooms_state.get()
#     mwi = txt_min_wage_inflation_percentage_state.get()
#     nc = txt_nightly_compensation_state.get()
#     st = txt_state.get()
#     st = st[0].upper() + st[1:]
#
#     output_state_title.configure(state='normal')
#     output_state_vals.configure(state='normal')
#
#     output_state_title.delete(0.0, END)
#     output_state_vals.delete(0.0, END)
#
#     output_vars = "In the state of " + st + ", assuming hotels house " + str(
#         ppr) + " people per room, use " + str(
#         ep10) + " employees per 10 rooms, inflate the minimum wage for their state by " + str(
#         mwi) + "% for each employee, and are compensated $" + str(
#         nc) + " per night per room: \n"
#
#     output_state_title.insert(END, output_vars)
#     output_state_title.tag_add("title", "1.0", "1.end")
#     output_state_title.tag_config("title", font=("Arial", 15, "bold"), justify="center")
#
#     emp_cost, comp_cost, tot_cost = Main(ppr, ep10, mwi / 100, nc).daily_cost_for_state(st)
#
#     formatted_emp_cost = "${:,.2f}".format(emp_cost)
#     formatted_comp_cost = "${:,.2f}".format(comp_cost)
#     formatted_tot_cost = "${:,.2f}".format(tot_cost)
#
#     ov = "For " + st + ", the employee cost per day would be " + formatted_emp_cost + \
#          "and the nightly compensation cost per day would be " + formatted_comp_cost + \
#          "\n This means the total daily expense for the state of " + st + " would be " + formatted_tot_cost + "\n\n"
#
#     df = Main(ppr, ep10, mwi / 100, nc).durational_total_state_costs()
#
#     df = df[df["state"].apply(lambda x: x.lower()) == st.lower()]
#
#     sum_1 = df["1_day"].values[0]
#     sum_15 = df["15_days"].values[0]
#     sum_30 = df["30_days"].values[0]
#     sum_45 = df["45_days"].values[0]
#     sum_60 = df["60_days"].values[0]
#
#     one = "The total durational cost and percent of the passed $2 trillion stimulus bill would be as follows: \n\n"
#
#     two = "Housing for 1 Night Cost: ${:,.2f} --> Percentage of stimulus bill {:3.4f}% \n".format(sum_1,
#                                                                                              sum_1 / 2000000000000 * 100.0)
#
#     three = "Housing for 15 Nights Cost: ${:,.2f} --> Percentage of stimulus bill {:3.4f}% \n".format(sum_15,
#                                                                                                  sum_15 / 2000000000000 * 100.0)
#
#     four = "Housing for 30 Nights Cost: ${:,.2f} --> Percentage of stimulus bill {:3.4f}% \n".format(sum_30,
#                                                                                                 sum_30 / 2000000000000 * 100.0)
#
#     five = "Housing for 45 Nights Cost: ${:,.2f} --> Percentage of stimulus bill {:3.4f}% \n".format(sum_45,
#                                                                                                 sum_45 / 2000000000000 * 100.0)
#
#     six = "Housing for 60 Nights Cost: ${:,.2f} --> Percentage of stimulus bill {:3.4f}% \n".format(sum_60,
#                                                                                                sum_60 / 2000000000000 * 100.0)
#
#     final_output = ov + one + two + three + four + five + six
#
#     output_state_vals.insert(END, final_output)
#     output_state_vals.tag_add("vals", "1.0", END)
#     output_state_vals.tag_config("vals", font=("Arial", 14), justify="center")
#
#     output_state_title.configure(state='disabled')
#     output_state_vals.configure(state='disabled')

# window = Tk()
# # a fix for running on OSX - to center the title text vertically
# if window.tk.call('tk', 'windowingsystem') == 'aqua':  # only for OSX
#     s = ttk.Style()
#     # Note: the name is specially for the text in the widgets
#     s.configure('TNotebook.Tab', padding=(12, 8, 12, 0))
#
# width = 1000
# height = 700
# bg_color = "white"
#
# window.title("Sheltering the Homeless During a Pandemic")
# window.geometry(str(width) + "x" + str(height))

# #Create Tab Control
# tab_control = ttk.Notebook(window)
# #Tab1
# tab1 = Frame(tab_control, background=bg_color)
# tab_control.add(tab1, text='National Level')
# #Tab2
# tab2 = Frame(tab_control, background=bg_color)
# tab_control.add(tab2, text='State Level')
# tab_control.pack(expand=1, fill="both")
#
# inputs_lf = LabelFrame(tab1, text='Inputs', background=bg_color, padx=30, pady=20)
# inputs_lf.grid(row=0, column=0, columnspan=4, rowspan=5)
#
# # Define the Input Labels
# lbl_people_per_room = Label(inputs_lf, text="People Per Room: ", pady=20, background=bg_color)
# lbl_people_per_room.grid(row=0, column=0)
#
# lbl_num_employees_per_10_rooms = Label(inputs_lf, text="Employees Per 10 Rooms: ", background=bg_color)
# lbl_num_employees_per_10_rooms.grid(row=0, column=2)
#
# lbl_min_wage_inflation_percentage = Label(inputs_lf, text="Minimum Wage Inflation Percentage: ", background=bg_color)
# lbl_min_wage_inflation_percentage.grid(row=1, column=0)
#
# lbl_nightly_compensation = Label(inputs_lf, text="Nightly Hotel Compensation", background=bg_color)
# lbl_nightly_compensation.grid(row=1, column=2)
#
# # Define the Entries
# txt_people_per_room = DoubleVar(value=2)
# entry_ppr = Entry(inputs_lf, textvariable=txt_people_per_room)
# entry_ppr.grid(row=0, column=1)
#
# txt_num_employees_per_10_rooms = DoubleVar(value=1)
# entry_ep10 = Entry(inputs_lf, textvariable=txt_num_employees_per_10_rooms)
# entry_ep10.grid(row=0, column=3)
#
# txt_min_wage_inflation_percentage = DoubleVar(value=50)
# entry_mwi = Entry(inputs_lf, textvariable=txt_min_wage_inflation_percentage)
# entry_mwi.grid(row=1, column=1)
#
# txt_nightly_compensation = DoubleVar(value=72.05)
# entry_nc = Entry(inputs_lf, textvariable=txt_nightly_compensation)
# entry_nc.grid(row=1, column=3)
#
# # spacer
# lbl_spacer = Label(inputs_lf, text="", background=bg_color)
# lbl_spacer.grid(row=3, column=0, columnspan=4)
#
#
# btn_calculate = ttk.Button(inputs_lf, text="Calculate", width=15,  command=click)
# btn_calculate.grid(row=4, column=0, columnspan=4)
#
# # spacer
# lbl_spacer = Label(tab1, text="", background=bg_color)
# lbl_spacer.grid(row=5, column=0, columnspan=4)
#
# outputs_lf = LabelFrame(tab1, text='Results', background=bg_color)
# outputs_lf.grid(row=6, column=0, columnspan=4, rowspan=2)
#
# # Output text box
# output_title = Text(outputs_lf, width=120, height=5, wrap=WORD, padx=10, pady=10)
# output_title.tag_configure("center", justify='center')
# output_title.configure(state='disabled')
# output_title.grid(row=5, column=0, columnspan=4)
#
# output_vals = Text(outputs_lf, width=120, height=10, wrap=WORD, padx=10)
# output_vals.grid(row=6, column=0, columnspan=4)
# output_vals.configure(state='disabled')




# Define the Input Labels
# lbl_people_per_room_state = Label(tab2, text="People Per Room: ", pady=20, background=bg_color)
# lbl_people_per_room_state.grid(row=0, column=0)
#
# lbl_num_employees_per_10_rooms_state = Label(tab2, text="Employees Per 10 Rooms: ", background=bg_color)
# lbl_num_employees_per_10_rooms_state.grid(row=0, column=2)
#
# lbl_min_wage_inflation_percentage_state = Label(tab2, text="Minimum Wage Inflation Percentage: ", background=bg_color)
# lbl_min_wage_inflation_percentage_state.grid(row=1, column=0)
#
# lbl_nightly_compensation_state = Label(tab2, text="Nightly Hotel Compensation", background=bg_color)
# lbl_nightly_compensation_state.grid(row=1, column=2)
#
# lbl_state = Label(tab2, text="State", pady=20)
# lbl_state.grid(row=2, column=0)
#
# # Define the Entries
# txt_people_per_room_state = DoubleVar(value=2)
# entry_ppr = Entry(tab2, textvariable=txt_people_per_room_state)
# entry_ppr.grid(row=0, column=1)
#
# txt_num_employees_per_10_rooms_state = DoubleVar(value=1)
# entry_ep10 = Entry(tab2, textvariable=txt_num_employees_per_10_rooms_state)
# entry_ep10.grid(row=0, column=3)
#
# txt_min_wage_inflation_percentage_state = DoubleVar(value=50)
# entry_mwi = Entry(tab2, textvariable=txt_min_wage_inflation_percentage_state)
# entry_mwi.grid(row=1, column=1)
#
# txt_nightly_compensation_state = DoubleVar(value=72.05)
# entry_nc = Entry(tab2, textvariable=txt_nightly_compensation_state)
# entry_nc.grid(row=1, column=3)
#
# txt_state = StringVar(value="Texas")
# entry_st = Entry(tab2, textvariable=txt_state)
# entry_st.grid(row=2, column=1)
#
# # spacer
# lbl_spacer = Label(tab2, text="", background=bg_color)
# lbl_spacer.grid(row=3, column=0, columnspan=4)
#
# btn_calculate = ttk.Button(tab2, text="Calculate", width=15,  command=click_state)
# btn_calculate.grid(row=4, column=0, columnspan=4)
#
# # spacer
# lbl_spacer = Label(tab2, text="", background=bg_color)
# lbl_spacer.grid(row=5, column=0, columnspan=4)
#
# # Output text box
# output_state_title = Text(tab2, width=120, height=5, wrap=WORD, background=bg_color, padx=10)
# output_state_title.tag_configure("center", justify='center')
# output_state_title.configure(state='disabled')
# output_state_title.grid(row=6, column=0, columnspan=4)
#
# output_state_vals = Text(tab2, width=120, height=14, wrap=WORD, background=bg_color, padx=10)
# output_state_vals.grid(row=7, column=0, columnspan=4)
# output_state_vals.configure(state='disabled')


    
# window.mainloop()

class GUI(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
    
        if parent.tk.call('tk', 'windowingsystem') == 'aqua':  # only for OSX
            s = ttk.Style()
            # Note: the name is specially for the text in the widgets
            s.configure('TNotebook.Tab', padding=(12, 8, 12, 0))
        width = 1000
        height = 700
        self.bg_color = "white"
    
        parent.title("Sheltering the Homeless During a Pandemic")
        parent.geometry(str(width) + "x" + str(height))
        self.tab_control = ttk.Notebook(parent)
        self.init_ui()
    
    def init_ui(self):
        self.create_tabs()
        self.national_level()
        self.state_level()

    def create_tabs(self):
        # Create Tab Control
        # Tab1
        self.tab1 = Frame(self.tab_control, background=self.bg_color)
        self.tab_control.add(self.tab1, text='National Level')
        # Tab2
        self.tab2 = Frame(self.tab_control, background=self.bg_color)
        self.tab_control.add(self.tab2, text='State Level')
        self.tab_control.pack(expand=1, fill="both")

    def national_level(self):
        """
        All internal components of the National Level tab
        """
        def click():
            """
            Actoin taken when Calculate Button is clicked
            """
            # obtain the values from the entries
            ppr = txt_people_per_room.get()
            ep10 = txt_num_employees_per_10_rooms.get()
            mwi = txt_min_wage_inflation_percentage.get()
            nc = txt_nightly_compensation.get()
        
            # enable writing
            output_title.configure(state='normal')
            output_vals.configure(state='normal')
        
            # delete existing writing
            output_title.delete(0.0, END)
            output_vals.delete(0.0, END)
        
            # Add the Variables chosen in sentence form
            output_vars = "Assuming hotels house " + str(ppr) + " people per room, use " + str(
                ep10) + " employees per 10 rooms, inflate the minimum wage for their state by " + str(
                mwi) + "% for each employee, and are compensated $" + str(
                nc) + " per night per room: \n"
        
            output_title.insert(END, output_vars)
            output_title.tag_add("title", "1.0", "1.end")
            output_title.tag_config("title", font=("Arial", 15, "bold"), justify="center")
        
            # Obtain the duration DataFrame and perform calculatoins
            df = Main(ppr, ep10, mwi / 100, nc).durational_total_state_costs()
        
            sum_1 = df["1_day"].sum()
            sum_15 = df["15_days"].sum()
            sum_30 = df["30_days"].sum()
            sum_45 = df["45_days"].sum()
            sum_60 = df["60_days"].sum()
        
            one = "The total durational cost and percent of the passed $2 trillion stimulus bill would be as follows: \n\n"
        
            two = "Housing for 1 Night Cost: ${:,.2f} --> Percentage of stimulus bill {:3.4f}% \n"\
                .format(sum_1, sum_1 / 2000000000000 * 100.0)
        
            three = "Housing for 15 Nights Cost: ${:,.2f} --> Percentage of stimulus bill {:3.4f}% \n"\
                .format(sum_15, sum_15 / 2000000000000 * 100.0)
        
            four = "Housing for 30 Nights Cost: ${:,.2f} --> Percentage of stimulus bill {:3.4f}% \n"\
                .format(sum_30, sum_30 / 2000000000000 * 100.0)
        
            five = "Housing for 45 Nights Cost: ${:,.2f} --> Percentage of stimulus bill {:3.4f}% \n"\
                .format(sum_45, sum_45 / 2000000000000 * 100.0)
        
            six = "Housing for 60 Nights Cost: ${:,.2f} --> Percentage of stimulus bill {:3.4f}% \n"\
                .format(sum_60, sum_60 / 2000000000000 * 100.0)
        
            final_output = one + two + three + four + five + six

            output_vals.insert(END, final_output)
            output_vals.tag_add("vals", "1.0", END)
            output_vals.tag_config("vals", font=("Arial", 14), justify="center")

            #disable writing
            output_title.configure(state='disabled')
            output_vals.configure(state='disabled')
            
        # Create a LabelFrame for the inputs
        inputs_lf = LabelFrame(self.tab1, text='Inputs', background=self.bg_color, padx=30, pady=20)
        inputs_lf.grid(row=0, column=0, columnspan=4, rowspan=5)
    
        # Define the Labels
        lbl_people_per_room = Label(inputs_lf, text="People Per Room: ", pady=20, background=self.bg_color)
        lbl_people_per_room.grid(row=0, column=0)
    
        lbl_num_employees_per_10_rooms = Label(inputs_lf, text="Employees Per 10 Rooms: ", background=self.bg_color)
        lbl_num_employees_per_10_rooms.grid(row=0, column=2)
    
        lbl_min_wage_inflation_percentage = Label(inputs_lf, text="Minimum Wage Inflation Percentage: ",
                                                  background=self.bg_color)
        lbl_min_wage_inflation_percentage.grid(row=1, column=0)
    
        lbl_nightly_compensation = Label(inputs_lf, text="Nightly Hotel Compensation: ($) ", background=self.bg_color)
        lbl_nightly_compensation.grid(row=1, column=2)
    
        # Define the Entries
        txt_people_per_room = DoubleVar(value=2)
        entry_ppr = Entry(inputs_lf, textvariable=txt_people_per_room)
        entry_ppr.grid(row=0, column=1)
    
        txt_num_employees_per_10_rooms = DoubleVar(value=1)
        entry_ep10 = Entry(inputs_lf, textvariable=txt_num_employees_per_10_rooms)
        entry_ep10.grid(row=0, column=3)
    
        txt_min_wage_inflation_percentage = DoubleVar(value=50)
        entry_mwi = Entry(inputs_lf, textvariable=txt_min_wage_inflation_percentage)
        entry_mwi.grid(row=1, column=1)
    
        txt_nightly_compensation = DoubleVar(value=72.05)
        entry_nc = Entry(inputs_lf, textvariable=txt_nightly_compensation)
        entry_nc.grid(row=1, column=3)
    
        # spacer
        lbl_spacer = Label(inputs_lf, text="", background=self.bg_color)
        lbl_spacer.grid(row=3, column=0, columnspan=4)
    
        btn_calculate = ttk.Button(inputs_lf, text="Calculate", width=15, command=click)
        btn_calculate.grid(row=4, column=0, columnspan=4)
    
        # spacer
        lbl_spacer = Label(self.tab1, text="", background=self.bg_color)
        lbl_spacer.grid(row=5, column=0, columnspan=4)
    
        outputs_lf = LabelFrame(self.tab1, text='Results', background=self.bg_color)
        outputs_lf.grid(row=6, column=0, columnspan=4, rowspan=2)
    
        # Output text box
        output_title = Text(outputs_lf, width=120, height=5, wrap=WORD, padx=10, pady=10)
        output_title.tag_configure("center", justify='center')
        output_title.configure(state='disabled')
        output_title.grid(row=5, column=0, columnspan=4)
    
        output_vals = Text(outputs_lf, width=120, height=14, wrap=WORD, padx=10)
        output_vals.grid(row=6, column=0, columnspan=4)
        output_vals.configure(state='disabled')
        
    def state_level(self):
        """
        All internal components for State Level
        """
        def click_state():
            # obtain the values from the entries
            ppr = txt_people_per_room_state.get()
            ep10 = txt_num_employees_per_10_rooms_state.get()
            mwi = txt_min_wage_inflation_percentage_state.get()
            nc = txt_nightly_compensation_state.get()
            st = txt_state.get()
            st = st[0].upper() + st[1:]

            # enable writing
            output_state_title.configure(state='normal')
            output_state_vals.configure(state='normal')

            # delete existing writing
            output_state_title.delete(0.0, END)
            output_state_vals.delete(0.0, END)

            # Add the Variables chosen in sentence form
            output_vars = "In the state of " + st + ", assuming hotels house " + str(
                ppr) + " people per room, use " + str(
                ep10) + " employees per 10 rooms, inflate the minimum wage for their state by " + str(
                mwi) + "% for each employee, and are compensated $" + str(
                nc) + " per night per room: \n"
        
            output_state_title.insert(END, output_vars)
            output_state_title.tag_add("title", "1.0", "1.end")
            output_state_title.tag_config("title", font=("Arial", 15, "bold"), justify="center")
        
            emp_cost, comp_cost, tot_cost = Main(ppr, ep10, mwi / 100, nc).daily_cost_for_state(st)
        
            formatted_emp_cost = "${:,.2f}".format(emp_cost)
            formatted_comp_cost = "${:,.2f}".format(comp_cost)
            formatted_tot_cost = "${:,.2f}".format(tot_cost)
        
            ov = "For " + st + ", the employee cost per day would be " + formatted_emp_cost + \
                 "and the nightly compensation cost per day would be " + formatted_comp_cost + \
                 "\n This means the total daily expense for the state of " + st + " would be " + formatted_tot_cost + "\n\n"

            # Obtain the duration DataFrame and perform calculations
            df = Main(ppr, ep10, mwi / 100, nc).durational_total_state_costs()
        
            df = df[df["state"].apply(lambda x: x.lower()) == st.lower()]
        
            sum_1 = df["1_day"].values[0]
            sum_15 = df["15_days"].values[0]
            sum_30 = df["30_days"].values[0]
            sum_45 = df["45_days"].values[0]
            sum_60 = df["60_days"].values[0]
        
            one = "The total durational cost and percent of the passed $2 trillion stimulus bill in "\
                  + st + " would be as follows: \n\n"
        
            two = "Housing for 1 Night Cost: ${:,.2f} --> Percentage of stimulus bill {:3.4f}% \n"\
                .format(sum_1, sum_1 / 2000000000000 * 100.0)
        
            three = "Housing for 15 Nights Cost: ${:,.2f} --> Percentage of stimulus bill {:3.4f}% \n"\
                .format(sum_15, sum_15 / 2000000000000 * 100.0)
        
            four = "Housing for 30 Nights Cost: ${:,.2f} --> Percentage of stimulus bill {:3.4f}% \n"\
                .format(sum_30, sum_30 / 2000000000000 * 100.0)
        
            five = "Housing for 45 Nights Cost: ${:,.2f} --> Percentage of stimulus bill {:3.4f}% \n"\
                .format(sum_45, sum_45 / 2000000000000 * 100.0)
        
            six = "Housing for 60 Nights Cost: ${:,.2f} --> Percentage of stimulus bill {:3.4f}% \n"\
                .format(sum_60, sum_60 / 2000000000000 * 100.0)
        
            final_output = ov + one + two + three + four + five + six
        
            output_state_vals.insert(END, final_output)
            output_state_vals.tag_add("vals", "1.0", END)
            output_state_vals.tag_config("vals", font=("Arial", 14), justify="center")
        
            output_state_title.configure(state='disabled')
            output_state_vals.configure(state='disabled')

        # Create a LabelFrame for the inputs
        state_inputs_lf = LabelFrame(self.tab2, text='Inputs', background=self.bg_color, padx=30, pady=20)
        state_inputs_lf.grid(row=0, column=0, columnspan=4, rowspan=5)
        
        # Define the Input Labels
        lbl_people_per_room_state = Label(state_inputs_lf, text="People Per Room: ", pady=20, background=self.bg_color)
        lbl_people_per_room_state.grid(row=0, column=0)

        lbl_num_employees_per_10_rooms_state = Label(state_inputs_lf, text="Employees Per 10 Rooms: ",
                                                     background=self.bg_color)
        lbl_num_employees_per_10_rooms_state.grid(row=0, column=2)

        lbl_min_wage_inflation_percentage_state = Label(state_inputs_lf, text="Minimum Wage Inflation Percentage: ",
                                                        background=self.bg_color)
        lbl_min_wage_inflation_percentage_state.grid(row=1, column=0)

        lbl_nightly_compensation_state = Label(state_inputs_lf, text="Nightly Hotel Compensation: ($) ",
                                               background=self.bg_color)
        lbl_nightly_compensation_state.grid(row=1, column=2)

        lbl_state = Label(state_inputs_lf, text="State", pady=20)
        lbl_state.grid(row=2, column=0)

        # Define the Entries
        txt_people_per_room_state = DoubleVar(value=2)
        entry_ppr = Entry(state_inputs_lf, textvariable=txt_people_per_room_state)
        entry_ppr.grid(row=0, column=1)

        txt_num_employees_per_10_rooms_state = DoubleVar(value=1)
        entry_ep10 = Entry(state_inputs_lf, textvariable=txt_num_employees_per_10_rooms_state)
        entry_ep10.grid(row=0, column=3)

        txt_min_wage_inflation_percentage_state = DoubleVar(value=50)
        entry_mwi = Entry(state_inputs_lf, textvariable=txt_min_wage_inflation_percentage_state)
        entry_mwi.grid(row=1, column=1)

        txt_nightly_compensation_state = DoubleVar(value=72.05)
        entry_nc = Entry(state_inputs_lf, textvariable=txt_nightly_compensation_state)
        entry_nc.grid(row=1, column=3)

        txt_state = StringVar(value="Texas")
        entry_st = Entry(state_inputs_lf, textvariable=txt_state)
        entry_st.grid(row=2, column=1)

        # spacer
        lbl_spacer = Label(state_inputs_lf, text="", background=self.bg_color)
        lbl_spacer.grid(row=4, column=0, columnspan=4)

        btn_calculate = ttk.Button(state_inputs_lf, text="Calculate", width=15, command=click_state)
        btn_calculate.grid(row=5, column=0, columnspan=4)
    
        # spacer
        lbl_spacer = Label(self.tab2, text="", background=self.bg_color)
        lbl_spacer.grid(row=6, column=0, columnspan=4)

        state_outputs_lf = LabelFrame(self.tab2, text='Results', background=self.bg_color)
        state_outputs_lf.grid(row=7, column=0, columnspan=4, rowspan=2)
    
        # Output text box
        output_state_title = Text(state_outputs_lf, width=120, height=5, wrap=WORD, background=self.bg_color, padx=10)
        output_state_title.tag_configure("center", justify='center')
        output_state_title.configure(state='disabled')
        output_state_title.grid(row=7, column=0, columnspan=4)
    
        output_state_vals = Text(state_outputs_lf, width=120, height=16, wrap=WORD, background=self.bg_color, padx=10)
        output_state_vals.grid(row=8, column=0, columnspan=4)
        output_state_vals.configure(state='disabled')
        
        
if __name__ == '__main__':
    root = Tk()
    GUI(root)
    root.mainloop()