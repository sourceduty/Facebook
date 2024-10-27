import requests
import json

# Set up your Facebook credentials (Access Token and Page ID)
ACCESS_TOKEN = 'your_page_access_token_here'
PAGE_ID = 'your_page_id_here'

def post_to_facebook_page(message):
    url = f'https://graph.facebook.com/{PAGE_ID}/feed'
    payload = {
        'message': message,
        'access_token': ACCESS_TOKEN
    }
    response = requests.post(url, data=payload)
    if response.status_code == 200:
        print('Post successful!')
    else:
        print('Error:', response.json())

def get_page_posts():
    url = f'https://graph.facebook.com/{PAGE_ID}/posts'
    params = {
        'access_token': ACCESS_TOKEN
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        posts = response.json().get('data', [])
        for i, post in enumerate(posts, start=1):
            print(f"Post {i}: {post.get('message', 'No message')} (ID: {post['id']})")
    else:
        print('Error:', response.json())

def delete_post(post_id):
    url = f'https://graph.facebook.com/{post_id}'
    params = {
        'access_token': ACCESS_TOKEN
    }
    response = requests.delete(url, params=params)
    if response.status_code == 200:
        print('Post deleted successfully!')
    else:
        print('Error:', response.json())

def terminal():
    while True:
        print("\nFacebook Terminal Options:")
        print("1. Post a message")
        print("2. View recent posts")
        print("3. Delete a post")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")
        if choice == '1':
            message = input("Enter the message to post: ")
            post_to_facebook_page(message)
        elif choice == '2':
            print("\nRecent posts on your page:")
            get_page_posts()
        elif choice == '3':
            post_id = input("Enter the ID of the post to delete: ")
            delete_post(post_id)
        elif choice == '4':
            print("Exiting Facebook Terminal. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    terminal()
