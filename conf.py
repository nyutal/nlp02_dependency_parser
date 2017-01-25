import time

class Conf(object):
    test_name='basic_train_filtered'
    train_file_name = 'HW2-files/train.labeled'
    train_max_samples = 0 # less than 1 to represent full samples
    train_niter = 100
    test_file_name = None #'HW2-files/train.labeled'
    test_max_samples = 0 # less than 1 to represent full samples
    weights_src = '/Users/nyutal/dev/nlp02_dependency_parser/results/complex_first/output_basic_train_filtered_20170124_183425_weights_60_iterations.txt'

    output_file_name = 'output_' + test_name + '_' + time.strftime("%Y%m%d_%H%M%S") + '.txt'
    output_weight_file_name = output_file_name[:-4] + '_weights.txt'

    weak_root = True
    is_complex = True

    filter = 0

    def get_conf_str(self):
        d = {}
        d['train_file_name'] = self.train_file_name
        d['train_max_samples'] = self.train_max_samples
        d['train_niter'] = self.train_niter
        d['test_file_name'] = self.test_file_name
        d['test_max_samples'] = self.test_max_samples
        d['weight_src'] = self.weights_src
        d['weak_root'] = self.weak_root
        d['is_complex'] = self.is_complex
        d['filter'] = self.filter
        return str(d)

    def __setattr__(self, *_):
        raise ValueError("don't you dare!")
Conf = Conf()

