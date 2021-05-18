# Honey Bee pollen

Bees vs Wasps

Synopsis

Hand-curated, close-up photos of bees, wasps, and other insects. The challenge is primarily to distinguish bees from wasps.

Credits

This image dataset collates and refines upon several sources:
"PollenDataset" by 2017 Ivan Rodriguez, Rémi Mégret, Edgar Acuña, José Agosto, Tugrul Giray, from https://www.kaggle.com/ivanfel/honey-bee-pollen
https://www.kaggle.com/tegwyntwmffat/european-wasp-vespula-vulgaris-kitti-format/ - there isn't any better description

Flicker search for bee, wasp and fly.

The photos have been hand-curated by the expert biologist, Callum Robertson https://www.linkedin.com/in/callum-robertson-358014109/
Collator and Kaggle competitor: George Rey https://www.linkedin.com/in/dr-george-rey-dziewierz/

Contributions:

Ivan Rodriguez, Rémi Mégret, Edgar Acuña, José Agosto, Tugrul Giray. Recognition of pollen-bearing bees from Video using Convolutional Neural Network, IEEE Winter Conf. on Applications of Computer Vision, 2018, Lake Tahoe, NV. https://doi.org/10.1109/WACV.2018.00041.

Convnets are the best type of machine-learning models for computer-vision tasks. It’s possible to train one from scratch even on a very small dataset,with decent results.

On a small dataset, overfitting will be the main issue.

Data augmentation is a powerful way to fight overfitting when we’re working with image data.
It’s easy to reuse an existing convnet on a new dataset via feature extraction. This is a valuable technique for working with small image datasets.
As a complement to feature extraction, we can use fine-tuning, which adapts to a new problem some of the representations previously learned by an existing model. This pushes performance a bit further.
