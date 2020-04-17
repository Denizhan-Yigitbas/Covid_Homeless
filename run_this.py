import fire

from src.util.main import Main

class FireCLI():
    def national_financial_analysis(self, people_per_room, num_employees_per_10_rooms, min_wage_inflation_percentage, nightly_compensation):
        df = Main(people_per_room, num_employees_per_10_rooms, min_wage_inflation_percentage, nightly_compensation)\
            .durational_total_state_costs()

        sum_1 = df["1_day"].sum()
        sum_15 = df["15_days"].sum()
        sum_30 = df["30_days"].sum()
        sum_45 = df["45_days"].sum()
        sum_60 = df["60_days"].sum()
        
        print("\n---------------------------------------------------------------------------------------------\n")
        
        print("Assuming hotels house " + str(people_per_room) +
              " people per room, use " + str(num_employees_per_10_rooms) +
              " employees per 10 rooms used for the homeless, "
              "inflate the miniumum wage for thier state by "
              + str(min_wage_inflation_percentage * 100 )+ "% for each employee, " +
              "and are compensated ${:,.2f} per night per room: \n".format(nightly_compensation))
        
        print("The total duratoinal cost and "
              "percent of the passed 2 trillion dollar stimulus bill would be as follows: \n")
        
        print("Housing for 1 Night Cost: ${:,.2f} --> Percentage of stimulus bill {}%"
              .format(sum_1, sum_1/2000000000000*100.0))

        print("Housing for 15 Nights Cost: ${:,.2f} --> Percentage of stimulus bill {}%"
              .format(sum_15, sum_15 / 2000000000000 * 100.0))

        print("Housing for 30 Nights Cost: ${:,.2f} --> Percentage of stimulus bill {}%"
              .format(sum_30, sum_30 / 2000000000000 * 100.0))

        print("Housing for 45 Nights Cost: ${:,.2f} --> Percentage of stimulus bill {}%"
              .format(sum_45, sum_45 / 2000000000000 * 100.0))

        print("Housing for 60 Nights Cost: ${:,.2f} --> Percentage of stimulus bill {}%"
              .format(sum_60, sum_60 / 2000000000000 * 100.0))

        print("\n---------------------------------------------------------------------------------------------\n")
if __name__ == '__main__':
    fire.Fire(FireCLI)