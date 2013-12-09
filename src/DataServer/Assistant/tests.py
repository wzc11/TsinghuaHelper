
import docs
from query.query_learn import *
# Create your tests here.

def course_info_get(user_id, course_sequence):
    result = {
        'error': 0,
        'data': {}
    }
    query_set = query_learn(user_id)
    if not query_set.user_id_exist():
        result['error'] = 1
        return result
    course_info = query_set.course_info_query(course_sequence)
    result['data'] = course_info._data
    print course_info._data['caption']

try:
    course_info_get('oUfi4uFv6agwCo-JGPBfWvXdgZBg', 1)
except Exception, e:
    print Exception, e