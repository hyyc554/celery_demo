from django.test import TestCase

# Create your tests here.
# import redis
# pool = redis.ConnectionPool(host='192.168.0.2', port=6379, password='hyc554', max_connections=1000)
# conn = redis.Redis(connection_pool=pool)
#
#
# conn.hset('hyyyc','hyc',123566)

from shapely.geometry import Point
from shapely.geometry.polygon import Polygon

point = Point(0.5, 0.5)
polygon = Polygon([(0, 0), (0, 1), (1, 1), (1, 0)])
print(polygon.contains(point))