from fcmeans import FCM
import pickle
with open("2022.pkl", "rb") as f: 
    X = pickle.load(f)
with open("2021.pkl", "rb") as f: 
    test = pickle.load(f)
X = np.array([x[0:2] for x in X])
y = [x[2] for x in X]
max_acc = 0
max_swap = 0

fcm = FCM(n_clusters=3,m=2) 
fcm.fit(X)
target = [x[2] for x in test]
label = fcm.predict(np.array([t[0:2] for t in test]))
acc = sum(label==target)
if acc > max_acc:
	with open("fcm2022.pkl", "wb") as f: 
		pickle.dump(fcm, f)
	with open("fcm2022results.pkl", "wb") as f: 
		pickle.dump(label, f) 
	max_acc = acc
	max_swap = 0
	print('salvo:',i,acc, max_swap) 
acc = 0
a = label
a = [3 if b == 2 else b for b in a]
a = [2 if b == 0 else b for b in a]
a = [0 if b == 3 else b for b in a]
acc = sum(np.asarray(a)==target)
if acc > max_acc:
	with open("fcm2022.pkl", "wb") as f: 
		pickle.dump(fcm, f)
	with open("fcm2022results.pkl", "wb") as f: 
		pickle.dump(np.asarray(a), f) 
	max_acc = acc
	max_swap = 1
	print('salvo:',i,acc, max_swap) 
a = label
a = [3 if b == 1 else b for b in a]
a = [1 if b == 0 else b for b in a]
a = [0 if b == 3 else b for b in a]
acc = sum(np.asarray(a)==target)
if acc > max_acc:
	with open("fcm2022.pkl", "wb") as f: 
		pickle.dump(fcm, f)
	with open("fcm2022results.pkl", "wb") as f: 
		pickle.dump(np.asarray(a), f) 
	max_acc = acc
	max_swap = 2
	print('salvo:',i,acc, max_swap) 

a = label
a = [3 if b == 2 else b for b in a]
a = [2 if b == 1 else b for b in a]
a = [1 if b == 3 else b for b in a]


acc = sum(np.asarray(a)==target)
if acc > max_acc:
	with open("fcm2022.pkl", "wb") as f: 
		pickle.dump(fcm, f)
	with open("fcm2022results.pkl", "wb") as f: 
		pickle.dump(np.asarray(a), f) 
	max_acc = acc
	max_swap = 3
	print('salvo:',i,acc,max_swap) 
	
a = label
a = [3 if b == 1 else b for b in a]
a = [1 if b == 0 else b for b in a]
a = [0 if b == 3 else b for b in a]
a = [3 if b == 2 else b for b in a]
a = [2 if b == 0 else b for b in a]
a = [0 if b == 3 else b for b in a]

acc = sum(np.asarray(a)==target)
if acc > max_acc:
	with open("fcm2022.pkl", "wb") as f: 
		pickle.dump(fcm, f)
	with open("fcm2022results.pkl", "wb") as f: 
		pickle.dump(np.asarray(a), f) 
	max_acc = acc
	max_swap = 3
	print('salvo:',i,acc,max_swap) #51,8%

a = label
a = [3 if b == 2 else b for b in a]
a = [2 if b == 1 else b for b in a]
a = [1 if b == 3 else b for b in a]
a = [3 if b == 2 else b for b in a]
a = [2 if b == 0 else b for b in a]
a = [0 if b == 3 else b for b in a]

acc = sum(np.asarray(a)==target)
if acc > max_acc:
	with open("fcm2022.pkl", "wb") as f: 
		pickle.dump(fcm, f)
	with open("fcm2022results.pkl", "wb") as f: 
		pickle.dump(np.asarray(a), f)  
	max_acc = acc
	max_swap = 3
	print('salvo:',i,acc,max_swap)
with open("fcm2022results.pkl", "rb") as f: 
    results = pickle.load(f)
r=0
results_dir='lsdoltts2022fcm/mlpLT/longterm/'
for i in os.listdir('groundtruth2022'): 
	with open("groundtruth2022/"+i+"/groundtruth.txt") as f:
		y=f.readlines()
	with open(results_dir + i+'/'+i+'_001.txt','w+') as f:
		f.write('1\n')
	r += 1
	with open(results_dir + i+'/'+i+'_001.txt','a') as f:
		for h in range(1,len(y)):
			if results[r] == 0:
			
				f.write(str(vitktm_bb[h][0])+','+str(vitktm_bb[h][1])+','+str(vitktm_bb[h][2])+','+str(vitktm_bb[h][3])+'\n')        
			elif results[r] == 1:
			
				f.write(str(mlpLT_bb[h][0])+','+str(mlpLT_bb[h][1])+','+str(mlpLT_bb[h][2])+','+str(mlpLT_bb[h][3])+'\n')   
			else:
			#out of view
				f.write(str(vitktm_bb[h][0])+','+str(vitktm_bb[h][1])+','+str(vitktm_bb[h][2])+','+str(vitktm_bb[h][3])+'\n')  
				