import pickle
import neat

def load_weights(filename):
    with open(filename, "rb") as file:
        weights = pickle.load(file)
    
    config_path = "./config.txt"
    config = neat.config.Config(neat.DefaultGenome,
                                neat.DefaultReproduction,
                                neat.DefaultSpeciesSet,
                                neat.DefaultStagnation,
                                config_path)
    
    # Create a minimal genome and add the connections with loaded weights
    genome = neat.DefaultGenome(0)
    for i, weight in enumerate(weights):
        genome.connections[i] = neat.Connection(0, 0, weight, True)
    
    # Create a neural network from the genome
    network = neat.nn.FeedForwardNetwork.create(genome, config)
    
    return network
