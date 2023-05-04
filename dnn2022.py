from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler  
import pickle

scaler = StandardScaler()

with open("2022.pkl", "rb") as f: 
    X = pickle.load(f)
with open("2021.pkl", "rb") as f: 
    test = pickle.load(f)
scaler.fit(np.array([x[0:2] for x in X]))
y = [x[2] for x in X]
target = [x[2] for x in test]
X = scaler.transform(np.array([x[0:2] for x in X]))
clf = MLPClassifier(solver='lbfgs', max_iter=5000,alpha=1e-4,hidden_layer_sizes=(3,2), random_state=2)
clf.fit(X,y)
results = clf.predict(scaler.transform(np.array([t[0:2] for t in test])))
print('accuracy:',sum(results==target))
with open("scaler2022.pkl", "wb") as f: 
    pickle.dump(scaler, f)
with open("dnn2022.pkl", "wb") as f: 
    pickle.dump(clf, f)
with open("dnn2022results.pkl", "wb") as f: 
    pickle.dump(results, f)

r=0
results_dir='lsdoltts2022dnn/mlpLT/longterm/'
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
				
