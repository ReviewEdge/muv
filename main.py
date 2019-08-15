import datetime


# date_data = now.strftime("%b %d, %Y")
# time_data = now.strftime("%I:%M %p")

def write_to_log(action, when, mode="a"):
    file_name_op = "muv_log.txt"
    open_file = open(file_name_op, mode)
    write = "#" + action + "#" + when + "\n"
    open_file.write(write)
    open_file.close()


# NOTES:
# ignores day, month, year
# MAKE IT SO IT CHECKS FOR MOVE, NOT JUST '#'
def find_last_log():
    file_name_op = "muv_log.txt"
    open_file = open(file_name_op, "r")
    last_time_raw = open_file.read()
    open_file.close()

    counter = 0
    for c in reversed(last_time_raw):
        counter += 1
        if c == "#":
            start_file_search = counter
            break

    search_string = last_time_raw[(len(last_time_raw) - start_file_search):]

    counter_2 = len(last_time_raw) - len(search_string)
    for i in search_string:
        counter_2 += 1

        if i == "H":
            hour = last_time_raw[counter_2]
            if last_time_raw[counter_2 + 1] != "-":
                hour = last_time_raw[counter_2] + last_time_raw[counter_2 + 1]

        if i == "m":
            minute = last_time_raw[counter_2]
            if last_time_raw[counter_2 + 1] != "-":
                minute = last_time_raw[counter_2] + last_time_raw[counter_2 + 1]

        if i == "S":
            sec = last_time_raw[counter_2]
            if last_time_raw[counter_2 + 1] != ("-" or "\n"):
                sec = last_time_raw[counter_2] + last_time_raw[counter_2 + 1]
            break

    return [int(hour), int(minute), int(sec)]


def find_time_difference(now_time_list, difference_time_list):
    hours = now_time_list[0] - difference_time_list[0]

    minutes = now_time_list[1] - difference_time_list[1]
    if minutes < 0:
        hours -= 1
        minutes += 60

    seconds = now_time_list[2] - difference_time_list[2]
    if seconds < 0:
        minutes -= 1
        seconds += 60

    difference_time_list = [hours, minutes, seconds]
    return difference_time_list


first = True
while 1:
    now = datetime.datetime.now()
    pretty_date_and_time_data = now.strftime("%b %d, %Y %I:%M %p")
    date_and_time_data = now.strftime("Y%Y-M%m-D%d-H%H-m%M-S%S")

    now_hour = int(now.strftime("%H"))
    now_minute = int(now.strftime("%M"))
    now_sec = int(now.strftime("%S"))

    now_time_data_list = [now_hour, now_minute, now_sec]

    if first:
        status = "Welcome!"
    else:
        compare_time_list = find_time_difference(now_time_data_list, find_last_log())
        status = "You last moved " + str(compare_time_list[0]) + " hours, " + str(compare_time_list[1]) +\
                 " minutes, and " + str(compare_time_list[2]) + " seconds ago."
    display = pretty_date_and_time_data + "\n" + status

    if first:
        write_to_log("Opened", date_and_time_data, "w")
        first = False

    print(display)
    com = input()

    if com == 'm':
        write_to_log("Moved", date_and_time_data)

    # this messes stuff up if the move that you enter wasn't the latest move
    if com == 'e':
        s = "00"
        print("Manual move entry:")
        h = input("Enter hour:\n")
        m = input("Enter minute:\n")
        s = input("Enter second (optional):\n")
        if s == "":
            s = "00"

        input_date_and_time_data = now.strftime("Y%Y-M%m-D%d")
        input_date_and_time_data += "-H" + h + "-m" + m + "-S" + s

        write_to_log("Moved", input_date_and_time_data)
