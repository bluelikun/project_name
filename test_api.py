import unittest
import requests
import ssl


class MyTestCase(unittest.TestCase):
    def test_something(self):
        context = ssl._create_unverified_context()
        url = 'https://www.v2ex.com/api/nodes/show.json'
        parm = {'name':'python'}
        response = requests.request(method='GET',url=url,params=parm,verify=False).json()
        print(response)
        self.assertEqual(response['name'],'python')
        self.assertEqual(response['id'],90)


if __name__ == '__main__':
    unittest.main()
