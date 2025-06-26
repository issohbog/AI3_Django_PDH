## 해결 
'''
    slug = models.SlugField(max_length=200, unique=True, null=True)
'''

우선적으로 , null 허용 지정하고 마이그레이션후, null=False를 변경하는 방법으로 해결