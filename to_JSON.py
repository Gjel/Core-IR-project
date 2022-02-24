import json
import numpy as np

Chiel_src = '..\\data\\collectionandqueries\\collection.tsv'
Chiel_target = '..\\data\\collectionandqueries\\test.json'


def tsv_to_json(start=0, end=10, src_path=Chiel_src, target_path=Chiel_target):
    arr = []
    with open(src_path, 'r', encoding='utf-8') as src:
        i = 0
        while i < start:
            i += 1
            src.readline()

        while i < end:
            line = src.readline()
            l = line.split('\t')
            entry = {'id': l[0], 'contents': l[1]}
            arr.append(entry)
            i += 1

    with open(target_path, 'w', encoding='utf-8') as target:
        target.write(json.dumps(arr))


def read_lines(end=10, src_path=Chiel_src):
    with open(src_path, 'r') as src:
        i = 0
        while i < end:
            print("line", i)
            print(src.readline())
            i += 1

