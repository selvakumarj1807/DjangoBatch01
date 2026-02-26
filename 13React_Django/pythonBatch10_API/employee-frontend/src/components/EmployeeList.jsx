import { useEffect, useState } from "react";
import API from "../services/api";

function EmployeeList({ onEdit }) {
    const [employees, setEmployees] = useState([]);

    const fetchEmployees = async () => {
        const response = await API.get("employees/");
        setEmployees(response.data);
    };

    useEffect(() => {
        fetchEmployees();
    }, []);

    const handleDelete = async (id) => {
        if (window.confirm("Are you sure you want to delete?")) {
            await API.delete(`employees/${id}/`);
            fetchEmployees();
        }
    };

    return (
        <div className="card">
            <h2>📋 Employee List</h2>

            <div className="tableWrapper">
                <table>
                    <thead>
                        <tr>
                            <th>ID</th>
                            <th>Name</th>
                            <th>Salary</th>
                            <th>Dept</th>
                            <th>Action</th>
                        </tr>
                    </thead>
                    <tbody>
                        {employees.map((emp) => (
                            <tr key={emp.id}>
                                <td>{emp.employee_id}</td>
                                <td>{emp.fullName}</td>
                                <td>${emp.salary}</td>
                                <td>{emp.department_id}</td>
                                <td className="actions">
                                    <button
                                        className="editBtn"
                                        onClick={() => onEdit(emp)}
                                    >
                                        Edit
                                    </button>

                                    <button
                                        className="deleteBtn"
                                        onClick={() => handleDelete(emp.id)}
                                    >
                                        Delete
                                    </button>
                                </td>
                            </tr>
                        ))}
                    </tbody>
                </table>
            </div>
        </div>
    );
}

export default EmployeeList;
