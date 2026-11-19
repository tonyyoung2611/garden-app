# Ask the user for the season and plant type
season = input("Enter a season: ").lower()
plant_type = input("Enter a plant type: ").lower()

# Function to provide advice based on the season
def get_season_advice(season):
    if season == "summer":
        return "Water your plants regularly and provide some shade."
    elif season == "winter":
        return "Protect your plants from frost with covers."
    else:
        return "No advice for this season."


# Function to provide advice based on the plant type
def get_plant_advice(plant_type):
    if plant_type == "flower":
        return "Use fertiliser to encourage blooms."
    elif plant_type == "vegetable":
        return "Keep an eye out for pests!"
    else:
        return "No advice for this type of plant."


# Generate and display gardening advice
print(get_season_advice(season))
print(get_plant_advice(plant_type))