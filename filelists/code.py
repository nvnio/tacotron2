import os
out_file = open("out.txt",mode="a", encoding="utf-8")
with open("ljs_audio_text_train_filelist.txt",'r', encoding='utf-8') as f:
    list_arr = f.readlines()
    for e in list_arr:
        idx, obj = e.split("|")
        idx = "DUMMY/"+idx+'.wav'
        out_file.write(f'{idx}|{obj}')
out_file.close()
