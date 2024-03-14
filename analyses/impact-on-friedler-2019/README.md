# Analysis of the Impact of Preprocessing Choices on Friedler et al. (2019)

This directory is based off the official code base of the paper "A comparative study of fairness-enhancing interventions in machine learning". The original code base can be found at https://github.com/algofairness/fairness-comparison.

We performed the following changes:

1. We wrote a Dockerfile to reproduce the environment used to run the original code, as the original code base does not work with modern versions of Python or the associated packages.
2. Created a new analysis script `run.py` which uses differently pre-processed versions of the Bank Dataset to compare the impact of preprocessing choices on the results of the original paper. The versions of the Bank Dataset are based upon the other analysis in this repository, which can be found at [analyses/impact-of-preprocessing](../impact-of-preprocessing/).

## Build the Docker Image

To build the Docker image yourself, run the following command in the root directory of this repository:

```bash
docker build -t fairness-comparison .
```

To run the just built Docker image, run the following command:

```bash
docker run -it fairness-comparison
```

# Original README

This repository is meant to facilitate the benchmarking of fairness aware machine learning algorithms.

The associated paper is:

A comparative study of fairness-enhancing interventions in machine learning by Sorelle A. Friedler, Carlos Scheidegger, Suresh Venkatasubramanian, Sonam Choudhary, Evan P. Hamilton, and Derek Roth. https://arxiv.org/abs/1802.04422

To install this software run:

    $ pip3 install fairness

The below instructions are still in the process of being updated to work with the new pip install-able version.

To run the benchmarks:

    $ from fairness.benchmark import run
    $ run()

This will write out metrics for each dataset to the results/ directory.

To generate graphs and other analysis run:

    $ python3 analysis.py

If you do not yet have all the packages installed, you may need to run:

    $ pip install -r requirements.txt

*Optional*:  The benchmarks rely on preprocessed versions of the datasets that have been included
in the repository.  If you would like to regenerate this preprocessing, run the below command
before running the benchmark script:

    $ python3 preprocess.py

To add new datasets or algorithms, see the instructions in the readme files in those directories.

## OS-specific things

### On Ubuntu

(We tested on Ubuntu 16.04, your mileage may vary)

You'll need `python3-dev`:

    $ sudo apt-get install python3-dev


### Additional analysis-specific requirements

To regenerate figures (this is messy right now. we're working on it)

Python requirements (use pip):

* `ggplot`

System requirements:

* `pandoc`  (`brew install pandoc` on a Mac or `apt-get install pandoc` on Linux)
* R  (Mac download link: https://cran.rstudio.com/bin/macosx/R-3.4.3.pkg)

R package requirements (use `install.packages`):

* `rmarkdown`
* `stringr`
* `ggplot2`
* `dplyr`
* `magrittr`
* `corrplot`
* `robust`
