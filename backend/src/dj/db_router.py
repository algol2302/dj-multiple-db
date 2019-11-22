import random


class DefaultReplicaRouter:
    """Copy-pasted from
    https://docs.djangoproject.com/en/2.2/topics/db/multi-db/
    """

    def db_for_read(self, model, **hints):
        """
        Reads go to a randomly-chosen replica.
        """
        return random.choice(['default', 'replica'])

    def db_for_write(self, model, **hints):
        """
        Writes always go to primary.
        """
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        """
        Relations between objects are allowed if both objects are
        in the primary/replica pool.
        """
        db_list = ('default', 'replica')

        if obj1._state.db in db_list and obj2._state.db in db_list:
            return True
        return False

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        All non-auth models end up in this pool.
        """
        return True
