from vocab import Vocabulary
import os
os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"
import evaluation
evaluation.evalrank('./runs/f30k_vse++/model_best.pth.tar', data_path='./data', split='test')