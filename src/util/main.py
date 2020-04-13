import pandas as pd
import matplotlib.pyplot as plt
import six
import numpy as np

# to ignore pandas warnings
import warnings
warnings.filterwarnings("ignore")

hotel_data = pd.read_csv("../../data/hotel_data.csv", index_col=False)
homeless_data = pd.read_csv("../../data/homeless_data.csv", index_col=False)
minimum_wage_data = pd.read_csv("../../data/minimum_wage.csv", index_col=False)

all_data = hotel_data.join(homeless_data.set_index("state"), on="state")\
    .join(minimum_wage_data.set_index("state"), on="state")

# 2017 avg nightly hotel rate in US - https://www.businesstravelnews.com/Corporate-Travel-Index/2018/Demand-Drives-US-Hotels
avg_hotel_rate = 180.12

# percent of avg nightly rate
percent_of_avg_nightly_fee = 0.40

# Number of people in a single room
people_per_room = 2

# Number of employees required per 10 rooms to take care of homeless population
num_employees_per_10_rooms = 1

# inflation rate to pay hotel employees extra for working
min_wage_inflation_percentage = 0.10

# work day hours for a hotel employee
work_day_hrs = 8


def homeless_pop_vs_avail_rooms(people_per_room, viz=False):
    """
    The effect of sheltering the entire homeless population into separate rooms out of all available hotel rooms
    
    :param people_per_room: Number of homeless people that will occupy a single room
    :param viz: boolean - display a bar graph of data (default False) - saves plot to img directory
    
    :return: dataframe with State and Percent of Rooms Occupied By Homeless Population (percent_comp)
    """
    df = all_data[["state", "num_avail_rooms", "tot_homeless_population"]]
    
    df["percent_comp"] = (df["tot_homeless_population"] / people_per_room) / df["num_avail_rooms"]

    # -----------PLOTTING------------------#
    if viz:
        df_viz = df[["state", "percent_comp"]]
        ax = df_viz.plot.bar(x='state', y='percent_comp', rot=90, figsize=(15,8), legend=False)
        plt.title("The Effect of Sheltering the Homeless Population into All Available Hotel Rooms ({} people per room)"
                  .format(people_per_room), pad=20)
        plt.xlabel("State", labelpad=15)
        plt.ylabel("Percent of Rooms Occupied By Homeless Population", labelpad=15)
        plt.subplots_adjust(bottom=0.25)
        plt.savefig("../../img/all_homeless_in_all_rooms_percentage.png")
        plt.show()
    
    return df[["state", "percent_comp"]]

def number_of_rooms_reserved(people_per_room, viz=False):
    """
    Produces a dataframe mapping each state to the number of reserved rooms that would be required to house the homeless
    population given a certain number of people per room.
    
    :param people_per_room: Number of people to occupy a single room
    :param viz: boolean - displays a bar graph (default False) - saves plot to img directory
    
    :return: dataframe with state and number of reserved rooms
    """
    df = all_data[["state", "num_avail_rooms"]]
    reserve_percent_df = homeless_pop_vs_avail_rooms(people_per_room)
    df = df.join(reserve_percent_df.set_index("state"), on="state")
    
    df["num_reserved_rooms"] = round(df["percent_comp"] * df["num_avail_rooms"])
    df["num_reserved_rooms"] = df["num_reserved_rooms"].apply(lambda x: int(x))

    # -----------PLOTTING------------------#
    if viz:
        df_viz = df[["state", "num_reserved_rooms"]]
        ax = df_viz.plot.bar(x='state', y='num_reserved_rooms', rot=90, figsize=(15, 8), legend=False)
        plt.title("Number of Reserved Rooms Per State by Homeless Population Composition")
        plt.xlabel("State", labelpad=15)
        plt.ylabel("Number of Rooms", labelpad=15)
        plt.subplots_adjust(bottom=0.25, right=0.95, left=0.10)
        plt.savefig("../../img/num_reserved_rooms.png")
        plt.show()

    return df[["state", "num_reserved_rooms"]]

