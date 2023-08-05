import factory
from django.contrib.auth.models import User
from djblogger.blog.models import Post


class UserFactory(factory.django.DjangoModelFactory):
    """
    Factory for handling User data.
    """

    class Meta:
        model = User

    password = "test"
    username = "test"
    is_superuser = True
    is_staff = True


class PostFactory(factory.django.DjangoModelFactory):
    """
    factory for handling Post data.
    """

    class Meta:
        model = Post

    title = "x"
    subtitle = "x"
    slug = "x"
    author = factory.SubFactory(UserFactory)
    content = "x"
    status = "published"

    @factory.post_generation
    def tags(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            self.tags.add(*extracted)
