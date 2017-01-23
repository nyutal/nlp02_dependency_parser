from dataParser import *
from basic_features.unigrams import *
from basic_features.bigrams import *
import perceptron as pr
from conf import Conf
import time


def main():

    out_file = open(Conf.output_file_name, 'w')
    out_weight_file = open(Conf.output_weight_file_name, 'w')

    dp = DataParser()
    train_corpus = dp.parse(Conf.train_file_name, Conf.train_max_samples)

    fv = FeatureVec()
    fv.add_feature_gen(F1())
    fv.add_feature_gen(F2())
    fv.add_feature_gen(F3())
    fv.add_feature_gen(F4())
    fv.add_feature_gen(F5())
    fv.add_feature_gen(F6())
    fv.add_feature_gen(F7())
    fv.add_feature_gen(F8())
    fv.add_feature_gen(F9())
    fv.add_feature_gen(F10())
    fv.add_feature_gen(F11())
    fv.add_feature_gen(F12())
    fv.add_feature_gen(F13())

    fv.generate_features(train_corpus)
    # fv.fgArr[0].filter_features(5)


    ##### training #######
    out_file.write('start training at ' + time.asctime())

    trainer = pr.Perceptron()
    weights = trainer.train(train_corpus, fv, Conf.train_niter)

    out_file.write('finish training at ' + time.asctime())
    ####################

    test_corpus = dp.parse(Conf.test_file_name, Conf.test_max_samples)

    ##### testing #######
    out_file.write('start testing at ' + time.asctime())

    accuracy = trainer.test(test_corpus, fv, weights)

    out_file.write('finish testing at ' + time.asctime())
    ####################




    out_file.write(Conf.get_conf_str() + "\n")
    out_file.write(str(fv.get_feature_gen_count()) + "\n")

    out_weight_file.write(str(weights.tostring()))
    out_file.write('accuracy=' + str(accuracy) + "\n")





if __name__ == '__main__':
    main()
