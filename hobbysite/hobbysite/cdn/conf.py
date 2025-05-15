import os

AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME="hobbysite-bucket"
AWS_S3_ENDPOINT_URL="https://sgp1.digitaloceanspaces.com"
AWS_S3_OBJECT_PARAMETERS = {
	"CacheControl": "max_age=86400"
}
AWS_LOCATION = "https://hobbysite-bucket.sgp1.digitaloceanspaces.com"

DEFAULT_FILE_STORAGE = 'hobbysite-bucket.cdn.backends.MediaRootS3Boto3Storage'
STATICFILES_STORAGE = 'hobbysite-bucket.cdn.backends.StaticRootS3Boto3Storage'