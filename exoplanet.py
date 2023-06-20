#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Siddarth Kerkar
Intro to Programming With Data

Date: Tue Oct 11 11:47:34 2022

File: exoplanets.py

Description: Analyze data regarding planets and find the planets
most similar to Earth

Enter a planet name to lookup: Earth
The planet most similar to Earth is TRAPPIST-1 d:
Mass: 0.29690926
Radius: 0.7672418000000001
Period: 0.011088039662448644
Semimajor Axis: 0.02228038
Temperature: 288.0

'''

import matplotlib.pyplot as plt


def read_data(filename):
    '''Reads all exoplanet data and returns each planet and its corresponding data
into a list of lists
filename - chosen filename'''
    all_planets = []
    # Read Data
    with open(filename, 'r') as infile:
        data = infile.readlines()
        for value in data:
            planet = []
            if '#' in value:
                pass
            else:
                # Fix data with no entry
                element = value.strip().split(',')
                planet.append(element[0])
                if element[2] == '':
                    planet.append(float(0))
                else:
                    mass = float(element[2]) * 317.89
                    planet.append(mass)
                if element[3] == '':
                    planet.append(float(0))
                else:
                    radii = float(element[3]) * 10.97
                    planet.append(radii)
                if element[4] == '':
                    planet.append(float(0))
                else:
                    period = float(element[4]) / 365.2422
                    planet.append(period)
                if element[5] == '':
                    planet.append(float(0))
                else:
                    planet.append(float(element[5]))
                if element[11] == '':
                    planet.append(float(0))
                else:
                    planet.append(float(element[11]))
                
                all_planets.append(planet)
    
    return all_planets
            

def lookup_planet(name, data):
    '''Enter in the name of a planet and returns a list of all its data
    name - chosen planet
    data - full dataset'''
    # Use name to find full data list for the planet
    for item in data:
        if name == item[0]:
            return item

def euclidean_distance(planet1, planet2):
    # get change in values
    c_mass = abs(planet1[1] - planet2[1])
    c_radius = abs(planet1[2] - planet2[2])
    c_period = abs(planet1[3] - planet2[3])
    c_sma = abs(planet1[4] - planet2[4])
    c_temp = abs(planet1[5] - planet2[5])

    # Compute
    euclid = ((c_mass**2) + (c_radius**2) + (c_period**2) + (c_sma**2) + 
              (c_temp**2))**(1/2)
     
    return euclid

def find_most_similar_planet(name, dataset):
    '''Enter the name of a planet and returns the planet that is most similar
    to it
    name - chosen planet
    dataset - full data'''
    planet_info = lookup_planet(name, dataset)
    distances = []
    #adj_distances = distances
    
    # Find most similar planet with smallest euclid distance
    for i in dataset:
        distance = euclidean_distance(planet_info, i)
        if distance == 0:
            distances.append(10000000000)
        else:
            distances.append(distance)
    
    #adj_distances.remove(0)
    #no_e_dataset = dataset
    #no_e_dataset.remove(planet_info)
    min_value = min(distances)
    min_index = distances.index(min_value)
    planet_similar = dataset[min_index][0]
    
    return planet_similar
        
def visualize_exoplanets(data):
    '''Plots Mass vs. Semimajor Axis all planets and highlights Earth
    data - the data fr all exoplanets'''
    sma = []
    mass = []
    e_sma = []
    e_mass = []
    
    # Used to check if Earth was in data
    #print(len(data))
    #res1 = any("Earth" in sublist for sublist in data)
    #print(res1)
    for i in data:
        if i[0] == 'Earth':
            e_sma.append(i[4])
            e_mass.append(i[1])
        else:
            sma.append(i[4])
            mass.append(i[1])
    
    # Plot graph
    plt.figure(dpi=500)
    plt.xlabel('Mass')
    plt.ylabel('Semimajor Axis')
    plt.title("Planet's mass v.s. Semimajor Axis", fontweight='bold')
    plt.scatter(x=mass, y=sma, color='blue', marker='.',
                label='Planets')
    plt.scatter(x=e_mass, y=e_sma, color='red', marker='x',
                label='Earth')
    plt.text(e_mass[0], e_sma[0],'Earth')
    plt.xscale('log')
    plt.yscale('log')
    plt.legend()
    plt.savefig('exoplanet.png', bbox_inches='tight')
    plt.show()
    
def generate_planet_report(planet_similar, dataset, chosen_planet):
    '''Details the planet most similar to the chosen planet and its data
    plane_simiar - the planet most similar to chose_planet
    data - full dataset
    return - none'''

    # Print out planets full attributes
    planet_info = lookup_planet(planet_similar, dataset)    
    print(f'The planet most similar to {chosen_planet} is {planet_info[0]}:'), 
    print(f'Mass: {planet_info[1]}'), 
    print(f'Radius: {planet_info[2]}'), print(f'Period: {planet_info[3]}'), 
    print(f'Semimajor Axis: {planet_info[4]}'), 
    print(f'Temperature: {planet_info[5]}')
    
      
    
    
    
def main():
    # Read the data
    planet_info = read_data('exoplanets.csv')
    # Find planet most similar to Earth
    planet_similar = find_most_similar_planet("Earth", planet_info)
    # Plot graph
    visualize_exoplanets(planet_info)
    # Generate planet report
    generate_planet_report(planet_similar, planet_info, "Earth")
   
    

main()
    
