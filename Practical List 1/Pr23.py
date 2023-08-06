# Mr. Roy is living in Canada where temperature is mapped in Fahrenheit.
# According to weather report current temperature in Canada is 130 °F. Roy’s
# mother is living in different region of Canada where temperatureismapped
# in Celsius. Convert current temperatureofCanadaintoCelsius.C=(F-32)*
# 5/ 9


# convert = (temperature_fahrenheit  - 32) * 5 / 9
# Convert Fahrenheit to Celsius using a lambda function
convert = lambda f : (f - 32) * 5 / 9  
#lambda is type of function or keyword 
temperature_celsius = convert(130) 

# Print the converted temperature
print(f"The current temperature in Celsius is: {temperature_celsius:.2f} °C")
