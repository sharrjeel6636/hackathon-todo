import { createContext, useContext, ReactNode, useState } from "react";

interface AuthContextType {
  user: any;
  loading: boolean;
  signIn: (email: string, password: string) => Promise<void>;
  signOut: () => Promise<void>;
  signUp: (name: string, email: string, password: string) => Promise<void>;
}

const AuthContext = createContext<AuthContextType | undefined>(undefined);

export function MockAuthProvider({ children }: { children: ReactNode }) {
  const [user, setUser] = useState<any>(null);
  const [loading, setLoading] = useState(false);

  const signIn = async (email: string, password: string) => {
    setLoading(true);
    // Simulate API call
    setTimeout(() => {
      setUser({ id: "1", name: "Test User", email });
      setLoading(false);
    }, 500);
  };

  const signOut = async () => {
    setLoading(true);
    // Simulate API call
    setTimeout(() => {
      setUser(null);
      setLoading(false);
    }, 500);
  };

  const signUp = async (name: string, email: string, password: string) => {
    setLoading(true);
    // Simulate API call
    setTimeout(() => {
      setUser({ id: "1", name, email });
      setLoading(false);
    }, 500);
  };

  const value = {
    user,
    loading,
    signIn,
    signOut,
    signUp
  };

  return (
    <AuthContext.Provider value={value}>
      {children}
    </AuthContext.Provider>
  );
}

export function useAuth() {
  const context = useContext(AuthContext);
  if (context === undefined) {
    throw new Error("useAuth must be used within an AuthProvider");
  }
  return context;
}