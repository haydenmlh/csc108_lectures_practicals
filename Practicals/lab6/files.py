import urllib.request
from typing import List, TextIO


# Precondition for all functions in this module: Each line of the url
# file contains the average monthly temperatures for a year (separated
# by spaces) starting with January.  The file must also have 3 header
# lines.
DATA_URL = 'http://robjhyndman.com/tsdldata/data/cryer2.dat'


def open_temperature_file(url: str) -> TextIO:
    '''Open the specified url, read past the three-line header, and 
    return the open file.
    '''
    file = urllib.request.urlopen(url)
    for _ in range(3):
        file.readline()
    return file


def avg_temp_march(f: TextIO) -> float:
    '''Return the average temperature for the month of March
    over all years in f.
    '''

    # We are providing the code for this function
    # to illustrate one important difference between reading from a URL
    # and reading from a regular file. When reading from a URL,
    # we must first convert the line to a string.
    # the str(line, 'ascii') conversion is not used on regular files.
    
    march_temps = []

    # read each line of the file and store the values
    # as floats in a list
    for line in f:
        line = str(line, 'ascii') # now line is a string
        temps = line.split()
        # there are some blank lines at the end of the temperature data
        # If we try to access temps[2] on a blank line,
        # we would get an error because the list would have no elements.
        # So, check that it is not empty.
        if temps != []:
            march_temps.append(float(temps[2]))

    # calculate the average and return it
    return sum(march_temps) / len(march_temps)


def avg_temp(f: TextIO, month: int) -> float:
    '''Return the average temperature for a month over all years
    in f. month is an integer between 0 and 11, representing
    January to December, respectively.
    '''
    month_temps = []
    for line in f:
        line = str(line, 'ascii')
        temps = line.split()
        # there are some blank lines at the end of the temperature data
        # If we try to access temps[2] on a blank line,
        # we would get an error because the list would have no elements.
        # So, check that it is not empty.
        if temps != []:
            month_temps.append(float(temps[month]))

    # calculate the average and return it
    return sum(month_temps) / len(month_temps)


def higher_avg_temp(url: str, month1: int, month2: int) -> int:
    '''Return either month1 or month2 (integers representing months in
    the range 0 to 11), whichever has the higher average temperature 
    over all years in the webpage at the given URL.  If the months have
    the same average temperature, then return -1.
    '''
    f = open_temperature_file(url)
    if avg_temp(f, month1) > avg_temp(f, month2):
        return avg_temp(f, month1)
    elif avg_temp(f, month1) < avg_temp(f, month2):
        return avg_temp(f, month2)
    else:
        return -1


def three_highest_temps(f: TextIO) -> List[float]:
    '''Return the three highest temperatures, in descending order, 
    over all months and years in f.
    '''
    max_1 = 0
    max_2 = 0
    max_3 = 0
    for i in f:
        i = str(i, 'ascii')
        temps = i.split()
        if temps != []:
            for j in temps:
                if float(j) > max_3:
                    max_3 = float(j)
                    if max_3 > max_2:
                        foo = max_2
                        max_2 = max_3
                        max_3 = foo
                    if max_2 > max_1:
                        foo = max_1
                        max_1 = max_2
                        max_2 = foo
    return [max_1, max_2, max_3]



def below_freezing(f: TextIO) -> List[float]:
    '''Return, in ascending order, all temperatures below freezing 
    (32 degrees Fahrenheit), for all temperature data in f. Include 
    any duplicates that occur.
    '''
    below = []
    for i in f:
        i = str(i, 'ascii')
        temps = i.split()
        if temps != []:
            for j in temps:
                if float(j) < 32:
                    below.append(float(j))
    below.sort()
    return below

