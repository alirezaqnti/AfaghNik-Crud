if IN_DOCKER:  # type: ignore # noqa
    assert MIDDLEWARE[:1] == [  # type: ignore # noqa
        "django.middleware.security.SecurityMiddleware"
    ]
