import vk_api


def auth_handler():
    key = input("Enter authentication code: ")
    remember_device = True
    return key, remember_device


def main():
    login, password = 'your_login', 'your_password'
    vk_session = vk_api.VkApi(
        login, password,
        auth_handler=auth_handler
    )

    try:
        vk_session.auth()
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return

    vk = vk_session.get_api()

    friends = vk.friends.get(order='random', count=5,
                             fields=['nickname', 'photo_100'])

    for i in range(5):
        first_name = friends['items'][i]['first_name']
        last_name = friends['items'][i]['last_name']
        uid = friends['items'][i]['id']
        photo = friends['items'][i]['photo_100']
        print(f"{first_name} {last_name}, id: {uid}")
        print(photo)


if __name__ == '__main__':
    main()