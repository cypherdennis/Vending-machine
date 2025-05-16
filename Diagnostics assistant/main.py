user = str(input("Write any symptoms that you may be feeling (Fever, cough, fatigue): "))

def diagnosis(output):
    if output == "fever and cough":
        print("Symptom: ", output, ", You have malaria.")
    elif output == "cough":
        print("Symptom: ", output, ", you might have a cold")
    elif output == "none":
        print("Symptom: ", output, ", you seen fine")

diagnosis(user)

