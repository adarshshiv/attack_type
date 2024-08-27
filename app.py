import streamlit as st
import tensorflow as tf
from tensorflow.keras.models import load_model
import numpy as np

# Load the saved model
model = load_model('rt-iot.keras')

# Title of the app
st.title("Attack Type Prediction")

# Input features
proto = st.selectbox('Select Protocol', ['tcp', 'udp', 'icmp'])
service = st.selectbox('Select Service', ['mqtt', '-', 'http', 'dns', 'ntp', 'ssl', 'dhcp', 'irc', 'ssh', 'radius'])

# Convert categorical values to numerical format (you might need to modify this according to your preprocessing)
proto_dict = {'tcp': 0, 'udp': 1, 'icmp': 2}
service_dict = {'mqtt': 0, '-': 1, 'http': 2, 'dns': 3, 'ntp': 4, 'ssl': 5, 'dhcp': 6, 'irc': 7, 'ssh': 8, 'radius': 9}

proto_input = proto_dict[proto]
service_input = service_dict[service]

# Prediction
if st.button('Predict Attack Type'):
    input_data = np.array([[proto_input, service_input]])
    prediction = model.predict(input_data)
    predicted_class = np.argmax(prediction, axis=1)
    confidence = np.max(prediction, axis=1)
    
    # Map the predicted class back to the attack type
    attack_types = ['MQTT_Publish', 'Thing_Speak', 'Wipro_bulb', 'ARP_poisioning', 'DDOS_Slowloris', 
                    'DOS_SYN_Hping', 'Metasploit_Brute_Force_SSH', 'NMAP_FIN_SCAN', 'NMAP_OS_DETECTION', 
                    'NMAP_TCP_scan', 'NMAP_UDP_SCAN', 'NMAP_XMAS_TREE_SCAN']
    st.write(f"The predicted attack type is: {attack_types[predicted_class[0]]}")
    st.write(f"Confidence: {confidence[0]:.2f}")

# Run the app with: streamlit run app.py
