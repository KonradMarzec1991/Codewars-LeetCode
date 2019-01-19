def what_is_the_time(time_in_mirror):
    time_nums = [int(x) for x in time_in_mirror.split(":")]

    hours = int(time_nums[0])
    minutes = int(time_nums[1])

    if hours == 12:
        hours = 0

    if minutes == 0:
        minutes = 60
        hours -= 1

    mirror = [str(11 - hours), str(60 - minutes)]

    if mirror[0] == '0':
        mirror[0] = '12'

    if len(mirror[0]) == 1:
        mirror[0] = '0' + mirror[0]

    if len(mirror[1]) == 1:
        mirror[1] = '0' + mirror[1]

    return ":".join(mirror)



print(what_is_the_time("05:25"))
print(what_is_the_time("01:50"))
print(what_is_the_time("11:58"))
