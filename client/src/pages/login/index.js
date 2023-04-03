//Write a base login page with 2 user: user and nurse
import React, { useState, useEffect, useRef } from "react";
import { useRouter } from "next/router";
import Head from "next/head";
import Image from 'next/image';
import logo from "@/assets/AxxessLogo.png";
import styles from "@/styles/Home.module.css";

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
        <>
            <video autoPlay muted loop className={styles.video}>
                <source src="https://axxessvideos.s3.amazonaws.com/axxessherovids/cahps.mp4" type="video/mp4"/>
            </video>
            <div className="flex flex-col items-center justify-center min-h-screen py-2 -mt-28 px-14 text-center">
            <div className="block max-w-md p-6 rounded-xl bg-gray-200 bg-opacity-60">
                <Head>
                    <link
                        rel="stylesheet"
                        href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@48,400,0,0"
                    />
                </Head>
                <Image src={logo} height={60} />
                <div className="mx-2 my-2">
                <label for="user"><b>Username:</b></label>
                <input type={user} placeholder="Enter Username" name="user" required onChange={(e) => setUser(e.target.value)} />
                </div>
                <div>
                <label for="password"><b>Password:  </b></label>
                <input type={"password"} placeholder="Enter Password" name="password" required onChange={(e) => setPassword(e.target.value)} />
                </div>

                <button className="my-2 mt-5 px-5 py-1 bg-axx-red text-white rounded-md" type="submit" onClick={handleSubmit}>Login</button>
            </div>
            </div>
        </>

    )

}
