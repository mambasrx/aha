import os
from mastodon import Mastodon

# Load Mastodon credentials
ACCESS_TOKEN = os.getenv("MASTODON_ACCESS_TOKEN")
MASTODON_INSTANCE = "https://mastodon.social"

# Initialize Mastodon API
mastodon = Mastodon(access_token=ACCESS_TOKEN, api_base_url=MASTODON_INSTANCE)

# Read and update posts.txt
POSTS_FILE = "posts.txt"
ARCHIVE_FILE = "archive.txt"

with open(POSTS_FILE, "r", encoding="utf-8") as f:
    posts = f.readlines()

if not posts:
    print("No posts left to publish.")
    exit(0)

# Get the first post
post_content = posts.pop(0).strip()

# Publish to Mastodon
mastodon.status_post(post_content)
print(f"Posted: {post_content}")

# Append the post to archive.txt
with open(ARCHIVE_FILE, "a", encoding="utf-8") as f:
    f.write(post_content + "\n")

# Update the posts.txt without the posted line
with open(POSTS_FILE, "w", encoding="utf-8") as f:
    f.writelines(posts)

print("Post archived and removed from posts.txt")
