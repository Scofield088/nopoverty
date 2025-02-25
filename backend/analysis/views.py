import os
import pandas as pd
import matplotlib.pyplot as plt
import base64
from io import BytesIO
from django.conf import settings
from django.shortcuts import render
from openai import OpenAI  # Import Gemini AI (if using OpenAI)

# Load the API key from .env
GEMINI_API_KEY = os.getenv("AIzaSyD9yuxRq4K3fI35BARLgwqSkVbpwARwotw")

# Define demographic columns
unique_columns = [
    "Population", "Male", "Female", "Literate", "Male_Literate", "Female_Literate",
    "Households_with_Internet", "Households_with_Computer", "Households",
    "Primary_Education", "Higher_Education", "Households_with_Bicycle",
    "Households_with_Car_Jeep_Van", "Condition_of_occupied_census_houses_Dilapidated_Households",
    "Having_bathing_facility_Total_Households", "Ownership_Owned_Households",
    "Type_of_bathing_facility_Enclosure_without_roof_Households",
    "Main_source_of_drinking_water_Tapwater_Households",
    "Power_Parity_Less_than_Rs_45000", "Urban_Households", "Married_couples_None_Households",
    "Households_with_TV_Computer_Laptop_Telephone_mobile_phone_and_Scooter_Car",
]

# Load data from CSV
csv_file_path = os.path.join(settings.BASE_DIR, "normalized_f0.csv")

try:
    df = pd.read_csv(csv_file_path)
    if "District" not in df.columns:
        raise ValueError("Missing 'District' column in CSV file.")
except Exception as e:
    print("Error loading CSV:", e)
    df = pd.DataFrame(columns=["District"] + unique_columns)  # Create empty DataFrame if file not found

def generate_graph(filtered_df):
    """Generate a bar graph for the selected district."""
    plt.figure(figsize=(10, 5))

    if not filtered_df.empty:
        filtered_df.set_index("District", inplace=True)  # Set index only if it exists
        filtered_df[["Population", "Literate"]].plot(kind="bar")

    plt.xlabel("Districts")
    plt.ylabel("Count")
    plt.title("Population vs Literacy Rate")

    # Save the graph as an image in base64 format
    buffer = BytesIO()
    plt.savefig(buffer, format="png")
    buffer.seek(0)
    encoded_graph = base64.b64encode(buffer.getvalue()).decode("utf-8")
    buffer.close()
    return encoded_graph

def ai_suggestions(filtered_df):
    """Fetch AI-based suggestions using Gemini API."""
    if filtered_df.empty:
        return "No data available for this district."

    district_name = filtered_df["District"].values[0]
    prompt = f"Analyze the demographic data of {district_name} and suggest improvements where it's lagging."

    try:
        client = OpenAI(api_key=GEMINI_API_KEY)
        response = client.Completion.create(
            model="gemini-1",
            prompt=prompt,
            max_tokens=100
        )
        suggestion_text = response["choices"][0]["text"]
    except Exception as e:
        print("AI API Error:", e)
        suggestion_text = "Could not fetch AI suggestions due to an API error."

    return suggestion_text

def analyze_data(request):
    """Render analysis page with graph and AI insights for the selected district."""
    district_name = request.GET.get("district", "").strip()

    if district_name:
        filtered_df = df[df["District"].str.lower() == district_name.lower()]
    else:
        filtered_df = df

    graph = generate_graph(filtered_df)
    ai_text = ai_suggestions(filtered_df)

    context = {
        "columns": df.columns.tolist(),
        "data": filtered_df.to_dict(orient="records"),
        "graph": graph,
        "ai_suggestions": ai_text,
        "district_name": district_name
    }

    return render(request, "analysis.html", context)
