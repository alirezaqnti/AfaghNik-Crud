DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": DB_NAME,  # type: ignore # noqa
        "HOST": DB_HOST,  # type: ignore # noqa
        "PORT": "5432",
        "USER": DB_USER,  # type: ignore # noqa
        "PASSWORD": DB_PASSWORD,  # type: ignore # noqa
    }
}
