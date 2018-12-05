#coding:utf-8
fn=('李','王', '张', '刘')
ln1=('娉','览', '莱', '屹')
ln2=('治明', '正顺', '书铎')
import random
class FakeUser:
    def fake_name(self, one_word=False, two_words=False):
        if one_word:
            full_name=random.choice(fn)+random.choice(ln1)
        elif two_words:
            full_name = random.choice(fn) +random.choice(ln2)
        else:
            full_name=random.choice(fn) +random.choice(ln1 +ln2)
        print (full_name)
    def fake_gender(self):
        gender=random.choice(['男', '女', '未知'])
        print(gender)
class SnsUser(FakeUser):
    def get_followers(self, few=True, a_lot=False):
        if(few):
            followers = random .randrange(1,50)
        elif a_lot:
            followers =random.randrange(20,10000)
        print (followers)
user_a = FakeUser()
user_b=SnsUser()
user_a.fake_name()
user_b.get_followers(few=True)
