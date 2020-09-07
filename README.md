# Computer-Vision

Bees vs Wasps
Synopsis
Hand-curated, close-up photos of bees, wasps, and other insects. The challenge is primarily to distinguish bees from wasps.

Credits
This image dataset collates and refines upon several sources:

"PollenDataset" by 2017 Ivan Rodriguez, Rémi Mégret, Edgar Acuña, José Agosto, Tugrul Giray, from https://www.kaggle.com/ivanfel/honey-bee-pollen

https://www.kaggle.com/tegwyntwmffat/european-wasp-vespula-vulgaris-kitti-format/ - there isn't any better description

Flicker search for bee, wasp and fly

The photos have been hand-curated by the expert biologist, Callum Robertson https://www.linkedin.com/in/callum-robertson-358014109/

Collator and Kaggle competitor: George Rey https://www.linkedin.com/in/dr-george-rey-dziewierz/

Contributions:

Ivan Rodriguez, Rémi Mégret, Edgar Acuña, José Agosto, Tugrul Giray. Recognition of pollen-bearing bees from Video using Convolutional Neural Network, IEEE Winter Conf. on Applications of Computer Vision, 2018, Lake Tahoe, NV. https://doi.org/10.1109/WACV.2018.00041

Inspiration
Some notes:

The data is probably biased:
Most bees are photographed on a flower, while most wasps are not. Your AI might learn to recognize the existence of a flower rather than existence of a bee.existence of a bee. You might want to test it against some "empty flowers" to verify.
