class User:

    def update_user_object(self, born_at, custom_attributes, email, first_name, gender, last_name, password, phone):

        user_update_list = []

        if born_at is not None:
            born_at_dict = {'born_at':born_at}
            user_update_list.append(born_at_dict)

        if custom_attributes is not None:
            custom_attributes_dict = {'custom_attributes':custom_attributes}
            user_update_list.append(custom_attributes_dict)

        if email is not None:
            email_dict = {'email': email}
            user_update_list.append(email_dict)

        if first_name is not None:
            first_name_dict = {'first_name':first_name}
            user_update_list.append(first_name_dict)

        if gender is not None:
            gender_dict = {'gender': gender}
            user_update_list.append(gender_dict)

        if last_name is not None:
            last_name_dict = {'last_name':last_name}
            user_update_list.append(last_name_dict)

        if password is not None:
            password_dict = {'password':password}
            user_update_list.append(password_dict)

        if phone is not None:
            phone_dict = {'phone':phone}
            user_update_list.append(phone_dict)

        return user_update_list




    def createUserObject(self, *args):
        api_key = ''
        user = ''
        email = ''
        first_name = ''
        last_name = ''
        phone = ''

        for value in args:
            if 'email' in value:
                email = value

            if 'first_name' in value:
                first_name = value

            if 'last_name' in value:
                last_name = value

            if 'phone' in value:
                phone = value

            if 'api_key' in value:
                api_key = value

        return {'api_key': api_key, 'user':{'email':email, 'first_name':first_name, 'last_name':last_name, 'phone':phone}, 'permission_keynames':['manage_user_payment_methods', 'create_orders']}

    def createGuestUserObject(self, *args):
        api_key = ''
        user = ''
        email = ''
        first_name = ''
        last_name = ''
        phone = ''

        for value in args:
            if 'email' in value:
                email = value

            if 'first_name' in value:
                first_name = value

            if 'last_name' in value:
                last_name = value

            if 'phone' in value:
                phone = value

            if 'api_key' in value:
                api_key = value

            if 'guest' in value:
                guest = value

        return {'api_key': api_key,
                'user': {'email': email, 'first_name': first_name, 'last_name': last_name, 'phone': phone, 'guest':guest},
                'permission_keynames': ['manage_user_payment_methods', 'create_orders']}

    def userAddress(self, *args):

        for key_value in args:
            if 'address_type' in key_value:
                address_type = key_value['address_type']

            if 'street_address' in key_value:
                street_address = key_value['street_address']

            if 'extended_address' in key_value:
                extended_address = key_value['extended_address']

            if 'locality' in key_value:
                locality = key_value['locality']

            if 'region' in key_value:
                region = key_value['region']

            if 'postal_code' in key_value:
                postal_code = key_value['postal_code']

            if address_type is None:
                address_type = ''

            if street_address is None:
                street_address = ''

            if extended_address is None:
                extended_address = ''

            if locality is None:
                locality = ''

            if region is None:
                region = ''

            if postal_code is None:
                postal_code = ''

            user_address = {'user_address':{'address_type':address_type, 'street_address':street_address, 'extended_address':extended_address, 'locality':locality, 'region':region, 'postal_code':postal_code}}

            return user_address