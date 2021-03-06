#!/usr/bin/env python
from submission_Det import model as baseDet
from sklearn.metrics import roc_auc_score

img_dir = "./val/baselin_image"
json_file = './val/text.json'


# load detection model
print('loading baseline detection model...')
detModel = baseDet.Model()

print('Detecting images ...')
img_names, prediction = detModel.run(img_dir, json_file)
assert isinstance(prediction, list)
assert isinstance(img_names, list)

labels =  [0]*5 + [1]*1000
score = roc_auc_score(labels, prediction)
print('AUC score is %f' % score)
