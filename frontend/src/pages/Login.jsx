import { useState } from "react";
import { Link } from "react-router-dom";

const Login = () => {
  const [loginData, setLoginData] = useState({
    email: "",
    password: "",
  });

  const handleChange = (e) => {
    setLoginData({
      ...loginData,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = (e) => {
    e.preventDefault();

    console.log(loginData);

    // Login API call
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-gradient-to-br from-indigo-100 via-white to-purple-100">

      <div className="bg-white p-8 rounded-2xl shadow-2xl w-96">

        <h2 className="text-4xl font-bold text-center text-indigo-700 mb-2">
          Welcome Back
        </h2>

        <p className="text-center text-gray-500 mb-6">
          Semantic Fact Retrieval System
        </p>

        <form onSubmit={handleSubmit}>

          <input
            type="email"
            name="email"
            placeholder="Email"
            className="w-full px-4 py-3 rounded-xl border mb-4 focus:outline-none focus:ring-2 focus:ring-indigo-500"
            onChange={handleChange}
          />

          <input
            type="password"
            name="password"
            placeholder="Password"
            className="w-full px-4 py-3 rounded-xl border mb-6 focus:outline-none focus:ring-2 focus:ring-indigo-500"
            onChange={handleChange}
          />

          <button
            className="w-full bg-indigo-600 text-white py-3 rounded-xl hover:bg-indigo-700 hover:scale-105 transition duration-300"
          >
            Login
          </button>

        </form>

        <p className="text-center mt-6 text-gray-600">
          Don't have an account?{" "}
          <Link
            to="/signup"
            className="text-indigo-600 font-semibold hover:underline"
          >
            Sign Up
          </Link>
        </p>

      </div>

    </div>
  );
};

export default Login;