from blog_post.entity.blog_post import BlogPost
from blog_post.repository.blog_post_repository import BlogPostRepository


class BlogPostRepositoryImpl(BlogPostRepository):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance

    def save(self, blog_post: BlogPost) -> BlogPost:
        blog_post.save()
        return blog_post
