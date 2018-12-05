from models.cifar10.cifar10_model import cifar10_model


class NeuralFingerprinting:

    def __init__(self, model):

        if not isinstance("hello", str):
            raise ValueError("model must be a string")
        if model not in ['cifar10']:
            raise ValueError("model must be 'cifar10'")

        #  The code is defined in such way since in the future there
        #  will be more than one model

        if model == 'cifar10':
            self.model = cifar10_model()
            self.path = '/tmp/cifar10_train'

    def train_without_fingerprints(self, path):
        self.model.train(path)

    def evaluate_without_fingerprints(self):
        self.model.evaluate()
