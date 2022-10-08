import gunicorn

max_requests = 1000
max_requests_jitter = 50

log_file = "-"

gunicorn.SERVER = "CloudFront"
