import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import time

# Set the title of the app
st.title("Intelligent Traffic Light Control System")

# Sidebar for user input
st.sidebar.header("Simulation Settings")
traffic_density = st.sidebar.slider("Traffic Density (vehicles per minute)", 10, 100, 50)
simulation_time = st.sidebar.slider("Simulation Time (minutes)", 1, 10, 5)

# Placeholder for the traffic light visualization
traffic_light_placeholder = st.empty()

# Function to simulate traffic light control
def simulate_traffic_control(traffic_density, simulation_time):
    # Initialize variables
    total_vehicles = traffic_density * simulation_time
    waiting_times = []
    green_light_duration = 1  # Initial green light duration in minutes

    # Simulate traffic light control
    for minute in range(simulation_time):
        # Simulate the number of vehicles arriving in this minute
        vehicles_arriving = np.random.poisson(traffic_density)
        waiting_time = max(0, vehicles_arriving - green_light_duration * 10)  # Assume 10 vehicles can pass per minute
        waiting_times.append(waiting_time)

        # Update traffic light visualization
        with traffic_light_placeholder.container():
            st.write(f"Minute {minute + 1}")
            if waiting_time > 0:
                st.error("Red Light - Vehicles Waiting")
            else:
                st.success("Green Light - No Waiting")
            st.write(f"Vehicles Waiting: {waiting_time}")
            time.sleep(1)

        # Adjust green light duration based on waiting time (simple RL simulation)
        if waiting_time > 5:
            green_light_duration += 1
        elif waiting_time == 0 and green_light_duration > 1:
            green_light_duration -= 1

    return waiting_times

# Run the simulation
if st.sidebar.button("Start Simulation"):
    st.write("Starting simulation...")
    waiting_times = simulate_traffic_control(traffic_density, simulation_time)

    # Plot the results
    st.write("Simulation completed. Waiting times per minute:")
    fig, ax = plt.subplots()
    ax.plot(range(1, simulation_time + 1), waiting_times, marker='o')
    ax.set_xlabel("Minute")
    ax.set_ylabel("Number of Vehicles Waiting")
    ax.set_title("Vehicles Waiting Over Time")
    st.pyplot(fig)