def daily_employee_cost(people_per_room, employees_needed_per_10_rooms, min_wage_inflation_percentage, work_day_hrs, table_viz=False, bar_viz=False):
    df = all_data[["state", "minimum_wage"]]
    rooms_reserved_df = number_of_rooms_reserved(people_per_room, viz=False)
    df = df.join(rooms_reserved_df.set_index("state"), on="state")
    
    df["num_employees_needed"] = (employees_needed_per_10_rooms/10) * df["num_reserved_rooms"]
    df["num_employees_needed"] = df["num_employees_needed"].apply(lambda x: np.math.ceil(x))

    df["final_hrly_wage"] = round((1 + min_wage_inflation_percentage) * df["minimum_wage"], 2)
    df["tot_daily_employee_cost"] = (work_day_hrs * df["final_hrly_wage"]) * df["num_employees_needed"]

    sum = df["tot_daily_employee_cost"].sum()

    if bar_viz:
        df_viz = df[["state", "tot_daily_employee_cost"]]
        ax = df_viz.plot.bar(x='state', y='tot_daily_employee_cost', rot=90, figsize=(15, 8), legend=False)
        plt.title("Employee Cost Per Day - {} employees per 10 rooms - {}% Minimum Wage Inflation"
                  .format(employees_needed_per_10_rooms, 100 * min_wage_inflation_percentage))
        plt.xlabel("State", labelpad=15)
        plt.ylabel("Cost ($)", labelpad=15)
    
        xmin, xmax, ymin, ymax = plt.axis()
        plt.text(0.75 * xmax, 0.80 * ymax, "Total National Daily Cost = ${:,.2f}".format(sum), size=15, rotation=0.,
                 ha="center", va="center",
                 bbox=dict(boxstyle="round",
                           ec=(1., 0.5, 0.5),
                           fc=(1., 0.8, 0.8),
                           )
                 )
        plt.subplots_adjust(bottom=0.25, right=0.95, left=0.10)
        plt.savefig("../../img/daily_employee_cost.png")
        plt.show()

    if table_viz:
        df_new = df[["state", "tot_daily_employee_cost"]]
    
        tot_row = ["TOTAL", sum]
        df_new.loc[len(df_new)] = tot_row
        # df_new.append(pd.DataFrame(tot_row, columns=["state", "tot_daily_employee_cost"]))
    
        df_new["tot_daily_employee_cost"] = df_new["tot_daily_employee_cost"].apply(lambda x: "${:,.2f}".format(x))
        df_new.rename(columns={"state": "State", "tot_daily_employee_cost": "Employee Cost Per Day"}, inplace=True)
        ax = display_df(df_new, col_width=3.8)
    
        plt.title("Employee Cost Per Day \n {} employees per 10 rooms - {}% Minimum Wage Inflation"
                  .format(employees_needed_per_10_rooms, 100 * min_wage_inflation_percentage)
                  , pad=20)
        plt.subplots_adjust(top=.95, bottom=0.02)
        plt.savefig("../../img/daily_employee_cost_table.png")
        plt.show()
        
    return df[["state", "tot_daily_employee_cost"]]
    
def employee_cost_by_percentage(employee_percent, min_wage_inflation_percentage, work_day_hrs, table_viz=False, bar_viz=False):
    """
    NONLOGICAL COMPUTATION - DO NOT USE - WAY OVERESTIMATE
    
    Computes the employee cost for hotels per state and national cost.
    
    This function just assumes the percent of the current employees that would be needed to accommodate for the homeless
    population addition. The cost, however, can be optimized by taking into consideration the exact number of rooms
    that will be needed per state and picking the number of employees for each state based off this number. This
    optimized computation is done in the function 'employee_cost'
    
    :param employee_percent: percent of the state's hotel workers that are needed
    :param min_wage_inflation_percentage: what percent to add onto the state's minimum wage for the workers (ex. 0.25)
    :param work_day_hrs: Number of hours that a single employee will work
    :param df_viz: display the output dataframe
    :param bar_viz: display the bar graph
    :return:
    """
    df = all_data[["state", "minimum_wage", "num_jobs"]]
    
    df["active_employees"] = round(employee_percent * df["num_jobs"])
    df["active_employees"] = df["active_employees"].apply(lambda x: int(x))
    df["final_hrly_wage"] = round((1 + min_wage_inflation_percentage) * df["minimum_wage"], 2)
    df["tot_daily_employee_cost"] = (work_day_hrs * df["final_hrly_wage"]) * df["active_employees"]
    
    sum = df["tot_daily_employee_cost"].sum()
    
    if bar_viz:
        df_viz = df[["state", "tot_daily_employee_cost"]]
        ax = df_viz.plot.bar(x='state', y='tot_daily_employee_cost', rot=90, figsize=(15, 8), legend=False)
        plt.title("Employee Cost Per Day - " + str(100 * employee_percent) + "% of Employees - "
                  + str(100 * min_wage_inflation_percentage) +"% Minimum Wage Inflation")
        plt.xlabel("State", labelpad=15)
        plt.ylabel("Cost ($)", labelpad=15)

        xmin, xmax, ymin, ymax = plt.axis()
        plt.text(0.75 * xmax,0.80 * ymax, "Total National Daily Cost = ${:,.2f}".format(sum), size=15, rotation=0.,
                 ha="center", va="center",
                 bbox=dict(boxstyle="round",
                           ec=(1., 0.5, 0.5),
                           fc=(1., 0.8, 0.8),
                           )
                 )
        plt.subplots_adjust(bottom=0.25, right=0.95, left=0.10)
        plt.savefig("../../img/daily_cost.png")
        plt.show()
    
    if table_viz:
        df_new = df[["state", "tot_daily_employee_cost"]]
        
        tot_row = ["TOTAL", sum]
        df_new.loc[len(df_new)] = tot_row
        # df_new.append(pd.DataFrame(tot_row, columns=["state", "tot_daily_employee_cost"]))

        df_new["tot_daily_employee_cost"] = df_new["tot_daily_employee_cost"].apply(lambda x: "${:,.2f}".format(x))
        df_new.rename(columns={"state": "State", "tot_daily_employee_cost": "Employee Cost Per Day"}, inplace=True)
        ax = display_df(df_new, col_width=3.8)

        plt.title("Employee Cost Per Day - " + str(100 * employee_percent) + "% of Employees - "
                  + str(100 * min_wage_inflation_percentage) + "% Minimum Wage Inflation", pad=20)
        plt.subplots_adjust(top=.95, bottom=0.02)
        plt.savefig("../../img/daily_cost_table.png")
        plt.show()
        
        
    return df

