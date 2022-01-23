# Automatic Music Generation Deep Learning Algorithms

Author: Alex Nguyen | Gettysburg College

`(Introduction to be written)`

## Requirements:
1. System: Window, Linux, and Mac.
2. Dataset:
  * Bach's Chorale: http://www-ens.iro.umontreal.ca/~boulanni/icml2012
3. Know the benchhmark: [https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0173392](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0173392)
4. VS Code (in order to run the jupyter notebook with python file: VS Code format)
5. [Anaconda](https://docs.anaconda.com/anaconda/install/index.html): The python environment (for systematic code execution)

## Project structure
* `docs`: Containing images for documentation
* `amg`: The core libraries for model training and evaluating
  * `__init__.py`: Package initialization
  * `const.py`: Constant for the library 
  * `loss.py`: Loss functions for the deep learning model
  * `model.py`: Deep learning models
  * `utils.py`: Utilization methods
* `main.py`:
* `requirements.txt`: Dependency file

## How to run the project

* First, install the required libraries: 
  ```
  conda create -n amg pip python=3.8
  conda activate amg
  pip install -r requirements.txt
  ```
* Next, go into one python file `main.py` and experiment with the VS Code notebook.

## Reports:

## References:
1. Midi file Structure:
  * Overall Structure: http://www.ccarh.org/courses/253/handout/smf/
  * Detailed Structure: http://www.music.mcgill.ca/~ich/classes/mumt306/StandardMIDIfileformat.html
2. Technical Work with Mido:
  * Mido docs: https://mido.readthedocs.io/en/latest/index.html
  * Mido Tutorial: https://www.twilio.com/blog/working-with-midi-data-in-python-using-mido
3. Sound font for playing midi file (and demo midi file): http://www.schristiancollins.com/generaluser.php
4. Demo midi files: 