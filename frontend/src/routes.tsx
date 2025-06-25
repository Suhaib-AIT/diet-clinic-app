import { createBrowserRouter } from 'react-router-dom';
import LoginPage from './pages/LoginPage';
import Dashboard from './pages/Dashboard';
import AppointmentForm from './pages/AppointmentForm';
import DietPlanBuilder from './pages/DietPlanBuilder';
import Settings from './pages/Settings';

const router = createBrowserRouter([
  { path: '/', element: <LoginPage /> },
  { path: '/dashboard', element: <Dashboard user="User" /> },
  { path: '/book-appointment', element: <AppointmentForm /> },
  { path: '/diet-plan', element: <DietPlanBuilder /> },
  { path: '/settings', element: <Settings /> },
]);

export default router;
