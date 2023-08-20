class Page:
  def __init__(self, name, page_id, description, like_count):
    self.__page_id = page_id
    self.__name = name
    self.__description = description
    self.__like_count = like_count

class Post:
  def __init__(self, post_id, content, image, like_count, share_count, post_owner, settings):
    self.__post_id = post_id
    self.__content = content
    self.__image = image
    self.__like_count = like_count
    self.__share_count = share_count
    self.__post_owner = post_owner
    self.__settings = settings
  
  def change_post_visibility(self, post):
    pass

class Comment:
  def __init__(self, comment_id, content, like_count, comment_owner):
    self.__comment_id = comment_id
    self.__content = content
    self.__like_count = like_count
    self.__comment_owner = comment_owner

class ProfilePrivacy:
    def change_friends_list_visibility(self, profile):
        pass
    def lock_profile(self, profile):
        pass
    def lock_profile_picture(self, profile):
        pass