def daily_guest_fee(people_per_room, percent_of_avg_nightly_fee, table_viz=False, bar_viz=False):
    df = number_of_rooms_reserved(people_per_room, viz=False)
    
    nightly_fee = avg_hotel_rate * percent_of_avg_nightly_fee
    df["guest_fee"] = round(df["num_reserved_rooms"] * nightly_fee, 2)

    sum = df["guest_fee"].sum()

    if bar_viz:
        df_viz = df[["state", "guest_fee"]]
        ax = df_viz.plot.bar(x='state', y='guest_fee', rot=90, figsize=(15, 8), legend=False)
        plt.title("Guest Fee Per Day - Nightly Rate = ${:,.2f} \n (Avg National Nightly Rate = ${:,.2f})"
                  .format(nightly_fee, avg_hotel_rate))
        plt.xlabel("State", labelpad=15)
        plt.ylabel("Cost ($)", labelpad=15)
    
        xmin, xmax, ymin, ymax = plt.axis()
        plt.text(0.75 * xmax, 0.80 * ymax, "Total National Daily Cost = ${:,.2f}".format(sum), size=15, rotation=0.,
                 ha="center", va="center",
                 bbox=dict(boxstyle="round",
                           ec=(1., 0.5, 0.5),
                           fc=(1., 0.8, 0.8),
                           )
                 )
        plt.subplots_adjust(bottom=0.25, right=0.95, left=0.10)
        plt.savefig("../../img/daily_guest_fee_cost.png")
        plt.show()
        
    if table_viz:
        df_new = df[["state", "guest_fee"]]
    
        tot_row = ["TOTAL", sum]
        df_new.loc[len(df_new)] = tot_row
    
        df_new["guest_fee"] = df_new["guest_fee"].apply(lambda x: "${:,.2f}".format(x))
        df_new.rename(columns={"state": "State", "guest_fee": "Guest Fee Per Day"}, inplace=True)
        ax = display_df(df_new, col_width=3.8)
    
        plt.title("Guest Fee Per Day - Nightly Rate = ${:,.2f} \n (Avg National Nightly Rate = ${:,.2f})"
                  .format(nightly_fee, avg_hotel_rate)
                  , pad=20)
        plt.subplots_adjust(top=.95, bottom=0.02)
        plt.savefig("../../img/daily_guest_fee_table.png")
        plt.show()
        
    return df[["state", "guest_fee"]]

