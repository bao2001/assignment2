from flask import Flask, request, jsonify
import random

app = Flask(__name__)

jokes = [
    "Why did the salamander go to Hollywood? To make newt movies!",
    "Did you hear the one about the New York Jets cocktail? Two of them, and you forget what Joe Namath.",
    "Why did the veterinarian prescribe birth-control pills for dogs? It’s part of an anti-litter campaign.",
    "What do you call fake spaghetti? An impasta.",
    "Why don’t pirates take a shower before they walk the plank? They just wash up on shore.",
    "On what grounds did the police arrest the devil? They got him on possession.",
    "How many telemarketers does it take to change a lightbulb? Only one, but he has to do it while you are eating dinner.",
    "How many therapists does it take to change a lightbulb? Only one, but the lightbulb has to want to change.",
    "Who was the roundest knight in King Arthur’s court? Sir Cumference.",
    "Why can't you play poker on the African Savanna? There's too many cheetahs."
]

@app.route('/jokes', methods=['GET'])
def get_jokes():
    num = request.args.get('num', default=5, type=int)
    if num > len(jokes):
        num = len(jokes)
    random_jokes = random.sample(jokes, num)
    return jsonify(random_jokes)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)