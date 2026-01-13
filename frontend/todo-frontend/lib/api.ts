// Create a custom hook to handle API calls
export const useApi = () => {
  const apiCall = async (url: string, options: RequestInit = {}) => {
    const headers = {
      "Content-Type": "application/json",
      ...options.headers,
    };

    const response = await fetch(`${process.env.NEXT_PUBLIC_API_BASE_URL}${url}`, {
      ...options,
      headers,
    });

    if (!response.ok) {
      throw new Error(`API call failed: ${response.status} ${response.statusText}`);
    }

    return response.json();
  };

  return { apiCall };
};

// Specific API functions
export const taskApi = {
  getTasks: async (status: "all" | "pending" | "completed" = "all") => {
    return fetch(`${process.env.NEXT_PUBLIC_API_BASE_URL}/api/tasks?status=${status}`, {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
      }
    }).then(res => res.json());
  },

  createTask: async (taskData: { title: string; description?: string }) => {
    return fetch(`${process.env.NEXT_PUBLIC_API_BASE_URL}/api/tasks`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(taskData)
    }).then(res => res.json());
  },

  updateTask: async (id: number, taskData: { title?: string; description?: string }) => {
    return fetch(`${process.env.NEXT_PUBLIC_API_BASE_URL}/api/tasks/${id}`, {
      method: "PUT",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(taskData)
    }).then(res => res.json());
  },

  deleteTask: async (id: number) => {
    return fetch(`${process.env.NEXT_PUBLIC_API_BASE_URL}/api/tasks/${id}`, {
      method: "DELETE",
      headers: {
        "Content-Type": "application/json",
      }
    }).then(res => res.json());
  },

  toggleTaskCompletion: async (id: number) => {
    return fetch(`${process.env.NEXT_PUBLIC_API_BASE_URL}/api/tasks/${id}/complete`, {
      method: "PATCH",
      headers: {
        "Content-Type": "application/json",
      }
    }).then(res => res.json());
  }
};