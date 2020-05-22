import requests, pprint

#添加评论功能测试

payload = {'q': '模拟', 'user': 'sq',
           'course_id': 1,
           'comment_of_the_course': '很好',
           'comment_of_the_teacher': '老师很耐心',
           'the_constitution_of_grade': '30平时分，70考试',
           'time_for_homework': '很多',
           'hard_core_mark': 4,
           'recommend_mark': 2,
           'mark_of_interest': 3}

response = requests.post('http://127.0.0.1:8000/add_judgement/', payload)
print(response.json())