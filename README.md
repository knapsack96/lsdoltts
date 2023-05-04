# lsdoltts
Learning Spatial Distribution of Long-Term Trackers Scores
To launch the experiments contained in the reference paper "Learning Spatial distribution of Long Term Trackers scores", you must perform the following steps:

1) Produce the results of the mlpLT and VITKT_M trackers, respectively, by running the codes published on VOT Challenge website, or proceed to step 2 otherwise.
2) To create the dataset from the VOT-LT2021 data, run the '2021.py' script, after installing scikit-learn and fuzzy-c-means via pip. Similarly for VOT-LT2022 with '2022.py'. The results of the works have already been stored in the repository for simplicity, in the folders mlpLT2021, mlpLT2022, VITKT_M2021 and VITKT_M2022.
3) To repeat the experiments contained in the paper, you need to perform step 2, after which you can run one of the 4 scripts 'dnn2021.py', 'dnn2022.py', 'fcm2021.py' and 'fcm2022.py'. The scripts correspond respectively to the training experiments on DNN with 2021 data and 2022 tests, then with 2022 and 2021 test data, then FCM with 2021 and 2022 test data, and finally with 2022 and 2021 test data.
4) In step 3, the results are also generated in the folders starting with 'lsdoltts..' with a suffix corresponding to the respective experiment. By copying the contents of one of the folders in the 'mlpLT' code, in particular in the 'results' subfolder, and performing the analysis step provided by the VOT protocol and described by the mlpLT guide, the values presented in the paper are obtained.
5) For any issue, do not esitate to contact the authors in private, to the following mails: vincenzo.scarrica@gmail.com or vincenzomariano.scarrica001@studenti.uniparthenope.it. Otherwise, open an issue in the corresponding git section.
