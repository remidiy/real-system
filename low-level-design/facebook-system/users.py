from abc import ABC, abstractmethod

class PageFunctionsByUser(ABC):
  def create_page(self, name):
    pass
  def share_page(self, page):
    pass
  def like_page(self, page):
    pass
  def follow_page(self, page):
    pass
  def unLike_page(self, page):
    pass
  def unFollow_page(self, page):
    pass

class GroupFunctions(ABC):
  def add_user(self, user):
    pass
  def delete_user(self, user):
    pass
  def notify_user(self, user):
    pass

  def create_group(self, name):
    pass
  def join_group(self, group):
    pass
  def leave_group(self, group):
    pass
  def send_group_invite(self, group):
    pass

class PostFunctionsByUser(ABC):
  def create_post(self, content):
    pass
  def share_post(self, post):
    pass
  def comment_on_post(self, post):
    pass
  def like_post(self, post):
    pass

class CommentFunctionsByUser(ABC):
  def create_comment(self, post, content):
    pass
  def like_comment(self, comment):
    pass

class Admin:  
  def block_user(self, user):
    pass
  def unblock_user(self, user):
    pass
  def enable_page(self, page):
    pass
  def disable_page(self, page):
    pass
  def delete_group(self, group):
    pass
  def change_group_privacy(self, group):
    pass

class Person(ABC):
  def __init__(self, name, address, email, phone, account):
    self.__name = name
    self.__address = address
    self.__email = email
    self.__phone = phone
    self.__account = account

# Will be using only one interface example
class User(Person, PageFunctionsByUser):
  def __init__(self, name, address, email, phone, account, user_id, date_of_joining, is_admin, profile):
    self.__name = name
    self.__user_id = user_id
    self.__date_of_joining = date_of_joining
    self.__profile= profile
    # The following lists contain the pages and groups that a user is admin of
    self.__pages_admin = []
    self.__groups_admin = []    
    super().__init__(name, address, email, phone, account)
  
  def send_message(self, message):
    pass
  def send_recommendation(self, page, group, user):
    pass    
  def send_friend_request(self, user):
    pass
  def unfriend_user(self, user):
    pass
  def block_user(self, user):
    pass
  def follow_user(self, user):
    pass

  # The functions of the different interfaces will be present here
  def create_page(self, name):
    # functionality
    pass
  def like_page(self, page):
    # functionality
    pass
  def follow_page(self, page):
    # functionality
    pass
  def unLike_page(self, page):
    # functionality
    pass
  def unFollow_page(self, page):
    # functionality
    pass
  def share_page(self, page):
    # functionality
    pass