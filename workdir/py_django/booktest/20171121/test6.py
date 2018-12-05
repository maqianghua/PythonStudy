#coding=utf-8

# for every_letter in 'Hello world':
#     print (every_letter)

# for num in range(1,11): #不包含11，因此实际范围是1~10
#     print (str(num) + ' + 1 = ', num+ 1)

songslist = ['Holy Diver', 'Thunderstruck', 'Rebel Rebel']
for song in songslist:
    if song == 'Holy Diver':
        print (song, ' - Dio')
    elif song == "Thunderstruck":
        print (song, ' - AC/DC')
    elif song == 'Rebel Rebel':
        print (song, '- David Bowie')
