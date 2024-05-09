import random

R_EATING = "I don't like eating anything because I'm a bot obviously!"
R_ADVICE = "If I were you, I would go to the internet and type exactly what you wrote there!"
R_FEEL="As an AI, I don't have feelings, but I'm here and ready to assist you!"
R_HOBBY="I'm passionate about providing helpful information and assisting users like you."
R_SMILE="While I don't smile, I always strive to provide helpful and accurate information to make your experience better!"
R_TRAVEL="I don't travel physically, but I have information on many exciting places!"
R_GOAL="My goal is to assist and provide the best possible help to usrs like you."
R_SUGGEST="Absolutely! What kind of getaway are you thinking of ... adventurous or relaxing?"
R_ADDVEN="How about a hiking trip to the mountains? It's a great way to unwind and explore nature."
R_RELAX="Absolutely! How about a serene beach destination or maybe a cozy cabin in the woods?"
R_RECOMMEND="The Rocky Mountains offer breathtaking scenery and plenty of hiking trails for all skill levels. Or perhaps the Smoky Mountains if you prefer a bit more greenery."
R_CABIN="Great choice! There are some lovely secluded cabins nestled in various national parks. Would you prefer one near a lake or surrounded by forest trails?"
R_LAKE="There are some beautiful options in places like the Adirondacks or the Pacific Northwest with stunning lakefront views and peaceful surroundings."
R_FOREST="Absolutely! Forest getaways can be incredibly serene."
R_BEACH="Great choice! Beach destinations offer relaxation and beautiful views. Are you thinking of a tropical breach or something closer to home?"
R_TROP="Excellent! There are stunning options like the Caribbean or Southeast Asia with pristine beaches and crystal-clear waters."
R_HOME="Understood! There are plenty of fantastic beaches nearer to various regions"
R_THANK="You're welcome! If you need more details or assistance, feel free to ask. Enjoy your time!"

def unknown():
    response = ["I didn't catch. Could you please re-phrase that? ",
                "...",
                "What does that mean?",
                "I'm not quite sure what you mean. Could you clarify more details?"][
        random.randrange(4)]
    return response