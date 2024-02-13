import pandas as pd
import random

common_diseases = {
    "Common Cold": ["Runny Nose", "Sneezing", "Cough", "Sore Throat"],
    "Seasonal Allergies": ["Sneezing", "Runny Nose", "Itchy Eyes", "Cough"],
    "Acid Reflux": ["Heartburn", "Indigestion", "Regurgitation", "Chest Pain"],
    "Mild Gastritis": ["Abdominal Pain", "Nausea", "Bloating", "Indigestion"],
    "Muscle Strain": ["Muscle Pain", "Stiffness", "Swelling", "Limited Range of Motion"],
    "Mild Anxiety": ["Restlessness", "Nervousness", "Trouble Sleeping", "Mild Difficulty Concentrating"],
    "Tension Headache": ["Mild Headache", "Pressure in Head", "Neck and Shoulder Tension"],
    "Common Skin Rash": ["Itching", "Redness", "Rash", "Dry Skin"],
    "Influenza (Flu)": ["Fever", "Chills", "Body Aches", "Fatigue"],
    "Minor Injury": ["Pain", "Swelling", "Bruising", "Limited Mobility"],
    "Gastroesophageal Reflux Disease (GERD)": ["Heartburn", "Chest Pain", "Regurgitation", "Difficulty Swallowing"],
    "Sinusitis": ["Facial Pain", "Nasal Congestion", "Headache", "Fatigue"],
    "Urinary Tract Infection (UTI)": ["Burning Sensation", "Frequent Urination", "Cloudy Urine", "Pelvic Pain"],
    "Sprained Ankle": ["Pain", "Swelling", "Bruising", "Limited Mobility"],
    "Common Cold": ["Runny Nose", "Sneezing", "Cough", "Sore Throat"],
    "Ear Infection": ["Ear Pain", "Fluid Drainage", "Hearing Loss", "Fever"],
    "Plantar Fasciitis": ["Heel Pain", "Foot Arch Pain", "Stiffness", "Foot Swelling"],
    "Gastroenteritis": ["Diarrhea", "Vomiting", "Abdominal Pain", "Nausea"],
    "Allergic Rhinitis": ["Runny Nose", "Sneezing", "Itchy Nose", "Watery Eyes"],
    "Mild Insomnia": ["Difficulty Falling Asleep", "Waking Up During the Night", "Daytime Sleepiness"],
    "Mild Depression": ["Low Energy", "Loss of Interest", "Trouble Concentrating", "Mood Changes"],
    "Mild Sunburn": ["Redness", "Pain", "Swelling", "Blisters"],
    "Hemorrhoids": ["Rectal Bleeding", "Pain or Discomfort", "Itching", "Swelling"],
    "Irritable Bowel Syndrome (IBS)": ["Abdominal Pain", "Bloating", "Gas", "Diarrhea or Constipation"],
    "Mild Vertigo": ["Dizziness", "Nausea", "Balance Issues"],
    "Seasonal Flu": ["Fever", "Chills", "Muscle Aches", "Weakness"],
    "Mild Eczema": ["Itching", "Redness", "Dry Skin", "Rash"],
    "Back Strain": ["Back Pain", "Muscle Tightness", "Limited Mobility", "Pain with Movement"],
    "Mild Asthma": ["Shortness of Breath", "Coughing", "Chest Tightness", "Wheezing"],
    "Stress-induced Headache": ["Tension Headache", "Pressure in Head", "Neck and Shoulder Tension"],
    "Mild Acne": ["Pimples", "Blackheads", "Whiteheads", "Redness"],
    "Shin Splints": ["Pain Along the Inner Edge of the Shin", "Swelling", "Tenderness"],
    "Mild Allergic Reaction": ["Itching", "Hives", "Swelling", "Redness"],
    "Minor Sunburn": ["Redness", "Pain", "Swelling", "Peeling Skin"],
    "Mild Food Poisoning": ["Nausea", "Vomiting", "Diarrhea", "Abdominal Pain"],
    "Mild Dehydration": ["Thirst", "Dark Yellow Urine", "Dry Mouth", "Fatigue"],
    "Mild Conjunctivitis (Pink Eye)": ["Redness", "Watery Eyes", "Itching", "Swelling"],
    "Mild Tendonitis": ["Pain", "Swelling", "Tenderness", "Limited Mobility"],
    "Common Migraine": ["Severe Headache", "Nausea", "Sensitivity to Light", "Visual Disturbances"],
    "Mild Sunstroke": ["Headache", "Dizziness", "Nausea", "Weakness"],
    "Mild Heat Exhaustion": ["Heavy Sweating", "Weakness", "Nausea", "Dizziness"],
    "Mild Heat Cramps": ["Muscle Cramps", "Pain", "Tightness", "Weakness"],
    "Mild Heat Rash": ["Red Bumps", "Itching", "Irritation", "Sweating"],
    "Common Insomnia": ["Difficulty Falling Asleep", "Waking Up During the Night", "Daytime Sleepiness"],
    "Common Depression": ["Low Energy", "Loss of Interest", "Trouble Concentrating", "Mood Changes"],
}

