"""Time Zone Conversion."""
# JDD 12/2023

import sys
from datetime import datetime
import pytz

def convert_time_zone(original_time, from_time_zone, to_time_zone):
    """function to formate time."""
    datetime_object = datetime.strptime(original_time, "%Y-%m-%d %H:%M:%S")

	# set orginal timezone
    source_timezone = pytz.timezone(from_time_zone)
    localized_datetime = source_timezone.localize(datetime_object)

	# convert to new timezone
    target_timezone = pytz.timezone(to_time_zone)
    converted_time = localized_datetime.astimezone(target_timezone)

    return converted_time

def main():
    """main is the Main."""
    print("\nWelcome to the PyTime Zone Conversion!")

    if len(sys.argv) > 3:
        #store command line argument that is provided
        original_time = sys.argv[1]		# formate "YYYY-MM-DD HH:MM:SS"
        from_time_zone = sys.argv[2]	# e.g., "US/Eastern"
        to_time_zone = sys.argv[3]		# e.g., "Asia/Tokyo"
    else:
        # prompt the user to input in the format(e.g., YYYY-MM-DD HH:MM:SS)
        # prompt the user to input time zones to convert
        original_time = input("\nEnter the original time (YYYY-MM-DD HH:MM:SS): ")
        print("\nPlease use the IANA time zone formate. "
              "Use the TZ identifier for the time zone input.\n")
        from_time_zone = input("Enter the source time zone (e.g., US/Eastern): ")
        print("\nPlease use the IANA time zone formate. "
              "Use the TZ identifier for the time zone input.\n")
        to_time_zone = input("Enter the target time zone (e.g., Asia/Tokyo): ")

	#retrieve the conversion result and format it for output
    converted_time = convert_time_zone(original_time, from_time_zone, to_time_zone)
    formatted_time = converted_time.strftime('%Y-%m-%d %H:%M:%S')
    print(f"\n\x1b[31mThe time in {to_time_zone} is: \x1b[11;30;42m{formatted_time}\x1b[0m\n")

# main

if __name__ == "__main__":
    main()

# end
