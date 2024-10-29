import os
import random

def gen_list(path,file):
    all_line=[]
    img_root = os.path.join(path, file)
    print(img_root)
    for img in os.listdir(img_root):
        img_path = os.path.join(img_root, img)
        if img_path.endswith('.jpg') or img_path.endswith('.png') or img_path.endswith('.jpeg'):
            all_line.append(img_path)
    return all_line

if __name__ == "__main__":
    # VOC数据集路径
    voc_path = '/home/aistudio/data/VOC/pascalvoc/VOCdevkit/'
    # 生成train.txt和val.txt的保存路径
    train_path = '/home/aistudio/work/yolov5-Paddle/data/voc/train.txt'
    val_path = '/home/aistudio/work/yolov5-Paddle/data/voc/val.txt'
    test_path = '/home/aistudio/work/yolov5-Paddle/data/voc/test.txt'
    
    # 遍历VOC数据集路径下的所有图片文件，生成filelist
    filelist = []
    for file1 in os.listdir(voc_path):
        if file1.startswith('VOC2007') or file1.startswith('VOC2012'):
            file_path1 = os.path.join(voc_path, file1)
            if os.path.isdir(file_path1):
                for file2 in os.listdir(file_path1):
                    if file2.startswith('JPEGImages'):
                        filelist += gen_list(file_path1, file2)       

    random.seed(42)
    random.shuffle(filelist)
   
    # 将filelist按照一定比例分成训练集和验证集
    split_ratio = 0.8
    split_index = int(len(filelist) * split_ratio)
    train_list = filelist[:split_index]
    val_list = filelist[split_index:int(len(filelist) * 0.9)]
    test_list = filelist[int(len(filelist) * 0.9):]

    # 保存训练集和验证集对应的文件路径到train.txt和val.txt
    with open(train_path, 'w') as f:
        for file_path in train_list:
            f.write(file_path + '\n')

    with open(val_path, 'w') as f:
        for file_path in val_list:
            f.write(file_path + '\n')
            
    with open(test_path, 'w') as f:
        for file_path in test_list:
            f.write(file_path + '\n')

    print('Filelist generated successfully!')