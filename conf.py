class Conf(object):
    train_file_name = 'HW2-files/train.labeled'
    train_max_samples = 1000 # less than 1 to represent full samples
    train_niter = 10
    test_file_name = 'HW2-files/train.labeled'
    test_max_samples = 10 # less than 1 to represent full samples
    comp_file_name = 'comp.words'
    parallel = True
    num_of_learners = 4
    num_of_viterbers = 1
    train = True
    isValidate = False
    testName = 'final_m2_comp'

    def __setattr__(self, *_):
        raise ValueError("don't you dare!")
Conf = Conf()
