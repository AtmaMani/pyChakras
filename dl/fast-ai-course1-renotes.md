## Genearl notes
1. image dimensions 224
2. normalizing images (mean 0, 1 SD) prior to training

3. data.c -> gives number of classes. data.classes -> gives the names of the classes.

4. we use transfer learning. We pick a model that already knows something about images and tune it to our case study.


## Workflow
1. download data into local directory
2. import data files into a `data_bunch`. This process automatically creates a validation set.
3. normalize
4. run `show_batch` to see the classes and labels
5. print the number of classes
6. create a `ConvLearner` object by passing the data bunch, specifying the model architecture and metrics to use to evaluate training stats
7. Fit the model. You can use `fit` or `fit_one_cycle` methods, but recommended is to use latter. Pass the epoch number (also called `cycles`)
8. look at the results and if good, save by calling `learn.save('filename')`
9. Validation - create an `interpreter` object using `ClassificationInterpretation.from_learner(learn)`. The learn object so far knows the data and the model used to train. Now its time to validate
10. Find the biggest losses using `interp.plot_top_losses(9, figsize=(15,11))`. You can also plot `interp.plot_confusion_matrix()` to view the CF matrix. Fastai also has `interp.most_confused(min_val=2)` which will return the top losses.

### Making model better
1. Generally, when you call `fit_one_cycle` it only trains the last or last few layers. To improve this better, you need to call `learn.unfreeze()` to unfreeze the model.

Next, you repeat the `learn.fit_one_cycle(numepochs)`. Sometimes, the error goes up when doing this. This happens because you have a reckless learning rate which makes the model lose it original learning. We need to be more nuanced here.

3. Find the optimal learning rate: Now load the original model using `learn.load('stage-1')`, then run `learn.lr_find()` and find the highest learning rate that has the lowest loss.

4. With this new information retrain the model. `learn.unfreeze(); learn.fit_one_cycle(epochs=2, max_lr=slice(1e-6, 1e-4))`. What the slice suggests is, train the initial layers at start value specified and last layer at the end value specified and interpolate for the rest of the layers. It is tradecraft to make the end learning rate about 10 times smaller than rate at which errors start to increase.


GPU RAM: have a minimum GPU memory at 8. Higher is better. For models like `resnet50`, you need `16GB` GPU RAM.


Example projects
----------------
1. classify micro usb, type c, lightning cable
2. 