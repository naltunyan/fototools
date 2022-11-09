from PIL import Image
from pathlib import Path
import sys

#исходная папка
source_folder = 'C:/Downloads/Баярд/Избранное/'
file_ext = 'jpg'
#папка для результатов - должна быть очищена
target_folder = 'C:/Downloads/Баярд/Ресайз/'
#нужна ширина
target_width = 2500
target_filename_prefix = 'Boyard_'
#счетчик имени файла
i=0

# перебираем файлы нужного расширения
files = Path(source_folder).glob('*.'+file_ext)

print(files)

for file in files:
    #print(file.name)

    try:
        img = Image.open(file)
    #except OSError as err:
    #    print ('Wrong file',file,':',err)
    #    exit
    except BaseException as err:
        print ('Ошибка при открытии файла',file,':',err)
        exit
    else: print('ok')

    #копируем метаданные, иначе они пропадут при сохранении
    exif = img.info['exif']
    i+=1
    target_file_name = target_folder+target_filename_prefix+str(i)+'.'+file_ext

    #print('width =',img.size[0])
    #print('height =',img.size[1])

    #если ширина больше нужной - рассчитываем пропорциональную высоту
    if img.size[0]>target_width:
        target_height = int(round(target_width*img.size[1]/img.size[0],0))
        #print('target_height =', target_height)
        new_image = img.resize((target_width, target_height))
        new_image.save(target_file_name, exif=exif)
        print('File',target_file_name,'successfully resized with size',str(target_width),'*',str(target_height))
    
    # иначе копируем без изменений
    else:
        target_height = img.size[1]
        img.save(target_file_name, exif=exif)

        print('File',target_file_name,'successfully saved with size',str(img.size[0]),'*',str(target_height))
