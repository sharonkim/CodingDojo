import re

def get_matching_words(regex):
 words = ["aimlessness", "assassin", "baby", "beekeeper", "belladonna", "cannonball", "crybaby", "denver", "embraceable", "facetious", "flashbulb", "gaslight", "hobgoblin", "iconoclast", "issue", "kebab", "kilo", "laundered", "mattress", "millennia", "natural", "obsessive", "paranoia", "queen", "rabble", "reabsorb", "sacrilegious", "schoolroom", "tabby", "tabloid", "unbearable", "union", "videotape"]

 return [word for word in words if re.search(regex, word)]

    print "1) All words that contain a 'v'"
    print get_matching_words(r'v')

    print "2) All words that contain a double-'s'"
    print get_matching_words(r's{2}')

    print "3) All words that contain an 'e'"
    print get_matching_words(r'e$')

    print "4) All words that contain a 'b', any character, then another 'b'"
    print get_matching_words(r'b\wb')

    print "5) All words that contain a 'b', at least one character, then another 'b'"
    print get_matching_words(r'b\w{1}b')

    print "6) All words that contain a 'b', any number of characters (including zero), then another 'b'"
    print get_matching_words(r'b\w*?b')

    print "7) All words that include all five vowels in order"
    print get_matching_words(r'a[^aiou]*?e[^aeou]*?i[^aeiu]*?o[^aeio]*?u')

    print "8) All words that use the letters in 'regular expression' (each letter can appear any number of times)"
    print get_matching_words(r'\b[regulaxpsion]+\b')

    print "9) All words that contain a double letter"
    print get_matching_words(r'(\w)\1')
