class Notification:
  def __init__(self, notification_id, created_on, content):
    self.__notification_id = notification_id
    self.__created_on = created_on
    self.__content = content

  def send_notification(self, account):
    pass