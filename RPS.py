# The example function kept track of the opponent's history and played whatever the opponent played two plays ago. It is not a good player so I changed the code to pass the challenge.
# Keep track of patterns in the opponent's history and play whatever the opponent is most likely to play based on their previous playing history.
def player(prev_play, opponent_history=[]):
    opponent_history.append(prev_play)
    
    num_rounds = len(opponent_history)
    guess = "R"
    #plays = { "RR": 0, "RP": 0, "RS": 0, "PR": 0, "PP": 0, "PS": 0, "SR": 0, "SP": 0, "SS": 0 }

    
    #if len(opponent_history) > 2:
    #    guess = opponent_history[-2]

    #for i in range(len(opponent_history) - 1):
    #    pair = "".join(opponent_history[i:i + 2])
    #    if pair in plays:
    #        plays[pair] += 1

    if num_rounds < 3:
        return guess
    
    pattern_size = 3
    pattern_next_counts = {}
    for i in range(num_rounds - pattern_size):
        pattern = tuple(opponent_history[i:i+pattern_size])
        next_item = opponent_history[i+pattern_size]
        
        if pattern not in pattern_next_counts:
            pattern_next_counts[pattern] = {}
        if next_item not in pattern_next_counts[pattern]:
            pattern_next_counts[pattern][next_item] = 0
        
        pattern_next_counts[pattern][next_item] += 1

    last_pattern = tuple(lst[-pattern_size:])
    if last_pattern not in pattern_next_counts:
        return guess

    next_play_counts = pattern_next_counts[last_pattern]
    guess = max(next_play_counts, key=next_play_counts.get)
        
    #potential_plays = [prev_play + "R", prev_play + "P", prev_play + "S"]
    #predicted_next_play = max(potential_plays, key=lambda play: plays.get(play, 0))[-1]

    #counter_play = {"R": "P", "P": "S", "S": "R"}
    #guess = counter_play[predicted_next_play]

    return guess
