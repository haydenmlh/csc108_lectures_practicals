from typing import TextIO

def highest_rated_band(file:TextIO) -> int:
    '''Given a file of bands, return the rating of the highest rated band in
    the file'''
    file.readline()
    highest = -1
    for i in file:
        i_split = i.rstrip().split(',') #need to strip the right EOL character
        value = int(i_split[1])
        if value > highest:
            highest = value
    file.close()
    return highest

def highest_rated_bandname(file: TextIO) -> str:
    '''Given a file of bands, return the name of the highest rated
    band in the file. In the case of ties, return the one with more plays'''
    file.readline()
    highest_rating, highest_view, highest_bandname = 0, 0, ''
    for i in file:
        i_split = i.rstrip().split(',')  # need to strip the right EOL character
        (name, value, view) = (i_split[0], int(i_split[1]), int(i_split[2]))
        if value > highest_rating or \
                (value == highest_rating and view > highest_view):
            highest_bandname, highest_rating, highest_view = name, value, view
    file.close()
    return highest_bandname

def write_bands_by_rating(file: TextIO, outfile: TextIO):
    '''Given a file of bands, write the data in the file to outfile ordered
    by rating. In the case of ties, the one with more plays comes first.

    Assumption: No band with have both the same rating and same number of plays
    '''
    file.readline()
    bands_dict = {}
    for i in file:
        i_split = i.rstrip().split(',')
        name, rating, views = i_split[0], int(i_split[1]), int(i_split[2])
        bands_dict[rating] = bands_dict.get(rating, [])
        bands_dict[rating].append([name, views])
    # file.close() - don't close other people's files

    sorted_keys = sorted(bands_dict.keys(), reverse = True)
    new_list = []
    for i in sorted_keys:
        while len(bands_dict[i]) > 0:
            highest = -1
            index = 0
            for j in range(len(bands_dict[i])):
                if bands_dict[i][j][1] > highest:
                    highest = bands_dict[i][j][1]
                    index = j
            bands_dict[i][index].append(i)
            new_list.append(bands_dict[i][index])
            bands_dict[i].pop(index)
    for (name, views, rating) in new_list:
        outfile.write(f'{name}, {rating}, {views}\n')
    # outfile.close() - don't close other people's files


def write_bands_by_rating_v2(file: TextIO, outfile: TextIO):
    '''Given a file of bands, write the data in the file to outfile ordered
    by rating. In the case of ties, the one with more plays comes first.

    Assumption: No band with have both the same rating and same number of plays
    '''
    file.readline()
    bands_dict = {}
    for i in file:
        i_split = i.rstrip().split(',')
        name, rating, views = i_split[0], int(i_split[1]), int(i_split[2])
        bands_dict[rating, views] = name
    # file.close() - don't close other people's files

    sorted_keys = sorted(bands_dict.keys(), reverse = True)

    for (rating, views) in sorted_keys:
        name = bands_dict[(rating,views)]
        outfile.write(f'{name}, {rating}, {views}\n')
    # outfile.close() - don't close other people's files


if __name__ == '__main__':
    bands = open('data\\bands.csv')
    bands_out = open('data\\bands_output.csv', 'w')
    write_bands_by_rating(bands, bands_out)