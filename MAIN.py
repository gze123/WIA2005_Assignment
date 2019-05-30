from createGraph import *
from getDistance import *
from djikstraPath import *

def calculate_average_sentiment(c):
    rslt = 0
    for c1 in c:
        if c1 == "Kuala Lumpur":
            continue
        rslt += my_dict[c1]
    return round(rslt / len(c), 2)


def get_score(distance, shortest, longest, sentiment):
    score = ((longest - distance)*70 / (longest-shortest)) + \
        ((sentiment + 100)*30/200)
    return round(score, 2)


def get_prob(score, total_score):
    prob_dist = score / total_score
    return round(prob_dist, 2)


def calculate_table(destination):
    # start find path
    source = "Kuala Lumpur"
    desti = destination
    rslt = get_paths(source, desti)
    # end find path
    # start find distances
    shortest_distance = round(get_distance(source, desti), 2)
    longest_distance_list = max(rslt, key=lambda x: x[-1])
    longest_distance = round(longest_distance_list[-1], 2)
    # end find distances
    # start find probability distribution
    # end find probability distribution
    rslt_str = []
    total_score = 0
    for i, r in enumerate(rslt):
        # start find sentiment
        current_sentiment = calculate_average_sentiment(r[:-1])
        # end find sentiment
        # start find score
        score = get_score(
            round(r[-1], 2), shortest_distance, longest_distance, current_sentiment)
        # end find score
        # start find total score
        total_score += score
        # end find total_score
        rslt_str_small = []
        tmp_path_str = "->".join(r[:-1])
        tmp_cost_str = str(round(r[-1], 2))
        rslt_str_small.append(tmp_path_str)
        rslt_str_small.append(tmp_cost_str)
        rslt_str_small.append(str(current_sentiment) + "%")
        rslt_str_small.append(str(score) + "%")
        rslt_str_small.append("0.5")
        rslt_str.append(rslt_str_small)
    for i1, r1 in enumerate(rslt):
        rslt_str[i1][-1] = str(get_prob(float(rslt_str[i1]
                                              [-2][:-1]), total_score))
    rslt_str.sort(key=lambda x: float(x[-2][:-1]), reverse=True)
    str(rslt_str).replace("'", '"')
    for i in range(len(rslt_str)):
        print(rslt_str[i])

destination = input("Enter your destination[Beijing,Singapore,Brunei,Jakarta,Taipei,Melbourne,Tokyo,Hanoi]:")
calculate_table(destination)
destinationInInt = place(destination)
g2.dijkstra(graph,0,destinationInInt)
