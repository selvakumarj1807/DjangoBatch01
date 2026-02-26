import { useState } from "react";
import EmployeeList from "./components/EmployeeList";
import EmployeeForm from "./components/EmployeeForm";
import "./App.css";

function App() {
  const [selectedEmployee, setSelectedEmployee] = useState(null);
  const [refreshKey, setRefreshKey] = useState(0);

  const refresh = () => {
    setRefreshKey((prev) => prev + 1);
    setSelectedEmployee(null);
  };

  return (
    <div className="appContainer" style={{marginTop: "-80px"}}>
      <h1 className="title">👨‍💼 Employee Management System</h1>

      <div className="layout">
        <EmployeeForm
          selectedEmployee={selectedEmployee}
          refresh={refresh}
        />

        <EmployeeList
          key={refreshKey}
          onEdit={(emp) => setSelectedEmployee(emp)}
        />
      </div>
    </div>
  );
}

export default App;
