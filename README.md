## Rock Paper Scissors Image Classification with FastAI

These notebooks contain the code from the medium blog articles from the series: [A Fast Introduction to Fastai-My Experience.](https://towardsdatascience.com/a-fast-introduction-to-fastai-my-experience-b18d4457f6a5?source=your_stories_page-------------------------------------)

Throughout these tutorials, I write about:
- Transfer learning for image classification
- Stochastic Gradient Descent from scratch
- Image clasification the naive way
- Text classification with transfer learning
- Making the frontend of the project easily with streamlit
- Containerizing the app with Docker


The ipynb files are as follows: 
1. **RPC.ipynb**: Simple image classification with fastai library, an introduction
2. **RPC-Pixel-sim.ipynb**: Image classification with Pixel Similarity Approach
3. **RPC SGD.ipynb**: Image classification with Stochastic Gradient Descent and Cross Entropy Loss function
4. **RPC-Learning Rate, Progressive Resizing Approach.ipynb** : Image Classification, state of the art training with learning rate finder, progressing resizing approach.
5. **Text Sentiment Classification(Covid-19 Tweets).ipynb** : Text Classification in just 20 lines of code
6. An interactive web app made with streamlit with the ability to run image classification on any uploaded image. 


**Next up: Contanerising the app with Docker.**


## Streamlit web app
The web app built through streamlit is now live. The code is located in [RockPaperScissorsClassification](https://github.com/yashprakash13/RockPaperScissorsFastAI/tree/main/RockPaperScissorsClassification) folder. 

### Screenshot of the app in action:
![](https://github.com/yashprakash13/RockPaperScissorsFastAI/blob/main/screenshots/Screenshot%202021-02-16%20at%2011.24.57%20AM.png)

## Steps to build and run the Streamlit web app
1. Install [Docker on your machine](https://docker.com).
2. In the root directory of the terminal, run to build the image:
```bash
docker build --tag rps:1.0 .
```
3. Lastly, run the app with: 
```bash
docker run --publish 8501:8501 -it rps:1.0
```
Open your browser and go to http://localhost:8501/.



