#Student Professional Orientational Tool

This project, developed by Team TOVSTOLOBKN during the "AI in Mriya" hackathon, aims to provide career guidance using artificial intelligence techniques. Utilizing a custom Feedforward Neural Network (FFN), it calculates RIASEC scores based on predefined questions sourced from various research studies (refer to the Acknowledgments section for details).

## Links

- Google Form: https://forms.gle/rbfjBneQG8V6XPwY8

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

## Acknowledgments

We acknowledge the contributions of the following sources from which we sourced questions for career prediction:

- Career Prediction System: https://github.com/hrugved06/Career-Prediction-System
- My Next Move: https://www.mynextmove.org/explore/ip
- OSF: https://osf.io/27rbh/
- Predict My Career: https://www.kaggle.com/code/umangaggarwal/predict-my-career
