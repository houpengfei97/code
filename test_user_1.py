import os,sys
import json
import pytest
sys.path.append(os.getcwd())

class TestUserInfo(object):
	@pytest.fixture
	def users(self):
		return json.loads(open('./data.json','r').read())

	def test_user_infolength(self,users):
		for user in users:
			uinfo = user['info']
			assert len(uinfo) >= 6
			msg = "user %s info" % (user['userName'])
			assert uinfo == 'huawei123123', msg
			assert uinfo != 'nokia123',msg



