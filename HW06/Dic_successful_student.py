lis = [{'name': 'Bob', 'score': [5, 4, 2, 7]},
       {'name': 'Jack', 'score': [1, 3, 6, 2]},
       {'name': 'Vital', 'score': [5, 3, 6, 7]}]

def big_score(l):
       name_max = ''
       name_min = ''
       max_score = 0
       min_score = 10
       for student in l:
              score = student.get('score')
              avg_score = sum(score)/len(score)
              if avg_score > max_score:
                     max_score = avg_score
                     name_max = student.get('name')
              if avg_score < min_score:
                     min_score = avg_score
                     name_min = student.get('name')
       return name_max, name_min

s_max, s_min = big_score(lis)
print(s_max)
print(s_min)