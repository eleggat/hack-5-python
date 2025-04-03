# imports
import streamlit as st
import pandas as pd
import numpy as np
import time

from wf_sim import Population

st.title('Simple Wright-Fisher Simulation of Genetic Drift :dna:')

# Add sliders to change population parameters
size = st.sidebar.slider("Population size", 10, 1000, 10, 10)
freq_init = st.sidebar.slider("Initial allele frequency", 0.0, 1.0, 0.2, 0.05)
gens = st.sidebar.slider("Generations", 5, 100, 50, 1)

# Add a progrss bar
progress_bar = st.sidebar.progress(0)
status_text = st.sidebar.empty()

# Create a new Population
# As a reminder these are the default values for population size (N)
# and initial derived allele frequency (f).
#   N=10, f=0.2
p = Population(N = size, f = freq_init)

# Initialize the chart with the initial allele frequency of the derived
# allele. `line_chart` expects a list, so we must wrap `p.f` in square
# brackets to pass a list
chart = st.line_chart([p.f])

# Initially we'll run a loop 50 times
for i in range(1, gens):
    # Step 1 wf generation
    p.step(ngens=1)
    # Calculate the current derived allele frequency
    freq = np.sum(p.pop)/len(p.pop)
    # Update the chart to add the current allele frequency
    chart.add_rows([freq])
    # sleep for a small amount of time so you can watch the animation
    time.sleep(0.05)
    # progress
    if i == (gens-1):
    	status_text.text(f"100% complete")
    	progress_bar.progress(1)
    else:
    	status_text.text(f"{round(i/gens*100)}% complete")
    	progress_bar.progress(i/gens)
    # stopping for 0 or 1
    if freq == 1:
    	st.write(f"The allele was fixed in generation {i}") #print if allele is fixed, then stop
    	status_text.text(f"100% complete")
    	break
    elif freq == 0:
    	st.write(f"The allele was lost in generation {i}") #print if allele is lost, then stop
    	status_text.text(f"100% complete")
    	break

progress_bar.empty()

# Add status
status_text = st.sidebar.write(p)

# Add a button to rerun the simulation
st.button("Rerun")










