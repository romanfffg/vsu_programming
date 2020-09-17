def time_of_year(n):

    if n < 3 or n == 12:

        return "winter"

    elif n < 6:

        return "spring"

    elif n < 9:

        return "summer"

    elif n < 12:

        return "vesna"

n = int(input("Enter the number of month: "))

print(time_of_year(n))
