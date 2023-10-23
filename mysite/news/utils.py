# здесь миксины

class MyMixin:
    mixin_prop = ''

    def get_upper(self, s):
        if isinstance(s, str):
            return s.upper()
        else:
            return s['title'].upper()