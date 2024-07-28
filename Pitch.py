import streamlit as st
import matplotlib.pyplot as plt
from mplsoccer import Pitch

# Create a pitch
pitch = Pitch()
fig, ax = pitch.draw()

# Optionally, add some data points or annotations
ax.scatter([20, 50, 80], [30, 50, 70], color='red', s=100, label='Sample Points')

# Add a legend
ax.legend(loc='upper right')

# Display the pitch in Streamlit
st.pyplot(fig)
