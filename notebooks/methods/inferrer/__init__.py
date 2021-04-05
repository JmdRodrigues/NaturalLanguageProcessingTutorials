import os
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'logs'))


from methods.inferrer.inferrer import Learner
from methods.inferrer import utils
from methods.inferrer import automaton
from methods.inferrer import algorithms
from methods.inferrer import oracle
