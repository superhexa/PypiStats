from FlashSQL import Client

class Database:
    def __init__(self, db_path='database.db'):
        self.db = Client(db_path)

    def add_user(self, user_id):
        if not self.user_exists(user_id):
            self.db.set(f'user:{user_id}', True)

    def user_exists(self, user_id):
        return self.db.exists(f'user:{user_id}')

    def add_pkg(self, pkg_name, downloads, timestamp):
        self.db.set(f'pkg:{pkg_name}', {'downloads': downloads, 'timestamp': timestamp})

    def del_pkg(self, pkg_name):
        self.db.delete(f'pkg:{pkg_name}')

    def pkg_exists(self, pkg_name):
        return self.db.exists(f'pkg:{pkg_name}')

    def get_pkg_stats(self, pkg_name):
        return self.db.get(f'pkg:{pkg_name}')

    def close(self):
        self.db.close()
