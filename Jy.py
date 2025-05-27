# Load the saved model
with open("model.pkl", "rb") as f:
    loaded_learn = pickle.load(f)

# Define input text
TEXT = "I liked this movie because"
N_WORDS = 40
N_SENTENCES = 2

# Generate predictions
preds = [loaded_learn.predict(TEXT, N_WORDS, temperature=0.75) for _ in range(N_SENTENCES)]

# Print predictions
print("\n".join(preds))
