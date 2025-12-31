import random

user_mood = "happy"
mood_activities = {
    "happy": ["dance to a song", "go for a walk", "cook something homey"],
    "sad": ["listen to a high beat song", "jump on the bed", "call a friend"],
    "stressed": ["take a deep breath", "make some tea", "stretch for 5 mins"],
    "tired": ["take a nap", "drink some water", "turn off screens"]
}

print("🐰 Welcome to Mood Bunny! 🐰")

while user_mood != "bye":
    # I added .lower() so it works even if you type "Happy" or "HAPPY"
    user_mood = input("\nHow are you feeling? (happy/sad/stressed/tired) or 'bye': ").lower()
    
    if user_mood in mood_activities:
        mood_activity = random.choice(mood_activities[user_mood])
        print(f"✨ You should: {mood_activity} ✨")
    elif user_mood != "bye":
        print("I don't know that mood yet, but I hope you feel better! 💖")

print("Bye bye! Take care! ☁️")

