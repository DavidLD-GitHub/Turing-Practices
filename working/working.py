import re

def main():
    print(convert(input("Hours: ")))

def meridian_to_militar(hour, meridian):
    hour = int(hour)
    if meridian == "PM" and hour < 12:
        hour += 12
    elif meridian == "AM" and hour == 12:
        hour = 0
    elif hour > 24:
        raise ValueError
    return str(hour).rjust(2,"0")

def minutes(mins):
    if mins is None:
        return "00"
    else:
        return mins.rjust(2,"0")


def convert(s):
    matches = re.fullmatch(r"^(\d\d?):?([1-5]\d|0\d)? (AM|PM) to (\d\d?):?([1-5]\d|0\d)? (AM|PM)$" , s)
    if matches:
        first_hour = meridian_to_militar(int(matches.group(1)),matches.group(3))
        first_minute = minutes(matches.group(2))
        second_hour = meridian_to_militar(int(matches.group(4)), matches.group(6))
        second_minute = minutes(matches.group(5))
        
        return first_hour + ":" + first_minute + " to " + second_hour + ":" +second_minute
    else:
        raise ValueError
    


if __name__ == "__main__":
    main() 