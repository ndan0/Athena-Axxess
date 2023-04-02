//Write a base login page with 2 user: user and nurse
import React, { useState, useEffect, useRef } from "react";
import { useRouter } from "next/router";
import Head from "next/head";
import Image from 'next/image';

export default function Login() {

    const router = useRouter();
    const [user, setUser] = useState("");
    const [password, setPassword] = useState("");
    const [error, setError] = useState("");
    const [loading, setLoading] = useState(false);

    const handleSubmit = async (e) => {
        e.preventDefault();
        setLoading(true);
        setError("");
        if (user === "user") {
            router.push("/chat");
        } else if (user === "nurse") {
            router.push("/dashboard");
        } else {
            setError("Invalid username or password");
        }
        setLoading(false);
    }

    return (
        <div className="flex flex-col items-center justify-center min-h-screen py-2 -mt-28 px-14 text-center">
            <Head>
                <link
                    rel="stylesheet"
                    href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@48,400,0,0"
                />
            </Head>
            <label for="user"><b>Username</b></label>
            <input type={user} placeholder="Enter Username" name="user" required onChange={(e) => setUser(e.target.value)} />
            <label for="password"><b>Password</b></label>
            <input type={password} placeholder="Enter Password" name="password" required onChange={(e) => setPassword(e.target.value)} />
            <button type="submit" onClick={handleSubmit}>Login</button>


        </div>
    )

}
