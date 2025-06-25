import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import { useState } from 'react';
import LoginPage from './pages/LoginPage';
import Dashboard from './pages/Dashboard';
import AppointmentForm from './pages/AppointmentForm';

function App() {
  const [user, setUser] = useState<string | null>(null);

  return (
    <Router>
      <Routes>
        <Route path="/" element={<LoginPage onLogin={setUser} />} />
        <Route
          path="/dashboard"
          element={user ? <Dashboard user={user} /> : <Navigate to="/" replace />} />
        <Route
          path="/book-appointment"
          element={user ? <AppointmentForm /> : <Navigate to="/" replace />} />
      </Routes>
    </Router>
  );
}

export default App;
