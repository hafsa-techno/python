import sys

print ("=== Player Score Analytics ===")
try:
    if (len(sys.argv) == 1):
        print ("No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ...")
    else:
        count = 1
        scores = []
        print ("Scores processed: [", end="")
        while count < len(sys.argv):
            score = int(sys.argv[count])
            print (f"{score}", end="")
            if (count != len(sys.argv) - 1):
                print (", ", end="")
            scores += [score]
            count += 1
        count -= 1
        print("]")
        print ("Total players:", count)
        total_score = sum(scores)
        print (f"Total score: {total_score}")
        print (f"Average score: {total_score / count}")
        max_nb = max(scores)
        print (f"High score: {max_nb}")
        min_nb = min(scores)
        print (f"Low scores: {min_nb}")
        print (f"Score range: {max_nb - min_nb}")
except ValueError:
    print ("oops, you have to enter numbers")
