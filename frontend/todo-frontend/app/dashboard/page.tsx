"use client";

import { useState, useEffect } from "react";
import { useAuth } from "@/components/AuthProvider";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { DropdownMenu, DropdownMenuContent, DropdownMenuItem, DropdownMenuTrigger } from "@/components/ui/dropdown-menu";
import { MoreHorizontal, Menu, Plus } from "lucide-react";
import { Checkbox } from "@/components/ui/checkbox";
import { Sheet, SheetContent, SheetTrigger } from "@/components/ui/sheet";
import { Dialog, DialogContent, DialogHeader, DialogTitle, DialogTrigger } from "@/components/ui/dialog";
import { AlertDialog, AlertDialogAction, AlertDialogCancel, AlertDialogContent, AlertDialogDescription, AlertDialogFooter, AlertDialogHeader, AlertDialogTitle, AlertDialogTrigger } from "@/components/ui/alert-dialog";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Textarea } from "@/components/ui/textarea";
import { taskApi } from "@/lib/api";
import { toast } from "sonner";
import { Skeleton } from "@/components/ui/skeleton";

export default function DashboardPage() {
  const { user, signOut } = useAuth();
  const [tasks, setTasks] = useState<any[]>([]);
  const [filter, setFilter] = useState<"all" | "pending" | "completed">("all");
  const [sidebarOpen, setSidebarOpen] = useState(false);
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [editingTask, setEditingTask] = useState<any>(null);
  const [taskForm, setTaskForm] = useState({ title: "", description: "" });
  const [loading, setLoading] = useState(true);

  // Fetch tasks when component mounts or filter changes
  useEffect(() => {
    const fetchTasks = async () => {
      try {
        setLoading(true);
        const fetchedTasks = await taskApi.getTasks(filter);
        setTasks(fetchedTasks);
      } catch (error) {
        console.error("Error fetching tasks:", error);
        toast.error("Failed to load tasks");
      } finally {
        setLoading(false);
      }
    };

    fetchTasks();
  }, [filter]);

  const filteredTasks = tasks.filter(task => {
    if (filter === "pending") return !task.completed;
    if (filter === "completed") return task.completed;
    return true;
  });

  const handleSignOut = async () => {
    await signOut();
  };

  const handleAddTaskClick = () => {
    setEditingTask(null);
    setTaskForm({ title: "", description: "" });
    setIsModalOpen(true);
  };

  const handleEditTaskClick = (task: any) => {
    setEditingTask(task);
    setTaskForm({ title: task.title, description: task.description || "" });
    setIsModalOpen(true);
  };

  const handleSaveTask = async () => {
    try {
      if (editingTask) {
        // Update existing task
        const updatedTask = await taskApi.updateTask(editingTask.id, taskForm);
        setTasks(tasks.map(task => task.id === editingTask.id ? updatedTask : task));
        toast.success("Task updated successfully");
      } else {
        // Create new task
        const newTask = await taskApi.createTask(taskForm);
        setTasks([...tasks, newTask]);
        toast.success("Task created successfully");
      }
      setIsModalOpen(false);
    } catch (error) {
      console.error("Error saving task:", error);
      toast.error(editingTask ? "Failed to update task" : "Failed to create task");
    }
  };

  const handleDeleteTask = async (taskId: number) => {
    // Optimistic update: immediately remove task from UI
    const updatedTasks = tasks.filter(task => task.id !== taskId);
    setTasks(updatedTasks);

    try {
      await taskApi.deleteTask(taskId);
      toast.success("Task deleted successfully");
    } catch (error) {
      // Revert optimistic update on error
      setTasks([...tasks]); // Restore original tasks
      console.error("Error deleting task:", error);
      toast.error("Failed to delete task");
    }
  };

  return (
    <div className="flex h-screen bg-gray-50">
      {/* Mobile sidebar */}
      <Sheet open={sidebarOpen} onOpenChange={setSidebarOpen}>
        <SheetTrigger asChild>
          <Button variant="outline" size="icon" className="lg:hidden fixed top-4 left-4 z-50" aria-label="Open menu">
            <Menu className="h-4 w-4" aria-hidden="true" />
          </Button>
        </SheetTrigger>
        <SheetContent side="left" className="w-64 p-0">
          <SidebarContent filter={filter} setFilter={setFilter} handleSignOut={handleSignOut} />
        </SheetContent>
      </Sheet>

      {/* Desktop sidebar */}
      <aside className="hidden lg:block w-64 bg-white shadow-md h-full" role="navigation" aria-label="Main navigation">
        <SidebarContent filter={filter} setFilter={setFilter} handleSignOut={handleSignOut} />
      </aside>

      {/* Main content */}
      <main className="flex-1 overflow-auto" id="main-content">
        <header className="bg-white shadow-sm sticky top-0 z-10" role="banner">
          <div className="max-w-7xl mx-auto px-4 py-4 sm:px-6 lg:px-8 flex justify-between items-center">
            <h1 className="text-xl font-semibold text-gray-900" id="page-title">My Tasks</h1>
            <div className="flex items-center space-x-4">
              <span className="text-gray-700 hidden sm:block">Welcome, {user?.name || user?.email}</span>
              <Button onClick={handleSignOut} variant="outline" aria-label="Sign out">
                Logout
              </Button>
            </div>
          </div>
        </header>

        <div className="max-w-7xl mx-auto px-4 py-6 sm:px-6 lg:px-8">
          <div className="flex justify-between items-center mb-6">
            <div className="flex space-x-2" role="radiogroup" aria-label="Task filters">
              <Button
                variant={filter === "all" ? "default" : "outline"}
                onClick={() => setFilter("all")}
                aria-pressed={filter === "all"}
              >
                All
              </Button>
              <Button
                variant={filter === "pending" ? "default" : "outline"}
                onClick={() => setFilter("pending")}
                aria-pressed={filter === "pending"}
              >
                Pending
              </Button>
              <Button
                variant={filter === "completed" ? "default" : "outline"}
                onClick={() => setFilter("completed")}
                aria-pressed={filter === "completed"}
              >
                Completed
              </Button>
            </div>
            <Dialog open={isModalOpen} onOpenChange={setIsModalOpen}>
              <DialogTrigger asChild>
                <Button onClick={handleAddTaskClick} aria-label="Add new task">
                  <Plus className="mr-2 h-4 w-4" aria-hidden="true" /> Add Task
                </Button>
              </DialogTrigger>
              <DialogContent className="sm:max-w-[425px]">
                <DialogHeader>
                  <DialogTitle>{editingTask ? "Edit Task" : "Add New Task"}</DialogTitle>
                </DialogHeader>
                <div className="grid gap-4 py-4">
                  <div className="grid grid-cols-4 items-center gap-4">
                    <Label htmlFor="title" className="text-right">
                      Title
                    </Label>
                    <Input
                      id="title"
                      value={taskForm.title}
                      onChange={(e) => setTaskForm({...taskForm, title: e.target.value})}
                      className="col-span-3"
                      required
                      aria-describedby="title-error"
                    />
                  </div>
                  <div className="grid grid-cols-4 items-center gap-4">
                    <Label htmlFor="description" className="text-right">
                      Description
                    </Label>
                    <Textarea
                      id="description"
                      value={taskForm.description}
                      onChange={(e) => setTaskForm({...taskForm, description: e.target.value})}
                      className="col-span-3"
                      aria-describedby="description-help"
                    />
                  </div>
                </div>
                <Button onClick={handleSaveTask}>Save Task</Button>
              </DialogContent>
            </Dialog>
          </div>

          <div className="grid grid-cols-1 gap-6">
            {loading ? (
              // Render skeleton loaders while loading
              Array.from({ length: 3 }).map((_, index) => (
                <Card key={index}>
                  <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
                    <div className="flex items-center space-x-2">
                      <Skeleton className="h-4 w-4" />
                      <Skeleton className="h-4 w-[200px]" />
                    </div>
                    <Skeleton className="h-8 w-8" />
                  </CardHeader>
                  <CardContent>
                    <Skeleton className="h-4 w-full" />
                    <Skeleton className="h-4 w-1/2 mt-2" />
                  </CardContent>
                </Card>
              ))
            ) : filteredTasks.length === 0 ? (
              <Card>
                <CardContent className="p-6 text-center text-gray-500">
                  No tasks yet — add your first one 🚀
                </CardContent>
              </Card>
            ) : (
              filteredTasks.map((task) => (
                <Card key={task.id}>
                  <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
                    <div className="flex items-center space-x-2">
                      <Checkbox
                        checked={task.completed}
                        onCheckedChange={async () => {
                          // Optimistic update: immediately update UI
                          const updatedTasks = tasks.map(t =>
                            t.id === task.id ? { ...t, completed: !t.completed } : t
                          );
                          setTasks(updatedTasks);

                          try {
                            const updatedTask = await taskApi.toggleTaskCompletion(task.id);
                            // Update with server response if different
                            setTasks(tasks.map(t => t.id === task.id ? updatedTask : t));
                            toast.success("Task updated successfully");
                          } catch (error) {
                            // Revert optimistic update on error
                            setTasks(tasks);
                            console.error("Error updating task:", error);
                            toast.error("Failed to update task");
                          }
                        }}
                      />
                      <CardTitle className={task.completed ? "line-through text-gray-500" : ""}>
                        {task.title}
                      </CardTitle>
                    </div>
                    <DropdownMenu>
                      <DropdownMenuTrigger asChild>
                        <Button variant="ghost" className="h-8 w-8 p-0">
                          <MoreHorizontal className="h-4 w-4" />
                        </Button>
                      </DropdownMenuTrigger>
                      <DropdownMenuContent align="end">
                        <DropdownMenuItem onClick={() => handleEditTaskClick(task)}>Edit</DropdownMenuItem>
                        <AlertDialog>
                          <AlertDialogTrigger asChild>
                            <DropdownMenuItem onSelect={(e) => e.preventDefault()}>
                              Delete
                            </DropdownMenuItem>
                          </AlertDialogTrigger>
                          <AlertDialogContent>
                            <AlertDialogHeader>
                              <AlertDialogTitle>Are you sure?</AlertDialogTitle>
                              <AlertDialogDescription>
                                This action cannot be undone. This will permanently delete your task.
                              </AlertDialogDescription>
                            </AlertDialogHeader>
                            <AlertDialogFooter>
                              <AlertDialogCancel>Cancel</AlertDialogCancel>
                              <AlertDialogAction onClick={() => handleDeleteTask(task.id)}>
                                Delete
                              </AlertDialogAction>
                            </AlertDialogFooter>
                          </AlertDialogContent>
                        </AlertDialog>
                      </DropdownMenuContent>
                    </DropdownMenu>
                  </CardHeader>
                  <CardContent>
                    {task.description && <p className="text-gray-600">{task.description}</p>}
                    <p className="text-sm text-gray-500 mt-2">Created: {new Date(task.created_at).toLocaleDateString()}</p>
                  </CardContent>
                </Card>
              ))
            )}
          </div>
        </div>
      </main>
    </div>
  );
}

function SidebarContent({ filter, setFilter, handleSignOut }: {
  filter: "all" | "pending" | "completed";
  setFilter: (filter: "all" | "pending" | "completed") => void;
  handleSignOut: () => void;
}) {
  return (
    <div className="flex flex-col h-full">
      <div className="p-4 border-b">
        <h2 className="text-xl font-bold">Todo App</h2>
      </div>
      <nav className="flex-1 p-4 space-y-2">
        <Button
          variant={filter === "all" ? "default" : "ghost"}
          className="w-full justify-start"
          onClick={() => setFilter("all")}
        >
          All Tasks
        </Button>
        <Button
          variant={filter === "pending" ? "default" : "ghost"}
          className="w-full justify-start"
          onClick={() => setFilter("pending")}
        >
          Pending
        </Button>
        <Button
          variant={filter === "completed" ? "default" : "ghost"}
          className="w-full justify-start"
          onClick={() => setFilter("completed")}
        >
          Completed
        </Button>
      </nav>
      <div className="p-4 border-t">
        <Button variant="outline" className="w-full" onClick={handleSignOut}>
          Logout
        </Button>
      </div>
    </div>
  );
}