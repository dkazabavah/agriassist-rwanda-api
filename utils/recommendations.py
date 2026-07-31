def recommend_crop(soil, season, water):

    if soil.lower() == "volcanic":
        return {
            "crop":"Potatoes",
            "reason":"Volcanic soil is excellent for potato production.",
            "advice":"Maintain moisture and use fertilizer."
        }


    if soil.lower() == "clay":
        return {
            "crop":"Rice",
            "reason":"Clay soil supports water retention.",
            "advice":"Use irrigation management."
        }


    if water.lower()=="low":
        return {
            "crop":"Cassava",
            "reason":"Cassava survives with limited water.",
            "advice":"Good drought-resistant option."
        }


    return {
        "crop":"Maize",
        "reason":"Maize performs well in Rwanda conditions.",
        "advice":"Plant during rainy season."
    }
