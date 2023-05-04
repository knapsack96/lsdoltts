import os
from matplotlib import pyplot as plt
import numpy as np
import pickle

def compute_iou(boxA, boxB):
    xA = max(boxA[0], boxB[0])
    yA = max(boxA[1], boxB[1])
    xB = min(boxA[0] + boxA[2], boxB[0] + boxB[2])
    yB = min(boxA[1] + boxA[3], boxB[1] + boxB[3])
    if xA < xB and yA < yB:
        interArea = (xB - xA) * (yB - yA)
        boxAArea = boxA[2] * boxA[3]
        boxBArea = boxB[2] * boxB[3]
        iou = interArea / float(boxAArea + boxBArea - interArea)
    else:
        iou = 0
    return iou
vitktm_path='VITKT_M2022/longterm/'
mlpLT_path='mlpLT2022/longterm/'
for i in os.listdir('groundtruth2022'): 
        with open(vitktm_path+i+'/'+i+'_001.txt') as f:
            x=f.readlines()
        with open("groundtruth2022/"+i+"groundtruth.txt") as f:
            y=f.readlines()
        with open(vitktm_path+i+'/'+i+'_001_confidence.value') as f:
            z=f.readlines()
        z[0]='1\n'
        y = [j.split(',') for j in y]
        print(y[0])
        vitktm = [j.split(',') for j in x]
        vitktm[0] = y[0] 
        vitktm_scores = [float(k) for k in z]
        gt = [[float(k[0]),float(k[1]),float(k[2]),float(k[3])] if len(k) == 4 else [float('nan'),float('nan'),float('nan'),float('nan')] for k in y]
        vitktm_bb = [[float(k[0]),float(k[1]),float(k[2]),float(k[3])] for k in vitktm]
        with open(mlpLT_path+i+'/'+i+'_001.txt') as f:
            x=f.readlines()
        with open(mlpLT_path+i+'/'+i+'_001_confidence.value') as f:
            z=f.readlines()
        z[0]='1\n'
        mlpLT = [j.split(',') for j in x]
        mlpLT[0] = y[0]
        mlpLT_scores = [float(k) for k in z]
        mlpLT_bb = [[float(k[0]),float(k[1]),float(k[2]),float(k[3])] for k in mlpLT]
		if len(gt) == len(vitktm_scores): 
			acc += len(gt)
			for h in range(0,len(gt)):
				if mlpLT_scores[h] > vitktm_scores[h] and compute_iou(mlpLT_bb[h],gt[h]) > compute_iou(vitktm_bb[h],gt[h]):
					dataset.append([mlpLT_scores[h],vitktm_scores[h],0,i,h])
				elif mlpLT_scores[h] > vitktm_scores[h] and compute_iou(mlpLT_bb[h],gt[h]) < compute_iou(vitktm_bb[h],gt[h]):
					dataset.append([mlpLT_scores[h],vitktm_scores[h],1,i,h])
				elif mlpLT_scores[h] < vitktm_scores[h] and compute_iou(mlpLT_bb[h],gt[h]) < compute_iou(vitktm_bb[h],gt[h]):
					dataset.append([mlpLT_scores[h],vitktm_scores[h],1,i,h])
				elif mlpLT_scores[h] < vitktm_scores[h] and compute_iou(mlpLT_bb[h],gt[h]) > compute_iou(vitktm_bb[h],gt[h]):
					dataset.append([mlpLT_scores[h],vitktm_scores[h],0,i,h])
				elif mlpLT_scores[h] == vitktm_scores[h] and compute_iou(mlpLT_bb[h],gt[h]) > compute_iou(vitktm_bb[h],gt[h]):
					dataset.append([mlpLT_scores[h],vitktm_scores[h],0,i,h])
				elif mlpLT_scores[h] == vitktm_scores[h] and compute_iou(mlpLT_bb[h],gt[h]) < compute_iou(vitktm_bb[h],gt[h]):
					dataset.append([mlpLT_scores[h],vitktm_scores[h],1,i,h])
				elif compute_iou(mlpLT_bb[h],gt[h]) == compute_iou(vitktm_bb[h],gt[h]):	
					dataset.append([mlpLT_scores[h],vitktm_scores[h],1,i,h]) # non capita mai
				else:
					dataset.append([mlpLT_scores[h],vitktm_scores[h],2,i,h])
with open("2022.pkl", "wb") as f: 
    test = pickle.dump(dataset, f)
