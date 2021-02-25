## Rock Paper Scissors Image Classification with FastAI
![](https://img.shields.io/badge/Powered%20by-Python%203.9.1-red?style=for-the-badge)
![](https://img.shields.io/badge/Built%20with-Fastai-brightgreen?style=for-the-badge) ![](https://img.shields.io/badge/-streamlit-orange?style=for-the-badge) ![](https://img.shields.io/badge/-Docker-blue?style=for-the-badge)

An end-to-end deep learning image classifier app built with Fastai and Pytorch.

The notebooks contain the code from the articles from the series: [A Fast Introduction to Fastai-My Experience.](https://towardsdatascience.com/a-fast-introduction-to-fastai-my-experience-b18d4457f6a5?source=your_stories_page-------------------------------------)

### Medium Article Series
This project began with a viral article about my first experience with Fastai. Then it evolved. Troughout these tutorials, I write about:
- [Transfer learning for image classification](https://towardsdatascience.com/a-fast-introduction-to-fastai-my-experience-b18d4457f6a5?source=your_stories_page-------------------------------------)
- [Stochastic Gradient Descent from scratch](https://towardsdatascience.com/fastai-multi-class-classification-with-stochastic-gradient-descent-from-scratch-8410fe3fea22?source=your_stories_page-------------------------------------)
- [Image clasification the naive way](https://towardsdatascience.com/fastai-exploring-the-training-process-the-pixel-similarity-approach-74bbdb844509?source=your_stories_page-------------------------------------)
- [Making a state of the art image classification model with learning Rate Finder and progressive resizing approach for getting the best results in a short amount of time](https://towardsdatascience.com/how-to-make-a-state-of-the-art-model-with-fastai-bd11e168b214?source=your_stories_page-------------------------------------)
- [Text classification with transfer learning](https://towardsdatascience.com/text-classification-in-just-20-lines-of-code-8baf9c2a0a53?source=your_stories_page-------------------------------------)
- [Making the frontend of the project easily with streamlit](https://towardsdatascience.com/a-guide-to-streamlit-frontend-for-data-science-made-simpler-c6dda54e3183?source=your_stories_page-------------------------------------)
- [Containerizing the app with Docker](https://pub.towardsai.net/how-to-dockerize-your-data-science-project-a-quick-guide-b6fa2d6a8ba1?source=your_stories_page-------------------------------------)


### Notebooks and code
The ipynb files are as follows: 
1. **RPC.ipynb**: Simple image classification with fastai library, an introduction
2. **RPC-Pixel-sim.ipynb**: Image classification with Pixel Similarity Approach
3. **RPC SGD.ipynb**: Image classification with Stochastic Gradient Descent and Cross Entropy Loss function
4. **RPC-Learning Rate, Progressive Resizing Approach.ipynb** : Image Classification, state of the art training with learning rate finder, progressing resizing approach.
5. **Text Sentiment Classification(Covid-19 Tweets).ipynb** : Text Classification in just 20 lines of code
6. An interactive web app made with streamlit with the ability to run image classification on any uploaded image. 
7. Contanerising the streamlit app with Docker.


### The streamlit web app
The web app built through streamlit is now live. The code is located in [RockPaperScissorsClassification](https://github.com/yashprakash13/RockPaperScissorsFastAI/tree/main/RockPaperScissorsClassification) folder. 

### Screenshot of the app in action:
![](https://github.com/yashprakash13/RockPaperScissorsFastAI/blob/main/screenshots/Screenshot%202021-02-16%20at%2011.24.57%20AM.png)

### Steps to build and run the Streamlit web app
1. Install [Docker on your machine](https://docker.com).
2. In the root directory of the terminal, run to build the image:
```bash
docker build --tag rps:1.0 .
```
3. Lastly, run the app with: 
```bash
docker run --publish 8501:8501 -it rps:1.0
```
Open your browser and go to http://localhost:8501/ and play with the app!
