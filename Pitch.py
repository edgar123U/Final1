import streamlit as st
import matplotlib.pyplot as plt
from mplsoccer import Pitch

# Create a pitch
pitch = Pitch(pitch_type="statsbomb", goal_type="box",corner_arcs=True)
fig, ax = pitch.draw()

# Optionally, add some data points or annotations
ax.scatter([20, 50, 80,20], [30, 50, 70,40], color='red', s=100, label='Sample Points')


# Display the pitch in Streamlit
st.pyplot(fig)