# main
def total_daily_state_costs(people_per_room, employees_needed_per_10_rooms, min_wage_inflation_percentage, work_day_hrs, percent_of_avg_nightly_fee, table_viz=True, bar_viz=True):
    
    employee_cost_df = daily_employee_cost(people_per_room, employees_needed_per_10_rooms, min_wage_inflation_percentage, work_day_hrs)
    guest_fee_df = daily_guest_fee(people_per_room, percent_of_avg_nightly_fee)
    
    df = employee_cost_df.join(guest_fee_df.set_index("state"), on="state")

    df['total'] = df.iloc[:, 1:].sum(axis=1)
    
    sum_emp = df["tot_daily_employee_cost"].sum()
    sum_guest = df["guest_fee"].sum()
    sum_tot = df["total"].sum()

    if bar_viz:
        df_viz = df[["state", "total"]]
        ax = df_viz.plot.bar(x='state', y='total', rot=90, figsize=(15, 8), legend=False)
        
        plt.xlabel("State", labelpad=15)
        plt.ylabel("Cost ($)", labelpad=15)
        plt.title("Total Daily Cost \n {} employees per 10 rooms - {}% Minimum Wage Inflation \n "
                  "Nightly Rate = ${:,.2f} ({}% of National Avg)"
                  .format(employees_needed_per_10_rooms, 100 * min_wage_inflation_percentage,
                          avg_hotel_rate * percent_of_avg_nightly_fee, percent_of_avg_nightly_fee * 100)
                  , pad=20)
        xmin, xmax, ymin, ymax = plt.axis()
        plt.text(0.75 * xmax, 0.80 * ymax, "Total National Daily Cost = ${:,.2f}".format(sum_tot), size=15, rotation=0.,
                 ha="center", va="center",
                 bbox=dict(boxstyle="round",
                           ec=(1., 0.5, 0.5),
                           fc=(1., 0.8, 0.8),
                           )
                 )
        plt.subplots_adjust(bottom=0.25, right=0.95, left=0.10)
        plt.savefig("../../img/total_daily_cost.png")
        plt.show()


    if table_viz:
        df_new = df.copy()
        tot_row = ["TOTAL", sum_emp, sum_guest, sum_tot]
        df_new.loc[len(df)] = tot_row

        df_new["tot_daily_employee_cost"] = df_new["tot_daily_employee_cost"].apply(lambda x: "${:,.2f}".format(x))
        df_new["guest_fee"] = df_new["guest_fee"].apply(lambda x: "${:,.2f}".format(x))
        df_new["total"] = df_new["total"].apply(lambda x: "${:,.2f}".format(x))

        df_new.rename(columns={"state": "State",
                           "tot_daily_employee_cost": "Employee Cost Per Day",
                           "guest_fee": "Guest Fee Per Day",
                           "total": "Total Daily Cost"}, inplace=True)
        ax = display_df(df_new, col_width=3.8)
    
        plt.title("Total Daily Cost \n {} employees per 10 rooms - {}% Minimum Wage Inflation \n "
                  "Nightly Rate = ${:,.2f} ({}% of National Avg)"
                  .format(employees_needed_per_10_rooms, 100 * min_wage_inflation_percentage,
                          avg_hotel_rate * percent_of_avg_nightly_fee, percent_of_avg_nightly_fee * 100)
                  , pad=20)
        plt.subplots_adjust(top=.92, bottom=0.02)
        plt.savefig("../../img/total_daily_cost_table.png")
        plt.show()
    
    return df
    
    
def daily_cost_for_state(state):
    df = employee_cost(num_employees_per_10_rooms, min_wage_inflation_percentage, work_day_hrs)
    
    df = df[["state", "tot_daily_employee_cost"]]
    
    df = df[df["state"].apply(lambda x: x.lower()) == state.lower()]
    
    state_cost = df["tot_daily_employee_cost"].values[0]
    
    formatted_state_cost = "${:,.2f}".format(state_cost)
    
    print("Daily cost for the state of " + state + " = " +formatted_state_cost)

def display_df(data, col_width=3.0, row_height=0.625, font_size=14,
                     header_color='#40466e', row_colors=['#f1f1f2', 'w'], edge_color='w',
                     bbox=[0, 0, 1, 1], header_columns=0,
                     ax=None, **kwargs):
    if ax is None:
        size = (np.array(data.shape[::-1]) + np.array([0, 1])) * np.array([col_width, row_height])
        size[0] = 15.2
        size[1] = 0.6 * size[1]
        fig, ax = plt.subplots(figsize=size)
        ax.axis('off')

    mpl_table = ax.table(cellText=data.values, bbox=bbox, colLabels=data.columns, **kwargs)

    mpl_table.auto_set_font_size(False)
    mpl_table.set_fontsize(font_size)

    for k, cell in six.iteritems(mpl_table._cells):
        cell.set_edgecolor(edge_color)
        if k[0] == 0 or k[1] < header_columns:
            cell.set_text_props(weight='bold', color='w')
            cell.set_facecolor(header_color)
        else:
            cell.set_facecolor(row_colors[k[0]%len(row_colors) ])
            
    return ax


# homeless_pop_vs_avail_rooms(people_per_room, viz=True)
# number_of_rooms_reserved(people_per_room, viz=True)
# daily_employee_cost(people_per_room, num_employees_per_10_rooms, min_wage_inflation_percentage, work_day_hrs, table_viz=True, bar_viz=False)
# daily_guest_fee(people_per_room, percent_of_avg_nightly_fee, table_viz=True, bar_viz=True)

total_daily_state_costs(people_per_room, num_employees_per_10_rooms, min_wage_inflation_percentage, work_day_hrs, percent_of_avg_nightly_fee, table_viz=True, bar_viz=True)

# daily_cost_for_state("Texas")