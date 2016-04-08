def access_fn(user, url_name, url_args=None, url_kwargs=None):
    return user.is_staff
