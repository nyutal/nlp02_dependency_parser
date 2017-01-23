import time

class Conf(object):
    test_name='basic_train_20'
    train_file_name = 'HW2-files/train.labeled'
    train_max_samples = 100 # less than 1 to represent full samples
    train_niter = 20
    test_file_name = 'HW2-files/test.labeled'
    test_max_samples = 10 # less than 1 to represent full samples
    weights_src = None

    output_file_name = 'output_' + test_name + '_' + time.strftime("%Y%m%d_%H%M%S") + '.txt'
    output_weight_file_name = output_file_name[:-4] + '_weights.txt'

    comp_file_name = 'comp.words'
    parallel = True
    num_of_learners = 4
    num_of_viterbers = 1
    train = True
    isValidate = False
    testName = 'final_m2_comp'

    def get_conf_str(self):
        d = {}
        d['train_file_name'] = self.train_file_name
        d['train_max_samples'] = self.train_max_samples
        d['train_niter'] = self.train_niter
        d['test_file_name'] = self.test_file_name
        d['test_max_samples'] = self.test_max_samples
        d['weight_src'] = self.weights_src
        return str(d)

    def __setattr__(self, *_):
        raise ValueError("don't you dare!")
Conf = Conf()
