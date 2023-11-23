import numpy as np
import matplotlib.pyplot as plt

# Class representing celestial bodies
class CelestialBody:
    def __init__(self, mass, position, velocity):
        self.mass = mass
        self.position = np.array(position, dtype=float)
        self.velocity = np.array(velocity, dtype=float)
        self.acceleration = np.zeros_like(self.position)

# Function to calculate gravitational force between two bodies
def calculate_force(body1, body2, G):
    r = body2.position - body1.position
    r_squared = np.sum(r ** 2)
    force_magnitude = G * body1.mass * body2.mass / r_squared
    force = force_magnitude * r / np.sqrt(r_squared)
    return force

# Function to update accelerations of all bodies
def update_acceleration(bodies, G):
    num_bodies = len(bodies)
    for i in range(num_bodies):
        bodies[i].acceleration = np.zeros_like(bodies[i].acceleration)
        for j in range(num_bodies):
            if i != j:
                force = calculate_force(bodies[i], bodies[j], G)
                bodies[i].acceleration += force / bodies[i].mass

# Function to update velocities of all bodies
def update_velocity(bodies, dt):
    for body in bodies:
        body.velocity += body.acceleration * dt

# Function to update positions of all bodies
def update_position(bodies, dt):
    for body in bodies:
        body.position += body.velocity * dt

# Function to simulate orbits for all bodies
def simulate_orbits(bodies, G, num_steps, dt):
    positions = [[] for _ in range(len(bodies))]
    for step in range(num_steps):
        update_acceleration(bodies, G)
        update_velocity(bodies, dt)
        update_position(bodies, dt)
        for i, body in enumerate(bodies):
            positions[i].append(body.position.copy())
    return positions

# Function to plot the orbits of celestial bodies
def plot_orbits(positions):
    for i, pos in enumerate(positions):
        pos = np.array(pos)
        plt.plot(pos[:, 0], pos[:, 1], label=f'Body {i+1}')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Celestial Body Orbits')
    plt.legend()
    plt.axis('equal')
    plt.show()

# Error handling for input celestial bodies' parameters
while True:
    try:
        num_bodies = int(input("Enter the number of celestial bodies: "))
        if num_bodies <= 0:
            print("Please enter a valid number greater than 0.")
            continue
        
        bodies = []
        for i in range(num_bodies):
            mass = float(input(f"Enter mass of body {i+1}: "))
            x_pos = float(input(f"Enter initial x position of body {i+1}: "))
            y_pos = float(input(f"Enter initial y position of body {i+1}: "))
            x_vel = float(input(f"Enter initial x velocity of body {i+1}: "))
            y_vel = float(input(f"Enter initial y velocity of body {i+1}: "))
            bodies.append(CelestialBody(mass, [x_pos, y_pos], [x_vel, y_vel]))
        
        # Set up simulation parameters
        G = 1.0
        num_steps = 1000
        dt = 0.01

        # Simulate orbits
        positions = simulate_orbits(bodies, G, num_steps, dt)

        # Plot orbits
        plot_orbits(positions)
        break
    
    except ValueError:
        print("Invalid input. Please enter numeric values.")
    except Exception as e:
        print("An error occurred:", e)
