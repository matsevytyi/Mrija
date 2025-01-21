# Student Professional Orientational Tool

This project aims to **provide career guidance** using artificial intelligence techniques. 

It utilises **Transformers**, **FAISS** and **Neural Collaborative Filtering** to efficiently process both single-answer and plaintext answers, taking in account user's answers both on predefined psychological questions as well as his study and hobby interests.

Initially it was started by _**Andrii Matsevytyi**_ and _**Artem Kornienko**_ as a Team TOVSTOLOBKN on the "AI in Mriya" hackathon. In the first version it used Google Forms with predefined questions, sourced from various research studies and a custom Feedforward Neural Network (FFN) to calculate RIASEC score, and then find the most compatible job positions.

Now we work on deploying the engine as a chatbot to make it easily accessible and reproducible as well as to increase user engagement and provide better personalisation.

## Features

**Implemented:**
- user test answers processing pipeline
- user plaintext answers processing pipeline
- psychotype evaluation based on predefined single-answer test questions
- psychotype modification based on user plaintext answers
- user feedback automated post-processing (to be used in automatical engine updates)

**In progress:**
- user feedback collection and processing pipeline
- chatbot integration
- chatbot deployment
  

Suggest us more features in **Issues** section, or feel free to implement them and make a pull request


## Links

- **matsevytyi**'s linkedin: https://www.linkedin.com/in/andrii-matsevytyi/
- **madam6**'s linkedin: https://www.linkedin.com/in/artem-korn11enko/
- initial Google Form: https://forms.gle/rbfjBneQG8V6XPwY8
- **support us so we can work on our projects without applying to another work**

## Acknowledgments

We acknowledge the contributions of the following sources from which we sourced questions for career prediction:

- Career Prediction System: https://github.com/hrugved06/Career-Prediction-System
- How Transformers Work by 3Blue1Brown: https://www.youtube.com/watch?v=wjZofJX0v4M
- Neural Collaborative Filtering paper: https://arxiv.org/pdf/1708.05031
- My Next Move: https://www.mynextmove.org/explore/ip
- OSF: https://osf.io/27rbh/
- Predict My Career: https://www.kaggle.com/code/umangaggarwal/predict-my-career

This project, developed by Team TOVSTOLOBKN during the "AI in Mriya" hackathon, aims to provide career guidance using artificial intelligence techniques. Utilizing a custom Feedforward Neural Network (FFN), it calculates RIASEC scores based on predefined questions sourced from various research studies (refer to the Acknowledgments section for details).

# Instruction to launch the project 
Initial version only, current solution is being integrated and deployed

## Dependencies

```bash
pip install gspread oauth2client pandas scikit-learn torch
```

## How to run?

To initiate the project, begin by installing the necessary dependencies and cloning the repository. Additionally, you must configure your own Google Spreadsheet API key. Store your credentials.json file in a convenient location. Ensure that you update the path to the credentials within the Python notebook accordingly.

```python
credentials_path = '../YourCredentialsPAth.json'
```
Once set up, fill out the [Google Form](https://forms.gle/rbfjBneQG8V6XPwY8) and execute the notebook to obtain results. An example of the results is shown below:

![Sample Results](https://github.com/matsevytyi/Mrija_hackaton/assets/118827294/d5a4d618-e7f3-4451-b5f3-b2a728a3db96)
