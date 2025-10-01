import os
import requests

# Sample field location (Iowa, USA: lat, lon; change if needed)
field_location = (42.0, -93.5)  # Example: Central Iowa farm area

# Function to fetch soil type from SoilGrids API (free, no key needed)
def get_soil_type(lat, lon):
    try:
        url = f"https://rest.isric.org/soilgrids/v2.0/classification/query?lon={lon}&lat={lat}"
        response = requests.get(url, timeout=10).json()
        soil_class = response.get("wrb_class_name", "Unknown")
        return soil_class if soil_class else "Chernozem"  # Fallback to mock soil type
    except:
        print("SoilGrids failed (offline or timeout). Using mock soil type: Chernozem.")
        return "Chernozem"

# Mock LLM response function (replaces API call)
def mock_llm_response(soil_type, question):
    responses = {
        "soil type": f"Hey, your Iowa field has {soil_type} soil—rich and fertile, great for crops like soybeans or corn!",
        "good for": f"The {soil_type} soil in your field is awesome for most crops, like corn or soybeans, due to its nutrient-rich profile. What are you planting?",
        "default": f"Based on the {soil_type} soil in your Iowa field, it’s solid for farming. Got specific crops in mind?"
    }
    question_lower = question.lower()
    if "soil type" in question_lower:
        return responses["soil type"]
    elif "good for" in question_lower or "corn" in question_lower:
        return responses["good for"]
    return responses["default"]

# Fetch soil data once at startup
print("Fetching soil data...")
soil_type = get_soil_type(field_location[0], field_location[1])
print(f"Soil type: {soil_type}")

# Simple chat loop (runs in the terminal)
while True:
    question = input("\nAsk about the soil at your field (or 'quit'): ").strip()
    if question.lower() == 'quit':
        break
    if "soil" not in question.lower() and "corn" not in question_lower():
        print("Please ask about the soil or crops at your field.")
        continue

    # Get mock response
    try:
        response = mock_llm_response(soil_type, question)
        print(response)
    except Exception as e:
        print(f"Error generating response: {str(e)}.")
        break