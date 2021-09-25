import ast

team = [10,20,30,40,50]
applicant = [30,60,80,40]

import statistics


def above_avg(data, check):
    return check > statistics.mean(data)


#for appl in applicant:
#    if above_avg(team, appl):
#        team.append(appl)

team.extend(appl for appl in applicant if above_avg(team, appl))
print(team)