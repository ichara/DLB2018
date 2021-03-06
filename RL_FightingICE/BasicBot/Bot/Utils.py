# -*- coding: utf-8 -*-

import os
from .Config import timer


def make_csv_logger(path, log_file_):
    # log performance to csv file
    with open(os.path.join(path, log_file_), 'wt') as f:
        f.write('epoch,time,test-score,train-score,loss,q_value,epsilon\n')

    def func_write_to_csv(epoch_, start_time_, testing_score_, training_score_, losses_, q_values_, epsilon_):
        with open(os.path.join(path, log_file_), 'at') as f:
            f.write('{},{},{},{},{},{},{}\n'.format(
                epoch_, timer() - start_time_,
                testing_score_.mean(), training_score_.mean(), losses_.mean(), q_values_.mean(), epsilon_))

    return func_write_to_csv
