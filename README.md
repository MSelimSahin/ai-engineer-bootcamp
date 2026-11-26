<div align="center">

# AI Engineer Bootcamp

From-scratch machine learning in pure Python.

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![pytest](https://img.shields.io/badge/pytest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)

</div>

## About The Project

- **Purpose**: A hands-on bootcamp where I build core machine learning tools from scratch in pure Python (no NumPy or scikit-learn) to understand how they work under the hood. Every module is tested with pytest.
- **Why coding from scratch?**: To understand what's going on behind the scenes of everything.

## Highlights

- [Nearest Centroid Classifier from scratch](day06/classifier.py): 96.67% test accuracy on the Iris dataset, no ML libraries.
- [Gradient descent + learning rate experiments](day03/gradient_descent.py): Gradient descent from scratch. Converges in 77 steps at lr=0.1, oscillates at lr=1.0 and diverges at lr=1.1.
- [Precision/recall/F1 evaluator](day02/model_evaluator.py): Precision, recall, F1 score from scratch.
- [Matrix multiplication + Transpose](day05/exercises.py): Pure-Python matrix multiplication and transpose.
- [pytest test suite](tests/)
- [Cross-validation](day08/arena.py): Compared nearest centroid vs. k-NN with leave-one-out cross-validation.

## Project Structure

- **day01**: Python basics: variables, strings, input, f-strings.
- **day02**: Make model evaluator with precision, recall and F1.
- **day03**: Make gradient descent from scratch and experiment with learning rates.
- **day04**: Create ML Toolkit. Including gradient descent, dot, F1 score, accuracy, precision, recall and make tests for the first time.
- **day05**: Split iris dataset into train, test datasets and fit the model.
- **day06**: Turn functions into NearestCentroidClassifier class and practice with exceptions.
- **day07**: Use pytest instead of assert statements and test the code.

## How To Run

```bash
python -m venv .venv
.venv\Scripts\Activate.ps1        # Windows
source .venv/bin/activate         # macOS / Linux
pip install -r requirements.txt
python -m day06.classifier
python -m pytest
```

## Built With

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![pytest](https://img.shields.io/badge/pytest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)
