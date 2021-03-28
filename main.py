import os
import datetime

file_path = './lessons'
lesson_list = []
for i, j, k in os.walk(file_path):
    lesson_list = k

print(lesson_list)
# define the step of ebbinghaus
forgetting_curves = [0, 1, 2, 4, 7, 15, 30]
# how much time will this cycle take
totalDay = len(lesson_list) + forgetting_curves[-1]
# beginning date
today = datetime.date.today()

def set_playlist(date: datetime.date, lesson_list: list):

    device_base_path = '/storage/emulated/0/'
    device_lesson_path = device_base_path + 'lessons/'
    store_path = './playlist/'

    today_str = date.strftime('%Y-%m-%d')
    play_list_name = today_str + '.m3u8'
    
    if not os.path.exists(store_path):
        os.makedirs(store_path)

    with open(store_path + play_list_name, 'w') as f:
        f.write('#EXTM3U\n')
        # 循环当日待复习列表
        for i in lesson_list:
            f.write('#EXT-X-RATING:0\n')
            f.write(device_lesson_path + i + '\n')


for s in range(0, totalDay):
    tmp = ''
    tmp_list = []
    for r in range(0, len(forgetting_curves))[::-1]:
        if s - forgetting_curves[r] >= 0 and s - forgetting_curves[r] < len(lesson_list)\
                and s >= forgetting_curves[r]:
            tmp = tmp + lesson_list[s -
                                    forgetting_curves[r]] + ','
            tmp_list.append(lesson_list[s -
                                        forgetting_curves[r]])
    if s < len(lesson_list):
        l = lesson_list[s]
    else:
        l = ''

    set_playlist(datetime.timedelta(days=s+1)+today, tmp_list)
    print('%s %15s %12s     %s' % (str(s).zfill(2),
                                   datetime.timedelta(days=s+1)+today, l, tmp[:-1]))
