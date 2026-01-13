// Mock auth implementation
export const signIn = async (provider: string, credentials: any) => {
  console.log("Mock sign in with", provider, credentials);
  // Simulate API call
  return Promise.resolve({ success: true });
};

export const signOut = async () => {
  console.log("Mock sign out");
  // Simulate API call
  return Promise.resolve();
};

export const useSession = () => {
  // Mock session data
  return {
    data: {
      user: { id: "1", name: "Test User", email: "test@example.com" }
    },
    isPending: false
  };
};