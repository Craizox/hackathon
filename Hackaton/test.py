from python.read_pics import get_pics_from_file

pics_name = ["pics_0", "pics_1", "pics_2", "pics_3"]
pics = dict()
info = dict()
listpics = []
for pic in pics_name:
    (curr_pic, info[pic]) = get_pics_from_file(f'data/{pic}.bin')
    pics[pic] = curr_pic
    listpics.append(curr_pic)

y = pics_name

print('Y = ', len(pics_name))

