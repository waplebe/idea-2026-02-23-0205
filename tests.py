import unittest
from app import app, db
from models import Task

class TestTasks(unittest.TestCase):

    setup_db = lambda: db.init_app(app)
    def setUp(self):
        self.app = app
        self.db = db
        self.setup_db()

    def test_task_creation(self):
        task = Task(title="Test Task", description="This is a test task")
        self.db.session.add(task)
        self.db.session.commit()
        task = Task.query.get(task.id)
        self.assertEqual(task.title, "Test Task")
        self.assertEqual(task.description, "This is a test task")

    def test_task_retrieval(self):
        task = Task(title="Retrieve Task", description="This task is for retrieval testing")
        self.db.session.add(task)
        self.db.session.commit()
        retrieved_task = Task.query.get(task.id)
        self.assertEqual(retrieved_task.title, "Retrieve Task")
        self.assertEqual(retrieved_task.description, "This task is for retrieval testing")

    def test_task_update(self):
        task = Task(title="Update Task", description="Original description")
        self.db.session.add(task)
        self.db.session.commit()
        updated_task = Task.query.get(task.id)
        updated_task.title = "Updated Task"
        updated_task.description = "Updated description"
        self.db.session.commit()
        self.assertEqual(updated_task.title, "Updated Task")
        self.assertEqual(updated_task.description, "Updated description")

    def test_task_deletion(self):
        task = Task(title="Delete Task", description="This task is for deletion testing")
        self.db.session.add(task)
        self.db.session.commit()
        task = Task.query.get(task.id)
        self.db.session.delete(task)
        self.db.session.commit()
        deleted_task = Task.query.get(task.id)
        self.assertIsNone(deleted_task)

if __name__ == '__main__':
    unittest.main()