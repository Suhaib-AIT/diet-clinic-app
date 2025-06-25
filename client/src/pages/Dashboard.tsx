type Props = {
  user: string;
};

const Dashboard = ({ user }: Props) => {
  return (
    <div className="dashboard">
      <h1>Patient Dashboard</h1>
      <p>Welcome, {user}!</p>
    </div>
  );
};

export default Dashboard;
