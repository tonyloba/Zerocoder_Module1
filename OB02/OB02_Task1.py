class User:
    def __init__(self, id, name, access_level):
        self._id = id
        self._name = name
        self._access_level = access_level
        self.users = []

    def get_id(self):
        return self._id

    def set_id(self, new_id):
        self._id = new_id

    def get_name(self):
        return self._name

    def set_name(self, new_name):
        self._name = new_name

    def get_access_level(self):
        return self._access_level

    def set_access_level(self, new_access_level):
        if new_access_level not in ["user", "admin"]:
            raise ValueError("Access level must be 'user' or 'admin'")
        self._access_level = new_access_level


class Admin(User):
    def __init__(self, id, name, access_level, admin_level):
        super().__init__(id, name, access_level)
        self._admin_level = admin_level

    def get_admin_level(self):
        return self._admin_level

    def set_admin_level(self, new_admin_level):
        if new_admin_level not in ["super_admin", "admin"]:
            raise ValueError("Admin level must be 'super_admin' or 'admin'")
        self._admin_level = new_admin_level

    def add_user(self, user_name):
        self.users.append(user_name)

    def remove_user(self, user_name):
        self.users.remove(user_name)


# Example usage:
admin = Admin(1, "John Doe", "admin", "superadmin")
user1 = User(2, "Jane Doe", "user")
user2 = User(3, "Bob Smith", "user")

admin.add_user(user1)
admin.add_user(user2)

print(admin.get_id())  # Output: 1
print(admin.get_name())  # Output: John Doe
print(admin.get_access_level())  # Output: admin
print(admin.get_admin_level())  # Output: superadmin

print("Admin's users:")
for user in admin.users:
    print(f"ID: {user.get_id()}, Name: {user.get_name()}, Access Level: {user.get_access_level()}")

try:
    admin.set_access_level("invalid")
except ValueError as e:
    print(e)  # Output: Invalid access level. Must be 'user' or 'admin'.

try:
    admin.set_admin_level("invalid")
except ValueError as e:
    print(e)  # Output: Invalid admin level. Must be 'superadmin' or 'admin'.

admin.remove_user(user1)
print("Admin's users after removal:")
for user in admin.users:
    print(f"ID: {user.get_id()}, Name: {user.get_name()}, Access Level: {user.get_access_level()}")

print(admin.get_access_level())  # Output: admin
print(admin.get_admin_level())