def create_common_dataset(num_samples_per_disease=100):
    data = []

    id=1
    for disease, symptoms in common_diseases.items():
        for _ in range(num_samples_per_disease):
            english_proficiency = random.choice(["limited", "moderate", "good"])
            patient_description = generate_patient_description(symptoms, english_proficiency)

            short_sentence = generate_short_sentence(symptoms)
            data.append({
                "Disease_ID": id,
                "Disease": disease,
                "Symptoms": ', '.join(symptoms),
                "Patient_Description": patient_description + f" The symptoms started from {random.randint(1,7)} days before the day of appointment. "
                                                           f"Symptoms got worse: {random.choice(['Yes', 'No'])}. On medication: {random.choice(['Yes', 'No'])}. "
                                                           f"Related to previous condition: {random.choice(['Yes', 'No'])}."
            })

            data.append({
                "Disease_ID": id,
                "Disease": disease,
                "Symptoms": ', '.join(symptoms),
                "Patient_Description": short_sentence + f" The symptoms started from {random.randint(1,7)} days before the day of appointment. "
                                                           f"Symptoms got worse: {random.choice(['Yes', 'No'])}. On medication: {random.choice(['Yes', 'No'])}. "
                                                           f"Related to previous condition: {random.choice(['Yes', 'No'])}."
            })
        id+=1

    df = pd.DataFrame(data)

    return df

def generate_patient_description(symptoms, english_proficiency):
    # Randomly decide whether to include multiple symptoms in the description
    include_multiple_symptoms = random.choice([True, False])

    if include_multiple_symptoms:
        # Include multiple symptoms in the patient description
        selected_symptoms = random.sample(symptoms, random.randint(1, len(symptoms)))
        onset_duration = random.choice(["recently", "in the last few days", "a couple of weeks ago"])
        impact_on_life = random.choice(["It's a bit inconvenient but not too disruptive to my daily activities.",
                                        "I've been managing it with some over-the-counter remedies.",
                                        "It's not severe, but the symptoms are noticeable.",
                                        "The symptoms come and go, but they are not too bothersome."])
        additional_info = random.choice(["I thought it might be due to the change in weather.",
                                          "I've had similar issues in the past but never this persistent.",
                                          "I'm trying some home remedies to see if it helps.",
                                          "I haven't seen a doctor yet, but I'm keeping an eye on the symptoms."])

        # Simplify medical terms for patients with limited English proficiency
        simplified_symptoms = [s.split()[0] for s in selected_symptoms]
        simplified_description = (f"I {random.choice(['have', 'am experiencing'])} {', '.join(simplified_symptoms)} {onset_duration}. "
                                  f"The {random.choice(simplified_symptoms)} is a bit {random.choice(['bothersome', 'troublesome', 'disturbing'])}. "
                                  f"{impact_on_life} "
                                  f"{additional_info}.")

    else:
        # Include a single symptom in the patient description
        selected_symptom = random.choice(symptoms)
        onset_duration = random.choice(["recently", "in the last few days", "a couple of weeks ago"])
        impact_on_life = random.choice(["It's a bit inconvenient but not too disruptive to my daily activities.",
                                        "I've been managing it with some over-the-counter remedies.",
                                        "It's not severe, but the symptom is noticeable.",
                                        "The symptom comes and goes, but it's not too bothersome."])
        additional_info = random.choice(["I thought it might be due to the change in weather.",
                                          "I've had similar issues in the past but never this persistent.",
                                          "I'm trying some home remedies to see if it helps.",
                                          "I haven't seen a doctor yet, but I'm keeping an eye on the symptom."])

        # Simplify medical terms for patients with limited English proficiency
        simplified_symptom = selected_symptom.split()[0]
        simplified_description = (f"I {random.choice(['have', 'am experiencing'])} {simplified_symptom} {onset_duration}. "
                                  f"The {simplified_symptom} is a bit {random.choice(['bothersome', 'troublesome', 'disturbing'])}. "
                                  f"{impact_on_life} "
                                  f"{additional_info}.")

    # Introduce variations in English proficiency
    if english_proficiency == "limited":
        patient_description = (f"{simplified_description} "
                               f"{random.choice(['I not understand much about these things.', 'It is hard for me to say exactly what is happening.'])}")
    elif english_proficiency == "moderate":
        patient_description = simplified_description
    else:
        patient_description = simplified_description

    return patient_description

def generate_short_sentence(symptoms):
    # Generate short sentences like "I have fever" or "I have headache"
    selected_symptom = random.choice(symptoms)
    short_sentence = f"I have {selected_symptom}."
    return short_sentence

# Set the desired number of samples per disease
num_samples_per_disease = 1000

# Create the common dataset
common_dataset = create_common_dataset(num_samples_per_disease)

# Save the dataset to a CSV file
common_dataset.to_csv("data_notp.csv", index=False)

print(f"Common dataset created with {num_samples_per_disease} samples per disease. "
      f"File saved as 'data_notp.csv'.")
