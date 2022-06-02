# Dataket at Rest-Mex 2022 😎

<p align="center">
    <img src="https://i.imgur.com/jGDtYFc.png" width = "400px"/>
</p>

All the code created for our participation in the [Rest-Mex 2022 Conference](https://sites.google.com/cicese.edu.mx/rest-mex-2022/home?authuser=0) is available at this GitHub Repository.

## Authors.

- Gabriel Missael Barco.
- Gil Estéfano Rodríguez Rivera.
- Delia Irazú Hernández Farías.

## Abstract.

We participated in the sentiment analysis track, classifying tourism reviews into two domains: the polarity measured by the number of stars assigned in the review (from 1 to 5) and the type of attraction being reviewed (namely Hotel, Restaurant, or Attractive).
For doing this, the conference organizers provided us with a labeled data-set. Given that the data-set was imbalanced, we extracted data from the [Yelp Open Dataset](https://www.yelp.com/dataset) to balance the data-set and performed translation from English to Spanish.

We used a pre-trained BERT model for the polarity sub-task ([_nlptown/bert-base-multilingual-uncased-sentiment_](https://huggingface.co/nlptown/bert-base-multilingual-uncased-sentiment)), and we fine tuned the model on the data. Our model excelled in classifying the low stars reviews (1 and 2) because of the data augmentation for balancing. We used a bag-of-words model with a classification head using different machine learning algorithms for the attraction type sub-task. We obtained good results in this sub-task while keeping the computational cost lower than if we were using a BERT-based model for this sub-task.


**Disclaimer**. 
The notebooks available in this repository are not meant to be executed; they are meant to be read-only, as a reference. The train data and the test data are not available in this repository.

## Conference notes.

In progress...

## Gallery.

Data augmentation:
<p align="center">
    <img src="images/Augmented dataset.png" width="500" />
</p>

Model evaluation for polarity sub-task:
<p align="center">
    <img src="images/Model before and after finetunning.png" width="500" />
</p>

Second approach for the polarity sub-task:
<p align="center">
    <img src="images/Try2 Architecture.png" width="500" />
</p>
