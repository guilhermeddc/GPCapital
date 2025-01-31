from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


class PublicStaticStorage(S3Boto3Storage):
    location = 'static'
    default_acl = 'public-read'
    file_overwrite = True
    secure_urls = True
    querystring_auth = False
    preload_metadata = True
    auto_create_bucket = True
    
    def path(self, name):
        return self.url(name)

    def get_accessed_time(self, name):
        pass

    def get_created_time(self, name):
        pass


class PublicMediaStorage(S3Boto3Storage):
    location = 'media'
    default_acl = 'public-read'
    file_overwrite = False
    secure_urls = True
    querystring_auth = False
    preload_metadata = True
    auto_create_bucket = True

    def path(self, name):
        return self.url(name)
    
    def get_accessed_time(self, name):
        pass
    
    def get_created_time(self, name):
        pass

