import datetime


# hey
# date_data = now.strftime("%b %d, %Y")
# time_data = now.strftime("%I:%M %p")

def write_to_log(action, when, mode="a"):
    file_name_op = "muv_log.txt"
    open_file = open(file_name_op, mode)
    write = "#" + action + "#" + when + "\n"
    open_file.write(write)
    open_file.close()


# doesn't check by day, month, year
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


first = True
while 1:
    now = datetime.datetime.now()
    pretty_date_and_time_data = now.strftime("%b %d, %Y %I:%M %p")
    date_and_time_data = now.strftime("Y%Y-M%m-D%d-H%H-m%M-S%S")

    now_hour = int(now.strftime("%H"))
    now_minute = int(now.strftime("%M"))
    now_sec = int(now.strftime("%S"))

    now_time_data_list = [now_hour, now_minute, now_sec]

    # THIS STATES THE TIME, NOT THE DIFFERENCE!
    if first:
        status = "Welcome!"
    else:
        status = "You last moved " + str(find_last_log()) + " ago."
    display = pretty_date_and_time_data + "\n" + status

    if first:
        write_to_log("Opened", date_and_time_data, "w")
        first = False

    print(display)
    com = input()

    if com == 'm':
        write_to_log("Moved", date_and_time_data)
