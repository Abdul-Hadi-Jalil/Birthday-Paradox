import datetime
import random


def getBirthdays(no_of_birthdays: int):
    """
    It returns the list of object datetime that has random birthdays
    """
    birthdays = []

    for i in range(no_of_birthdays):
        start_of_year = datetime.date('2001', '1', '1')
        random_day_of_year = datetime.timedelta(random.randint(0, 364))
        birthday = start_of_year + random_day_of_year
        birthdays.append(birthday)

    return birthdays


if __name__=="__main__":
    MONTHS = {'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'}

    while True:
        print("How many birthdays shall i generate? (Max 100)")
        user_input = input("> ")

        # validate the user_input, it has to be a number between 1 and 100.
        if user_input.isdecimal and (1 <= int(user_input) <= 100):
            num_of_days = int(user_input)
            break

    print()          
    birthdays = getBirthdays(int(user_input))
    print(f"Here are {user_input} birthdays:")

    for i, birthday in enumerate(birthdays):
        if i != 0:
            print(', ', end=' ')
        month_name = MONTHS[birthday.month - 1]
        print(f"{month_name} {birthday.day}")