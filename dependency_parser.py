from dataParser import *
from basic_features.unigrams import *
from basic_features.bigrams import *
import perceptron as pr


def main():
    dp = DataParser()
    corpus = dp.parse('HW2-files/train.labeled')
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

    fv.generate_features(corpus)
    # fv.fgArr[0].filter_features(5)

    trainer = pr.Perceptron()

    trainer.train(corpus, fv, 30)



if __name__ == '__main__':
    main()
