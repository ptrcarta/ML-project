from models.AbstractModel import AbstractModel

import tensorflow as tf

import models.cifar10.cifar10_training as cifar10_training
import models.cifar10.cifar10_evaluating as cifar10_evaluating
import models.cifar10.cifar10_nn as cifar10_nn


class cifar10_model(AbstractModel):

    def __download_and_check_dir(self, path):
        # If not already done, download and extract locally the dataset
        cifar10_nn.maybe_download_and_extract()

        # Make directory to write events logs and checkpoints
        if tf.gfile.Exists(path):
            tf.gfile.DeleteRecursively(path)
        tf.gfile.MakeDirs(path)

    def train(self, path):
        """Train the naive model (without fingerprints)"""
        self.__download_and_check_dir(path)
        cifar10_training.train(path)

    def evaluate(self):
        """Evaluate the naive trained model (without fingerprints)"""
        cifar10_evaluating.evaluate()
