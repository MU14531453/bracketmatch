
def bracket_match(text: str, starting_symbol = '(', ending_symbol = ')'):

    gotos = []
    bracket_check = [x for x in text]
    
    while starting_symbol in bracket_check:
        nested_srs = 0

        for x, char in enumerate(bracket_check):
            if char == starting_symbol:
                nested_srs += 1
                if nested_srs == 1:
                    pair = [x]
            elif char == ending_symbol:
                if nested_srs == 1:
                    pair = pair + [x]
                    gotos.append(pair)
                    bracket_check[pair[0]] = '.'
                    bracket_check[pair[1]] = '.'
                else:
                    nested_srs -= 1

    return gotos
