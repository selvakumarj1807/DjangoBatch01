import { useState, useEffect } from "react";
import API from "../services/api";

function EmployeeForm({ selectedEmployee, refresh }) {
    const [form, setForm] = useState({
        employee_id: "",
        fullName: "",
        salary: "",
        department_id: "",
    });

    useEffect(() => {
        if (selectedEmployee) {
            setForm(selectedEmployee);
        }
    }, [selectedEmployee]);

    const handleChange = (e) => {
        setForm({ ...form, [e.target.name]: e.target.value });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();

        if (form.id) {
            await API.put(`employees/${form.id}/`, form);
        } else {
            await API.post("employees/", form);
        }

        setForm({
            employee_id: "",
            fullName: "",
            salary: "",
            department_id: "",
        });

        refresh();
    };

    return (
        <div className="card">
            <h2>{form.id ? "✏ Update Employee" : "➕ Add Employee"}</h2>

            <form onSubmit={handleSubmit} className="form">
                <input
                    name="employee_id"
                    placeholder="Employee ID"
                    value={form.employee_id}
                    onChange={handleChange}
                    required
                />

                <input
                    name="fullName"
                    placeholder="Full Name"
                    value={form.fullName}
                    onChange={handleChange}
                    required
                />

                <input
                    name="salary"
                    type="number"
                    placeholder="Salary"
                    value={form.salary}
                    onChange={handleChange}
                    required
                />

                <input
                    name="department_id"
                    placeholder="Department"
                    value={form.department_id}
                    onChange={handleChange}
                    required
                />

                <button type="submit" className="primaryBtn">
                    Save
                </button>
            </form>
        </div>
    );
}

export default EmployeeForm;
