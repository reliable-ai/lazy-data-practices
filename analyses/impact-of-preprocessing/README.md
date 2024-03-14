# Analysis of the Impact of Preprocessing Choices on Algorithmic Fairness and Performance

## Setup

To install dependendencies for the analysis you will need to have Python 3.9 installed on your system and the `pipenv` package. Then, you can run the following command to install the necessary python packages and create a virtual environment:

```bash
pipenv sync -d
```

After installation, you can activate the virtual environment by running:

```bash
pipenv shell
```

## Running the Analysis

To run the analysis, execute the jupyter notebook `bank-analysis.ipynb`. This can either be done either in a graphical interface via e.g. Visual Studio Code or Jupyter Notebook or by executing the notebook directly through running the following command in the terminal (after activating the environment via `pipenv shell`):

```bash
jupyter notebook bank-analysis.ipynb
```

The results of the analysis will be saved in `bank-analysis-results.csv`. Generated datasets will be stored under `generated_data/`.
