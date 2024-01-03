# Neural Car Simulation

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

## Overview

Welcome to the Neural Car Simulation project! 🚗💨 This is a simple yet creative implementation of a neural network controlling a car to navigate through a map. The project uses the NEAT (NeuroEvolution of Augmenting Topologies) algorithm.

## How It Works

The simulation involves cars with neural networks as their brains. These networks learn to drive by evolving over generations. The cars make decisions (left, right, slow down, speed up) based on their neural network's output, and the best-performing genomes are selected for the next generation.

## Features

- Neural network-controlled cars
- Evolutionary learning using NEAT algorithm
- Simple map environment
- Real-time visualization of the simulation

## Getting Started

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/ffathy-tdx/pygame-neat-car.git
   cd pygame-neat-car

2. **Install Dependancies:**
   ```bash
   pip install -r requirements.txt

3. **Run the Simulation:**
   ```bash
   python newcar.py
   
   
**Saving the Best Performing Model**

During the simulation, the script saves the best-performing genome in a file named best_genome.pkl. This file contains the weights and information needed to reproduce the neural network of the most successful car. You can find this file in the project directory.

**Customize and Contribute**

Feel free to experiment and tweak the parameters in the config.txt file to see how it affects the learning process. If you have ideas for improvements, create a fork, make changes, and submit a pull request.

License
This project is licensed under the MIT License.

Happy Coding!
