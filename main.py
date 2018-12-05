from api.NeuralFingerprinting import NeuralFingerprinting


model = NeuralFingerprinting("cifar10")

model.train_without_fingerprints("/tmp/cifar10/")

# model.evaluate_without_fingerprints()
