from __future__ import print_function

from genomic_neuralnet.config import SINGLE_CORE_BACKEND, JOBLIB_BACKEND
from genomic_neuralnet.analyses import run_optimization, HIDDEN, DROPOUT, EPOCHS, BATCH_SIZE
from genomic_neuralnet.methods import get_net_prediction
from genomic_neuralnet.util import get_is_on_gpu

def main():
    params = { 'hidden': HIDDEN 
             , 'dropout_prob': DROPOUT 
             , 'batch_size': (BATCH_SIZE,)
             , 'epochs': (EPOCHS,)
             }

    backend = JOBLIB_BACKEND
    if get_is_on_gpu():
        backend = SINGLE_CORE_BACKEND

    run_optimization(get_net_prediction, params, 'optimal_donn.shelf', 'NDO', backend=backend)

if __name__ == '__main__':
    main()
