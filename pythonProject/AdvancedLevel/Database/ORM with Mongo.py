import mongoengine as me
from datetime import datetime

# Connect to MongoDB
me.connect(db="my_database", host="localhost", port=27017)


# Define a User model
class User(me.Document):
    # Fields
    username = me.StringField(required=True, max_length=50, unique=True)
    email = me.EmailField(required=True, unique=True)
    password = me.StringField(required=True, min_length=8)
    created_at = me.DateTimeField(default=datetime.utcnow)

    # Meta options (like specifying collection name)
    meta = {
        'collection': 'users',  # Specifies the collection name
        'indexes': [
            'email',  # Indexed field for faster queries
            'username'
        ]
    }


# Define a BlogPost model
class BlogPost(me.Document):
    title = me.StringField(required=True, max_length=120)
    content = me.StringField(required=True)
    author = me.ReferenceField(User, required=True)  # Reference to User
    created_at = me.DateTimeField(default=datetime.utcnow)
    tags = me.ListField(me.StringField())  # Array of tags

    # Meta options
    meta = {
        'collection': 'posts',  # Specifies the collection name
        'indexes': [
            'author',  # Index to optimize queries based on author
            '$title'  # Full-text index on the 'title' field for text searches
        ]
    }


# Define a Comment model
class Comment(me.EmbeddedDocument):
    content = me.StringField(required=True, max_length=500)
    author = me.ReferenceField(User, required=True)
    created_at = me.DateTimeField(default=datetime.utcnow)


# Embedding comments into BlogPost model
class BlogPostWithComments(me.Document):
    title = me.StringField(required=True, max_length=120)
    content = me.StringField(required=True)
    author = me.ReferenceField(User, required=True)
    comments = me.ListField(me.EmbeddedDocumentField(Comment))  # List of embedded comments
    created_at = me.DateTimeField(default=datetime.utcnow)

    # Meta options
    meta = {
        'collection': 'posts_with_comments',
        'indexes': [
            'author',
            '$title'  # Full-text index
        ]
    }


# Sample usage
if __name__ == "__main__":
    # Create a new user
    user = User(username="john_doe", email="john@example.com", password="password123")
    user.save()

    # Create a new blog post
    post = BlogPost(title="My First Blog Post", content="This is my first post!", author=user)
    post.save()

    # Create a comment
    comment = Comment(content="Nice post!", author=user)

    # Add the comment to a new post with comments
    post_with_comments = BlogPostWithComments(
        title="Another Post",
        content="This post has comments.",
        author=user,
        comments=[comment]
    )
    post_with_comments.save()

    print("Data successfully saved to MongoDB")
