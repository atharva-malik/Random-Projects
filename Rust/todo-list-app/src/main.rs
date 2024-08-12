struct Task {
    id: u32,
    description: String,
    completed: bool,
}

struct TodoList {
    tasks: Vec<Task>,
}

impl Task {
    fn new(id: u32, description: String) -> Self {
        Task {
            id,
            description,
            completed: false,
        }
    }

    fn mark_completed(&mut self) {
        self.completed = true;
    }
}

impl TodoList {
    fn new() -> Self {
        TodoList { tasks: Vec::new() }
    }

    fn add_task(&mut self, task: Task) {
        self.tasks.push(task);
    }

    fn remove_task(&mut self, id: u32) {
        self.tasks.retain(|task| task.id != id);
    }

    fn list_tasks(&self) {
        for task in &self.tasks {
            println!("{}: {}", task.id, task.description);
        }
    }
}

fn main() {
    let mut todo_list = TodoList::new();

    todo_list.add_task(Task::new(1, "Buy groceries".to_string()));
    todo_list.add_task(Task::new(2, "Learn Rust".to_string()));

    todo_list.list_tasks();

    todo_list.tasks[0].mark_completed();

    todo_list.list_tasks();
}
