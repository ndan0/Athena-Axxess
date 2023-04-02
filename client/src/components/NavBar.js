//Create a Nav bar component with Logo and 3 links
import React from "react";
import Link from "next/link";
import Image from "next/image";
import { useRouter } from "next/router";
import logo from "../assets/AxxessLogo.png";

const NavBar = () => {


}
export default function Navbar() {
    return (
    <>

        <div className="flex flex-row justify-between items-center bg-white p-4">
            <div className="flex flex-row items-center h-0.5">
                <Image href="/" src={logo} height={30} />


            </div>
            <div className="flex flex-row items-center">
                <a href="/" className="text-xl font-extrabold text-axx-red px-4">Home</a>
                <a href="/login" className="text-xl font-extrabold px-4">Login</a>
                <a href="https://www.axxess.com/contact/" className="text-xl font-extrabold px-4">Contact us</a>
            </div>
        </div>

    </>

    )
}